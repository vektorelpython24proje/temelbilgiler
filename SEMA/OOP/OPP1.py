# inharitance

class A:
    def __init__(self):
        self.a = "A"
    
    def imet(self):
        print("Merhaba")

    def imet2(self):
        print(self.a)

class B():
    def __init__(self):
        self.b = "B"

class C(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        self.c = "C"
    
    def imet3(self):
        A.imet2(self)

obj1 = C()
obj1.imet3()
