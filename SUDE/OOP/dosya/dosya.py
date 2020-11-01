import os
class DosyaTool:
    __tur = ".csv"
    __ayrac = ";"
    def __init__(self,adres="defter",alanlar=["Adı","Soyadı","Tel"]):
        self.adres = adres + DosyaTool.__tur
        self.alanlar = alanlar
        self.dosya=self.dosyaAc()
        self.kayitlar=self.dosya.readlines()

    
    def dosyaAc(self):
        if os.path.exists(self.adres):
            return open(self.adres,"r+",encoding="UTF-8")
        else:
            return open(self.adres,"w+",encoding="UTF-8")

    def listeleme(self):
        sayac = 1
        for item in self.kayitlar:
            print(f"{sayac}","{*item.split(DosyaTool.__ayrac)}",end="")
            sayac+=1

    def girisYap(self):
        liste=[]
        for item in self.alanlar:
            liste.append(input(f"{item} Giriniz:"))
            return DosyaTool.__ayrac.join(liste) + "\n"

    def ekleme(self):
        self.kayitlar.append(self.girisYap())

    def silme(self):
        self.listeleme()
        kayitNum = int(input("Silmek istediğiniz kaydı seçin"))
        del self.kayitlar[kayitNum-1]

    def guncelleme(self):
        self.listeleme()
        kayitNum = int(input("Güncelleme istediğiniz kaydı seçin"))
        del self.kayitlar[kayitNum-1] = self.girisYap()

    def kaydetme(self):
        self.dosya.seek(0)
        self.dosya.truncate()
        self.dosya.writeLines(self.kayitlar)
        self.dosya.flush()


    def __del__(self):
        self.dosya.seek(0)
        self.dosya.truncate()
        self.dosya.writeLines(self.kayitlar)
        self.dosya.close()

    def menu(self):
        menu = """
        1-listele
        2-ekle
        3-sil
        4-güncel
        5-kayıt
        6-çıkış
        işlem seç:
        """
        liste["",self.listeleme,self.ekleme,self.silme,self.guncelleme,self.kayit]
        while True:
            islem = int(input(menu))
            if 0<islem<7:
                liste[islem]()
            elif islem == 6:
                break
            else:
                print("Yanlıs işlem numarası")


obj1=DosyaTool()
obj.listeleme()
