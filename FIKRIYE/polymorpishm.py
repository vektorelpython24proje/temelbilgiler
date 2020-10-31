class A():
    def __init__(self):
        self.a = "A"
    def imet(self):
        return self.a


class B(A):
    def __init__(self):
        super().__init__()
        self.b = "B"
    def imet(self):
        print(super().imet()) 
        return self.b


obj1 = B()
print(obj1.imet())         
obj1 = A()
print(obj1.imet())