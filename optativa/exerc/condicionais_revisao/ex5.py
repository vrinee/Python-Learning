cargos = ["Escrituário",50],["Secretário",35],["Caixa",20],["Gerente",10],["Diretor", 0]

cod = int(input("Digite o seu código: "))
salario = float(input("Digite o seu salário atual: "))

salario *= 1 + cargos[cod-1][1]/100


print(f"Seu novo salário de {cargos[cod-1][0]} é R${salario:.2f}")