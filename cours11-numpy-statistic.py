import numpy as np

np.random.seed(0)

A = np.random.randint(1,10,[2,3])


print(A)

print(A.sum())

print(A.sum(axis=0))
print(A.sum(axis=1))

print(A.cumsum())

print(A.prod())

print(A.min())

print(A.min(axis=0))

print(A.argmin())

print(A.argmin(axis=0))

print(np.exp(A))

print(np.log(A))

print(np.cos(A))

print(A.mean())
print(A.std())

print(A.var())

print(np.corrcoef(A))

print(np.corrcoef(A)[0,1])

print(np.unique(A,return_counts=True))

values,counts = np.unique(A,return_counts=True)

print(counts.argsort())

print(values[counts.argsort()])

print("\n")
print("\n")

for i,j in zip(values[counts.argsort()],counts[counts.argsort()]):
    print(f"valeur de {i} apparais : {j} fois")

print("\n")
print("\n")


A2 =np.random.randn(5,5)

A2[0,2] = np.nan
A2[4,3] = np.nan

print(A2)

print(np.nanmean(A2))
print(np.nanstd(A2))

print(np.isnan(A2))
print(np.isnan(A2).sum())
print(np.isnan(A2).sum()/A2.size)

A2[np.isnan(A2)] = 0

print(A2)

A3 = np.random.randint(0,100,[10,5])

moyenne = A3.mean(axis=0)
ecart_type = A3.std(axis=0)

A3_normalise = (A3 - moyenne) / ecart_type

print(A3_normalise)
