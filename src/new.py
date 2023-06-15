import pytesseract
from PIL import Image


def metin_ayikla(gorsel_yolu):
    try:
        # Görsele PIL kütüphanesi ile erişim sağla
        image = Image.open(gorsel_yolu)

        # OCR işlemi için pytesseract kullanarak metni al
        metin = pytesseract.image_to_string(image, lang='tur')

        return metin
    except IOError:
        print(f"Dosya bulunamadı.{0}\n hata: {1}",
              gorsel_yolu, IOError.strerror)
        return None


# Ana program döngüsü
while True:
    gorsel_yolu = input(
        "Metin çıkarmak istediğiniz görsel dosyasının yolunu girin (çıkmak için 'q' tuşuna basın): ")

    if gorsel_yolu == 'q':
        break

    metin = metin_ayikla(gorsel_yolu)

    if metin:
        print("Çıktı:")
        print(metin)
