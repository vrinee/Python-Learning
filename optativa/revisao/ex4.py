import numpy as np

N = 6

vetor = np.zeros(N)

for i in range(N):
    vetor[i] = int(input("Digite um número: "))
    

for i in vetor:
    print(i)
for i in vetor[::-1]:
    print(i)