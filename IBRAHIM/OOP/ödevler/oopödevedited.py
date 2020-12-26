
from abc import ABC,abstractmethod,abstractproperty #abstract sınıfıf ve metodları import ettik
import random as rnd
import time

class Hero(ABC): #Bidaha Bidaha Yazmamak için bir zemin Hazırladık
    @abstractmethod
    def vurus(self): #şablon
        pass

    @abstractmethod
    def darbe(self,guc):#şablon
        pass

    @abstractproperty
    def durum(self):#şablon
        pass

class TurkishHero(Hero):#kahramanları kategoriye ayırmak için 
    def __init__(self,ad,guc,saglik): #initialize yani constructor yapılandırıcı oluşturucu
        self.ad=ad
        self.guc=guc
        self.saglik=saglik
    
    def vurus(self): #absract classlaarın şablonlarına atama yaptık (vurus)
        return self.guc
    
    def darbe(self,guc): #absract classlaarın şablonlarına atama yaptık (aldığı darbe)
        self.saglik -= guc
        return self.saglik

    def vurus2(self):
        return self.guc*2

    def vurus3(self):
        return self.guc*3

    def darbe2(self,guc):
        self.saglik -= guc//2
        return self.saglik

    def darbe3(self,guc):
        self.saglik -= guc//3
        return self.saglik    

    @property
    def durum(self):
        return f"{self.ad} Sağlık:{self.saglik}"



# parent sistemi kullanarak baştan initialize etmemize gerek kalmadan parametreleri girdik
class DedeKorkut(TurkishHero): 
    def __init__(self):
        super().__init__("Dede Korkut",200,10000)

# parent sistemi kullanarak baştan initialize etmemize gerek kalmadan parametreleri girdik
class KaraMurat(TurkishHero):
    def __init__(self):
        super().__init__("Kara Murat",300,9000)

class BattalGazi(TurkishHero):# parent sistemi kullanarak baştan initialize etmemize gerek kalmadan parametreleri girdik
    def __init__(self):
        super().__init__("Battal Gazi",400,10000)

class MarvelHero(Hero):
    def __init__(self,ad,guc,saglik,superGucci): #initialize yani constructor yapılandırıcı oluşturucu
        self.ad=ad
        self.guc=guc
        self.saglik=saglik
        self.superGucci=superGucci
    
    def vurus(self): #absract classlaarın şablonlarına atama yaptık (vurus)
        return self.guc
    
    def darbe(self,guc): #absract classların şablonlarına atama yaptık (aldığı darbe)
        self.saglik -= guc
        return self.saglik

    def vurus2(self):
        return self.guc*2

    def vurus3(self):
        return self.guc*3

    def darbe2(self,guc):
        self.saglik -= guc//2
        return self.saglik

    def darbe3(self,guc):
        self.saglik -= guc//3
        return self.saglik    

    @property
    def durum(self):
        return f"{self.ad} Sağlık:{self.saglik}"


# parent sistemi kullanarak baştan initialize etmemize gerek kalmadan parametreleri girdik
class Dedpul(MarvelHero):
    def __init__(self):
        super().__init__("Deadpool",400,6000,True)

# parent sistemi kullanarak baştan initialize etmemize gerek kalmadan parametreleri girdik
class HalkEkmek(MarvelHero):
    def __init__(self):
        super().__init__("Hulk",300,10000,True)

# parent sistemi kullanarak baştan initialize etmemize gerek kalmadan parametreleri girdik
class USA(MarvelHero):
    def __init__(self):
        super().__init__("Captain Amariganya",200,5000,False)


#birbirleriyle eşleştirmek için onları listeledik
mList=[Dedpul,HalkEkmek,USA]
tList=[DedeKorkut,KaraMurat,BattalGazi]


 #random fonksiyonuyla iki tane eleman aldırdık
P1= rnd.choice(mList)()
P2= rnd.choice(tList)()



P1vurListe = [P1.vurus,P1.vurus2,P1.vurus3] #katlanma vuruşları
P1darbeListe = [P1.darbe,P1.darbe2,P1.darbe3]

P2vurListe = [P2.vurus,P2.vurus2,P2.vurus3] #katlanma darbeleri
P2darbeListe = [P2.darbe,P2.darbe2,P2.darbe3]

#p1 in ve p2 nin sağlığı 0 dan büyük olduğu sürece birbirlerine sırayla vurdurduk ve her vuruştan sonra durumlarını yazdırdık
while P1.saglik > 0 and P2.saglik>0:
    time.sleep(1)
    rnd.choice(P1darbeListe)(rnd.choice(P2vurListe)()) #random seçip uygula
    rnd.choice(P2darbeListe)(rnd.choice(P1vurListe)())
    print(P1.durum,"|    |",P2.durum)
