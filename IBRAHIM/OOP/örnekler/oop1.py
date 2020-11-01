class Araba():
    tur="Binek" #class attribute
    def __init__(self,marka,model): #constructor
        #self.renk="" instance attribute
        self.marka=marka
        #self.yakit=""
        self.model=model
        #self.guc= ""
    
    def ileri(self): #instance method
        print(self.marka + self.model,"Hareket Etti")


    def geri(self): #instance method
        print(self.marka + self.model,"Hareket Etti")

arac1= Araba("Shuriken","Explosive")
arac2= Araba("Reunault","Toros 1.20")

arac1.ileri()
arac2.ileri()