import base64
from tkinter import *
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

#pencere
pencere = Tk()
pencere.minsize(width=500,height=750)
pencere.resizable(width=False,height=False)
pencere.config(bg="white",pady=5)
pencere.title("Secret Notes App")

#png dosyası
secret_resim = PhotoImage(file="Secret.png")
resim = Label(pencere, image=secret_resim,bg="white")
resim.pack(pady=10)

# - - - fonksiyonlar - - -
# def kaydet(sifreli_metin,title):
#     with open("Secret_Note.txt","a") as f:
#         f.write(f"\n--- {title}---\n")
#         f.write(f"{sifreli_metin}\n")
# def sifrele():
#     title = baslik_gir.get()
#     not_al = not_gir.get(index1="1.0",index2=END)
#     not_to_byte = not_al.encode("utf-8")
#     not_byte_to_base64 = base64.b64encode(not_to_byte)
#     sifreli_metin = not_byte_to_base64.decode("utf-8")
#     return kaydet(sifreli_metin,title)
# def cozumle():
#     not_al = not_gir.get(index1="1.0",index2=END)
#     not_to_byte = not_al.encode("utf-8")
#     not_byte_to_base64 = base64.b64decode(not_to_byte)
#     metin = not_byte_to_base64.decode("utf-8")
#     not_gir.delete(index1="1.0",index2=END)
#     not_gir.insert(index="1.0",chars=metin)

# -------------------------------------------------------------------
# --------------------------- FONKSİYONLAR ---------------------------
# -------------------------------------------------------------------
#NOT: aes şifreleme fonksiyonları için alıntı yaptım

# ----------------------- Kaydetme Fonksiyonu ------------------------
def kaydet(iv, sifreli_metin, title):
    """
    Başlığı, IV'yi ve şifreli veriyi Secret_Note.txt dosyasına ekler.
    """
    with open("Secret_Note.txt", "a", encoding="utf-8") as f:
        f.write(f"\n--- {title} ---\n")
        f.write(f"IV: {iv}\n")
        f.write(f"DATA: {sifreli_metin}\n")


# ------------------ Save & Encrypt (AES ile şifreleme) ------------------
def aesle_ve_kaydet():
    """
    Kullanıcının girdiği metni ve anahtarı alır,
    AES ile şifreler ve dosyaya kaydeder.
    """
    title = baslik_gir.get()
    metin = not_gir.get("1.0", END)
    anahtar = master_key_gir.get()

    # AES şifreleme
    iv, sifreli_veri = aes_sifrele(metin, anahtar)

    # Dosyaya yaz
    kaydet(iv, sifreli_veri, title)


# ------------------ Decrypt (AES ile çözme ve ekrana yaz) ------------------
def aes_coz_ve_goster():
    anahtar = master_key_gir.get()

    try:
        with open("Secret_Note.txt", "r", encoding="utf-8") as f:
            satirlar = f.readlines()

        # Son eklenen IV ve DATA'yı bulmak için sondan tarayacağız
        iv = None
        data = None

        for satir in reversed(satirlar):
            if satir.startswith("DATA: "):
                data = satir.replace("DATA: ", "").strip()
            if satir.startswith("IV: "):
                iv = satir.replace("IV: ", "").strip()

            # ikisi de bulununca dur
            if iv and data:
                break

        # Hâlâ bulunamadıysa hata ver
        if iv is None or data is None:
            not_gir.delete("1.0", END)
            not_gir.insert("1.0", "❌ Dosyada IV veya DATA bulunamadı!")
            return

        # AES çözme
        cozulmus = aes_coz(iv, data, anahtar)

        # Sonucu ekrana yaz
        not_gir.delete("1.0", END)
        not_gir.insert("1.0", cozulmus)

    except FileNotFoundError:
        not_gir.delete("1.0", END)
        not_gir.insert("1.0", "❌ Secret_Note.txt bulunamadı!")
    except Exception as e:
        not_gir.delete("1.0", END)
        not_gir.insert("1.0", f"❌ Hata: {e}")



# ----------------------- AES Yardımcı Fonksiyonları -----------------------
def aes_pad(veri: bytes) -> bytes:
    """
    PKCS7 padding ekleyerek veriyi 16 byte'ın katına tamamlar.
    """
    eksik = 16 - (len(veri) % 16)
    return veri + bytes([eksik]) * eksik


def aes_unpad(veri: bytes) -> bytes:
    """
    PKCS7 padding'i kaldırır.
    """
    eksik = veri[-1]
    return veri[:-eksik]


# ---------------------------- AES Şifreleme ----------------------------
def aes_sifrele(metin: str, anahtar: str):
    """
    Metni AES CBC ile şifreler ve IV + şifreli metni Base64 formatında döndürür.
    """
    # Anahtar 16 byte yapılır
    anahtar = anahtar.ljust(16)[:16].encode("utf-8")

    # Rastgele IV üretilir
    iv = get_random_bytes(16)

    # AES CBC oluştur
    sifreleyici = AES.new(anahtar, AES.MODE_CBC, iv)

    # Metni byte yap + padding
    metin_bytes = metin.encode("utf-8")
    metin_padded = aes_pad(metin_bytes)

    # Şifreleme
    sifreli_veri = sifreleyici.encrypt(metin_padded)

    # Base64 formatında döndür
    iv_b64 = base64.b64encode(iv).decode("utf-8")
    sifreli_b64 = base64.b64encode(sifreli_veri).decode("utf-8")

    return iv_b64, sifreli_b64


# ---------------------------- AES Çözme ----------------------------
def aes_coz(iv_b64: str, sifreli_b64: str, anahtar: str) -> str:
    """
    IV + şifreli Base64 veriyi çözerek orijinal metni döndürür.
    """
    anahtar = anahtar.ljust(16)[:16].encode("utf-8")

    iv = base64.b64decode(iv_b64)
    sifreli_veri = base64.b64decode(sifreli_b64)

    cozucu = AES.new(anahtar, AES.MODE_CBC, iv)

    cozulmus_padded = cozucu.decrypt(sifreli_veri)
    temiz_veri = aes_unpad(cozulmus_padded)

    return temiz_veri.decode("utf-8")


#title
baslik = Label(pencere, text="Enter your title",bg="white", font=("Arial",15,"normal"))
baslik.pack()

baslik_gir = Entry(width=30,bg="white")
baslik_gir.pack(pady=10)

#Note
not_= Label(pencere, text="Enter your secret",bg="white", font=("Arial",15,"normal"))
not_.pack()

not_gir = Text(height=20,width=40,bg="white")
not_gir.pack(pady=10)

#Anahtar kelime
master_key = Label(pencere, text="Enter Master Key:",bg="white",font=("Arial",15,"normal"))
master_key.pack()
master_key_gir = Entry(width=30,bg="white")
master_key_gir.pack(pady=10)

#Save and Encrypt button
save_and_encrypt=Button(bg="white",fg="black",font=("Arial",10,"normal"),text="Save & Encrypt",width=17)
save_and_encrypt.config(command=aesle_ve_kaydet)
save_and_encrypt.pack()

#Decode Button
Decrypt=Button(bg="white",fg="black",font=("Arial",8,"normal"),text="Decrypt",width=15)
Decrypt.pack(pady=20)
Decrypt.config(command=aes_coz_ve_goster)

pencere.mainloop()
