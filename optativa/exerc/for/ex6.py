positivos = 0
negativos = 0

for i in range(20):
    x = int(input("Digite um número: "))
    if x > 0:
        positivos += x
    if x < 0:
        negativos += 1