
m = 8

x = (float(input("Digite um número: ")) for i in range(m))
y = []

z = []



    
for i in x:
    if i > 0:
        y += [i]
    elif i < 0:
        z += [i]



print(y)
print(z)

