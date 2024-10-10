import numpy as np

m = 6
matriz = np.zeros((m,m))


for i in range(m):
    for j in range(m):
        if j == 3:
            matriz[i][j] = i
        else:
            matriz[i][j] = i +1
print(matriz)       


for i in range(m):
    matriz[1][i] = matriz[4][i]
    
for i in range(m):
    matriz[i][3] = matriz[i][5]
        

print(matriz)
