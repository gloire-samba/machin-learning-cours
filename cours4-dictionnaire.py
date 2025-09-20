import numpy as np


traduction = {
    "chien":"dog",
    "chat" : "cat",
    "souris":"mouse",
    "oiseau":"bird"
}

inventaire = {
    
    "bananes": 5000,
    "pommes": 2094,
    "poires":412809,
    "cerises": 2893
}

dictionaire_3 = {
    
    "dictionaire_1": traduction,
    "dictionaire_2": inventaire
}

parametre ={
    
    "w1": np.random.randn(10,100),
    "b1": np.random.randn(10,1),
    "w2": np.random.randn(10,10),
    "b2": np.random.randn(10,1)
}

print(inventaire.values())
print(inventaire.keys())

inventaire["abricots"] = 4092

print(inventaire)

print(inventaire.get("peches",0))

print(inventaire.get("cerises",0))

villes =("Paris","Berlin","Londres","Bruxelles")

inventaire2 = dict.fromkeys(villes,"défaut")


print(inventaire2)

fruit = inventaire.pop("abricots")

print(fruit)
print(inventaire)

for k in inventaire.keys():
    print(k)

for i in inventaire.values():
    print(i)
 
 
for k,v in inventaire.items():
    print(k,v)
    
def trier(classeur,nombres):
    
    if nombres >= 0 :
        classeur.setdefault("positifs", []).append(nombres)
        classeur["positifs"].sort()
    else:
        classeur.setdefault("negatifs", []).append(nombres)
        classeur["negatifs"].sort(reverse=True)  
        
    return classeur

classeur = {
    "positifs": [],
    "negatifs": []
}

print(trier(classeur,10))
print(trier(classeur,-5))
print(trier(classeur,3))
print(trier(classeur,-8))
print(trier(classeur,0))
