### DAHA BİTMEDİ

class ARAC():
  "Ulaşım veya taşıma amaçlı üretilen araçlar sınıfı"
    def __init__(self,tur,yakit,kapasite,hız):
        self.tur = tur
        self.yakit = yakit
        self.kapasite = kapasite
        self.hız = hız

    def neTur(self):
        return "{} tipi yakıt kullanan {}'nda seyredebilen araçtır".format(self.yakit,self.tur)

    def neYapar(self):
        return "{} yolcuyu {} hız ile taşır".format(self.kapasite,self.hız)


class Karayolu(ARAC):
    "Karayolunda gidebilen araçlar sınıfı"
    def __init__(self,tur,yakit,kapasite,hız,marka,renk,cins):
        super().__init__(tur,yakıt,kapasite,hız)
        self.marka=marka
        self.renk=renk
        self.cins=cins
class Denizyolu(ARAC):
    "Denizyolunda gidebilen araçlar sınıfı"
    def __init__(self,tur,yakit,kapasite,hız,kaptan,renk,cins):
        super().__init__(tur,yakıt,kapasite,hız)
        self.kaptan=kaptan
        self.renk=renk
        self.cins=cins
class Havayolu(ARAC):
    "Havayolunda gidebilen araçlar sınıfı"
    def __init__(self,tur,yakit,kapasite,hız,pilot,renk,cins):
        super().__init__(tur,yakıt,kapasite,hız)
        self.pilot=pilot
        self.renk=renk
        self.cins=cins

otomobil1= ARAC("karayolu","benzin",5,"250km/h")
uçak1=ARAC("havayolu","mazot",150,"450km/h")
yat1=ARAC("denizyolu","blendoil",5000,"19knot")^

### DAHA BİTMEDİ 