"""
Ejercicio 002

Escribir un programa que solicite al usuario su nombre y su edad, 
y luego muestre por pantalla un mensaje que diga "Hola, [nombre]. Tu edad es [edad] años."


"Hola, {nombre}. Tu edad es {edad} años."

Ejemplo de ejecución:

    Ingrese su nombre: Juan
    Ingrese su edad: 30

    Hola, Juan. Tu edad es 30 años.

"""

nombre = input("Ingrese su nombre: ")
edad = int(input("Edad: "))


cadena = "Hola, {nombre}. Tu edad es {edad} años."

print(cadena)

print(f"Hola, {nombre}. Tu edad es {edad} años.")
