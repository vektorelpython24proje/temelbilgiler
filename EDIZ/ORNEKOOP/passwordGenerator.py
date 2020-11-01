import os
import random as rnd
class PassGen:
    def __init__(self,var1,var2):
        self.var1 = var1
        self.var2 = var2
        self.NKarList = """ _,;:.-_'^+%&/()=}{[]*!'" """
    
    def passControl(self,password):
        bHarf = NKar = Num =kHarf = False
        sonuc = ""
        if len(password)>=8:
            for item in password:
                if item.isupper() and not bHarf:
                    bHarf = True
                elif item.islower()  and not kHarf:
                    kHarf = True
                elif item.isdigit() and not Num:
                    Num = True
                elif item in self.NKarList and not NKar:
                    NKar = True
        else:
            sonuc = "Uzunluk"
        sonuc +=  f"""
          {"* Büyük Harf" if not bHarf else ""}
          {"* Küçük Harf" if not kHarf else ""}
          {"* Numara " if not Num else ""}
          {"* Karakter " if not NKar else ""}
         """
        return sonuc

    def passControlCheck(self,password):
        bHarf = NKar = Num =kHarf = False
        if len(password)>=8:
            for item in password:
                if item.isupper() and not bHarf:
                    bHarf = True
                elif item.islower()  and not kHarf:
                    kHarf = True
                elif item.isdigit() and not Num:
                    Num = True
                elif item in self.NKarList:
                    NKar = True
        else:
            return False
        return bHarf and NKar and Num and kHarf
      
    def sifreUret(self):
        Fonkvar1 = lambda :rnd.choice(self.var1).lower()
        Fonkvar1Up = lambda :rnd.choice(self.var1).upper()
        Fonkvar2 = lambda :rnd.choice(self.var2).lower()
        Fonkvar2Up = lambda :rnd.choice(self.var2).upper()
        FonknKar =  lambda :self.NKarList[rnd.randrange(0,len(self.NKarList))]
        FonkNum = lambda :str(rnd.randint(0,9))
        liste = [Fonkvar1,Fonkvar1Up,FonknKar,FonkNum,Fonkvar2,Fonkvar2Up]
        sonuc = ""
        while not self.passControlCheck(sonuc):
            sonuc += rnd.choice(liste)()
        return sonuc


print(PassGen("İbrahim","ediz").sifreUret())

