media = 0
qnt = 0

while 1:
    x = int(input("Digite um número: "))
    if x < 0:
        break
    media += x 
    qnt += 1

media = media / qnt
print(f"A média dos números digitados é {media:.2f}")