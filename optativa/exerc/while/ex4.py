numbers = {}
i = 0
while i < 10:
    numbers[i] = int(input('Enter a number: '))
    i += 1
    
for x in numbers:
    print(numbers[x]/2)