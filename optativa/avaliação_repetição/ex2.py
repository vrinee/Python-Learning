run = 1
firstTime = True
result = 0


while run != 0:
    if firstTime:
        x = int(input("Digite o primeiro número: "))
        firstTime = False
    op = input("Digite a operação: ")
    y = int(input("Digite o segundo número: "))
    if op == "+":
        result = x + y
    elif op == "-":
        result = x - y
    elif op == "*":
        result = x * y
    elif op == "/":
        result = x / y
    elif op == "^":
        result = x ** y
    print(result)
    run = int(input("Digite 0 para sair ou 1 para continuar: "))
    x = result
        
    