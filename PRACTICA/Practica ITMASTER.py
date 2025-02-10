"""
Ejercicio 44

"""
#import random


#def main():
#    a = int(input("Numero 1: "))
#    b = int(input("Numero 2: "))
#    copia_b = b  #Tengo que crear una copia para que el programa destruya la variable "copia" sino b siempre va a terminar en 0 y siempre me va a multiplicar por 0
#    #Tengo que usar un chivo para que sea ese el que temrine en 0 y me multiplique b tranquilamente
#    suma = 0
#    cadena = ""  #Defino a la variable con una str
#    while copia_b > 0:
#        suma += a
#        if copia_b == 1:
#            cadena += str(a) #Tuvimos que crear este condicional para que no nos muestre un "+" al final del print por consecuenta de que solo se agrega el mas cuando es != de 1
#        else:
#            cadena += (str(a) + '+') #Con este else estamos agregarndo el simbolo "+" a la cadena siempre que sea distinto de 1. Cuando es igual a =
#            # 1 la funcion ya no agrega ese "+" al final
#        copia_b -= 1
#    print(f"{a} * {b} = {cadena} = {suma}")
#    #Esto es una forma de switchear la variable
#    """"auxiliar = a
#    a = b   #Importate respetar el orden en el que cambiamos las variables con el auxiliar
#    b = auxiliar
#    """""
#    #Esto es otra forma de switchear la variable
#    a,b = b,a
#
#    print("*" * 100) #Esto es solo de estetica nada mas
#    #COPIAMOS EL MISMO CODIGO EXACTAMENTE ABAJO PERO CON LA VARIABLE CAMBIADA PARA QUE ME MUESTRE LOS 2 EJEMPLO QUE SOLICITA EL EJERCICIO
#    # 3*4 = 3+3+3+3
#    # 4*3 = 4+4+4
#    copia_b = b  #Tengo que crear una copia para que el programa destruya la variable "copia" sino b siempre va a terminar en 0 y siempre me va a multiplicar por 0
#    #Tengo que usar un chivo para que sea ese el que temrine en 0 y me multiplique b tranquilamente
#    suma = 0
#    cadena = ""
#    while copia_b > 0:
#        suma += a
#        if copia_b == 1:
#            cadena += str(a) #Tuvimos que crear este condicional para que no nos muestre un "+" al final del print por consecuenta de que solo se agrega el mas cuando es != de 1
#        else:
#            cadena += (str(a) + '+') #Con este else estamos agregarndo el simbolo "+" a la cadena siempre que sea distinto de 1. Cuando es igual a =
#            # 1 la funcion ya no agrega ese "+" al final
#        copia_b -= 1
#    print(f"{a} * {b} = {cadena} = {suma}")
#       
#main()

#Esto es otra forma de resolver el ejercicio pero con el bucle for

#def multiplicacion_de_numero(a,b):
#    sumatoria = 0
#
#    for _ in range(b):
#        sumatoria += a  
#    return sumatoria
#
#
#resultado = multiplicacion_de_numero(2,3)
#print(resultado)


""""
Ejercicio 41 A

"""
#Vamos a usar la tecnica del absurdo

#def main():
#    mayor = - float('inf')  #Utilizamos este metodo para conseguir un infinito
#
#    n = random.randint(-10,10)
#
#    while n != 0:
#        print(n)
#
#        if n > mayor:  #Esto siempre va a pasar ya que mayor es - infinito
#            mayor = n
#        n = random.randint(-10,10)  #Aca le pedimos al bucle que vuelva a generar un numero random hasta que llegue a 0 y cierre el bucle
#
#    print(f"Maximo: {mayor}")
#
#main()

""""

CALCULO DE UN FACTORIAL

"""

#def factorial(n):
#   copia_n = n  #Creo la variable chivo espiatorio para que sea la que va disminuyendo
#   resultado = 1 #La variable que se va a ir transformando en el bucle a lo que quiero
#
#   if copia_n <= 1:
#       resultado = 1
#
#   else:
#       while copia_n >= 1:
#           resultado *= copia_n
#           copia_n -= 1
#   
#   print(f"El factorial de {n} es igual a {float(resultado)}")
#
#   return resultado


#numero = factorial(7)



