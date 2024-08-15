nome = input("Digite seu nome: ")
aux = list(nome.upper())
leng = len(nome)
leng2 = 1
mud = 1

for i in range(1000):
    for j in range(leng2):
        print(aux[j], end="")
    leng2 += mud
    if leng2 == leng:
        mud = -1
    if leng2 == 1:
        mud = 1
    print(" ")