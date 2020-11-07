#------------------------------------------------------------------------------------------------

class SistemGereksinimi():
    tur="Bilgisayar"
    def __init__(self,oyun,ekrankarti,islemci,ram,depolama):
        self.oyun = oyun
        self.ekrankarti = ekrankarti
        self.islemci = islemci
        self.ram = ram
        self.depolama = depolama
    def gereksinim(self):
        print(f"Oyun Adı: {self.oyun} | Ekran Kartı: {self.ekrankarti} | İşlemci: {self.islemci} | Ram: {self.ram} | Depolama: {self.depolama}")

#-------------------------------------------------------------------------------------------------

print("---------------------MİNİMUM SİSTEM GEREKSİNİMLERİ---------------------")

oyun1=SistemGereksinimi("CSGO","NVidia GeForce GT 420","Intel® Core™ 2 Duo E6600","4 GB","15 GB kullanılabilir alan")
oyun2=SistemGereksinimi("LOL","Nvidia GeForce 8800","3 GHz çift çekirdekli işlemci","4 GB","16 GB kullanılabilir alan")
oyun3=SistemGereksinimi("GTA5","NVIDIA 9800 GT 1 GB","İntel Core 2 Quad, Q6600","4 GB","80 GB kullanılabilir alan")
oyun4=SistemGereksinimi("Rainbow Six Siege"," NVIDIA GeForce GTX 460","Intel Core i3 560 @ 3.3 GHz","6 GB","30 GB kullanılabilir alan")
oyun5=SistemGereksinimi("Fortnite","Intel HD 4000","i3 2.4 Ghz","4 GB","30 GB kullanılabilir alan")
oyun6=SistemGereksinimi("Cod Warzone","NVIDIA GeForce GTX 670 2 GB","Intel Core i3 4340","8 GB","175 GB kullanılabilir alan")
oyun7=SistemGereksinimi("Battlerite","Intel HD 3000","Intel ya da AMD çift çekirdekli 2.8 GHz işlemci","4 GB","3 GB kullanılabilir alan")
oyun8=SistemGereksinimi("Payday2","NVIDIA GeForce 8800","Intel Dual Core 2 Ghz","2 GB","13 GB kullanılabilir alan")
oyun9=SistemGereksinimi("PUBG","NVIDIA GeForce GTX 960 2GB","Intel i5-4430","8 GB","30 GB kullanılabilir alan")
oyun10=SistemGereksinimi("Forza Horizon 4","NVIDIA GTX 650 Ti","Intel i3-4170 @ 3.7Ghz","8 GB","75 GB kullanılabilir alan")

#-------------------------------------------------------------------------------------------------

print("")
print("►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►     ")
print("")
oyun1.gereksinim()
print("")
print("►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►     ")
print("")
oyun2.gereksinim()
print("")
print("►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►     ")
print("")
oyun3.gereksinim()
print("")
print("►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►     ")
print("")
oyun4.gereksinim()
print("")
print("►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►     ")
print("")
oyun5.gereksinim()
print("")
print("►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►     ")
print("")
oyun6.gereksinim()
print("")
print("►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►     ")
print("")
oyun7.gereksinim()
print("")
print("►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►     ")
print("")
oyun8.gereksinim()
print("")
print("►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►     ")
print("")
oyun9.gereksinim()
print("")
print("►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►     ")
print("")
oyun10.gereksinim()
print("")
print("►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►     ")
print("")

#-------------------------------------------------------------------------------------------------