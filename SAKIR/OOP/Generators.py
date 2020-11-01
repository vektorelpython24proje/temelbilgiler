import random as rnd
liste = [i for i in range(1000)]
def luckies(liste,count):
    for i in range(count):
        yield rnd.choice(liste)

x = luckies(liste,3)
print(x.__next__())
print(x.__next__())
print(x.__next__())

# for item in luckies(liste,3):
#     print(item)

# print(rnd.sample(liste,3))



# liste = [1,2,3,4,5,6,7,8]
# devam = True
# while devam:
#     secim = rnd.choice(liste)
#     while secim in birinci:
#         secim = rnd.choice(liste)
#     birinci.append(secim)
#     liste.remove(secim)
# birincil = []
# ikincil = []

# def tekrar(liste1,liste2):
#     for item in liste1:
#         if item in liste2:
#             return True
#     if not liste1 or not liste2:
#         return True
#     return False
# while tekrar(birincil,ikincil): 
#     birincil = rnd.sample(liste,len(liste)//2)
#     ikincil = rnd.sample(liste,len(liste)//2)
# else:
#     print(birincil,ikincil)

# class PowTwo:
#     def __init__(self, max=0):
#         self.n = 0
#         self.max = max

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.n > self.max:
#             raise StopIteration

#         result = 2 ** self.n
#         self.n += 1
#         return result

# print(PowTo(20).__next__())
# print(PowTo(20).__next__())
# print(PowTo(20).__next__())
# print(PowTo(20).__next__())
# print(PowTo(20).__next__())
# print(PowTo(20).__next__())
# print(PowTo(20).__next__())
# print(PowTo(20).__next__())
# print(PowTo(20).__next__())

class Deneme:

    def __init__(self,limit):
        self.limit = limit

    def __iter



