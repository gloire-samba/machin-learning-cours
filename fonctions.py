def e_potentielle(masse,hauteur,g):
    return masse * g * hauteur

def check_energy(masse,hauteur,g,energie_limite) :
    return e_potentielle(masse, hauteur, g) <= energie_limite

def fiboncaci(n):
    a, b = 0, 1
    while b < n:
        print(a)
        a, b = b, a+b

def listFiboncaci(n):
    
    
    a, b = 0, 1
    resultat = [a]
    while b < n:  
        a, b = b, a+b
        resultat.append(a)
        
    return resultat

def trier(classeur,nombres):
    
    if nombres >= 0 :
        classeur.setdefault("positifs", []).append(nombres)
        classeur["positifs"].sort()
    else:
        classeur.setdefault("negatifs", []).append(nombres)
        classeur["negatifs"].sort(reverse=True)  
        
    return classeur