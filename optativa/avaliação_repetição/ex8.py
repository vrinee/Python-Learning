fibo = 0
fiboAnt = 0

while fibo < 500:
    print(fibo)
    fibo = fibo + fiboAnt
    fiboAnt = fibo - fiboAnt
    if fibo == 0:
        fibo = 1