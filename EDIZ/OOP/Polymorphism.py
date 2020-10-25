# polymorphism

# fonksiyonlarda polymorphism

# var1 = "metin"
# var2 = [1,2,3,4]
# print(len(var1))
# print(len(var2))

# def add(x,y,z=0):
#     return x+y+z

# print(add(2,3))
# print(add(2,3,4))

class Azerbaycan():
    def baskent(self):
        print("Bakü Azerbaycan Başkentidir.")

    def dil(self):
        print("Türkçe")

    def type(self):
        print("Demokrasi")


class Turkiye():
    def baskent(self):
        print("Ankara Türkiye Başkentidir.")

    def dil(self):
        print("Türkçe")

    def type(self):
        print("Demokrasi-Cumhuriyet")

obj1 = Azerbaycan()
obj2 = Turkiye()

for ulke in (obj1,obj2):
    ulke.baskent()
    ulke.dil()
    ulke.type()