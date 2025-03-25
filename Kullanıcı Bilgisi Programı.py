from IPython.display import clear_output

while True:
    girdiİsim1 = input("Adınızı Girin: ")
    clear_output()
    girdiSoyisim1 = input("Soyadınızı Girin: ")
    clear_output()

    print("=" * 30)
    print(f"Merhaba {girdiİsim1.title()} {girdiSoyisim1.title()} hoş geldiniz!")
    print("=" * 30)
    kullanıcıİsim1 = f"{girdiİsim1.title()} {girdiSoyisim1.title()}"

    while True:
        try:
            girdiYas1 = int(input("Yaşınızı Girin: "))
            if girdiYas1 <= 0:
                print("Yaşınız sıfırdan büyük olmalıdır. Lütfen tekrar deneyin!")
                continue
            break
        except ValueError:
            print("Geçerli bir sayı giriniz!")

    clear_output()

    kullanıcıBilgisiPrint = f"Adınız: {kullanıcıİsim1} | Yaşınız: {girdiYas1}"
    
    print("Bilgilerinizi onaylayınız:")
    print(kullanıcıBilgisiPrint)
    print("Doğruysa 1'e, yanlışsa 0'a basınız.")

    doğrulama = input()

    if doğrulama == "1":
        print("Bilgiler onaylandı. Programdan çıkılıyor...")
        break
    elif doğrulama == "0":
        print("Bilgiler sıfırlanıyor. Yeniden başlayın...")
        continue
    elif doğrulama not in ["1", "0"]:
        clear_output()
        print("Geçersiz seçim yaptınız! Lütfen sadece '1' veya '0' girin.")
