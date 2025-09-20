
import time


start = time.time()
list_1 = [i**2 for i in range(10)]
print(list_1)
end = time.time()
print(end - start)

list_2 = [[i+j for i in range(3)]for j in range(3)]

print(list_2)

prenoms =["Pierre","Jean","Julie","Sophie"]

dico ={k:v for k,v in enumerate(prenoms)}

print(dico)

ages =[24,62,10,23]

dico_2 = {k:v for k,v in zip(prenoms,ages)}

print(dico_2)

dico_3 ={prenom:age for prenom,age in zip(prenoms,ages) if age > 20} 

print(dico_3)

tuple_1 = tuple(i**2 for i in range(10))    
print(tuple_1)

dico_4 ={k:k**2 for k in range(21)}

print(dico_4)