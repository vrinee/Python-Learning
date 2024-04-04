litro = float(input("Digite a quantidade de litros vendidos: "))
tipo = input("Foi álcool ou gasolina? (A ou G): ")
precoA = 6.50
precoG = 7.20

if tipo == "A":
    preco = precoA*litro
    if litro <= 20:
        preco = precoA*0.97
    else:
        preco = precoA*0.95
elif tipo == "G":
    preco = precoG*litro
    if litro <= 20:
        preco = precoG*0.96
    else:
        preco = precoG*0.94
else:
    print("Tipo inválido")
    exit()
    
    
print("O preço é: R$", preco)
    