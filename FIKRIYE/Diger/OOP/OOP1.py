class Araba():
    tur = "Binek" # class attribute
    def __init__(self,marka,model): # constructor 
        # self.renk = "" # instance attribute
        self.marka = marka
        # self.yakit = ""
        self.model = model
        # self.guc = ""

    def ileri(self): #instance method
        print(self.marka + self.model,"Hareket etti")


    def geri(self): #instance method
        print(self.marka + self.model,"Hareket etti")

arac1 = Araba("Alfa Romeo","Stelvio")
arac2 = Araba("Reunault","Toros 1.2")

arac1.ileri()
arac2.ileri()