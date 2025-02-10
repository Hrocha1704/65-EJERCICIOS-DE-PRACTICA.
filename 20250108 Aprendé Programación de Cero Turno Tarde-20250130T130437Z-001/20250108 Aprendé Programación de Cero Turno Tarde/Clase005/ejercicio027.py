"""
Ejercicio 027

Escribir un programa que permita ingresar una edad (entre 1 y 120 años), 
un género ('F'para mujeres, 'M' para hombres) y un nombre. 
En caso de haber ingresado valores erróneos (edad fuera de rango o género inválido), 
informar tal situación indicando el nombre de la persona. 

Si los datos están bien ingresados el programa debe indicar, sabiendo que las 
mujeres se jubilan con 60 años o más y los hombres con 65 años o más, 
si la persona está en edad de jubilarse.

"""

import random as rd

EDAD_MINIMA = 1
EDAD_MAXIMA = 120
EDAD_JUBILATORIA_FEMENINA = 60
EDAD_JUBILATORIA_MASCULINA = 65
GENERO_FEMENINO = 'F' 
GENERO_MASCULINO = 'M' 
GENEROS_POSIBLES = GENERO_FEMENINO,GENERO_MASCULINO

# Lista de nombres masculinos
NOMBRE_MASCULINOS = (
    "Mateo", "Santiago", "Sebastián", "Benjamín", "Lucas", "Martín", "Joaquín", "Tomás", "Gabriel", "Felipe",
    "Samuel", "Daniel", "Diego", "Emiliano", "Nicolás", "Alejandro", "Pablo", "Maximiliano", "Axel", "Juan",
    "Agustín", "Iván", "Emanuel", "Adrián", "Bruno", "Elías", "Simón", "Lorenzo", "Matías", "Esteban",
    "Facundo", "Gonzalo", "Cristian", "Andrés", "Franco", "Leonardo", "Hugo", "Ignacio", "David", "Rodrigo",
    "Ricardo", "Julián", "Sergio", "Renzo", "César", "Ramiro", "Francisco", "Damián", "Álvaro", "Héctor"
)

# Lista de nombres femeninos
NOMBRE_FEMENINOS = (
    "Sofía", "Isabella", "Valentina", "Martina", "Camila", "Lucía", "Victoria", "María", "Emma", "Emilia",
    "Mía", "Julieta", "Catalina", "Elena", "Gabriela", "Daniela", "Agustina", "Carolina", "Florencia", "Renata",
    "Paula", "Ana", "Sara", "Laura", "Clara", "Lola", "Luciana", "Ariadna", "Delfina", "Isabel",
    "Eva", "Olivia", "Mariana", "Silvana", "Ángela", "Viviana", "Miranda", "Noelia", "Rebeca", "Mariela",
    "Bianca", "Antonella", "Milagros", "Elisa", "Cecilia", "Natalia", "Rocío", "Andrea", "Melina", "Selena"
)

def main():
    edad = rd.randint(EDAD_MINIMA,EDAD_MAXIMA)
    genero = rd.choice(GENEROS_POSIBLES)
    if genero == GENERO_FEMENINO:
        nombre = rd.choice(NOMBRE_FEMENINOS)
        se_jubila = edad >= EDAD_JUBILATORIA_FEMENINA
    else:
        nombre = rd.choice(NOMBRE_MASCULINOS)
        se_jubila = edad >= EDAD_JUBILATORIA_MASCULINA

    print(f"{nombre} {edad} {genero} {se_jubila}")
        
main()


