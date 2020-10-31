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

# Class Method polymorphism
# class Azerbaycan():
#     def baskent(self):
#         print("Bakü Azerbaycan Başkentidir.")

#     def dil(self):
#         print("Türkçe")

#     def type(self):
#         print("Demokrasi")


# class Turkiye():
#     def baskent(self):
#         print("Ankara Türkiye Başkentidir.")

#     def dil(self):
#         print("Türkçe")

#     def type(self):
#         print("Demokrasi-Cumhuriyet")

# obj1 = Azerbaycan()
# obj2 = Turkiye()

# for ulke in (obj1,obj2):
#     ulke.baskent()
#     ulke.dil()
#     ulke.type()


class A():
    def __init__(self):
        self.a = "A"
    def imet(self):
        return self.a 



class B(A):
    
    def __init__(self):
        super().__init__()
        self.b = "B"
    def imet(self):
        print(super().imet())
        return self.b


obj1 = B()
print(obj1.imet())
obj1 = A()
print(obj1.imet())
