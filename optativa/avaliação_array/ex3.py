X = []
m = 100
parCont = 0
imparList = 0
imparCont = 0
for i in range(m):
    X.append(i)
    
for i in X:
    if i % 2 == 0:
        parCont +=1
    else:
        imparList += i
        imparCont +=1
    
print("A quantidade de pares é:",parCont) 
print("A média de impares é:",imparList/imparCont)  
