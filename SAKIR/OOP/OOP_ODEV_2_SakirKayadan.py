"""
*************************************************************
*****               Ş A K İ R    K A Y A D A N              *
*****                       OOP ÖDEVİ-2                     *
*************************************************************
1-GENEL İDARE HİZMETLERİ SINIFI
  yonetim,
  icra,
  buro memurlari
2-TEKNİK HİZMETLER SINIFI
  yüksek mühendis,
  mühendis,
  yüksek mimar,
  mimar,
  şehir plancısı,
  fizikçi,
  kimyager,
  istatistikçi,
  matematikçi,
  tekniker,
  teknisyen
3-SAĞLIK HİZMETLERİ VE YARDIMCI SAĞLIK HİZMETLERİ SINIFI
  tabip,
  diş tabibi,
  hemşire,
  hasta bakıcı,
  ebe,
  sağlık memuru,
  biyolog,
  psikolog
4-EĞİTİM VE ÖĞRETİM HİZMETLERİ SINIFI
  müfettiş,
  öğretmen
5-AVUKATLIK HİZMETLERİ SINIFI
  avukat
6-DİN HİZMETLERİ SINIFI
  imam,
  hoca,
  müezzin
7-EMNİYET HİZMETLERİ SINIFI
  emniyet müfettişi,
  polis müfettişi,
  emniyet müdürü,
  emniyet amiri,
  başkomiser,
  komiser,polis
8-YARDIMCI HİZMETLER SINIFI
  müstahdem
9-MÜLKİ İDARE AMİRLİĞİ HİZMETLERİ SINIFI
  vali,
  kaymakam,
  mahiyet memurları
10-MİLLİ İSTİHBARAT HİZMETLERİ SINIFI
  MİT personeli
11-ADALET HİZMETLERİ SINIFI
  Hakim,
  savcı,
  zabıt katibi,
  mübaşir
"""

class kamuPersoneli():
    tur = "657 nolu kanuna göre istihdam edilen kamu personeli"
    def __init__(self,ad,soyad,yas):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas

    def istihdam(self):
        print(f"{self.ad} {self.soyad} kendisine verilen görevi en iyi şekilde yapmak için çalışır.")

class genelHizmetler(kamuPersoneli):
    tur_1 = "1-GENEL İDARE HİZMETLERİ SINIFI"
    def __init__(self,ad,soyad,yas,sinif,meslek):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.sinif = sinif
        self.meslek = meslek

    def yaptigiIs(self,tur,gorev):
        self.tur = tur
        self.gorev = gorev
        print(tur)
        print("Yapılan iş: {}".format(self.gorev))
        print(
f"""
Ad      : {self.ad}
Soyadı  : {self.soyad}
Yaş     : {self.yas}
Sınıf : {self.sinif}
Meslek : {self.meslek} olarak istihdam edilmektedir.
Görevliler : yönetim,icra,büro memurlari""")

class teknikHizmetler(kamuPersoneli):
    tur_2 = "2-TEKNİK HİZMETLER SINIFI"
    def __init__(self,ad,soyad,yas,sinif,meslek):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.sinif = sinif
        self.meslek = meslek

    def yaptigiIs(self,tur,gorev):
        self.tur = tur
        self.gorev = gorev
        print(tur)
        print("Yapılan iş: {}".format(self.gorev))
        print(
f"""
Ad      : {self.ad}
Soyadı  : {self.soyad}
Yaş     : {self.yas}
Sınıf : {self.sinif}
Meslek : {self.meslek} olarak istihdam edilmektedir.
Görevliler  : yüksek mühendis,mühendis,yüksek mimar,mimar,şehir plancısı,fizikçi,kimyager,istatistikçi,matematikçi,tekniker,teknisyen
""")

class saglikHizmetler(kamuPersoneli):
    tur_3 = "3-SAĞLIK HİZMETLERİ VE YARDIMCI SAĞLIK HİZMETLERİ SINIFI"
    def __init__(self,ad,soyad,yas,sinif,meslek):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.sinif = sinif
        self.meslek = meslek

    def yaptigiIs(self,tur,gorev):
        self.tur = tur
        self.gorev = gorev
        print(tur)
        print("Yapılan iş: {}".format(self.gorev))
        print(
f"""
Ad      : {self.ad}
Soyadı  : {self.soyad}
Yaş     : {self.yas}
Sınıf : {self.sinif}
Meslek : {self.meslek} olarak istihdam edilmektedir.
Görevliler  : tabip, diş tabibi, hemşire, hasta bakıcı, sağlık memuru, ebe
""")

