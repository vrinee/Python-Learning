n1 = float(input("Digite a primeira nota: "))
p1 = 3

n2 = float(input("Digite a segunda nota: "))
p2 = 2

n3 = float(input("Digite a terceira nota: "))
p3 = 5

media = (n1*p1 + n2*p2 + n3*p3) / (p1 + p2 + p3)

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")