"""
Ejercicio 041

Escribir un programa que genere números enteros hasta que se ingrese un 0, 
y muestre el máximo.

"""


import random as rd

def main():
    mayor = -float('inf')

    n = rd.randint(-10,10)

    while n != 0:
        print(n)

        if n > mayor:
            mayor = n
        n = rd.randint(-10,10)

    print(f"Maximo: {mayor}")
    


main()