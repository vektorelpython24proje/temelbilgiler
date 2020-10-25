#Inharitance

class A:
    def __init__(self):
        self.a="A"
    
    def imet(self):
        print("Merhaba")
    
    def imet2(self):
        print(self.a)


class B(A):
    def __init__(self):
        super().__init__()
        self.b = "B"

class C(B,A):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        self.c = "C"

    def imet3(self):
        A.imet2(self)

obj1 = B()
obj1.imet()
obj1.imet2()
