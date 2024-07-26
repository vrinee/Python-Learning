X = []

for i in range(0,5):
    j = int(input("Digite um número: "))
    X += [j]

maior = X[0]
menor = X[0]

for i in range(0,5):
    if X[i] > maior:
        maior = X[i]
    if X[i] < menor:
        menor = X[i]
        
print("Maior elemento do vetor: ", maior)
print("Menor elemento do vetor: ", menor)