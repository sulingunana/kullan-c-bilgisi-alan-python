def girisfonksiyonu():
    kullanici_adi = input("Kullanıcı adınızı girin: ")
    sifre = input("Şifrenizi girin: ")

    dogrulama_bilgisi = (kullanici_adi, sifre)
    kullanici_bilgileri = []

    with open("kullanici_bilgileri.txt", "r") as dosya:
        kullanici_bilgileri = [satir.strip().split(",") for satir in dosya]

    if dogrulama_bilgisi in kullanici_bilgileri:
        print("Giriş yapıldı")
    else:
        print("Kullanıcı adı veya şifre yanlış, tekrar deneyin")


girisfonksiyonu()

