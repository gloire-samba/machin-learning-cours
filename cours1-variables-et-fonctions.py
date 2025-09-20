f = lambda x : x**2

g = lambda x,y: x**2 + y

print(f(3))

print(g(3, 5))

print(True ^ False)

def e_potentielle(masse,hauteur,g):
    return masse * g * hauteur
print(e_potentielle(masse=10, hauteur=5, g=9.81), "joules")


def check_energy(masse,hauteur,g,energie_limite) :
    return e_potentielle(masse, hauteur, g) <= energie_limite
print(check_energy(masse=10, hauteur=5, g=9.81, energie_limite=500))

print(check_energy(masse=10, hauteur=5, g=9.81, energie_limite=20))