class egitimHizmetler(kamuPersoneli):
    tur_4 = "4-EĞİTİM VE ÖĞRETİM HİZMETLERİ SINIFI"
    def __init__(self,ad,soyad,yas,sinif,meslek):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.sinif = sinif
        self.meslek = meslek

    def yaptigiIs(self,tur,gorev):
        self.tur = tur
        self.gorev = gorev
        print(tur)
        print("Yapılan iş: {}".format(self.gorev))
        print(
f"""
Ad      : {self.ad}
Soyadı  : {self.soyad}
Yaş     : {self.yas}
Sınıf : {self.sinif}
Meslek : {self.meslek} olarak istihdam edilmektedir.
Görevliler  : müfettiş, öğretmen
""")
class avukatlikHizmetler(kamuPersoneli):
    tur_5 = "5-AVUKATLIK HİZMETLERİ SINIFI"
    def __init__(self,ad,soyad,yas,sinif,meslek):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.sinif = sinif
        self.meslek = meslek

    def yaptigiIs(self,tur,gorev):
        self.tur = tur
        self.gorev = gorev
        print(tur)
        print("Yapılan iş: {}".format(self.gorev))
        print(
f"""
Ad          : {self.ad}
Soyadı      : {self.soyad}
Yaş         : {self.yas}
Sınıf       : {self.sinif}
Meslek      : {self.meslek} olarak istihdam edilmektedir.
Görevliler  : avukat
""")

class dinHizmetler(kamuPersoneli):
    tur_6 = "6-DİN HİZMETLERİ SINIFI"
    def __init__(self,ad,soyad,yas,sinif,meslek):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.sinif = sinif
        self.meslek = meslek

    def yaptigiIs(self,tur,gorev):
        self.tur = tur
        self.gorev = gorev
        print(tur)
        print("Yapılan iş: {}".format(self.gorev))
        print(
f"""
Ad          : {self.ad}
Soyadı      : {self.soyad}
Yaş         : {self.yas}
Sınıf       : {self.sinif}
Meslek      : {self.meslek} olarak istihdam edilmektedir.
Görevliler  : imam, hoca, müezzin
""")

class emniyetHizmetler(kamuPersoneli):
    tur_7 = "7-EMNİYET HİZMETLERİ SINIFI"
    def __init__(self,ad,soyad,yas,sinif,meslek):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.sinif = sinif
        self.meslek = meslek

    def yaptigiIs(self,tur,gorev):
        self.tur = tur
        self.gorev = gorev
        print(tur)
        print("Yapılan iş: {}".format(self.gorev))
        print(
f"""
Ad          : {self.ad}
Soyadı      : {self.soyad}
Yaş         : {self.yas}
Sınıf       : {self.sinif}
Meslek      : {self.meslek} olarak istihdam edilmektedir.
Görevliler  : emniyet müfettişi, polis müfettişi, emniyet müdürü, emniyet amiri, başkomiser, komiser, polis
""")

class yardimciHizmetler(kamuPersoneli):
    tur_8 = "8-YARDIMCI HİZMETLER SINIFI"
    def __init__(self,ad,soyad,yas,sinif,meslek):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.sinif = sinif
        self.meslek = meslek

    def yaptigiIs(self,tur,gorev):
        self.tur = tur
        self.gorev = gorev
        print(tur)
        print("Yapılan iş: {}".format(self.gorev))
        print(
f"""
Ad          : {self.ad}
Soyadı      : {self.soyad}
Yaş         : {self.yas}
Sınıf       : {self.sinif}
Meslek      : {self.meslek} olarak istihdam edilmektedir.
Görevliler  : müstahdem
""")

class mulkiHizmetler(kamuPersoneli):
    tur_9 = "9-MÜLKİ İDARE AMİRLİĞİ HİZMETLERİ SINIFI"
    def __init__(self,ad,soyad,yas,sinif,meslek):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.sinif = sinif
        self.meslek = meslek

    def yaptigiIs(self,tur,gorev):
        self.tur = tur
        self.gorev = gorev
        print(tur)
        print("Yapılan iş: {}".format(self.gorev))
        print(
f"""
Ad          : {self.ad}
Soyadı      : {self.soyad}
Yaş         : {self.yas}
Sınıf       : {self.sinif}
Meslek      : {self.meslek} olarak istihdam edilmektedir.
Görevliler  : vali, kaymakam, mahiyet memurları
""")

class mitHizmetler(kamuPersoneli):
    tur_10 = "10-MİLLİ İSTİHBARAT HİZMETLERİ SINIFI"
    def __init__(self,ad,soyad,yas,sinif,meslek):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.sinif = sinif
        self.meslek = meslek

    def yaptigiIs(self,tur,gorev):
        self.tur = tur
        self.gorev = gorev
        print(tur)
        print("Yapılan iş: {}".format(self.gorev))
        print(
f"""
Ad          : {self.ad}
Soyadı      : {self.soyad}
Yaş         : {self.yas}
Sınıf       : {self.sinif}
Meslek      : {self.meslek} olarak istihdam edilmektedir.
Görevliler  : MİT personeli
""")

class adaletHizmetler(kamuPersoneli):
    tur_11 = "11-ADALET HİZMETLERİ SINIFI"
    def __init__(self,ad,soyad,yas,sinif,meslek):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.sinif = sinif
        self.meslek = meslek

    def yaptigiIs(self,tur,gorev):
        self.tur = tur
        self.gorev = gorev
        print(tur)
        print("Yapılan iş: {}".format(self.gorev))
        print(
f"""
Ad          : {self.ad}
Soyadı      : {self.soyad}
Yaş         : {self.yas}
Sınıf       : {self.sinif}
Meslek      : {self.meslek} olarak istihdam edilmektedir.
Görevliler  : Hakim, savcı, zabıt katibi, mübaşirMİT personeli
""")

