class Benchmark():
    def __init__(self,ekrankartı,oyun,fps,sıcaklık):
        self.ekrankartı=ekrankartı
        self.oyun=oyun
        self.fps=fps
        self.sıcaklık=sıcaklık

    def stats(self):
        print(f"Ekran Kartı: {self.ekrankartı}| Oyun Adı: {self.oyun}| FPS: {self.fps}| Ortalama Sıcaklık :  {self.sıcaklık}")

    
e1=Benchmark("GTX 1660 ti Notebook Series","CS:GO","150-300","70'-90'")
e2=Benchmark("RTX 2060","CSGO","300-500","60-70")
e3=Benchmark("GTX 1660 ti Desktop","CSGO","200-350","70-85")
#----------------------------------------------------------------------------
e4=Benchmark("GTX 1660 ti Notebook Series","LoL","150-200","60")
e5=Benchmark("RTX 2060","LoL","144 Sabit","50")
e6=Benchmark("GTX 1660 ti Desktop","LoL","90","60-70")
#----------------------------------------------------------------------------
e7=Benchmark("GTX 1660 ti Notebook Series","GTA 5","60-70","80-90")
e8=Benchmark("RTX 2060","GTA 5","100-150","60")
e9=Benchmark("GTX 1660 ti Desktop","GTA 5","70-90","80-90")
#----------------------------------------------------------------------------
e10=Benchmark("RTX 3080","Metro Exodus","51-67","???")


print("------------------------------------------------------------------------------------------------")
e1.stats()
print("")
print("►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►     ")
print("")
e2.stats()
print("")
print("►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►     ")
print("")
e3.stats()
print("------------------------------------------------------------------------------------------------")
print("")
e4.stats()
print("")
print("►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►     ")
print("")
e5.stats()
print("")
print("►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►     ")
print("")
e6.stats()
print("")
print("------------------------------------------------------------------------------------------------")
print("")
e7.stats()
print("")
print("►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►     ")
print("")
e8.stats()
print("")
print("►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►      ►     ")
print("")
e9.stats()
print("")
print("------------------------------------------------------------------------------------------------")
print("")
e10.stats()
print("")
print("------------------------------------------------------------------------------------------------")