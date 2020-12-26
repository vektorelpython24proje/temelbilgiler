class A:
    def __init__(self):
        self.a = "A"

    @staticmethod
    def pi():
        return 22/7

obj1 = A()
print(obj1.pi())


import time

def hesapZaman(fonk):
    def icFonk(*args,**kwargs):
        basla = time.time()
        fonk(*args,**kwargs)
        bitis = time.time()
        print("Bu işlem için geçen zaman:",fonk.__name__,bitis-basla)

    return icFonk
@hesapZaman
def birlestirCon(*args):
    time.sleep(1)
    sonuc = ""
    for item in args:
        sonuc += " " + item
    print(sonuc)
@hesapZaman
def birlestirJoin(*args):
    time.sleep(1)
    return " ".join(args)


birlestirCon("UWUWEWEWE", "ONYETENWEWE","UGWEUHEM","OSAS")
birlestirJoin("UWUWEWEWE", "ONYETENWEWE","UGWEUHEM","OSAS")

