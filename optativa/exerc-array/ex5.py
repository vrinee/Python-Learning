X = []

for i in range(0,10):
    j = int(input("Digite um número: "))
    X += [j]

maior = X[0]
menor = X[0]


for i in range(0,10):
    if X[i] > maior:
        maior = X[i]
        posMaior = i
    if X[i] <= menor:
        menor = X[i]
        posMenor = i
        
print("Maior elemento do vetor: ", maior)
print("Posição do maior elemento: ", posMaior)
print("Menor elemento do vetor: ", menor)
print("Posição do menor elemento: ", posMenor)