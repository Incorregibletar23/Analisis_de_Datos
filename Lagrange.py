import numpy as np 
def lagrange(x, y, xint):
    n = len(x)
    L = np.zeros(n)
    for i in range(0, n):
        L[i] = 1.0
        for j in range(0, n):
            if i != j:
                L[i] = L[i] * (xint - x[j])/(x[i] - x[j])
    yint = np.sum(L*y)
    return yint 
x = [1,2,3,4,5]
y = [4,6,9,12,14]
xint = 4
r = lagrange(x, y, xint)
print(f"El valor de inerpolación para x: {x} es {r}")