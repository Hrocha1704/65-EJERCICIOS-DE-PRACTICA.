"""
Ejercicio 026

Escribir un programa que permita ingresar la cantidad de invitados 
a una fiesta y la cantidad de asientos disponibles en el salon. 

Debes indicar si alcanzan los asientos, Si los asientos no alcanzaran 
indicar cuántos faltan para que todos los invitados puedan sentarse.
"""

import random as rd

def main():
    faltan = None
    asientos = rd.randint(10,50)
    invitados = rd.randint(10,50)

    alcanzan_los_asientos =  invitados <= asientos
    cartel = "Todo bien!!"

    if not alcanzan_los_asientos:
        faltan = invitados - asientos
        cartel = f"Faltan {faltan} aientos"

    print(f"Asientos: {asientos} Invitados: {invitados} ==> {cartel}")

main()

