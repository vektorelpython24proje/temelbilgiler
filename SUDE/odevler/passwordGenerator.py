# uzunluk 8
#küçük harf olmalı
#büyük harf olmalı
#noktalama işareti olmalı
#girilen iki kelime üzerinden şifre üreten
#girilen şifrenin güvenli bir şifre olup olmadığı 
#eksikleriyle söylen bir 
#OOP temelli Şifre önerici sınıf yazalım

import random as rnd
import string

buyukHarfler = string.ascii_uppercase
kucukHarfler = string.ascii_lowercase
sayılar = string.digits
noktalamalar = string.punctuation
password = ""

tercih = input("""
1-Önerilen Şifre İstiyorum
2-Kelimelerimden Şifre Üret
3-Kendi şifremi yazmak istiyorum
"""
)

if tercih == "1":

    for i in range(2):
        password += rnd.choice(kucukHarfler)
        for j in range(1):
            password += rnd.choice(buyukHarfler)
            for k in range (1):
                password += rnd.choice(sayılar)+rnd.choice(noktalamalar)
    print(password)

elif tercih == "2":

    kelime1=input("İlk kelimeyi giriniz: ")
    kelime2=input("İkinci kelimeyi giriniz: ")

    for i in range(2):
        password += rnd.choice(kelime1)
        for j in range(1):
            password += rnd.choice(kelime2)
            for k in range (1):
                password += rnd.choice(sayılar)+rnd.choice(noktalamalar)
    print(password)

elif tercih== "3":

    sifre = input("Bir şifre giriniz: ")
    l, u, p, d = 0, 0, 0, 0

    if (len(sifre) <= 8): 
        for i in sifre: 
    
            if (i.islower()): 
                l+=1            
    
            if (i.isupper()): 
                u+=1            

            if (i.isdigit()): 
                d+=1            

            if(i.ispunct()): 
                p+=1   
                        
    if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(sifre)): 
        print("Kullanılabilir") 

    elif (l<=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(sifre)): 
        print("Küçük harf yazınız!!")

    elif (l>=1 and u<=1 and p>=1 and d>=1 and l+p+u+d==len(sifre)):
        print("Büyük harf yazınız!!")

    elif (l>=1 and u>=1 and p<=1 and d>=1 and l+p+u+d==len(sifre)):
        print("Noktalama kullan!!")

    elif (l>=1 and u>=1 and p>=1 and d<=1 and l+p+u+d==len(sifre)):
        print("Sayı kullan!!")

    else:
        print("Kullanılamaz")

else:
    print("Lütfen sadece 1 veya 2 giriniz!!!")





