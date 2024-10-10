import numpy as np

m = 25

X = np.zeros(m)
Y = np.zeros(m)

#RNG foi minha tentativa de fazer um random 
RNG = 10
aux = 1

for i in range(m):
    RNG = RNG * (-1*aux) + 5 - 15*aux
    aux += 1
    X[i] = RNG

print(X)

Y = X[::-1]

for i in range(m):
    Y[i] *= -1

print(Y)