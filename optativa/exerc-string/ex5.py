frase = input("Digite uma frase: ")

espacos = frase.count(" ")
vogais = [frase.count("a"), frase.count("e"), frase.count("i"), frase.count("o"), frase.count("u")]

print ("A frase tem", espacos, "espaços")
print ("A frase tem", vogais[0], "vogais 'a'")
print ("A frase tem", vogais[1], "vogais 'e'")
print ("A frase tem", vogais[2], "vogais 'i'")
print ("A frase tem", vogais[3], "vogais 'o'")
print ("A frase tem", vogais[4], "vogais 'u'")