import numpy as np

A = np.array([1,2,3])
print(A.ndim)
print(A.shape)

print("\n")
print("\n")

B = np.zeros((3,2))
print(B)
print(B.ndim)
print(B.shape)
print(type(B.shape))

print("\n")
print("\n")

C = np.ones((3,4))
print(C)
print(C.size)

print("\n")
print("\n")

D = np.full((2,3),9)
print(D)

print("\n")
print("\n")

np.random.seed(0)
E = np.random.random((3, 4))
print(E)

print("\n")
print("\n")

F = np.eye(4)
print(F)

print("\n")
print("\n")

print(np.linspace(0,10,20))

print("\n")
print("\n")

print(np.arange(0,10,1))

print("\n")
print("\n")

print(np.arange(0,10,0.5))

print("\n")
print("\n")

print(np.linspace(0,10,20,dtype=np.float64))

print("\n")
print("\n")

print(np.linspace(0,10,20,dtype=np.float16))

print("\n")
print("\n")

A2 = np.zeros((3,2))
B2 = np.ones((3,2))

C2 = np.hstack((A2,B2))

print(C2)
print(C2.shape)

print("\n")
print("\n")

D2 = np.vstack((A2,B2))
print(D2)
print(D2.shape)

print("\n")
print("\n")

E2 = np.concatenate((A2,B2), axis= 0)
print(E2)

print("\n")
print("\n")

F2 = np.concatenate((A2,B2), axis=1)
print(F2)

print("\n")
print("\n")

print(E2.size)

print("\n")
print("\n")

G = E2.reshape((3,4))
print(G)

print("\n")
print("\n")


A = np.array([1,2,3])

A = A.reshape((A.shape[0],1))

print("nouvau A ",A)

print(A.shape)

print("\n")
print("\n")

A= A.squeeze()

print("après squeeze A ",A)

print(A.shape)

print("\n")
print("\n")

print(E2.ravel())


def initialisation(m,n):
    matrice = np.random.randn(m, n)
    biais = np.ones((m,1))
    return np.concatenate((matrice,biais), axis=1)

print("\n")
print("\n")

print(initialisation(3,4))