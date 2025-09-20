import numpy as np

A = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(A)

print(A[0,0])

print("\n")
print("\n")

print(A[0, :])

print("\n")
print("\n")

print(A[:, 0])

print("\n")
print("\n")

print(A[0])

print("\n")
print("\n")

print(A[1])

print("\n")
print("\n")

print(A[2])

print("\n")
print("\n")

B = A[0:2, 0:2]

print(B)

print(B.shape)

print("\n")
print("\n")

A[0:2, 0:2] = 10

print(A)

print("\n")
print("\n")

print(A[:,-2:])

B = np.zeros((4,4))
print(B)

print("\n")
print("\n")

B[1:3, 1:3] = 1

print(B)

print("\n")
print("\n")


C = np.zeros((5,5))
print(C)

print("\n")
print("\n")

C[:: 2, :: 2] = 1

print(C)

print("\n")
print("\n")

A2 = np.random.randint(0,10,(5,5))

print(A2)

print("\n")
print("\n")

print(A2 < 5)

print("\n")
print("\n")

A2[A2<5] = 10

print(A2)

print("\n")
print("\n")


print(A[A>5])
print(A[A>5].shape)

