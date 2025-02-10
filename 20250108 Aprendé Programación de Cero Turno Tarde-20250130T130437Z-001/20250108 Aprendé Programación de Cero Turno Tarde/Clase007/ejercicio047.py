"""
Ejercicio 047

Escribir un programa que permita validar la nota de un examen. 


Se espera que la nota que el usuario ingrese sea un número 
comprendido entre 0 y 10.  

La misma debe ser ingresada tantas veces como sea necesario hasta que quede 
comprendida dentro del rango indicado
"""

def main():

    nota = int(input("Nota: "))

    while nota < 0 or nota > 10: # ERROR
        print("Error: Nota fuera de rango!!")
        nota = int(input("Nota: "))


    print(f"Nota: {nota}")
main()



