
"""
LEER UNA LISTA DE NUMEROS TERMINADA EN CERO. 

MOSTRAR LA SUMA.
MOSTRAR LA CANTIDAD DE NUMEROS

lista1 ==> 1,8,4,5,7,4,5,8,7,4,5,87,4,0

lista2 ==> 5,87,4,0

lista3 ==> 0

"""

def main():    
    # ANTES ==> una sola vez

    cantidad = 0
    suma = 0
    numero = int(input("Numero: "))
    while numero != 0: # MIENTRAS HAY DATOS
        # DURANTE ==> proceso cada dato

        suma += numero # suma = suma + numero

        cantidad += 1  # contador = contador + 1 
        
        numero = int(input("Numero: "))
    # DESPUES ==> totales
    print(f"Suma: {suma}")
    print(f"Contador: {cantidad}")



main()