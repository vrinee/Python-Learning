numbers = {}
i = 0
while i < 5:
    numbers[i] = int(input('Enter a number: '))
    i += 1
    
for x in numbers:
    print(f"O cubo de {numbers[x]} é: {numbers[x]**3}")