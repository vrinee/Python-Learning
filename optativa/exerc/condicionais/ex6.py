dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))
print("Data: ", dia, "/", mes, "/", ano)

diaX = int(input("Digite quantos dias vai adicionar: "))

diaD = diaX + dia + mes*30 + ano*365
diaF = diaD % 365
dia = diaF % 30
ano = (diaD - diaF)/365
mes = (diaF - dia)/30

if dia == 0:
    dia = 30
    mes -= 1


print("Nova data: ", dia, "/", mes, "/", ano)