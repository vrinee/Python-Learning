import numpy as np

n = 5

M = np.zeros((n,n))

for i in range(n):
    for j in range(n):
        M[i][j] = float(input("Digite um número para M: "))
soma =0
soma1 = 0  
for elemento in M:
    soma += elemento[2]
    
for i in range(n):
    soma1 += M[i][i]
    
    
print(soma)
print(soma1)
