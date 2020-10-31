from abc import ABC,abstractmethod
#Fikriye İlik

class roman(ABC):
  @abstractmethod
  def RomanTürü(self):
    return"Türü ne"

class Tarihiroman(roman):
    def Romantürü(self):
        return super().RomanTürü()

class Maceraroman(roman):
    def Romantürü(self):
        return super().RomanTürü()  

class Sosyalroman(roman):
    def Romantürü(self):
        return super().RomanTürü()

class Tahlilroman(roman):
    def Romantürü(self):
        return super().RomanTürü()

class Bilimkurguroman(roman):
    def Bilimkurgu(self):
        return super().RomanTürü()   

class Realistroman(roman):
    def Realistroman(self):
        return super().RomanTürü()

class Romantikroman(roman):
    def Romantikroman(self):
        return super().Romantürü() 

class Naturalistroman(roman):
    def Naturalistroman(self):
        return super().Romantürü()

class Postmodern(roman):
    def Postmodern(self):
        return super().Romantürü()

    




obj1 = Tarihiroman()
obj2 = Maceraroman()
obj3 = Sosyalroman()
obj4 = Tahlilroman()
obj5 = Bilimkurguroman()
obj6 = Realistroman()
obj7 = Romantikroman()
obj8 = Naturalistroman()
obj9 = Postmodernroman()


