"""
Ejercicio 037

Escribir un programa que muestre todos los números enteros del 1 al 5, 
y luego los mismos números pero en orden inverso.
"""

def main():
    desde = 1
    hasta = 5

    numero = desde
    while numero <= hasta:
        print(numero)

        numero += 1

    print("-"*100)

    numero = hasta
    while numero > 0:
        print(numero)

        numero -= 1

main()