import numpy as np
def lagrange(X,Y,Xint):
    n=len(X)
    L = np.zeros(n)
    for i in range(0,n):
        L[i] = 1.0
        for j in range (0,n):
            if i != j:
                L[i] = L[i]*(Xint - X[j])/(X[i]-X[j])
    Yint = np.sum(L*Y)
    return Yint
x = [1,2,3,4,5]
y = [4,6,9,12,14]
Xint = 4.5
R = lagrange(x,y,Xint)
print("El valor de interpolación para ", Xint, " es: ", R)