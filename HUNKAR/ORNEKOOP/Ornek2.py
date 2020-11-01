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

    @property

    def vurus(self):
        return self.guc

    def vurus2(self):
        return self.guc*2

    def vurus3(self):
        return self.guc*3

    def darbe(self,guc):
        self.saglik -= guc
        return self.saglik

    def darbe2(self,guc):
        self.saglik -= guc//2
        return self.saglik
    
    def darbe3(self,guc):
        self.saglik -= guc//3
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
        self.adi = adi
        self.guc = guc
        self.saglik = saglik
        self.superGuc = superGuc

    def vurus(self):
        return self.guc

    def vurus2(self):
        return self.guc*2

    def vurus3(self):
        return self.guc*3

    def darbe(self,guc):
        self.saglik -= guc
        return self.saglik
    
    def darbe2(self,guc):
        self.saglik -= guc//2
        return self.saglik
    
    def darbe3(self,guc):
        self.saglik -= guc//3
        return self.saglik

    @property
    def durum(self):
        return f"{self.adi} Sağlık:{self.saglik}"

class DeadPool(MarvelHero):
    def __init__(self):
        super().__init__("Dead Pool",400,1000,True)

    def darbe2(self,guc):
        self.saglik -= guc//3
        return self.saglik
    
    def darbe3(self,guc):
        self.saglik -= guc//4
        return self.saglik

class Hulk(MarvelHero):
    def __init__(self):
        super().__init__("Hulk",500,1000,True)

class CaptainAmerica(MarvelHero):
    def __init__(self):
        super().__init__("Captain America",200,500,True)

# P1 = DeadPool()
# P2 = KaraMurat()
# P1.darbe(P2.vurus())
# P2.darbe(P1.vurus())
# print(P1.durum)
# print(P2.durum)

import random as rnd
import time

mListe = [DeadPool,Hulk,CaptainAmerica]
tListe = [DedeKorkut,KaraMurat,BattalGazi]
P1 = rnd.choice(mListe)()
P2 = rnd.choice(tListe)()

P1vurListe = [P1.vurus,P1.vurus2,P1.vurus3]
P1darbeListe = [P1.darbe,P1.darbe2,P1.darbe3]
P2vurListe = [P2.vurus,P2.vurus2,P2.vurus3]
P2darbeListe = [P2.darbe,P2.darbe2,P2.darbe3]

while P1.saglik > 0 and P2.saglik > 0:
    time.sleep(1)
    rnd.choice(P1darbeListe)(rnd.choice(P2vurListe)())
    rnd.choice(P2darbeListe)(rnd.choice(P1vurListe)())
    # P1.darbe(P2.vurus())
    # P2.darbe(P1.vurus())
    print(P1.durum,P2.durum)

else:
    if P1.saglik > P2.saglik:
        print(P1.adi,"Kazandı")
    else:
        print(P1.adi,"Kazanamadı")