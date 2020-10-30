### DAHA BİTMEDİ
from abc import ABC, abstractmethod

class ARAC(ABC):
    "Ulaşım veya taşıma amaçlı üretilen araçlar sınıfı"
    
    def __init__(self,tur,yakit,kapasite,hiz,fiyat):
        self.tur = tur
        self.yakit = yakit
        self.kapasite = kapasite
        self.hiz = hiz
        self.__fiyat = fiyat

    def getFiyat(self):
        return self.__fiyat

    def setFiyat(self, kacPara):
        self.__fiyat=kacPara

    @absract method
        def neTur(self):
            return "{} tipi yakıt kullanan {}'nda seyredebilen araçtır".format(self.yakit,self.tur)
    @absract method
        def neYapar(self):
            return "{} yolcuyu {} hız ile taşır".format(self.kapasite,self.hiz)

class Karayolu(ARAC):
    "Karayolunda gidebilen araçlar sınıfı"
    def __init__(self,tur,yakit,kapasite,hiz,fiyat,marka,renk,cins):
        super().__init__(tur,yakit,kapasite,hiz,fiyat)
        self.marka=marka
        self.renk=renk
        self.cins=cins


class Denizyolu(ARAC):
    "Denizyolunda gidebilen araçlar sınıfı"
    def __init__(self,tur,yakit,kapasite,hiz,fiyat,kaptan,renk,cins):
        super().__init__(tur,yakit,kapasite,hiz,fiyat)
        self.kaptan=kaptan
        self.renk=renk
        self.cins=cins


class Havayolu(ARAC):
    "Havayolunda gidebilen araçlar sınıfı"
    def __init__(self,tur,yakit,kapasite,hiz,fiyat,pilot,renk,cins):
        super().__init__(tur,yakit,kapasite,hiz,fiyat)
        self.pilot=pilot
        self.renk=renk
        self.cins=cins

otomobil1 = Karayolu("otomobil","benzin",5,"250km/h","€5,000","ford","siyah","sedan")
otobus1 = Karayolu("otomobil","benzin",60,"180m/h","€25,000","MAN","mavi","yolcuOtobüsü")
yat1 = Denizyolu("yat","blendoil",35,"11knot/h","€50,000","JackSparrow","beyaz","YOLE")
yat2 = Denizyolu("yat","blendoil",15,"19knot/h","€65,000","Barbossa","beyaz","yelkenli")
ucak1=Havayolu("ucak","kerosen",200,"450km/h","€1,200,000","HalilSezai","kırmızı","yolcuUçağı")
helikopter1=("helikopter","kerosen",8,"200km/h","€1,005,000","Ajdar","gri","askeri")

neTur(otomobil1)

### DAHA BİTMEDİ 