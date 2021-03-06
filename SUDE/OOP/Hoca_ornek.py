from abc import ABC,abstractmethod,abstractproperty
class Hero(ABC):
    @abstractmethod
    def vurus(self):
        pass
    @abstractmethod
    def darbe(self,guc):
        pass

    @abstractproperty
    def durum(self):
        pass


class TurkishHero(Hero):
    def __init__(self,adi,guc,saglik):
        self.adi = adi
        self.guc = guc
        self.saglik = saglik

    def vurus(self):
        return self.guc
    
    def darbe(self,guc):
        self.saglik -= guc
        return self.saglik
    
    @property
    def durum(self):
        return f"{self.adi} Sağlık:{self.saglik}"

class DedeKorkut(TurkishHero):
    def __init__(self):
        super().__init__("Dede Korkut",200,1000)

class KaraMurat(TurkishHero):
    def __init__(self):
        super().__init__("Kara Murat",300,900)

class BattalGazi(TurkishHero):
    def __init__(self):
        super().__init__("Battal Gazi",250,1000)


class MarvelHero(Hero):
    def __init__(self,adi,guc,saglik,superGuc):
        self.superGuc = superGuc
        self.adi = adi
        self.guc = guc
        self.saglik = saglik
    def vurus(self):
        return self.guc
    
    def darbe(self,guc):
        self.saglik -= guc
        return self.saglik

    @property
    def durum(self):
        return f"{self.adi} Sağlık:{self.saglik}"
    
class DeadPool(MarvelHero):
    def __init__(self):
        super().__init__("DeadPool",400,600,True)

class Hulk(MarvelHero):
    def __init__(self):
        super().__init__("Hulk",500,1000,True)

class CaptainAmerica(MarvelHero):
    def __init__(self):
        super().__init__("Captain America",200,500,True)


import random as rnd
import time

mListe[DeadPool,Hulk,CaptainAmerica]
tListe[DedeKorkut,KaraMurat,BattalGazi]

P1 = rnd.choice(mListe)()
P2=rnd.choice(tListe)()

while P1.saglik > 0 and P2.saglik>0:
    time.sleep()
    P1.darbe(P2.vurus())

