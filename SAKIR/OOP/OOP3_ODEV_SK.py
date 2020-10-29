class KP657():  # Sınıf-Class
    tur = "Kamu Personeli"  # class attribute - Sınıf Özelliği
    def __init__(self,ad,soyad,yas,gorev,maas): # constructor - yapıcı
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.gorev = gorev
        self.maas = maas
        print(f"Bir {gorev} istihdam edildi.")

    def calis(self):    # instance method - Örnek Metodu
        print(f"{self.ad} {self.soyad} {self.gorev} olarak çalışıyor.")
    
    def paraKazan(self):
        print(f"{self.ad} {self.soyad} {self.maas} TL kazanıyor.")

    @classmethod
    def gorevAlma(cls): # class method - Sınıf Metodu
        print("Bir",cls.tur," daha görev aldı ")

    def __del__(self):  # deconstructor - Yıkıcı
        print(f"{self.ad} {self.soyad} istirahate çekildi dinleniyor ...")

Personel1 = KP657("Ahmet","Mülayim",21,"Doktor",15000) # nesne - object
Personel2 = KP657("Ayşe","Çalışkan",25,"öğretmen",7500)
Personel3 = KP657("Mahmut","Korkmaz",32,"Savcı",16000)
Personel4 = KP657("Cevdet","Yorulmaz",28,"Mühendis",12000)

for Personel in (Personel1,Personel2,Personel3,Personel4):
    Personel.calis()
    Personel.paraKazan()
    Personel.gorevAlma()
