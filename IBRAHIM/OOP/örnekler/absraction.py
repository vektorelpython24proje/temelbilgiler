from abc import ABC,abstractmethod

# class abs_class(ABC):
#     def metod(self):
#         print("Normal")

#     @abstractmethod
#     def abs_method(self):
#         pass

# class A(abs_class):
#     def __init__(self):
#         self.a = 2

#     def abs_method(self):
#         return self.a


# class B(abs_class):
#     def __init__(self):
#             self.a = 2

#     def abs_method(self):
#         return self.b

# obj1 = B()
    
class Cokgen(ABC):
    @abstractmethod
    def KenarSayisi(self):
        print("Ne bileyim ben")

class Ucgen(Cokgen):
    def KenarSayisi(self):
        return 3

class Kare(Cokgen):
    def KenarSayisi(self):
        return 4

obj1 = Ucgen()
obj2= Kare()