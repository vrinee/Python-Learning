
x = []
y = []
z = []

for i in range(5):
    x += [0]
    y += [0]
    z += [0]

vezes = 5
p = vezes - 1

for i in range(-1,vezes-1):
    j = int(input("Digite um número para a primeira lista: "))
    x[i] = j
    k = int(input("Digite um número para a segunda lista: "))
    y[i] = k

for i in range(vezes):
    z[i] = x[i] * y[p]
    p -= 1

    
print(x)
print(y)
print(z)