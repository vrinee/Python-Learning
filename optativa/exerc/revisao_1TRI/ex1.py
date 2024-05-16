data = int(input("Digite a data:"))

dia = data // 1000000
data = data % 1000000
mes = data // 10000
data = data % 10000
ano = data

match mes:
    case 1:
        mesM = 31
    case 2:
        if ano % 4 == 0:
            mesM = 29
        else:
            mesM = 28
    case 3:
        mesM = 31
    case 4:
        mesM = 30
    case 5:
        mesM = 31
    case 6:
        mesM = 30
    case 7:
        mesM = 31
    case 8:
        mesM = 31
    case 9:
        mesM = 30
    case 10:
        mesM = 31
    case 11:
        mesM = 30
    case 12:
        mesM = 31
    case _:
        mesM = 0

if dia > mesM:
    print("Data inválida")
else:
    print("Data válida")
    print(f"{dia}/{mes}/{ano}")