sifre = input("Şifre Giriniz:")  # Bilgis@y@r
bHarf = kHarf = Sembol = Rakam =  True
import string
semboller = string.punctuation
if sifre:
    if len(sifre)>=8:
        for item in sifre: # B i lgis@y@r
            if item.isalpha():
                if item.isupper():
                    bHarf = False
                if item.islower():
                    kHarf = False
            if item.isdigit():
                Rakam = False
            if item in semboller:
                Sembol = False
        if bHarf:
            print("Büyük Harf Girilmeli")
        if Rakam:
            print("Rakam  Girilmeli")
        if Sembol:
            print("Sembol  Girilmeli")
        if kHarf:
            print("Küçük Harf Girilmeli")
    else:
        print("Şifre Uzunlğu")
else:
    print("Şifre Girilimeli")   