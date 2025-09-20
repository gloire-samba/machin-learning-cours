import numpy as np


print(round(6,89655))

liste1 = [True, False, True, False]

print(all(liste1))

print(any(liste1))

x = 10

print(type(x))

x = str(x)

print(x)

print(type(x))

y = "20"

y= int(y)

print(type(y))

liste2 = [-12,40,10,0,3]

print(min(liste2))
print(max(liste2))

tuple1 = tuple(liste2)
print(tuple1)

liste3 = list(tuple1)
print(liste3)

inventaire = {
    
    "bananes": 5000,
    "pommes": 2094,
    "poires":412809,
    "cerises": 2893
}

liste4 = list(inventaire.keys())
print(liste4)

#x = int(input("Entrez un nombre: "))

#print(type(x))

x = 25
ville = "Nantes"

message = "La température est de {}°C à {}".format(x,ville)
print(message)

message = f"La température est de {x}°C à {ville}"
print(message)

parametre ={
    
    "w1": np.random.randn(10,100),
    "b1": np.random.randn(10,1),
    "w2": np.random.randn(10,10),
    "b2": np.random.randn(10,1)
}

for i in range(1,3):
    print("couche", i)
    print(parametre["w{}".format(i)])
    
print("\n")
print("\n")
    
for i in range(1,3):
    print("couche", i)
    print(parametre[f"w{i}"])

'''f = open("fichier.txt","w")
f.write("Bonjour")
f.close()'''

f = open("fichier.txt","r")
print(f.read())
f.close()

with open("fichier.txt","r") as f:
    print(f.read())


'''with open("calcule.txt", "w") as f:
    
    for i in range(10):
        f.write(f"{i}^2 = {i**2}\n")'''
        
with open("calcule.txt", "r") as f:
    
    liste5 = [line.strip() for line in f]
    
print(liste5)

with open("calcule.txt", "r") as f:
    
    dictionnaire = {gauche:droite for line in f for gauche, droite in [line.strip().split("=")]}
    
  
print(dictionnaire)      