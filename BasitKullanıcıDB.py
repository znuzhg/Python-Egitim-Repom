import time

kullanicilar = [
    {"ad": "MAHMUT", "yas": 22},
    {"ad": "MAHMUT", "yas": 32},
    {"ad": "AYŞE", "yas": 30}
]

def kullanici_ekle():
    while True:
        try:
            isim = input("İsim : ").strip()
            if not isim.isalpha():
                print("\nLütfen ismi rakam veya özel karakter olmadan giriniz!\n")
                continue

            isim = isim.upper()

            yas = input("Yaş : ").strip()
            if not yas.isdigit():
                print("Lütfen Yaşı harf ve özel karakter olmadan giriniz!\n")
                continue

            kullanicilar.append({"ad": isim, "yas": int(yas)})
            print(">> Kullanıcı eklendi !\n")

        except ValueError:
            print("\nLütfen Doğru Değeri Girdiğinizden Emin Olun\n")
            continue
        break


def kullanici_sil():
    sil = input("Silinecek kişi: ").strip().upper()
    eslesenler = []

    for index, kisi in enumerate(kullanicilar):
        if kisi["ad"].upper() == sil:
            eslesenler.append((index, kisi))

    if not eslesenler:
        print(">> Böyle bir kullanıcı bulunamadı.\n")
        return

    print("\nBulunan Kullanıcılar:")
    for i, (_, kisi) in enumerate(eslesenler):
        print(f"[{i}] {kisi}")

    sec = input("Silmek istediğiniz kişi: ")

    if not sec.isdigit() or int(sec) >= len(eslesenler):
        print(">> Geçersiz seçim!")
        return

    sec = int(sec)
    silinecek_index = eslesenler[sec][0]
    silinen = kullanicilar.pop(silinecek_index)
    print(f">> Silindi: {silinen}\n")


def kullanici_listele():
    print("\nKullanıcılar : ")
    for kullanici in sorted(kullanicilar, key=lambda x: x["ad"]):
        print(f"- {kullanici['ad']} ({kullanici['yas']})")
    print()


def kullanici_ara():
    ara = input("Ara: ").strip().upper()
    bulundu = False

    for kullanici in kullanicilar:
        if kullanici["ad"].upper() == ara:
            print(f">> Bulundu: {kullanici['ad']} - {kullanici['yas']} yaşında\n")
            bulundu = True
            break

    if not bulundu:
        print(f">> '{ara}' kullanıcılar arasında bulunamadı!\n")


def menu():
    print("\n1 - Kullanıcı Ekle\n"
          "2 - Kullanıcı Sil\n"
          "3 - Kullanıcıları Listele\n"
          "4 - Kullanıcı Ara\n"
          "q - Çıkış\n")

    while True:
        sec = input("İşlem: ").strip()

        if sec == "q":
            print("\n --- Sistemden Çıkılıyor ---\n")
            time.sleep(1)
            print("\n --- Program Başarı İle Kapatıldı ---\n")
            break

        if sec not in ["1", "2", "3", "4"]:
            print("\nLütfen İşlemi Düzgün Giriniz!\n")
            continue

        if sec == "1":
            kullanici_ekle()
        elif sec == "2":
            kullanici_sil()
        elif sec == "3":
            kullanici_listele()
        elif sec == "4":
            kullanici_ara()


menu()
