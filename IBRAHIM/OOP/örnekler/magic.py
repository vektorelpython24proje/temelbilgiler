class isci:
    def __new__(cls):
        print("__new__ çalıştı kardeşim")
        inst=object.__new__(cls)
        return inst
    
    def __init__ (self):
        print("__init__ çalıştı")
        self.name="Ahmet"

e1=isci()
print(e1.name)