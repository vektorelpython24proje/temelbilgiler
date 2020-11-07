import random as rnd
liste = [ i for i in range(1000)]
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
# birincil = []
# ikincil = []

# def tekrar(liste1,liste2):
#     for item in liste1:
#         if item in liste2:
#             return True
#     if not liste1 or not liste2:
#         return True
#     return False
# while tekrar(birincil,ikincil) :
#     birincil =  rnd.sample(liste,len(liste)//2)
#     ikincil = rnd.sample(liste,len(liste)//2)
# else:
#     print(birincil,ikincil)



