string1 = input("Digite uma palavra: ")
string2 = input("Digite outra palavra: ")
string1 = string1.lower()
string2 = string2.lower()

pos = string1.find(string2)

if pos == -1:
    print("Não é encontrada")
else:
    print("Encontrada na posição", pos)