
class A:
    def __init__(self):
        self.a = "A"
    
    def imet(self):
        print("Merhaba")
    
    def imet2(self):
        print(self.a)


class B(A):
    def __init__(self):
        super().__init__()
        self.b = "B"


obj1 = B()
obj1.imet()


var1="metin"
var2=[1,2,3,4]
print(len(var1))
print(len(var2))

def add(x,y,z=0):
    return x+y+z

print(add(2,3))
print(add(2,3,4))


class Azerbaycan():
    def baskent(self):
        print("Bakü<3")

    def dil(self):
        print("türkçe")

    def type(self):
        print("demokrasi")

class Turkiye():
    def baskent(self):
        print("Ankara<3")

    def dil(self):
        print("türkçe")

    def type(self):
        print("demokrasi cumhuriyet")

obj1=Azerbaycan()
obj2=Turkiye()

for ulke in (obj1,obj2)
ulke.baskent
