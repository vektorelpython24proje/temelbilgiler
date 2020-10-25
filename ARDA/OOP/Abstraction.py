from abc import ABC,abstractmethod
class Cokgen(ABC):
    @abstractmethod
    def KenarSayisi(self):
        return "NE bileyim ben"

class Ucgen(Cokgen):
    def KenarSayisi(self):
        return 3


class Kare(Cokgen):
    def KenarSayisi(self):
        return 4

obj1 = Ucgen()
obj2 = Kare()
