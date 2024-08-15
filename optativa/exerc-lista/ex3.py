
x = []
y = []
z = []

vezes = 5

for i in range(vezes):
    j = int(input("Digite um número para a primeira lista: "))
    x += [j]
    k = int(input("Digite um número para a segunda lista: "))
    y += [k]
    
for i in range(vezes):
    z += [x[i] + y[i]]
    
print(x)
print(y)
print(z)