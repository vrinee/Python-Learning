preco1 = float(input("Digite o preço do primeiro produto: "))
preco2 = float(input("Digite o preço do segundo produto: "))
preco3 = float(input("Digite o preço do terceiro produto: "))

menor = preco1

if preco2 < menor:
    menor = preco2
elif preco3 < menor:
    menor = preco3
    
    
print(f"O produto mais barato custa R${menor:.2f}")