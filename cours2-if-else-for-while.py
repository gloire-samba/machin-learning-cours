for i in range(10):
    print(i)
    
print("\n")
print("\n") 

for i in range(5, 10):
    print(i)
    
print("\n")
print("\n") 

for i in range(5, 10, 2):
    print(i)

print("\n")
print("\n") 
    
for i in range(10, -10, -1):
    print(i)
    
def fiboncaci(n):
    a, b = 0, 1
    while a < n:
        print(a)
        a, b = b, a+b


print(fiboncaci(1000))