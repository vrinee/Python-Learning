dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))
print("Data: ", dia, "/", mes, "/", ano)

diaX = int(input("Digite quantos dias vai adicionar: "))
if mes == 2:
    diasM = 28
elif mes%2 == 0:
    diasM = 30
else:
    diasM = 31
    
dia += diaX
if dia > diasM:
    dia -= diasM
    mes += 1
    if mes > 12:
        mes = 1
        ano += 1
print("Nova data: ", dia, "/", mes, "/", ano)