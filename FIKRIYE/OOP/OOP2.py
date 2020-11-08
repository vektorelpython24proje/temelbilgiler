class Kedi(): # class
    tur = "FELIS" # class attribute
    def __init__(self,ADI,yas): # constructor
        self.adi = ADI # instance attribute
        self.yas = yas
        print(f"1 {Kedi.tur} üretildi")

    def yasSoyle(self): # instance method
        print(f"{self.adi} {self.yas} yaşında")
    
    def Miyavla(self):
        print(f"{self.adi} miyavladı")

    @classmethod #decorator
    def turGetir(cls): # class method
        print(f"{cls.tur} bir eleman üretir.")

    def __del__(self): #destructor
        print(f"{self.adi} RIP")


kedi1 = Kedi("Melek",10) # object
kedi2 = Kedi("Tekir",20)
#----------------
kedi1.yasSoyle()
kedi2.yasSoyle()
#----------------
Kedi.turGetir()
#----------------
kedi1.turGetir()
kedi2.turGetir()

