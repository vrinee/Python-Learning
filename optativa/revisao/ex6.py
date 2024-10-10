Notas = {'João': 9, 'Maria': 10, 'José': 4}

nome = input("Digite o nome de um aluno: ")

if nome in Notas:
    print("A nota de", nome, "é", Notas[nome])
else:
    print("O aluno não está na lista.")