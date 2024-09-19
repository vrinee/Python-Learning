R = set()
S = set()

for i in range(5):
    R.add(float(input("Digite um número para R: ")))
    
for i in range(10):
    S.add(float(input("Digite um número para S: ")))
    
X = R & S
print("X:", X)
print("R:", R)
print("S:", S)
    