for i in range(1, 1000):
    soma = 0
    for j in range(1, i):
        if i % j == 0:
            soma += j
    if soma == i:
        print(i)