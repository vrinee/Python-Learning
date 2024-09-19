X = []
Y = []

for i in range(10):
    X.append(int(input("Digite um número para X: ")))
    Y.append(int(input("Digite um número para Y: ")))
    
X = set(X)
Y = set(Y)

print(X - Y)