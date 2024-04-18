ano = int(input("Digite sua data de nascimento:"))
anoAtual = int(input("Digite o ano atual:"))
idade = anoAtual - ano

if idade >= 16:
    print("Você pode votar")
else:
    print("Você não pode votar")

