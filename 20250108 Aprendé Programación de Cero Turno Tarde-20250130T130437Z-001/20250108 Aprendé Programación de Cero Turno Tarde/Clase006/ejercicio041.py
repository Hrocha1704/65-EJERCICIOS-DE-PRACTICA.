"""
Ejercicio 041

Escribir un programa que genere números enteros hasta que se ingrese un 0, 
y muestre el máximo.

"""


import random as rd

def main():
    mayor = None
    primera_vez = True

    n = rd.randint(-10,10)

    while n != 0:
        print(n)

        if primera_vez == True:
            primera_vez = False
            mayor = n
        else:
            if n > mayor:
                mayor = n
        n = rd.randint(-10,10)

    print(f"Maximo: {mayor}")
    


main()