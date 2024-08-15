#Faça um algoritmo que lê duas listas A e B com 5 elementos cada. Construir uma
#lista C, sendo este a junção das duas outras listas, ou seja, a lista C deverá conter
#10 elementos. Mostre no final a lista C.

A = []
B = []
C = []
C2 = []

vezes = 5

    

for i in range(vezes):
    j = int(input("Digite um número para a primeira lista: "))
    A += [j]
    k = int(input("Digite um número para a segunda lista: "))
    B += [k]
    
for i in range(vezes):
    C += [A[i]]
    C += [B[i]]
    
for i in range(vezes):
    C2 += [A[i]]
    
for i in range(vezes):
    C2 += [B[i]]
    
print(C)
print(C2)