lista = []

for i in range(5):
    x = int(input("Digite um número: "))
    lista.append(x)
maior = lista[0]
menor = lista[0]
for i in lista:
    if i > maior:
        maior = i
    if i < menor:
        menor = i
        
print("Maior: ", maior)
print("Menor: ", menor)
print("Lista: ", lista)