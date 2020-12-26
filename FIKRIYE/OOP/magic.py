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


class TurkishHero():
    def __init__(self,adi,guc,saglik):
        self.adi = adi
        self.guc = guc
        self.saglik = saglik

    def __str__(self):
        return self.adi + " " + str(self.guc)

    def __repr__(self):
        return self.adi + "-" + str(self.guc)


    def __ge__(self,x):
        if x.guc >= self.guc:
            return False
        else:
            return True

    def __iadd__(self,guc):
        self.guc += guc


h1 = TurkishHero("Taksim Dayı",20,100)
h2 = TurkishHero("Aleyna",50,100)
# deneme = str(h1)
# print(deneme)

print(h1.guc)
h1.guc += 60
print(h1.guc)

"""
https://www.tutorialsteacher.com/python/magic-methods-in-python#:~:text=Python%20%2D%20Course%20%26%20Books-,Python%20%2D%20Magic%20Methods,%22magic%22%20to%20your%20class.&text=As%20you%20can%20see%20above,two%20numbers%20using%20the%20%2B%20operator.
"""
