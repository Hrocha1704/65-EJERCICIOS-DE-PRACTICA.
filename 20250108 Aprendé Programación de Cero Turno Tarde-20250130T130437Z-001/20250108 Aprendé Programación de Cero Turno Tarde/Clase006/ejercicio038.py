"""
Ejercicio 038

Escribir un programa que permita ingresar un número entero n. 
Debe mostrar los primeros 10 múltiplos de n.

Ejemplo  
n = 5  

n x 1 = 5  
n x 2 = 10  
n x 3 = 15  
n x 4 = 20  
n x 5 = 25  
n x 6 = 30  
n x 7 = 35  
n x 8 = 40  
n x 9 = 45  
n x 10 = 50   
"""


CANTIDAD_MULTIPLOS = 10


def main():
    tabla_del = int(input("ingrese el numero de la tabla que quiere: "))
    numero = 1
    while numero <= CANTIDAD_MULTIPLOS:
        print(f"{tabla_del} x {numero} = {numero*tabla_del}")
        numero += 1

    print("Usando un for")


    for numero in range(1,CANTIDAD_MULTIPLOS+1):
        print(f"{tabla_del} x {numero} = {numero*tabla_del}")


main()


