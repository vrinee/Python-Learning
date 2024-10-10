import numpy as np
N = 2 

matriz = np.zeros((N,N))

for i in range(N):
    for j in range(N):
        matriz[i][j] = float(input("Digite um número: "))
        
        
diag = []

for i in range(N):
    x = matriz[i][i]
    diag.append(x)
    
print(matriz)

print(diag)

