
import random as rd

# 4,5,8,4,8,6,4

def main():
     
    maximo = -float('inf')
    contador_repet=0
    cantidad_de_numeros = rd.randint(20,100)
    
    for posicion in range(1,cantidad_de_numeros+1):

        numero = rd.randint(1,10)
        print(f"{posicion} ==> {numero}")
        
        if numero > maximo:
            maximo = numero
            posicion_primer_maximo = posicion
            posicion_ultimo_maximo = posicion
            contador_repet = 0
            repetidos = f"{posicion:3}"
        elif numero == maximo:
            contador_repet += 1
            posicion_ultimo_maximo = posicion
            repetidos += f"{posicion:3}"
    print(f"Cantidad: {cantidad_de_numeros}")
    
    print(f"Maximo: {maximo} Primero: {posicion_primer_maximo} Ultimo: {posicion_ultimo_maximo} Repetidos: {contador_repet} [{repetidos}]")    

    
    



main()