#numero1 = int(input("Ingrese un numero: "))
#numero2 = int(input("Ingrese un numero: "))
#numero3 = int(input("Ingrese un numero: "))
#
#
#mayor = numero1
#medio = numero2
#menor = numero3
#
#""""
#if: Siempre se evalúa independientemente de las condiciones previas. 
#Si es verdadera, se ejecuta el bloque de código correspondiente.
#
#elif (else if): Se evalúa solo si las condiciones anteriores (es decir, los if anteriores) no se cumplen. 
#Es decir, si una condición en un bloque if es verdadera, los bloques elif siguientes no se evalúan, incluso si podrían ser verdaderos.
#
#
#RAZON POR LA CUAL NO ME FUNCIONABA EL CODIGO SI UTILIZABA ELIF EN VEZ DE IF.
#
#EL ELIF ES UN ELSE IF, ES DECIR, SOLO SE EJECUTAN SI EL IF ANTERIOR ES FALSO.
#SI QUEREMOS QUE SE ANALICEN TODAS LAS CONDICIONES, USAMOS IF SIEMPRE ASI SE EJECUTA EL CODIGO CORRECTAMENTE
#
#Cuando usas elif en lugar de if, el flujo de ejecución es el siguiente:
#
#Si la condición de un if es verdadera, se ejecuta ese bloque y se omiten las siguientes condiciones (en los bloques elif).
#Si la condición de un if es falsa, solo se evaluará el bloque elif siguiente, y si hay un intercambio que debería ocurrir, no se realizará porque el elif solo se ejecuta si el if anterior fue falso.
#
#"""
#if mayor < medio:
#    auxiliar = mayor
#    mayor = medio
#    medio = auxiliar
#
#if mayor < menor:
#    auxiliar = mayor
#    mayor = menor
#    menor = auxiliar
#
#if medio < menor:
#    auxiliar = medio
#    medio = menor
#    menor = auxiliar
#
#print(f"El numero mayor es {mayor}, el del medio es {medio} y el menor es {menor}")


""""

## Ejercicio 047

### Escribir un programa que permita validar la nota de un examen. Se espera que la nota que el usuario ingrese sea un número comprendido entre 0 y 10.  
### La misma debe ser ingresada tantas veces como sea necesario hasta que quede comprendida dentro del rango indicado.



"""


#def main():
#    nota = int(input("Nota: "))
#
#    while nota < 0 or nota > 10:  #ERROR 
#        print("Error: Nota fuera de rango")
#        nota = int(input("Nota: ")) #LE DOY OPORTUNIDAD NUEVAMENTE HASTA QUE SEA UN NUMERO QUE ROMPA EL CICLO
#
#    print(f"Nota: {nota}")  #Si esta dentro del rango no entra en el ciclo
#
#main()


""""


## Ejercicio 048

### Escribir un programa que permita realizar varias operaciones matemáticas ingresando un caracter por cada una la operación a realizar 
# (‘+’, ‘-’, ‘*’, ‘/’, ‘F’) y dos números enteros en el caso que no haya elegido ‘F’. 
# La computadora debe mostrar el resultado para la operación ingresada. Considerar que no se puede dividir por cero. 
# Cuando la operación ingresada sea ‘F’ nos indicará que no se desean calcular más operaciones.


"""

#OPERACIONES_POSIBLES = "+","-","*","/","%","//","F"  #Esto es una tupla
#
#def main():
#
#    operacion = input(f"Ingrese una operacion {OPERACIONES_POSIBLES}: ").upper()
#    while operacion != "F":
#        if operacion in OPERACIONES_POSIBLES:
#            operando1 = int(input("Numero 1: "))
#            operando2 = int(input("Numero 2: "))
#
#            if operacion == '+':
#                resultado = operando1 + operando2
#            elif operacion == '-':
#                resultado = operando1 - operando2
#            elif operacion == '*':
#                resultado = operando1 * operando2
#            else:
#                if operando2 != 0:
#                    if operacion == '/':
#                        resultado = operando1 / operando2
#                    elif operacion == '//':
#                        resultado = operando1 // operando2
#                    else:
#                        resultado = operando1 % operando2
#    
#                else:
#                    resultado = "Error"
#
#            print(f"{operando1} {operacion} {operando2} = {resultado}")
#        else:
#            print(f"{operacion} Operacion erronea")
#
#        operacion = input(f"Ingrese una operaciones {OPERACIONES_POSIBLES}: ").upper()
#
#main()



""""

## Ejercicio 050

### Escribir un programa que permita validar la nota de un examen. Se espera que la nota que el usuario ingrese sea un número comprendido entre 0 y 10.  
### La misma debe ser ingresada tantas veces como sea necesario hasta que quede comprendida dentro del rango indicado.
- Las notas 1 y 3 no usan nunca.  
- La nota 0 se reserva para los ausentes.  
### Las notas válidas pueden ser un 2 o un valor entre 4 y 10.


"""




