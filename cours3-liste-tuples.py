liste_1 = [1,4,2,7,35,84]
villes =["Paris","Berlin","Londres","Bruxelles"]
liste_2 =[liste_1, villes]
liste_3 = []

tuple_1=(1,2,6,1,7)

prenom = "gloire"

print(villes[-1])
print(villes[-2])
print(villes[-3])
print(villes[-4])

print(villes[:3])
print(villes[2:])

print(villes[::2])
print(villes[::-1])   

villes.append("Dublin") 

print(villes)

villes.insert(2, "Madrid")
print(villes)

villes_2 = ["Amsterdam", "Rome"]

villes.extend(villes_2)
print(villes)

print(len(villes))

villes.sort()

print(villes)

villes.sort(reverse=True)   
print(villes)

liste_1.sort()
print(liste_1)


print(villes.count("Paris"))

if "Paris" in villes:
    print("Paris est dans la liste des villes")
else:
    print("Paris n'est pas dans la liste des villes")
    
for i in villes:
    print(i)
    
for index, valeur in enumerate(villes):
    print(index, valeur)
    
for a, b in zip(villes, liste_1):
    print(a, b)
    
def fiboncaci(n):
    
    resultat = []
    a, b = 0, 1
    while b < n:
        resultat.append(a)
        a, b = b, a+b
        
    return resultat


print(fiboncaci(1000))