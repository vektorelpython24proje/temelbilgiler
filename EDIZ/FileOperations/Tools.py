import os
class DosyaTool:
    __tur = ".csv"
    __ayrac = ";"
    def __init__(self,adres="defter",alanlar=["Adı","Soyadı","Tel"]):
        self.adres = adres + DosyaTool.__tur
        self.alanlar = alanlar
        self.dosya = self.dosyaAc()
        self.kayitlar = self.dosya.readlines()
    
    def dosyaAc(self):
        if os.path.exists(self.adres):
            return open(self.adres,"r+",encoding="UTF-8")
        else:
            return open(self.adres,"w+",encoding="UTF-8")


    def listeleme(self):
        # ali;veli;123\n
        sayac = 1
        for item in self.kayitlar:
            print(f"{sayac}",*item.split(DosyaTool.__ayrac),end="")
            sayac+=1
    
    def girisYap(self):
        liste = []
        for item in self.alanlar:
            liste.append(input(f"{item} Giriniz:"))
        return DosyaTool.__ayrac.join(liste) + "\n"


    def ekleme(self):
        self.kayitlar.append(self.girisYap())

    def silme(self):
        self.listeleme()
        kayitNum = int(input("Silmek istediğiniz kaydı seçiniz:"))
        del self.kayitlar[kayitNum-1]

    
    def guncelleme(self):
        self.listeleme()
        kayitNum = int(input("Güncellemek istediğiniz kaydı seçiniz:"))
        self.kayitlar[kayitNum-1] = self.girisYap()
    
    def kaydetme(self):
        self.dosya.seek(0)
        self.dosya.truncate()
        self.dosya.writelines(self.kayitlar)
        self.dosya.flush()

    def __del__(self):
        self.dosya.seek(0)
        self.dosya.truncate()
        self.dosya.writelines(self.kayitlar)
        self.dosya.close()

    def menu(self):
        menu = f"""
        {self.adres} üzerinde çalışılıyor
        1-Listeleme
        2-Ekleme
        3-Silme
        4-Güncelleme
        5-Kayıt
        6-Çıkış
        İşlem Seçiniz:
        """
        liste = ["",self.listeleme,self.ekleme,self.silme,self.guncelleme,self.kaydetme]
        while True:
            islem = int(input(menu))
            if 1<=islem<6:
                liste[islem]()
            elif islem == 6:
                break
            else:
                print("Yanlış İşlem Numarası")


    
