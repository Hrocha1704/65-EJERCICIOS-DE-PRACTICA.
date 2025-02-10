"""
Ejercicio 064

Un animal en rehabilitación después de una cirugía requiere ser alimentado y monitoreado 
en un zoológico. 

Se alimenta al animal 3 veces al día y se le da de comer 
hasta que ya no tenga ganas de comer.

Por cada tanda de comida, se debe ingresar la cantidad de alimento en kg (número entero) 
que se le dio y se le debe preguntar al animal si quiere seguir comiendo ('S', 'N').


Se desea conocer:

Cuál de las 3 comidas fue la que el animal comió más cantidad de alimento y 
cuánto fue esa cantidad.

    comida_mayor ==> 1,2,3
    mayor ==> ?kg


El total en kg de alimento recibido.
    totalkg

Promedio de alimento por tanda.
    suma_kg_tanda
    cantidad_comidas_tanda
"""

CANTIDAD_TANDAS = 3


def main():
    # ANTES FOR
    comida_mayor = 0
    mayor = -float('inf')
    
    
    totalkg = 0
    for tanda in range(1,CANTIDAD_TANDAS+1):   
        # para cada tanda     
        print(f"Tanda: {tanda}")
        continua_comiendo = True
        suma_kg_tanda = 0
        cantidad_comidas_tanda = 0

        # ANTES WHILE
        while continua_comiendo:
            kg = int(input("Kg: "))
            suma_kg_tanda += kg
            totalkg += kg
            cantidad_comidas_tanda += 1 
            continua_comiendo = input("Continua comiendo (S/N)?: ").upper() == 'S'
        # fin del while ==> fin de una tanda 
        # para cada tanda
        promedio_tanda = suma_kg_tanda/cantidad_comidas_tanda
        print(f"Tanda: {tanda} Promedio: {promedio_tanda:.2f}")
        if suma_kg_tanda > mayor:
            mayor = suma_kg_tanda
            comida_mayor = tanda
    # fin del for ==> fin de todas las tandas
    print(f"Total de alimento: {totalkg}") 
    print(f"La comida donde mas comio fue: {comida_mayor} con {mayor} kg consumidos.")       
main()



