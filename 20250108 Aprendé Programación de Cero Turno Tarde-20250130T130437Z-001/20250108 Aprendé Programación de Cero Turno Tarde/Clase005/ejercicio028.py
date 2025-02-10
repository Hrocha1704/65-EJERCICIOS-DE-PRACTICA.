"""
Ejercicio 028

Crear un programa que pida un número de mes (ejemplo 4) 
y escriba el nombre del mes en letras ("abril"). 

Verificar que el mes sea válido e informar en caso que no lo sea.
"""


MES_DESDE =  1
MES_HASTA = 12

def main():
    nombre = None
    numero_mes = int(input("Mes [1..12]: "))
    # if  MES_DESDE <= numero_mes <= MES_HASTA: # python
    if  numero_mes >= MES_DESDE and numero_mes <= MES_HASTA:
        if numero_mes == 1:
            nombre = 'enero'
        elif numero_mes == 2:
            nombre = 'febrero'
        elif numero_mes == 3:
            pass
        elif numero_mes == 4:
            pass
        elif numero_mes == 5:
            pass
        elif numero_mes == 6:
            pass
        elif numero_mes == 7:
            pass
        elif numero_mes == 8:
            pass
        elif numero_mes == 9:
            pass
        elif numero_mes == 10:
            pass
        elif numero_mes == 11:
            pass
        elif numero_mes == 12:
            pass
    print(nombre)
                

    
main()