#def main():
#
#    
#    todo_bien = False
#
#    while not todo_bien:
#         nota = int(input("Ingrese una nota: "))
#         verdadero = 0 <= nota <= 10
#
#         if nota == 1 or nota == 3:
#              print("Error, nota no posible")
#              todo_bien = False
#
#         elif nota == 0:
#             print("Usted estuvo ausente")
#             todo_bien = True
#
#         elif not verdadero:
#             print(f"Nota {nota} no se encuentra dentro de los rangos aceptados")
#             todo_bien = False
#         else:
#             print(f"Su nota es {nota}")
#             todo_bien = True
#
#    
#main()


""""
## Ejercicio 046

### Escribir un programa que a partir de un número entero cant ingresado por el usuario permita cargar por teclado cant números enteros. 
# La computadora debe mostrar cuál fue el mayor número y en qué posición apareció.



"""
#def main():
#    posicion = 0
#    maximo = -float("inf")  #Definimos al numero mayor por absurdo. Le damos un numero muy bajito para que el mayor numero de los que estemos analizando salga como el mayor
#    minimo = float("inf")   #Definimos al numero menor por absurdo. Le damos un numero muy alto para que el menor numero de los que estemos analizando salga como el menor
#    cantidad_de_numeros = int(input("Ingrese una cantidad de numeros: "))
#
#    for x in range (cantidad_de_numeros):
#        numero = int(input("Ingrese un numero: "))
#        posicion += 1
#
#        if numero >= maximo:
#            maximo = numero
#            posicion_maximo = posicion
#
#        if numero <= minimo:
#            minimo = numero
#            posicion_minimo = posicion
#
#    print(f"Maximo {maximo} posicion: {posicion_maximo}")
#    print(f"Minimo {minimo} posicion: {posicion_minimo}")
#        
#main()



""""
## Ejercicio 046 (B)

### Escribir un programa que a partir de un número entero cant ingresado por el usuario permita cargar por teclado cant números enteros. 
# La computadora debe mostrar cuál fue el mayor número y en qué posición apareció.



"""
#import random as rd
#
#
#posicion = 0
#maximo = -float("inf")  #Definimos al numero mayor por absurdo. Le damos un numero muy bajito para que el mayor numero de los que estemos analizando salga como el mayor
#contador = 0
#contador_numeros = 0
#cantidad_de_numeros = rd.randint(1,100)
#
#
#for posicion in range (cantidad_de_numeros+1):   #Usamos la variable que itera para que vaya contando 
#    numero = rd.randint(1,100)
#    print(f" Numero {contador_numeros} ==> {numero}")
#    
#
#    if numero > maximo:
#        maximo = numero
#        posicion_maximo_primer = posicion #Aca, como estoy en la primera parte del ciclo, el mayor numero es el primero y ultimo a la vez y lo defino asi
#        posicion_ultimo_maximo = posicion #Aca, como estoy en la primera parte del ciclo, el mayor numero es el primero y ultimo a la vez y lo defino asi
#        contador = 0  #Determino el contador 0 y va a ir sumando a medida que se vayan sumando mayores en la seccion de abajo
#        repetidos = 0 #Definimos esta variable para que me diga en que posicion estuvieron los repetidos
#    elif numero == maximo:
#        contador += 1
#        posicion_ultimo_maximo = posicion #Determino el contador 0 y va a ir sumando a medida que se vayan sumando mayores en la seccion de abajo
#        repetidos += posicion #Definimos esta variable para que me diga en que posicion estuvieron los repetidos
#
#    contador_numeros += 1
#
#
#print(f"La cantidad de numeros es: {cantidad_de_numeros}")
#print(f"Maximo {maximo} Primero: {posicion_maximo_primer} Ultimo: {posicion_ultimo_maximo} Repetidos: {contador} [{repetidos}]")


""""
## Ejercicio 053

### Escribir un programa que permita ingresar nombre y edad de un grupo de personas (para cada una, nombre y edad). 
# La carga termina cuando en el nombre de la persona se ingresa un asterisco ('*'). Mostrar al final cómo se llama la persona más joven.


"""    


#def obtener_datos():
#
#    nombre = ""
#    apellido = ""  #Tengo que declarar el punto de partida de las variables primero
#    edad = 0  #Si yo uso el if sin declarar las variables me va a salir un error por no tenes declarado el tipo de dato
#
#    nombre = input("Nombre: ")
#    if nombre != '*':
#        apellido = input("Apellido: ")
#        edad = int(input("Edad: "))
#
#    return nombre, apellido, edad
#
#
#
#def main():
#    """"
#    Programa principial
#    
#    """
#
#    nombre,apellido,edad = obtener_datos()
#    while nombre != '*':
#
#        nombre_completo = f"{nombre.capitalize}  {apellido.capitalize}"
#
#        print(nombre_completo)
#
#        nombre,apellido,edad = obtener_datos()
#
#main()


