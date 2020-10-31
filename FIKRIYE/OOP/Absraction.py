from abc import ABC,abstractmethod

class cokgen(ABC):
    @abstractmethod
    def Kenarsayisi(self):
        pass

class Ucgen(Cokgen):
    def KenarSayisi(self):
    Rutu super().KenarSayisi()

obj1 = Ucgen()
