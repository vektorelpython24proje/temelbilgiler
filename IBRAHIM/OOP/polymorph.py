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
        print("Bakü Azerbaycanın Başkentidir")
        
    def dil(self):
        print("Türkçe")
    
    def typex(self):
        print("Demokrasi")

class Turkiye():
    def baskent(self):
        print("Ankara Türkiye Başkentidir")
    
    def dil(self):
        print("Törkiş")
        
    def typex(self):
        print("karma")

