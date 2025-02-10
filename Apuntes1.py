import random as rd

# Los () sirven para indicar accion

#Python es una secuencia ordenada de instrucciones 

#a = 0
#
#q = 1
#
#
#r = 0
#
#print("Hola")

# ctr + ñ para ir a la consola

# Si definimos una variable con MAYUSCULAS estoy difiniendo una constante. No significa que no se pueda modificar, simplemente que la idea es que no la modifiquemos, es un modismo

"""Enunciado = Leer 2 numeros y mostrar la suma

Revisar que la codificacion (abajo a la derechA) este siempre en UTF - 8 que es basicamente el conjunto de letras que utilizamos (en  este caso inglesa, no hay "ñ") si la uso el progrma me sale con error

"""

#Input es una funcion que permite ingresar un dato o ingresar algo al usuario

#numero1 = input("Ingrese un numero: ")  #El input me arroja una variable str, no me sirve como numero
#numero2 = input("Ingrese un numero: ")  #El input me arroja una variable str, no me sirve como numero
#
#suma = (int(numero1) + int(numero2))  #Si aca no los convierto en int, me concatena las palabras formando una cadena de caracteres y me arroja 22 en vez de 4
#
#print(f"La suma es: {suma}")

#El resultado de una division en python siempre es un flotante

# La funcion "Round" redondea el numero (Ver ejercicio 5 donde hay un ejemplo) que tambien se le pueden agregar los decimales que quieras despues de una ,

#pygame es un modulo para hacer juegos (siempre es necesario) como importa random

#a = 0 #Operador de asignacion
#b = a + 1 #Operador de adiccion
#
#c = 3/2 #Division
#c = 4//2 #El resultado siempre es un numero entero, no es un flotante
#
#x = 20 % 2 #Operador del resto, da como resultado el resto de una ddivison factorizado a su minima expresion ejemplo 17 / 5 es 3 con un resto de 2
#
#print(x)

#AAAAMMDD
#fecha = 20010417
#
##DD/MM/AAAAA
##Para quedarme con lo que hay a la derecha utilizo el operador %
#dia = fecha%100  #AAAAMM ===> DD #despues del "1" hay dos "00" que representan la cantidad de digitos que precisamos de nuestra variable, en este caso usamos 2 para el dia
##Para quedarme con lo qye hay a la izquierda utilizo el operador //
#anio = fecha // 10000 #AAAA <=== MMDD # Despues de "1" hay cuatro "0000" que representan la cantidad de digitos de los primera 4 numeros para nuestra variable años
#
#anio_mes = fecha // 100
#mes = anio_mes % 100
#
#cadena = f"{dia}/{mes}/{anio}"
#
#print(cadena)


""""
## Ejercicio 009

### Escribir un programa que permita ingresar valores del mismo tipo para las variables num1 y num2. Una vez cargadas, mostrar ambas variables por pantalla, intercambiá sus valores (que lo cargado en num1 quede en num2, y viceversa) y volvé a mostrarlas actualizadas.

### Como pensarlo:

1- Pedir al usuario que ingrese un valor para la variable num1.

2- Pedir al usuario que ingrese un valor para la variable num2.

3- Mostrar por pantalla el valor de las variables num1 y num2.

4- Intercambiar los valores de las variables num1 y num2.

5- Mostrar por pantalla el valor de las variables num1 y num2. 

"""

#num1 = int(input("Por favor ingresar el valor numero1 : "))
#num2 = int(input("Por favor ingresar el valor numero2 : "))
#
#print(num1)
#print(num2)
#
#a = num1
#b = num2
#
#auxiliar = num1 
#
#a = b
#b = auxiliar
#
#print(a)
#print(b)


""""
## Ejercicio 011

### Escribir un programa que permita resolver el siguiente problema:
### Tres personas aportan diferente capital a una sociedad y desean saber el valor total aportado y qué porcentaje aportó cada una (indicando nombre y porcentaje).
### Solicitar la carga por teclado del nombre de cada socio y su capital aportado, a partir de esto calcular e informar lo requerido previamente.

"""

