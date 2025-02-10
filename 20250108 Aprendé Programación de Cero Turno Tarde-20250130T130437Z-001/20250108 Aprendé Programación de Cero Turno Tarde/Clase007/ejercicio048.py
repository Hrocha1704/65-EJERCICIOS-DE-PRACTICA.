"""
Ejercicio 048

Escribir un programa que permita realizar varias operaciones matemáticas 
ingresando un caracter por cada una la operación a realizar (‘+’, ‘-’, ‘*’, ‘/’, ‘F’) 
y dos números enteros en el caso que no haya elegido ‘F’. 
La computadora debe mostrar el resultado para la operación ingresada. 

Considerar que no se puede dividir por cero. 
Cuando la operación ingresada sea ‘F’ nos indicará que no se 
desean calcular más operaciones.

"""

OPERACIONES_POSIBLES = '+','-','*','/','%','//','F'

def main():
    
    operacion = input(f"Ingrese una operacion {OPERACIONES_POSIBLES}: ").upper()
    while operacion != 'F':

        if operacion  in OPERACIONES_POSIBLES:
            operando1 = int(input("Operando 1: "))
            operando2 = int(input("Operando 2: "))

            if operacion == '+':
                resultado = operando1 + operando2
            elif operacion == '-':
                resultado = operando1 - operando2
            elif operacion == '*':
                resultado = operando1 * operando2
            else:
                if operando2 != 0:
                    if operacion == '/':
                        resultado = operando1 / operando2
                    elif operacion == '//':
                        resultado = operando1 // operando2
                    else:
                        resultado = operando1 % operando2
                else:
                    resultado = "Error"
            print(f"{operando1} {operacion} {operando2} = {resultado}")   
        else:
            print(f"{operacion} Operacion erronea!!!")


        operacion = input(f"Ingrese una operacion {OPERACIONES_POSIBLES}: ").upper()

main()
