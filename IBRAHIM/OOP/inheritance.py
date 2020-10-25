class A:
    def __init(self):
        self.a="A"
    
    def imet(self):
        print("Merhaba")

    def imet2(self):
        print(self.a)

class B(A):
    def __init__(self):
        super().__init__()
        self.b="B"

obj1=B()
obj1.imet()