#nombre1 = input("Nombre: ")
#capital1 = float(input(f"Ingrese el capital de {nombre1}: "))
#
#nombre2 = input("Nombre: ")
#capital2 = float(input(f"Ingrese el capital de {nombre2}: "))
#
#nombre3 = input("Nombre: ")
#capital3 = float(input(f"Ingrese el capital de {nombre3}: "))
#
#capital_total = capital1 + capital2 + capital3
#
#por1 = capital1 * 100 / capital_total
#por2 = capital2 * 100 / capital_total
#por3 = capital3 * 100 / capital_total
#
#cadena = f"""
#
#{nombre1:10}${capital1:20.2f} % {por1:5.2f}
#{nombre2:10}${capital2:20.2f} % {por2:5.2f}
#{nombre3:10}${capital3:20.2f} % {por3:5.2f}
#
#"""

#Despues del nombre1 le pusimos la cantidad de caracteres que queremos que ocupe como maximo despues del ":"
#Despues del capital1 le asignamos la cantidad maxima de caracteres y la cantidad de decimales a usar "2" y la "f" que representa "float". 
#Al final estamos usando una f-string, una cadena formateada, a la que le podemos dar el formato que a nosotros nos guste como la cantidad de decimales o de caracteres

#print(cadena)

#import random

"""

## Ejercicio 016

### Escribir un programa que permita al usuario ingresar un período de tiempo en segundos. Luego, el programa debe convertir ese período de tiempo a una forma más legible y comprensible para el usuario, expresando el resultado en días, horas, minutos y segundos. El resultado se mostrará en pantalla en un mensaje que indique la cantidad de segundos ingresados y su equivalente en días, horas, minutos y segundos.  

Ejemplo: 200000 segundos equivalen a 2 días, 7 horas, 33 minutos y 20 segundos.

### Usar en el programa las siguientes instrucciones:

dias = segundos // 86400 # 86400 segundos = 1 día

horas = (segundos % 86400) // 3600 # 3600 segundos = 1 hora

minutos = (segundos % 3600) // 60 # 60 segundos = 1 minuto

segundos_restantes = segundos % 60 # segundos restantes

"""

#segundos = random.randint(20000,900000)
#
#dias = segundos // 86400 # 86400 segundos = 1 dia
#
#horas = (segundos % 86400) // 3600  # 3600 segundos = hora   #(segundos / 86400 te da la cantidad de dias y segundos % 86400 te dan las horas restantes que no equivalen a 1 dia literalmente el resto)
#
#minutos = (segundos % 3600) // 60  # 60 segundos = 1 minutos # (si segundos % 3600 son el resto de minutos que no entran en un dia para formar 24 hs, a eso lo divido por 60 para que me de minutos exactos)
#
#segundos_restantes = segundos % 60  #Segundos restantes
#
#print(f"{dias} dias, {horas} horas, {minutos} minutos y {segundos_restantes} segundos")



"""""
## Ejercicio 018

### Escribir un programa que permita al usuario ingresar un número entero y luego muestre un mensaje indicando si el número es par o impar.

#### Pensando los pasos para resolver el problema:

-1 Pedir al usuario que ingrese un número entero.  
-2 Almacenar ese número en una variable.  

-3 __Verificar si el número es par o impar__.  

- Si el número es par, mostrar un mensaje indicando que es par.  
- Si el número es impar, mostrar un mensaje indicando que es impar.  

(Para verificar si un número es par o impar, se puede utilizar el operador módulo (%). Si el resto de la división del número por 2 es 0, entonces el número es par. Si el resto de la división del número por 2 es 1, entonces el número es impar.)


"""

#numero_1 = int(input("Por favor ingrese un numero: "))
#
#b = 2
#
#valor = numero_1 % b
#
#if valor == 0:
#    print("Esto es un numero par")
#else:
#    print("Esto es un numero impar")



""""
## Ejercicio 019

### Escribir un programa que permita ingresar dos números enteros e indicar si son iguales o distintos. 

# """


#numero_1 = int(input("Numero 1: "))
#numero_2 = int(input("Numero 2: "))
#
#if numero_1 == numero_2:
#    print("Los numeros son iguales")
#else:
#    print("Los numeros son distintos")

"""""

## Ejercicio 020

### Escribir un programa que permita ingresar dos cadenas de caracteres e indicar si son iguales o distintas.


"""

