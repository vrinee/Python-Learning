R = set()

for i in range(5):
    R.add(i)
    
A = set()

for i in range(10):
    A.add(int(input("Digite um número para a aposta: ")))
    
X = R & A

print("Foram ", len(X), " acertos.")