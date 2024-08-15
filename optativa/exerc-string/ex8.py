string = input("Digite uma palavra: ")
string = string.lower()
string = list(string)

passadas = []
atual = string[0]
run = True
j = 0
k = -1
caracteres = []

for i in range(len(string)):
    caracteres.append(0)

while run:
    if string[j] not in passadas:
        passadas.append(string[j])
        k += 1
        if string[j] not in atual:
            atual=string[j]
    for i in range(len(string)):
        if string[i] == atual:     
            caracteres[k] += 1
    j += 1
    if j == len(string):
        run = False
                
                
for i in range(len(passadas)):
    print(passadas[i], "aparece", caracteres[i], "vezes")