#valor_1 = input("Ingrese un texto: ")
#valor_2 = input("Ingrese un texto: ")
#
#valor_1 = valor_1.lower()
#valor_2 = valor_2.lower()
#
#final = valor_1 == valor_2
#
#if final:
#    print("Son iguales")
#else:
#    print("Son distintos")  


""""
## Ejercicio 024

### Para acceder a cierta atracción, es necesario cumplir con dos requisitos: tener __al menos__ 10 años de edad y medir __más__ de 1,60 metros.

<center>(Ojo, tener en cuenta las palabras: más,al menos y sobre todo la letra y)</center>

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



#edad = int(input("Escriba su edad: "))
#altura = float(input("Escriba su altura: "))
#
#condicion_1 = edad >= 10
#condicion_2 = altura > 1.60
#
#if condicion_1 and condicion_2:
#    print("Puede acceder")
#elif not condicion_1:
#    print("Usted es menor de edad")
#else:
#    print("Usted es muy enano")


#-------------------------------------------------------
#OTRA FORMA
#------------------------------------------------------


#import random as rd
#
#edad = rd.randint(5,20)
#altura = rd.uniform(1,2.10)
#
#print(edad)
#print(round(altura,2))
#
#condicion_1 = edad >= 10
#condicion_2 = altura > 1.60
#
#if condicion_1 and condicion_2:
#    print("Puede acceder")
#elif not condicion_1:
#    print("Usted es menor de edad")
#else:
#    print("Usted es muy enano")

""""
## Ejercicio 025

"""
#import random
#
#
#def main():
#
#    edad = random.randint(4,20)
#    estatura = random.uniform(0.5,2.1)
#
#    entra_por_edad = edad > 6
#    entra_por_estatura = estatura > 1.5
#    entrar_al_parque = entra_por_edad or entra_por_estatura
#
#    cadena = f"Edad: {edad}, Estatura: {round(estatura,2)}, {entrar_al_parque}"
#
#    print(cadena)
#main()

""""
# Ejercicio 026

"""

#def main():
#    faltan = None
#    asientos = random.randint(10,50)
#    invitados = random.randint(10,50)
#
#    alcanza_los_asientos = invitados <= asientos
#    cartel = "Todo bien!"
#
#    if not alcanza_los_asientos:
#        faltan = invitados - asientos
#        cartel = f"Faltan {faltan} asientos"
#
#    print(f"Asientos: {asientos}, Invitados: {invitados} ==> {cartel}")
#main()



""""
## Ejercicio 027

### Escribir un programa que permita ingresar una edad (entre 1 y 120 años), un género ('F'para mujeres, 'M' para hombres) y un nombre. 
# En caso de haber ingresado valores erróneos (edad fuera de rango o género inválido), informar tal situación indicando el nombre de la persona. 
# Si los datos están bien ingresados el programa debe indicar, sabiendo que las mujeres se jubilan con 60 años o más y los hombres con 65 años o más, si la persona está en edad de jubilarse.

"""




Generos_posibles =["Femenino", "Masculino"]

nombres_masculinos = [
    "Alejandro", "Carlos", "David", "Eduardo", "Fernando",
    "Gabriel", "Héctor", "Iván", "Javier", "Luis"]

nombres_femeninos = [
    "Andrea", "Beatriz", "Carla", "Diana", "Elena",
    "Florencia", "Gabriela", "Helena", "Isabel", "Juana"
]

edad_jubilacion_mujer = 60
edad_jubilacion_hombre = 65

genero = rd.choice(Generos_posibles)
edad = rd.randint(1,121)

if genero == "Femenino":
    nombre = rd.choice(nombres_femeninos)
    if edad >= edad_jubilacion_mujer:
        cartel = f"Nombre: {nombre}, Edad: {edad}, Genero: {genero} puede jubilarse"
    if not edad >= edad_jubilacion_mujer:
        cartel = f" {nombre}, {genero}, {edad} No puede jubilarse"
else:
    nombre = rd.choice(nombres_masculinos)
    if edad >= edad_jubilacion_hombre:
        cartel = f"Nombre: {nombre}, Edad: {edad}, Genero: {genero} puede jubilarse"
    if not edad >= edad_jubilacion_hombre:
        cartel = f" {nombre}, {genero}, {edad} No puede jubilarse"
print(cartel)



