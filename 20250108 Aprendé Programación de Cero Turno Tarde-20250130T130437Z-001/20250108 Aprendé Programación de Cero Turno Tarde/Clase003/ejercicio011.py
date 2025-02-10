"""
Ejercicio 011

Escribir un programa que permita resolver el siguiente problema:

Tres personas aportan diferente capital a una sociedad y desean saber el 
valor total aportado y qué porcentaje aportó cada una 

(indicando nombre y porcentaje).

Solicitar la carga por teclado del nombre de cada socio y su capital aportado,
a partir de esto calcular e informar lo requerido previamente.

"""

nombre1 = input("Nombre: ")
capital1 = float(input(f"Ingrese el capital de {nombre1}: "))

nombre2 = input("Nombre: ")
capital2 = float(input(f"Ingrese el capital de {nombre2}: "))

nombre3 = input("Nombre: ")
capital3 = float(input(f"Ingrese el capital de {nombre3}: "))


capital_total = capital1 + capital2 + capital3

por1 = capital1 * 100 / capital_total
por2 = capital2 * 100 / capital_total
por3 = capital3 * 100 / capital_total

cadena = f"""
------------------------------------------------------
El Chiringo
------------------------------------------------------
Capital Total: {capital_total:20.2f}
------------------------------------------------------
{nombre1:25} ${capital1:20.2f} % {por1:5.2f}
{nombre2:25} ${capital2:20.2f} % {por2:5.2f}
{nombre3:25} ${capital3:20.2f} % {por3:5.2f}
------------------------------------------------------
"""

print(cadena)
