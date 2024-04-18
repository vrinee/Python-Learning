sexo = input("Digite o seu sexo(F ou M): ")  
idade  = int(input("Digite a sua idade: "))

if idade < 0:
    print("Idade inválida")
    exit()
if sexo == 'f' or sexo == 'F':
    if idade >= 0 and idade < 12:
        print("Menina")
    elif idade >= 12 and idade < 24:
        print("Moça")
    elif idade >= 24:
        print("Mulher")
elif sexo == 'm' or sexo == 'M':
    if idade >= 0 and idade < 12:
        print("Menino")
    elif idade >= 12 and idade < 24:
        print("Rapaz")
    elif idade >= 24:
        print("Homem")
else:
    print("Sexo inválido")
        