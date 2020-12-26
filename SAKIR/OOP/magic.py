# __new__
class isci:
    sayi = 0
    def __new__(cls):
        print("__new__ çalıştı")
        inst = object.__new__(cls)
        return inst
    def __init__(self):
        print("__init__ çalıştı")
        self.name = "Ahmet"

e1 = isci()
print(e1.name)
print(isci.sayi)
e2 = isci()
print(isci.sayi)

sayi = 10
# sayi + 5
print(sayi.__add__(5))


class TurkishHero():
    def __init__(self,adi,guc,saglik):
        self.adi = adi
        self.guc = guc
        self.saglik = saglik

    def __str__(self):
        return self.adi + " " + str(self.guc)

    def __repr__(self):
        return self.adi + " " + str(guc)

    def __ge__(self,x):
        if x.guc >= self.guc:
            return True
        else:
            return False

    def __iadd__(self,guc):
        self.guc += guc


h1 = TurkishHero("Taksim Dayı",20,100)
h2 = TurkishHero("Aleyna",50,100)
# deneme = str(h1)
# print(deneme)

if h2>=h1:
    print("Doğru")

"""
https://www.tutorialsteacher.com/python/magic-methods-in"
"""