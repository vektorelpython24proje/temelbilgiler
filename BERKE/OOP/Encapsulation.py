# encapsulation
# class A:
#     __tur = "A"
#     def __init__(self):
#         self.a = 1
#         self.__gizli = 2

#     def gizli(self):
#         if self.a == 1:
#             return self.__gizli
#         else:
#             return "Değiştirilmiştir."

# # # Private
# # # __gizli gizli
# # # __gizli_ gizli
# # # __gizli__ gizli değil

# # # Semi Private
# # # _yarigizli

# obj1 = A()
# print(obj1.gizli())


# encapsulation
class A:
    __tur = "A"
    def __init__(self):
        self.a = 1
        self.__gizli = 2

    @property
    def gizli(self):
        if self.a == 1:
            return self.__gizli
        else:
            return "Değiştirilmiştir."

    @gizli.setter
    def gizli(self,var):
        if isinstance(var,int):
            self.__gizli = var

    @gizli.deleter
    def gizli(self):
        self.a = 1
        self.__gizli = 2
        
obj1 = A()
print("Gizli Değer",obj1.gizli)
obj1.gizli = "as"
print("Gizli Değer",obj1.gizli)
obj1.gizli = 6
print("Gizli Değer",obj1.gizli)
obj1.a = 4
print("Gizli Değer",obj1.gizli)
del obj1.gizli
print("Gizli Değer",obj1.gizli)

