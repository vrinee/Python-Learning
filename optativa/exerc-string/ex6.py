palindromo = input("Digite uma palavra/frase: ")

palindromo = palindromo.replace(" ", "")
palindromo = palindromo.lower()
palindromo = list(palindromo)
aux = palindromo.copy()
aux.reverse()

if (palindromo == aux):
    print("É palíndromo")
else:
    print("Não é palíndromo")
    
for i in range(len(palindromo)):
    print(palindromo[i], end="")
print(" ")
for i in range(len(aux)):
    print(aux[i], end="")
