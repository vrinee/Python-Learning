K = []
x = []
y = []

for i in range(20):
    K.append(i)
    
for i in K:
    if i % 2 == 0:
        x.append(i)
    else:
        y.append(i)
j = 0
l = 0
for i in range(20):
    if i % 2 == 0:
        K[i] = y[j]
        j += 1
    else:
        K[i] = x[l]
        l += 1
print(K)