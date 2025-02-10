"""
Ejercicio 053

Escribir un programa que permita ingresar nombre, apellido y edad de un grupo de personas 

(para cada una, nombre apellido y edad). 

La carga termina cuando en el nombre de la persona se ingresa un asterisco ('*'). 

Mostrar al final cómo se llama la persona más joven.
"""

def obtener_datos_de_una_persona_desde_teclado():
    """
    Solicita datos de una persona desde el teclado y los devuelve como una tupla.

    La función pide al usuario que ingrese su nombre, apellido y edad.
    Si el nombre ingresado es '*', no solicita el resto de los datos y devuelve
    una tupla con el nombre '*' y los demás valores vacíos o cero.

    Retorno:
        tuple: Una tupla con tres elementos:
            - nombre (str): El nombre ingresado por el usuario. Si el usuario
              ingresa '*', este será el único valor retornado.
            - apellido (str): El apellido ingresado por el usuario. Si el nombre
              es '*', este valor será una cadena vacía.
            - edad (int): La edad ingresada por el usuario. Si el nombre es '*',
              este valor será 0.

    Ejemplo de uso:
        >>> obtener_datos_de_una_persona_desde_teclado()
        Nombre: Juan
        Apellido: Pérez
        Edad: 30
        ('Juan', 'Pérez', 30)

        >>> obtener_datos_de_una_persona_desde_teclado()
        Nombre: *
        ('*', '', 0)
    """
    nombre = ""
    apellido = ""
    edad = 0

    nombre = input("Nombre: ")

    if nombre != '*':
        apellido = input("Apellido: ")
        edad = int(input("Edad: "))

    return nombre, apellido, edad


def main():
    """
    Programa principal
    """
    nombre,apellido,edad =  obtener_datos_de_una_persona_desde_teclado()
    while nombre != '*':

        nombre_completo = f"{nombre.title()} {apellido.title()}"
        print(nombre_completo,edad)
        
        nombre,apellido,edad =  obtener_datos_de_una_persona_desde_teclado()

main()