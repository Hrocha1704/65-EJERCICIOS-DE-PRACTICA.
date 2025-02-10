"""
Ejercicio 005

Escribir un programa que solicite al usuario ingresar dos notas de un alumno. 

El programa debe mostrar por pantalla el promedio de las notas de la siguiente manera: 

"Notas: {nota1} , {nota2} ==> promedio: {(nota1+nota2)/2}".

Ejemplo: Si el usuario ingresa 7 y 8, el programa debe mostrar por pantalla: 

"Notas: 7 , 8 ==> promedio: 7.5".
"""


nota1 = input("Nota 1: ") # CADENA!!
nota1 = float(nota1) # FLOAT .9999999999999
nota1 = round(nota1,2) # FLOAT.99



nota2 = round(float(input("Nota 2: ")),2)


promedio = round(  (nota1 + nota2) / 2 , 2)

print(f"Notas: {nota1} , {nota2} ==> promedio: {promedio}.")