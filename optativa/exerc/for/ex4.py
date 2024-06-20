rMin = int(input("Enter the first number of the range: "))
rMax = int(input("Enter the second number of the range: "))
soma = 0

for i in range(rMin, rMax):
    if i % 2 == 0:
        print(i)
        soma += i
        
print(soma)