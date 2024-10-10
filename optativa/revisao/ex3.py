A = set()
B = set()

for i in range(1,11):
    if i % 2 == 0:
        A.add(i)
    else:
        B.add(i)
        
print(A | B)
print(A & B)