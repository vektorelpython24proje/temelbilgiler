import time
import math


class A():
    def __init__(self):
        self.a="A"

    @staticmethod
    def pi():
        return 22/7

obj1 =A()
print(obj1.pi())

def hesapzaman(fonk):
    def icfonk(*args,**kwargs):
        basla =time.time()
        fonk(*args,**kwargs)
        bitis=time.time()
        fonk(*args,**kwargs)
        #|------------------
        print("Bu işlem için geçen zaman:" , fonk.__name__,bitis-basla)

    return icfonk

@hesapzaman
def birlestirCon(*args):
    sonuc=" "
    for item in args:
        sonuc += " "+item
    
    print(sonuc)

@hesapzaman
def birlestirJoin(*args):
    time.sleep(1)
    print(" ".join(args))

birlestirCon("UWUWEWEWE","ONYETENWEWE","UGWEUHEM","OSAS","UWUWEWEWE","ONYETENWEWE","UGWEUHEM","OSAS","UWUWEWEWE","ONYETENWEWE","UGWEUHEM","OSAS")
birlestirJoin("UWUWEWEWE","ONYETENWEWE","UGWEUHEM","OSAS","UWUWEWEWE","ONYETENWEWE","UGWEUHEM","OSAS","UWUWEWEWE","ONYETENWEWE","UGWEUHEM","OSAS")