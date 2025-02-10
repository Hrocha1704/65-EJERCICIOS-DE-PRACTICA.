"""
Ejercicio 046

Escribir un programa que a partir de un número entero cant ingresado 
por el usuario permita cargar por teclado cant números enteros. 

La computadora debe mostrar cuál fue el mayor y el menor número y 
en qué posiciones apareció cada uno.
"""

def main():
    posicion = 0 
    maximo = -float('inf')
    minimo = float('inf')
    cantidad_de_numeros = int(input("Cantidad de numeros: "))
    for x in range(cantidad_de_numeros):

        numero = int(input("Numero: "))
        posicion += 1

        if numero > maximo:
            maximo = numero
            posicion_maximo = posicion

        if numero < minimo:
            minimo = numero
            posicion_minimo = posicion

    print(f"Maximo: {maximo} posicion: {posicion_maximo}")    
    print(f"Minimo: {minimo} posicion: {posicion_minimo}")    


main()