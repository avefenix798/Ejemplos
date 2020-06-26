


def Tabla(x):
    numeros = [1,2,3,4,5,6,7,8,9,10]
    for n in numeros:
        print(n ,' x ' ,x ,' = ', n*x )

print('Que tabla desea obtener \n')
numero = int(input())
print('La tabla de ', numero , " es ")

Tabla(numero)
input()
