import numpy as np

m = 3

vetor = np.zeros(m)

matriz = np.zeros((m,m))


for i in range(m):
    vetor[i] = float(input("Digite um número:"))

for i in range(m):
    for j in range(m):
        matriz[i][j] = float(input("Digite um número"))
        
resultado = matriz.copy()
for i in range(m):
    for j in range(m):
        resultado[i][j] *= vetor[j]
        
print(vetor)
print(matriz)
print(resultado)