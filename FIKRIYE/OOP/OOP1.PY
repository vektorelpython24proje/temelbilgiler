class A :
    def __init__(self):
        self.a = "A"

    def imet(self):
        print("Merhaba")

    def imet2(self):
        print(self.a)

class B():
    def __init__(self):
       super().__init__()
       self.b = "B"

class C(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        self.c = "C"

    def imet3()    

obj1 = C()
obj1.imet2()


class A():
    def __init__(self):
        self.a ="A"
    def imet(self):
        return self.a

class B():
    def __init__(self):
        super().__init__()
        self.b = "B"  
    def imet(self):
        print(super().imet())
        return self.b

obj1 =B()
print(obj1.imet()
obj1 = A()
print(obj1.imet())

