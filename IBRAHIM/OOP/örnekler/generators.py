import random as rnd
liste =[i for i in range (1000)]

def luckies(liste,count):
    for i in range(count):
        yield rnd.choice(liste)

for item in luckies(liste,3):
    print(item)

print(rnd.sample(liste,3))