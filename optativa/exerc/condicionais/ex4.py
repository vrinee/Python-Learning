A = float(input("Digite um número: "))
B = float(input("Digite outro número: "))

if (A+B)*(30/100)> 500:
    C = B
    B = A
    A = C
    print("A = ", A)
    print("B = ", B)
    exit()
    
if A < B:
    print("A é o menor valor")
else:
    print("B é o menor valor")

    