HIZMETLER = [
    "1-GENEL İDARE HİZMETLERİ SINIFI",\
    "2-TEKNİK HİZMETLER SINIFI",\
    "3-SAĞLIK HİZMETLERİ VE YARDIMCI SAĞLIK HİZMETLERİ SINIFI",\
    "4-EĞİTİM VE ÖĞRETİM HİZMETLERİ SINIFI",\
    "5-AVUKATLIK HİZMETLERİ SINIFI",\
    "6-DİN HİZMETLERİ SINIFI",\
    "7-EMNİYET HİZMETLERİ SINIFI",\
    "8-YARDIMCI HİZMETLER SINIFI",\
    "9-MÜLKİ İDARE AMİRLİĞİ HİZMETLERİ SINIFI",\
    "10-MİLLİ İSTİHBARAT HİZMETLERİ SINIFI",\
    "11-ADALET HİZMETLERİ SINIFI"
]

TODO:Hizmetlerde sözlük kullanamadım. Tekrar incelenecek
# HIZMETLER = {
#     "1":"GENEL İDARE HİZMETLERİ SINIFI",\
#     "2":"TEKNİK HİZMETLER SINIFI",\
#     "3":"SAĞLIK HİZMETLERİ VE YARDIMCI SAĞLIK HİZMETLERİ SINIFI",\
#     "4":"EĞİTİM VE ÖĞRETİM HİZMETLERİ SINIFI",\
#     "5":"AVUKATLIK HİZMETLERİ SINIFI",\
#     "6":"DİN HİZMETLERİ SINIFI",\
#     "7":"EMNİYET HİZMETLERİ SINIFI",\
#     "8":"YARDIMCI HİZMETLER SINIFI",\
#     "9":"MÜLKİ İDARE AMİRLİĞİ HİZMETLERİ SINIFI",\
#     "10":"MİLLİ İSTİHBARAT HİZMETLERİ SINIFI",\
#     "11":"ADALET HİZMETLERİ SINIFI"}

MEMURLAR = [
    ["Şakir","Kayadan",25,HIZMETLER[0],"Memur"],
    ["Kenan","Kayadan",24,HIZMETLER[1],"Mühendis"],
    ["Busenur","Kayadan",22,HIZMETLER[2],"Hemşire"],
    ["Büşragül","Kayadan",23,HIZMETLER[3],"Öğretmen"],
    ["Ahmet","Çelik",28,HIZMETLER[4],"Avukat"],
    ["Aydın","Çelik",32,HIZMETLER[5],"Müezzin"],
    ["Osman","Gülcan",25,HIZMETLER[6],"Komiser"],
    ["Bünyamin","Durmaz",28,HIZMETLER[7],"Müstahdem"],
    ["Murat","Kolukısa",33,HIZMETLER[8],"Kaymakam"],
    ["Mustafa","Boğazlık",35,HIZMETLER[9],"Mit Personeli"],
    ["Zehra","Durmaz",22,HIZMETLER[10],"Savcı"]
]

TODO: Hizmet sınıflarını kullanamadım. Tekrar incelenecek.
# Hizmet_Siniflari = [
#     genelHizmetler,\
#     teknikHizmetler,\
#     saglikHizmetler,\
#     egitimHizmetler,\
#     avukatlikHizmetler,\
#     dinHizmetler,\
#     emniyetHizmetler,\
#     yardimciHizmetler,\
#     mulkiHizmetler,\
#     mitHizmetler,\
#     adaletHizmetler
#     ]

TODO: For döngüsü çözülürse, kod kısalacak.
# for hizmet in Hizmet_Siniflari:
#     for memur in MEMURLAR:
#         sayi = MEMURLAR.count()
#         for i in range(MEMURLAR.count()-1):
#             Personel = hizmet(memur)
#             Personel.istihdam()
#             Personel.yaptigiIs(HIZMETLER[i])

gorevler = {
    1:"Büro işleri yapar.",
    2:"Teknik işlerde çalışır.",
    3:"İnsanları tedavi eder.",
    4:"İnsanları eğitir ve bilgilendirir.",
    5:"Adaletin savunma görevini icra eder.",
    6:"Manevi bilgiler verir.",
    7:"Aşayişi düzenli halde tutar.",
    8:"Destek hizmetler verir.",
    9:"Kamu yönetim görevini icra eder.",
    10:"İç ve dış güvenliğimizi sağlar.",
    11:"Adalet hizmetlerini düzenler."
    }

for i in range(len(MEMURLAR)):
    Personel1 = genelHizmetler(MEMURLAR[i][0],MEMURLAR[i][1],MEMURLAR[i][2],MEMURLAR[i][3],MEMURLAR[i][4])
    Personel1.istihdam()
    Personel1.yaptigiIs(HIZMETLER[i],gorevler[i+1])
    print(80*"*")