""""
## Ejercicio 054

### Escribir un programa que permita controlar con validación el ingreso a un sitio web. Teniendo dos constantes con un nombre de usuario ("admin") y una contraseña ("123456"), el programa debe permitir al usuario ingresar sus credenciales. Si las mismas son erróneas, se volverán a pedir hasta un máximo de 3 intentos. 
# Finalmente, la computadora debe mostrar alguno de los siguientes mensajes según sea el caso: "Acceso concedido" o "Se ha bloqueado la cuenta"

"""

#USUARIO  = "admin"
#CONTRASENA = "1234"
#max_intentos = 3
#
#def ingresar_credenciales() -> bool: #El -> bool es opcional, es simplemente a nivel informativo
#
#    ingreso_ok = False
#    intento = 0
#    
#    while intento < max_intentos and not ingreso_ok:  #El bucle se va a ejecutar hasta encontrar un verdadero. Si yo declaro ingreso_ok como falso de una no se va a ejecutar el bucle
#
#        usuario = input("Usuario: ") #Variables locales
#        contrasena = input("Contrasena: ")  #Variables locales
#        intento += 1
#        
#        if USUARIO == usuario and CONTRASENA == contrasena:
#            ingreso_ok = True
#        else:
#            ingreso_ok = False
#
#    return ingreso_ok
#
#
#
#def main():
#    ingreso_ok = ingresar_credenciales()
#    if ingreso_ok:
#        print("Acceso concedido")
#    else:
#        print("Se ha bloqueado la cuenta")
#
#main()

#----------------------------------------------------------IMPORTANTISIMO (FUNCIONES)------------------------------------------------------------------------------------
""""
import random as rd


def obtener_dia(aaaammdd: int) -> int:
    # AAAAMM ==> DD
    dia = aaaammdd % 100

    return dia

def obtener_anio(aaaammdd: int) -> int:
     #AAAA <== MMDD
    anio = aaaammdd//10000  #10.000 porque son 4 numeros

    return anio

def obtener_mes(aaaammdd: int) -> int:

    # AAAA ==> MM <== DD
    mes = (aaaammdd//100)%100

    return mes

def str_fecha_corta(aaaammdd: int) -> int: #DESPUES DE TERMINAR EJECUTARSE LA PRIMERA, SE EJECUTA ESTA 4TA
     
     dia = obtener_dia(aaaammdd)
     mes = obtener_mes(aaaammdd)
     anio = obtener_anio(aaaammdd)

     cadena = f"{dia:02}/{mes:02}/{anio:04}"  #Los numeros despues de los ":" es para darle formato a la cadena formateada

     return cadena

def isbisiesto(anio:int) -> bool:  #TERCERA FUNCION QUE SE EJECUTA
    return anio % 4 == 0

def obtener_los_dias_del_mes(mes:int,anio:int) -> int:  #SEGUNDA FUNCION QUE SE EJECUTA
    cantidad = 31
    
    if mes in(4,6,9,11):
        cantidad = 30

    elif mes == 2:
        if isbisiesto(anio):
            cantidad = 29
        else:
            cantidad = 28

    return cantidad

def crear_fecha_random(anio: int) -> int:  #PRIMERA FUNCION QUE SE EJECUTA
    mes = rd.randint(1,12)

    cantidad_de_dias = obtener_los_dias_del_mes(mes,anio)

    dia = rd.randint(1,cantidad_de_dias)

    return (anio*10000) + (mes*100) + (dia)   #El necesito multiplicar el anio por 10000 para agregar los 4 "0" y multiplicar a mes por 100 para agregar los 2 "0"

    '''
    dia =        12
    mes =       900
    anio = 20250000
---------------------
            20250912
    
    
    '''
    




def main():

    # AAAAMMDD
    fecha = crear_fecha_random(2025)

    print(str_fecha_corta(fecha))

main() 

if __name__ == "__main__":
    main()

"""
#----------------------------------------------------------IMPORTANTISIMO (FUNCIONES)------------------------------------------------------------------------------------

"""
## Ejercicio 064

### Un animal en rehabilitación después de una cirugía requiere ser alimentado y monitoreado en un zoológico. Se alimenta al animal 3 veces al día y se le da de comer hasta que ya no tenga ganas de comer.
### Por cada tanda de comida, se debe ingresar la cantidad de alimento en kg (número entero) que se le dio y se le debe preguntar al animal si quiere seguir comiendo ('S', 'N').
### Se desea conocer:
- ### Cuál de las 3 comidas fue la que el animal comió más cantidad de alimento y cuánto fue esa cantidad.
- ### El total en kg de alimento recibido.
- ### Promedio de alimento por tanda.

"""




      

      
