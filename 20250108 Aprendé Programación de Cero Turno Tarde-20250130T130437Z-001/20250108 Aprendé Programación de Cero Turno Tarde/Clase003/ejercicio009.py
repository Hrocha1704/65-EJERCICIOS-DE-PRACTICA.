"""
Ejercicio 009
Escribir un programa que permita ingresar valores 
para las variables a y b. Una vez cargadas, mostrar ambas 
variables por pantalla, intercambiá sus valores 
(que lo cargado en a quede en b, y viceversa) y 
volvé a mostrarlas actualizadas.

Como pensarlo:

1- Pedir al usuario que ingrese un valor para la variable a.

2- Pedir al usuario que ingrese un valor para la variable b.

3- Mostrar por pantalla el valor de las variables a y b.

4- Intercambiar los valores de las variables a y b.

5- Mostrar por pantalla el valor de las variables a y b.   
"""


a = input("a: ")
b = int(input("b: "))

print(f"{a}  <====>  {b}")

auxiliar = a
a = b
b = auxiliar

print(f"{a}  <====>  {b}")


# python

# 2,3  <== 3,2
a,b = b,a

print(f"{a}  <====>  {b}")




