import numpy as np

def interNewton(x, y, xint):
    n = len(x)
    a = np.zeros(n)
    difDiv = np.zeros((n-1, n-1))
    a[0] = y[0]
    for i in range(0, n-1):
        difDiv[i, 0] = (y[i+1] - y[i]) / (x[i+1] - x[i])
    print(f"Primer calculo en \n[difDiv]")
    for j in range(1, n-1):
        for i in range(0, n-1-j):
            difDiv[i, j] = (difDiv[i+1, j-1] - difDiv[i, j-1]) / (x[i+j+1] - x[i])
    print(f"Calculo completo de difDiv: \n[difDiv]")
    for i in range(1, n):
        a[i] = difDiv[0, i-1]
    yint = a[0]
    prodx = 1
    for z in range(1, n):
        prodx *= (xint - x[z-1])
        yint += a[z] * prodx
    return a, yint


# Código de prueba
x = [-1, 0, 2, 3]
y = [-5, -1, 1, 11]
numInter = 2.5
coef, valInter = interNewton(x, y, numInter)
print(f"Coeficientes: {coef}")
print(f"Interpolación en {numInter} da {valInter}")
