num = []

for i in range(15):
    x = int(input("Digite um número: "))
    num.append(x)
    
for i in range(15):
    if num[i] > 30:
        print(num[i])