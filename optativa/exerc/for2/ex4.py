primos = 0
for i in range (2,1000):
    if primos == 10:
        break
    prime = True
    for j in range (2,i):
        if i % j == 0:
            prime = False
            break
    if prime:
        primos += 1
        print(i)
        
        