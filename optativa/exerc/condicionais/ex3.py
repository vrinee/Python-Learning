n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))
n4 = float(input("Digite o quarto número: "))
n5 = float(input("Digite o quinto número: "))

maior = n1

if n2 >= maior:
    maior = n2
if n3 >= maior:
    maior = n3
if n4 >= maior:
    maior = n4
if n5 >= maior:
    maior = n5
    
print("O maior número é: ", maior)
