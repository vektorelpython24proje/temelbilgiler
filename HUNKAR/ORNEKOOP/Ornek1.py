from abc import ABC,abstractmethod

class Hero(ABC):
    @abstractmethod
    def vurus(self):
        pass

    @abstractmethod
    def darbe(self,guc):
        pass

class TurkishHero(Hero):
    def __init__(self,adi,guc,saglik):
        self.adi = adi
        self.guc = guc
        self.saglik = saglik

    def vurus(self):
        return self.guc

    def darbe(self,guc):
        return self.saglik - guc

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

    def darbe(self,guc):
        return self.saglik - guc

class DeadPool(MarvelHero):
    def __init__(self):
        super().__init__("Dead Pool",400,1000,True)

class Hulk(MarvelHero):
    def __init__(self):
        super().__init__("Hulk",500,1000,True)

class CaptainAmerica(MarvelHero):
    def __init__(self):
        super().__init__("Captain America",200,500,True)