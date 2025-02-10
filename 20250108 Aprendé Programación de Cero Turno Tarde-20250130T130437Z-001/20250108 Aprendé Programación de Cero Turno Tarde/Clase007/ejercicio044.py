"""
Ejercicio 044

Escribir un programa que permita leer dos números A y B 
(enteros positivos). Calcular el producto A * B por sumas 
sucesivas e imprimir el resultado.

Ejemplo:

- 4*3 = 4 + 4 + 4 (4 sumado 3 veces).  
- 3*4 = 3 + 3 + 3 + 3 (3 sumado 4 veces).
"""

import random as rd




def main():
    a = rd.randint(1,10)
    b =  rd.randint(1,10)

    copia_b = b
    suma = 0
    cadena = ""
    while copia_b > 0:
        suma += a
        if copia_b > 1:
            cadena +=  (str(a) + ' + ')    
        else:
            cadena +=  str(a)
        copia_b -= 1


    print(f"{a}*{b} = {cadena} = {suma}")

    a,b=b,a
    print("*"*100)
    copia_b = b
    suma = 0
    cadena = ""
    while copia_b > 0:
        suma += a
        if copia_b == 1:
            cadena +=  str(a)
        else:
            cadena +=  (str(a) + ' + ')    
        copia_b -= 1


    print(f"{a}*{b} = {cadena} = {suma}")

main()

