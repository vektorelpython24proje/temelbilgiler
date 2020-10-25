import time
class Basketbol():
    tur="NBA"
    def __init__(self,oyuncu,ayakkabi,numara):#concstructor
        self.oyuncu = oyuncu
        self.ayakkabi = ayakkabi
        self.numara = numara
    def oyuncuinfo(self):
        print(f"{self.oyuncu} Oyuncu Adı II {self.numara} Numara II {self.ayakkabi} Giydiği Ayakkabı")
    
    def dunk(self):#instance method
        print(f"{self.oyuncu}  Potaya Bastı !!!")

    def ayakkabiinfo(self):
        print(f"{self.ayakkabi} giydiği ayakkabısı bu fiyatı epey pahalı olmalı :d")
    
    def threepoint(self):
        print(f"{self.oyuncu} 3'lüğü potaya sokuyor!!!")
    
    @classmethod
    def turGetir(cls):#class method
        print(f"{cls.tur} bir takım üretir")
    def __del__(self):
        print(f"{self.oyuncu} RIP KOBE")


oyuncu1= Basketbol("Kyrie Irving","Flytrap 3 Metallic Gold",13)#object
oyuncu2= Basketbol("Allen İverson","PG 2.5",25)
#----------------
print("--------------------------------------------")
oyuncu1.oyuncuinfo()
oyuncu2.oyuncuinfo()
print("--------------------------------------------")
time.sleep(2)
#-----------------
print("--------------------------------------------")
oyuncu1.ayakkabiinfo()
oyuncu2.ayakkabiinfo()
print("--------------------------------------------")
time.sleep(2)
#-----------------
print("--------------------------------------------")
oyuncu1.dunk()
oyuncu2.dunk()
print("--------------------------------------------")
time.sleep(2)
#-----------------
print("--------------------------------------------")
oyuncu1.threepoint()
oyuncu2.threepoint()
print("--------------------------------------------")
time.sleep(2)
#-----------------
print("--------------------------------------------")
oyuncu1.turGetir()
oyuncu2.turGetir()
print("--------------------------------------------")
time.sleep(2)