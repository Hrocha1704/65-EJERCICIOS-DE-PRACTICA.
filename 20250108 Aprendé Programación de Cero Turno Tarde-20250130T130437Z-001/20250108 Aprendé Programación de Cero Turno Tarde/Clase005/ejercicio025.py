"""
Ejercicio 025

Para acceder a cierta atracción, alcanza con que se cumpla solamente 
una de las siguientes condiciones: 

ser mayorde 6 años 
entra_por_edad =  edad > 6
o 

medir más de 1,50 metros.
entra_por_estatura = estatura > 1.5
### Escribir un programa en Python que solicite al usuario su edad y estatura, y que determine si cumple con los requisitos para subir a la atracción. Si cumple con al menos una de las condiciones, el programa debe imprimir "¡Puede acceder!" en la pantalla. Si no cumple con ninguna de las condiciones, el programa debe imprimir un mensaje que lo indique.

<center>(Ojo, tener en cuenta las palabras: más, mayor y sobre todo la letra o)</center>

 El conector "or" se utiliza para combinar dos o más expresiones lógicas y evaluarlas en conjunto. La expresión completa es verdadera si al menos una de las expresiones individuales es verdadera. Por ejemplo, la expresión lógica "A or B" será verdadera si al menos una de las variables A o B es verdadera. Solo si ambas variables son falsas, entonces la expresión completa será falsa.

La tabla de verdad del "or" es la siguiente:

<center>

| P | Q | P or Q |
|:-:|:-:|:------:|
| V | V |    V   |
| V | F |    V   |
| F | V |    V   |
| F | F |    F   |

</center>

El conector "or" se utiliza para crear expresiones lógicas que requieren que al menos una condición sea verdadera para ser verdadera.
"""

import random as rd

def main(): # PROGRAMA PRINCIPAL

    edad = rd.randint(4,20)
    estatura = rd.uniform(.5,2.1)

    entra_por_edad =  edad > 6
    entra_por_estatura = estatura > 1.5
    entra_al_juego = entra_por_edad or entra_por_estatura


    cadena = f"""
    Edad: {edad:10}
    Estatura: {estatura:10.2f}
    Entra al juego ? {entra_al_juego}
    """

    print(cadena)
main() # <== PUNTO DE ENTRADA

