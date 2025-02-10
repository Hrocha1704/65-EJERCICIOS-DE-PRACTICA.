"""
Ejercicio 040

Escribir un programa que permita ingresar dos numeros enteros a y b. 
El programa debe mostrar:

- La suma de los numeros pares entre a y b.  
- El producto de los numeros impares entre a y b.
"""



def main():
    a = int(input("a: "))
    b = int(input("b: "))

    if b < a:
        a,b = b,a

    suma = 0
    producto = 1
    for numero in range(a,b+1):

        print(numero)
        
        if numero%2==0:
            suma += numero
        else:
            producto *= numero

    print(f"Suma Pares: {suma}")
    print(f"Producto Impares: {producto}")

main()