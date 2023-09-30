# pylint: disable=C0103
# pylint: disable=C0304
# pylint: disable=C0111

run = True

while run:
    n1 = input("Enter the first number of the range: ")
    n2 = input("Enter the second number of the range: ")


    for i in range(int(n1), int(n2) + 1):
        prime = True
        for j in range(2, i):
            if i % j == 0:
                prime = False
                break
        if prime:
            print(i)
    run = input("Would you like to run the program again? (y/n): ")
    if run == "n":
        run = False
    else:
        run = True