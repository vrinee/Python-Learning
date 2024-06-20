
for i in range(10):
    x = int(input("Digite um número: "))
    if i == 0:
        maior = x
        menor = x
    
    if x > maior:
        maior = x
    if x < menor:
        menor = x

print("Maior:", maior)
print("Menor:", menor)
    
    