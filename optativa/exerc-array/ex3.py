X = []

for i in range(0,5):
    j = int(input("Digite um número: "))
    X += [j]

media = 0
    
for i in range(0,5):
    media += X[i]


media = media/5

print("Média dos elementos do vetor: ", media)
    
