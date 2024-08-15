
x = []
vezes = 10

for i in range(vezes):
    j = int(input("Digite um número: "))
    x += [j]
    
for i in range(vezes):
    if x[i] % 2 == 0:
        x[i] = x[i] * i
    else:
        x[i] = i
        
print(x)