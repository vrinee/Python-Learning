X = []

for i in range(0,5):
    j = int(input("Digite um número: "))
    X += [j]

soma = 0
    
for i in range(0,5):
    soma += X[i]
    
    
print("Soma dos elementos do vetor: ", soma)