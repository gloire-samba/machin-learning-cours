from fonctions import listFiboncaci

import math
import statistics as st
import random as rd
import os
import glob

liste1 = listFiboncaci(1000)

print(liste1)

print(math.pi)

print(st.mean(liste1))

rd.seed(0)

print(rd.choice(liste1))

print(rd.random())
print(rd.randint(5, 10))
print(rd.randrange(100))

print(rd.sample(range(100), 10))

print(rd.sample(range(100), rd.randrange(100)))

rd.shuffle(liste1)
print(liste1)

print(os.getcwd())

print(glob.glob("*"))

chemin = os.path.join(os.path.dirname(__file__), "cours6", "*.txt")

filesnames = glob.glob(chemin)

for filename in filesnames:
    with open(filename, "r") as f:
        print(f.read())


dict ={}
for filename in filesnames:
    with open(filename,"r") as f:
        dict[filename] = f.read()
        
print(dict)