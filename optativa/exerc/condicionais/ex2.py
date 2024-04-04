A = float(input("Digite um número: "))
B = float(input("Digite outro número: "))
C = float(input("Digite mais um número: "))

print("Os números em ordem crescente são: ")
if A < B and A < C:
    print(A)
    if B < C:
        print(B,"\n",C)
    else:
        print(C,"\n",B)
elif B < A and B < C:
    print(B)
    if A < C:
        print(A,"\n",C)
    else:
        print(C,"\n",A)        
elif C < A and C < B:
    print(C)
    if A < B:
        print(A,"\n",B)
    else:
        print(B,"\n",A)