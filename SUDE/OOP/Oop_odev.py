### DAHA BİTMEDİ
from abc import ABC, abstractmethod

class ARAC(ABC):
    "Ulaşım veya taşıma amaçlı üretilen araçlar sınıfı"
    
    def __init__(self,tur,yakit,kapasite,hiz):
        self.tur = tur
        self.yakit = yakit
        self.kapasite = kapasite
        self.hiz = hiz

    @abstractmethod
    def neTur(self):
        return "{} tipi yakıt kullanan {}'nda seyredebilen araçtır".format(self.yakit,self.tur)
    @abstractmethod
    def neYapar(self):
        return "{} yolcuyu {} hız ile taşır".format(self.kapasite,self.hiz)   
        


class Karayolu(ARAC):
    "Karayolunda gidebilen araçlar sınıfı"
    def __init__(self,tur,yakit,kapasite,hiz,marka,renk,cins):
        super().__init__(tur,yakit,kapasite,hiz)
        self.marka=marka
        self.renk=renk
        self.cins=cins
    
    def neTur(self):
        return "{} tipi yakıt kullanan {}'nda seyredebilen araçtır".format(self.yakit,self.tur)
    
    def neYapar(self):
        return "{} yolcuyu {} hız ile taşır".format(self.kapasite,self.hiz)


class Denizyolu(ARAC):
    "Denizyolunda gidebilen araçlar sınıfı"
    def __init__(self,tur,yakit,kapasite,hiz,kaptan,renk,cins):
        super().__init__(tur,yakit,kapasite,hiz)
        self.kaptan=kaptan
        self.renk=renk
        self.cins=cins
    
    def neTur(self):
        return "{} tipi yakıt kullanan {}'nda seyredebilen araçtır".format(self.yakit,self.tur)
    
    def neYapar(self):
        return "{} yolcuyu {} hız ile taşır".format(self.kapasite,self.hiz)


class Havayolu(ARAC):
    "Havayolunda gidebilen araçlar sınıfı"
    def __init__(self,tur,yakit,kapasite,hiz,pilot,renk,cins):
        super().__init__(tur,yakit,kapasite,hiz)
        self.pilot=pilot
        self.renk=renk
        self.cins=cins
    
    def neTur(self):
        return "{} tipi yakıt kullanan {}'nda seyredebilen araçtır".format(self.yakit,self.tur)
    
    def neYapar(self):
        return "{} yolcuyu {} hız ile taşır".format(self.kapasite,self.hiz)


def genelBilgi(arac):
    arac.neTur()
    arac.neYapar()

otomobil = Karayolu()

### DAHA BİTMEDİ 