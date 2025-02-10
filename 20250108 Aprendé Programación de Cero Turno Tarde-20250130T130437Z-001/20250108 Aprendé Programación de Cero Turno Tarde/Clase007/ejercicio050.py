"""
Ejercicio 050

Escribir un programa que permita validar la nota de un examen. 

Se espera que la nota que el usuario ingrese sea un número comprendido entre 0 y 10.  

La misma debe ser ingresada tantas veces como sea necesario hasta que quede 
comprendida dentro del rango indicado.

Las notas 1 y 3 no usan nunca.  
La nota 0 se reserva para los ausentes.  

Las notas válidas pueden ser un 2 o un valor entre 4 y 10.

"""

def main():

    todo_bien = False
    while not todo_bien:
        nota = int(input("Nota: "))
        # todo_bien = (0 <= nota <= 10)
        todo_bien = (4 <= nota <= 10) or nota == 28
        7-Uu`-s`
    print(f"Nota  {nota}")

    

main()
