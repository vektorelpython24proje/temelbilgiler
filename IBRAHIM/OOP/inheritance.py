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
        self.b="B"

class C(A,B):
    def __init__(self):
        A.__init__()
        B.__init__()

 
obj1=C()
obj1.imet2()