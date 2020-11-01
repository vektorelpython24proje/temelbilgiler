class A:
    def __init__(self):
        self.a="A"

    @staticmethod
    def pi():
        return

obj1 = A()
print(obj1.pi())

import time

def zaman(fonk):
    def icFonk (*args,**kwargs):
        basla = time.time()
        fonk(*args,**kwargs)
        bitis = time.time()
        print("dfgd")

    return icFonk
@zaman
def birles(*args):
    sonuc = ""
    for item in args:
        sonuc+= " " + item
    print(sonuc)
@zaman
def birjoin(*args):
    return " ".join(args)

birles("hjgyjjh","gjygjhjk","khkhkkjhkh","osas")
birjoin("hjgyjjh","gjygjhjk","khkhkkjhkh","osas")

