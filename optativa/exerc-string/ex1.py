nome = input("Digite seu nome: ")
aux = list(nome.upper())
nomefinal = []

leng = len(nome)
inleng = leng - 1
for i in range(leng):
    nomefinal += [0]
for i in range(leng):
    nomefinal[i] = aux[inleng]
    inleng -= 1




print("Seu nome é: ", nome)
print("Seu nome invertido é: ", end='')
for i in range(leng):
    print(nomefinal[i], end="")
print('\n')