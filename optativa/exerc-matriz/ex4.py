import numpy as np

n = 5

M = np.zeros((n,n))

for i in range(n):
    for j in range(n):
        M[i][j] = float(input("Digite um número para M: "))

soma = 0
for elemento in M[4]:
    soma += elemento
    
