import json
import os


class SayiAnaliz:
    def __init__(self, sayi: int):
        self.sayi = sayi

    def asal_mi(self) -> bool:
        if self.sayi <= 1:
            return False
        if self.sayi == 2:
            return True

        for i in range(2, self.sayi):
            if self.sayi % i == 0:
                return False
        return True

    def cift_mi(self) -> bool:
        return self.sayi % 2 == 0

    def tek_mi(self) -> bool:
        return not self.cift_mi()

    def analiz_et(self) -> dict:
        return {
            "sayi": self.sayi,
            "asal": self.asal_mi(),
            "cift": self.cift_mi(),
            "tek": self.tek_mi()
        }


class SonucYonetici:
    DOSYA_ADI = "sonuclar.json"

    @staticmethod
    def yukle() -> list:
        if not os.path.exists(SonucYonetici.DOSYA_ADI):
            return []
        with open(SonucYonetici.DOSYA_ADI, "r", encoding="utf-8") as f:
            return json.load(f)

    @staticmethod
    def kaydet(sonuc: dict) -> None:
        veriler = SonucYonetici.yukle()
        veriler.append(sonuc)
        with open(SonucYonetici.DOSYA_ADI, "w", encoding="utf-8") as f:
            json.dump(veriler, f, indent=4, ensure_ascii=False)

    @staticmethod
    def goster() -> None:
        veriler = SonucYonetici.yukle()
        if not veriler:
            print("Henüz kayıtlı sonuç yok.")
            return

        for kayit in veriler:
            print(kayit)


def menu():
    while True:
        print(
            "\n--- Sayı Analiz Aracı ---\n"
            "1 - Sayı analiz et\n"
            "2 - Kayıtlı sonuçları göster\n"
            "3 - Çıkış\n"
        )

        try:
            secim = int(input("İşlem: "))
        except ValueError:
            print("Geçersiz seçim.")
            continue

        if secim == 3:
            print("Program kapatıldı.")
            break

        elif secim == 1:
            try:
                sayi = int(input("Sayı girin: "))
            except ValueError:
                print("Geçersiz sayı.")
                continue

            analiz = SayiAnaliz(sayi)
            sonuc = analiz.analiz_et()
            SonucYonetici.kaydet(sonuc)
            print("Analiz sonucu:", sonuc)

        elif secim == 2:
            SonucYonetici.goster()

        else:
            print("Geçersiz seçim.")


if __name__ == "__main__":
    menu()
