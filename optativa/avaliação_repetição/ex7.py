num = 69
x = 0

while x != num:
    x = int(input("Digite um número entre 1 e 100: "))
    if x == num:
        print("Acertou!")
    elif x < num - 30 :
        print("Muito Menor")
    elif x > num + 30:
        print("Muito Maior")
    elif x < num:
        print("Maior")
    elif x > num:
        print("Menor")
    