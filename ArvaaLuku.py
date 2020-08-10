import random

i = 0
luku = random.randint(1, 20)
#arvaus = int(input("Arvaa luku 1-20 väliltä: "))

while i < 3:
    arvaus = int(input("Arvaa luku 1-20 väliltä: "))
    if arvaus > luku:
        print("Arvasit väärin! Luku on pienempi.")
    elif arvaus < luku:
        print("Arvasit väärin! Luku on isompi.")
    else:
        print("Arvasit OIKEIN!")
        break
    i += 1
