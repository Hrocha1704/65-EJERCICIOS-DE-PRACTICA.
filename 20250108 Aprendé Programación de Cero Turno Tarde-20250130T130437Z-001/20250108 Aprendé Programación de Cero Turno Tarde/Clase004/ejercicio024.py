"""
Ejercicio 024

Para acceder a cierta atracción, es necesario cumplir con dos requisitos: 

tener al menos 10 años de edad   

entra_por_edad = edad >= 10

medir más de 1,60 metros.

entra_por_estatura = estatura > 1.6

(Ojo, tener en cuenta las palabras: más,al menos y sobre todo la letra y)

### Escribir un programa en Python que solicite al usuario su edad y estatura, y que determine si cumple con los requisitos para subir a la atracción. Si cumple con ambos requisitos, el programa debe imprimir "¡Puede acceder!" en la pantalla. Si no cumple con alguno de los requisitos, el programa debe imprimir un mensaje que indique el motivo por el cual no puede subir. Por ejemplo, si no cumple con el requisito de la edad, el programa debe imprimir "Lo siento, eres demasiado joven para acceder." Si no cumple con el requisito de la estatura, el programa debe imprimir "Lo siento, eres demasiado bajo para acceder"


Los conectores lógicos "and" y "or" son operadores booleanos utilizados en programación y en lógica matemática para combinar o unir dos o más expresiones lógicas.

El conector "and" se utiliza para combinar dos o más expresiones lógicas y evaluarlas en conjunto. La expresión completa es verdadera sólo si todas las expresiones individuales son verdaderas. Por ejemplo, la expresión lógica "A and B" será verdadera sólo si tanto A como B son verdaderos. Si alguna de las expresiones es falsa, la expresión completa será falsa.

La tabla de verdad del operador "and" se utiliza en lógica proposicional para determinar el valor de verdad de una proposición compuesta formada por dos proposiciones simples unidas por "and". La tabla de verdad del "and" se construye evaluando todas las posibles combinaciones de valores de verdad de las proposiciones simples, y determinando el valor de verdad de la proposición compuesta para cada combinación.

La tabla de verdad del "and" es la siguiente:

<center>

| P | Q | P and Q |
|:-:|:-:|:-------:|
| V | V |    V    |
| V | F |    F    |
| F | V |    F    |
| F | F |    F    |

</center>

En resumen, el conector "and" se utiliza para crear expresiones lógicas que requieren que todas las condiciones sean verdaderas para que la expresión sea verdadera.
"""

import random as rd

edad = rd.randint(1,20)
estatura = rd.uniform(0.50,2.10)

# tener al menos 10 años de edad   
entra_por_edad = edad >= 10

# medir más de 1,60 metros.
entra_por_estatura = estatura > 1.6

entra_al_juego = entra_por_edad and entra_por_estatura

cartel = ""

if entra_al_juego:
    cartel = "Entraste"
else:
    if not entra_por_edad:
        cartel = "Edad "

    if not entra_por_estatura:
        cartel = cartel + "Altura"

print(f"Edad: {edad:4} Estatura: {estatura:5.2f} ==> {cartel}")        