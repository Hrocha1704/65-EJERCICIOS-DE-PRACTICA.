"""
Ejercicio 029

Escribir un programa que permita Ingresar las notas de los dos 
parciales de un alumno e indicar si promocionó, aprobó o debe recuperar. 

Si el valor de la nota no esta entre 0 y 10, debe informar un error.

- Se promociona cuando las notas de ambos parciales son mayores o iguales a 7.
- Se aprueba cuando las notas de ambos parciales son mayores o iguales a 4.
- Se debe recuperar cuando al menos una de las dos notas es menor a 4.

"""

def main():
    nota1 = 0
    nota2 = 0
    
    nota1 = int(input("Nota 1: "))
    if 0 <= nota1 <= 10: 
        nota2 = int(input("Nota 2: "))
        if 0 <= nota2 <= 10:
            aprueba =  nota1 >= 4 and nota2 >= 4
            promociona = nota1 >= 7 and nota2 >= 7
            recupera = nota1 < 4 or nota2 < 4

            if recupera:
                cartel = "Recupera!"
            elif promociona:
                cartel = "promociona!"
            else:
                cartel = "aprueba!" 
        else:
            cartel = f"Error en la nota 2!" 
    else:
        cartel = f"Error en la nota 1!" 

    print(f"Notas [{nota1},{nota2}] ==> {cartel}")
main()