import matplotlib.pyplot as ptl

def Linea(x):
    ptl.plot(x)
    ptl.show()

def cuadrado(x):
    return x*x

x = [-2,-1,0,1,2,3,4]

y = x

print(y)

con = 0

for i in y:
    y[con] = cuadrado(i)
    con = con +  1

print(y)

Linea(y)

input()