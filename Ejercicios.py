""""
## Ejercicio 001

### Escribir un programa que permita que el usuario ingrese su nombre. El programa debe emitir una salida con un mensaje de bienvenida que incluya el nombre ingresado.
Ejemplo de ejecución:

    Ingrese su nombre: Juan
    Bienvenido Juan


"""


#nombre = input("Ingrese su nombre: ")
#
#print("Bienvenido!", nombre)


""""

## Ejercicio 002

### Escribir un programa que solicite al usuario su nombre y su edad, y luego muestre por pantalla un mensaje que diga "Hola, [nombre]. Tu edad es [edad] años."
Ejemplo de ejecución:

    Ingrese su nombre: Juan
    Ingrese su edad: 30
    Hola, Juan. Tu edad es 30 años.


"""

#nombre = input("Ingrese su nombre: ")
#edad = int(input("Ingrese su edad: "))
#
#print("Buenas!", nombre, "Tu edad es", edad)


""""
## Ejercicio 003

### Escribir un programa que solicite al usuario su nombre y su edad, después pida una cantidad de años y muestre por pantalla un mensaje que indique cuántos años tendrá la persona después de sumarle a su edad la cantidad de años ingresada. El mensaje debe tener el siguiente formato: 'Hola, [nombre]. Dentro de [cantidad] años tendrás [edad + cantidad] años'".
Ejemplo: Si el usuario ingresa "Juan" y "20" y luego ingresa "5", el programa debe mostrar por pantalla "Hola, Juan. Dentro de 5 años tendrás 25 años".


"""

#nombre = input("Ingrese su nombre: ")
#edad = int(input("Ingrese su edad: "))
#cantidad_años = int(input("Ingrese una cantidad de años: "))
#
#print("Hola", nombre, "dentro de", cantidad_años ,"años", "Tendras", edad + cantidad_años)

""""
## Ejercicio 004

### Escribir un programa que solicite al usuario ingresar tres numeros enteros.El programa debe mostrar por pantalla el resultado de sumar los tres numeros de la siguiente manera: "[numero1] + [numero2] + [numero3] = [suma]".
Ejemplo: Si el usuario ingresa 1, 2 y 3, el programa debe mostrar por pantalla: "1 + 2 + 3 = 6".

"""

#numero1 = int(input("Ingrese un numero: "))
#numero2 = int(input("Ingrese un numero: "))
#numero3 = int(input("Ingrese un numero: "))
#
#print(numero1 + numero2 + numero3)

""""
## Ejercicio 005

### Escribir un programa que solicite al usuario ingresar dos notas de un alumno. El programa debe mostrar por pantalla el promedio de las notas de la siguiente manera: "Notas: [nota1] , [nota2] ==> promedio: [(nota1+nota2)/2]".
Ejemplo: Si el usuario ingresa 7 y 8, el programa debe mostrar por pantalla: "Notas: 7 , 8 ==> promedio: 7.5".


"""
#nota1 = float(input("Ingrese su nota: "))
#nota2 = float(input("Ingrese su nota: "))
#
#promedio = (nota1 + nota2) / 2
#
#print("Notas", nota1, nota2, "===>", promedio)


#contador = 0
#sumatoria = 0
#
#while contador <= 5:
#    sumatoria += contador
#    contador += 1
#
#print(sumatoria)



""""
## Ejercicio 038

### Escribir un programa que permita ingresar un número entero n. Debe mostrar los primeros 10 múltiplos de n.
### Ejemplo  
n = 5  

n x 1 = 5  
n x 2 = 10  
n x 3 = 15  
n x 4 = 20  
n x 5 = 25  
n x 6 = 30  
n x 7 = 35  
n x 8 = 40  
n x 9 = 45  
n x 10 = 50   


"""

 #RESUELTO CON WHILE
#CANTIDAD_MULTIPLOS = 10   #Variable global
#
#def main():
#    n = int(input("Inserte un numero natural: "))
#    naturales = 1  #Variable local
#
#    while naturales <= CANTIDAD_MULTIPLOS:
#        multiplicacion = n * naturales
#        print(f" {n} x {naturales} = {multiplicacion}")
#        naturales += 1
#
#
#main()
#
##RESUELTO CON FOR
#def main():
#    multiplo = list(range(0,11))  #Tuvimos que definir al rango como una lista para poder realizar el bucle for y que nuestra variable lea, itere y nos diga las multiplicaciones
#    n = int(input("Inserte un numero natural: "))
#    naturales = 1
#
#    for x in multiplo:
#        multiplicacion = n * x
#        print(f"{n} x {x} = {multiplicacion}")
#        naturales += 1  #Agregamos el +=1 despues del print para que mi variable no empieze en 1
#
#main()



""""

## Ejercicio 040

### Escribir un programa que permita ingresar dos numeros enteros a y b. El programa debe mostrar:

- La suma de los numeros pares entre a y b.  
- El producto de los numeros impares entre a y b.


"""

#def main():
#    a = int(input("a: "))
#    b = int(input("b: "))
#
#    if b < a:
#        a,b = b,a
#
#    suma = 0
#    producto = 1
#
#    for numero in range(a,b+1): #el b+1 lo ponemos para que se incluya en numero "b" en el rango (por definicion, python no lo hace)
#        if numero % 2 == 0:
#            suma += numero  
#        else:
#            producto *= numero
#
#    print(f"Suma pares: {suma}")
#    print(f"Producto impares: {producto}")
    


#main()


""""

## Ejercicio 011

### Escribir un programa que permita resolver el siguiente problema:
### Tres personas aportan diferente capital a una sociedad y desean saber el valor total aportado y qué porcentaje aportó cada una (indicando nombre y porcentaje).
### Solicitar la carga por teclado del nombre de cada socio y su capital aportado, a partir de esto calcular e informar lo requerido previamente.

"""

#def main():
#    persona1 = input("nombre: ")
#    persona2 = input("nombre: ")
#    persona3 = input("nombre: ")
#
#    aporte1 = int(input("Capital a aportar: "))
#    aporte2 = int(input("Capital a aportar: "))
#    aporte3 = int(input("Capital a aportar: "))
#
#
#    total = aporte1 + aporte2 + aporte3
#
#    print(f"El total aportado del capital es {total} del cual {persona1} aporto el {round((aporte1/total),2)}%, {persona2} aporto el {round((aporte2/total),2)}% y {persona3} aporto el {round((aporte3/total),2)}%")
#
#main()

""""
## Ejercicio 022

### Escribir un programa que permita ingresar tres números enteros e indicar cual es el mayor.

y 

## Ejercicio 023

### Escribir un programa que permita ingresar tres números enteros y mostrar el mayor el menor y el valor que esta en medio.

### Ejemplo: Si se ingresan los números 5, 3 y 7, el programa debe mostrar el número 5 como el menor, el número 7 como el mayor y el número 3 como el que esta en medio.

### Otra vez se mezclaron las instrucciones, ¿podrías arreglarlas?


"""

#def main():
#    n1 = int(input("Ingrese un numero: "))
#    n2 = int(input("Ingrese un numero: "))
#    n3 = int(input("Ingrese un numero: "))
#
#
#    mayor = n1
#    medio = n2
#    menor = n3
#
#
#    if menor > mayor:
#        menor,mayor = mayor, menor
#
#    if medio > mayor:
#        medio,mayor = mayor, medio
#
#    if menor > medio:
#        menor,medio = medio, menor
#
#    
#    print(f"El numero mayor es {mayor}, el medio es {medio} y el menor es {menor}")
#
#main()



""""
## Ejercicio 024

### Para acceder a cierta atracción, es necesario cumplir con dos requisitos: tener __al menos__ 10 años de edad y medir __más__ de 1,60 metros.

<center>(Ojo, tener en cuenta las palabras: más,al menos y sobre todo la letra y)</center>

### Escribir un programa en Python que solicite al usuario su edad y estatura, y que determine si cumple con los requisitos para subir a la atracción. Si cumple con ambos requisitos, el programa debe imprimir "¡Puede acceder!" en la pantalla. Si no cumple con alguno de los requisitos, el programa debe imprimir un mensaje que indique el motivo por el cual no puede subir. Por ejemplo, si no cumple con el requisito de la edad, el programa debe imprimir "Lo siento, eres demasiado joven para acceder." Si no cumple con el requisito de la estatura, el programa debe imprimir "Lo siento, eres demasiado bajo para acceder"


"""

#def main():
#    condicion1 = 10
#    condicion2 = 1.60
#
#
#    edad = int(input("Edad: "))
#    estatura = float(input("Altura: "))
#
#    if edad >= condicion1 and estatura >= condicion2:
#        cartel = "Puedes ingresar al parque"
#
#    if edad < condicion1:
#        cartel = "Usted es menor de edad"
#
#    if estatura < condicion2:
#        cartel = "Usted es enano"
#
#    if edad < condicion1 and estatura < condicion2:
#        cartel = "Usted no cumple ningun requisito"
#
#    print(cartel)
#
#main()


""""
## Ejercicio 026

### Escribir un programa que permita ingresar la cantidad de invitados a una fiesta y la cantidad de asientos disponibles en el salon. 
# Debes indicar si alcanzan los asientos, Si los asientos no alcanzaran indicar cuántos faltan para que todos los invitados puedan sentarse.



"""

#import random as rd 
#
#
#cantidad_invitados = rd.randint(1,100)
#cantidad_asientos = rd.randint(1,100)
#
#
#fiesta = cantidad_asientos >= cantidad_invitados
#
#if fiesta:
#    cartel = "Se puede hacer la fiesta"
#else:
#    faltante = cantidad_invitados - cantidad_asientos
#    cartel = f"hay {cantidad_invitados} invitados y {cantidad_asientos} asientos por ende faltan {faltante} de asientos"
#
#
#    
#    
#print(cartel)


""""

## Ejercicio 027

### Escribir un programa que permita ingresar una edad (entre 1 y 120 años), un género ('F'para mujeres, 'M' para hombres) y un nombre.
# En caso de haber ingresado valores erróneos (edad fuera de rango o género inválido), informar tal situación indicando el nombre de la persona. Si los datos están bien ingresados el programa debe indicar, sabiendo que las mujeres se jubilan con 60 años o más y los hombres con 65 años o más, si la persona está en edad de jubilarse.




"""

#Generos_posibles =["Femenino", "Masculino"]
#
#nombres_masculinos = [
#    "Alejandro", "Carlos", "David", "Eduardo", "Fernando",
#    "Gabriel", "Héctor", "Iván", "Javier", "Luis"]
#
#nombres_femeninos = [
#    "Andrea", "Beatriz", "Carla", "Diana", "Elena",
#    "Florencia", "Gabriela", "Helena", "Isabel", "Juana"
#]
#
#edad_jubilacion_mujer = 60
#edad_jubilacion_hombre = 65
#
#genero = rd.choice(Generos_posibles)
#edad = rd.randint(1,121)
#
#if genero == "Femenino":
#    nombre = rd.choice(nombres_femeninos)
#    if edad >= edad_jubilacion_mujer:
#        cartel = f"Nombre: {nombre}, Edad: {edad}, Genero: {genero} puede jubilarse"
#    if not edad >= edad_jubilacion_mujer:
#        cartel = f" {nombre}, {genero}, {edad} No puede jubilarse"
#else:
#    nombre = rd.choice(nombres_masculinos)
#    if edad >= edad_jubilacion_hombre:
#        cartel = f"Nombre: {nombre}, Edad: {edad}, Genero: {genero} puede jubilarse"
#    if not edad >= edad_jubilacion_hombre:
#        cartel = f" {nombre}, {genero}, {edad} No puede jubilarse"
#print(cartel)

"""

## Ejercicio 028

### Crear un programa que pida un número de mes (ejemplo 4) y escriba el nombre del mes en letras ("abril"). 
# Verificar que el mes sea válido e informar en caso que no lo sea.


"""

#posibilidad = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#
#mes = int(input("Ingrese un mes en numero: "))
#
#if mes in posibilidad:
#    if mes == 1:
#        cartel = "Enero"
#    elif mes == 2:
#        cartel = "Febrero"
#    elif mes == 3:
#        cartel = "Marzo"
#    elif mes == 4:
#        cartel = "Abril"
#    elif mes == 5:
#        cartel = "Mayo"
#    elif mes == 6:
#        cartel = "Junio"
#    elif mes == 7:
#        cartel = "Julio"
#    elif mes == 8:
#        cartel = "Agosto"
#    elif mes == 9:
#        cartel = "Septiembre"
#    elif mes == 10:
#        cartel = "Octubre"
#    elif mes == 11:
#        cartel = "Noviembre"
#    elif mes == 12:
#        cartel = "Diciembre"
#    
#else:
#    cartel = f"{mes} es un mes invalido"
#
#print(cartel)


""""
## Ejercicio 029

### Escribir un programa que permita Ingresar las notas de los dos parciales de un alumno e indicar si promocionó, aprobó o debe recuperar. Si el valor de la nota no esta entre 0 y 10, debe informar un error.
- Se promociona cuando las notas de ambos parciales son mayores o iguales a 7.
- Se aprueba cuando las notas de ambos parciales son mayores o iguales a 4.
- Se debe recuperar cuando al menos una de las dos notas es menor a 4.


"""

#nota1 = int(input("Nota 1: "))
#nota2 = int(input("Nota 2: "))
#
#notaposible = list(range(1, 11))  
#
#promociona = nota1 >= 7 and nota2 >= 7
#aprueba = 4 <= nota1 < 7 and 4 <= nota2 < 7
#recupera = nota1 < 4 or nota2 < 4
#
#if promociona and nota1 in notaposible and nota2 in notaposible:
#    cartel = "Promociona"
#elif aprueba and nota1 in notaposible and nota2 in notaposible:
#    cartel = "Aprueba"
#elif recupera and nota1 in notaposible and nota2 in notaposible:
#    cartel = "Recupera"
#else:
#    cartel = "Nota imposible"
#
#print(cartel)


    
""""
## Ejercicio 030

### Escribir un programa que permita al usuario ingresar dos números enteros. La computadora debe indicar si el mayor es divisible por el menor.

(Un número entero a es divisible por un número entero b cuando el resto de la división entre a y b es 0)

"""


#numero1 = int(input("Numero 1: "))
#numero2 = int(input("Numero 2: "))
#
#mayor = numero1
#menor = numero2
#
#if mayor < menor:
#    mayor, menor = menor, mayor
#
#
#if menor != 0 and mayor % menor == 0:
#    cartel = "Es divisible"
#else:
#    cartel = "No es divisible"
#
#print(cartel)



""""
## Ejercicio 032

### Una remisería requiere un sistema que calcule el precio de un viaje a partir de la cantidad de km que desea recorrer el usuario.
### Tiene la siguiente tarifa:

- Viaje mínimo $50  

- Si recorre entre 0 y 10km: $20/km  

- Si recorre 10km o más: $15/km  


### Escribir un programa que permita ingresar la cantidad de km que desea recorrer el usuario y muestre el precio del viaje.


"""

#def main():
#
#    km = int(input("Cuantos km vas a recorrer: "))
#    viaje_minimo = 50
#
#    if km in range(0,11):
#        cartel = f"El costo del viaje sera {(viaje_minimo + 20)}"
#    elif km >= 10:
#        cartel = f"El costo del viaje sera {(viaje_minimo + 15)}"
#    
#
#    print(cartel)
#
#main()




""""

## Ejercicio 037

### Escribir un programa que muestre todos los números enteros del 1 al 5, y luego los mismos números pero en orden inverso.


"""

#for i in range (1,6):
#    print(i) 
#
#
#print("*"*10)
#
#for j in range (5,0,-1):
#    print(j)


""""

## Ejercicio 038

### Escribir un programa que permita ingresar un número entero n. Debe mostrar los primeros 10 múltiplos de n.
### Ejemplo  
n = 5  

n x 1 = 5  
n x 2 = 10  
n x 3 = 15  
n x 4 = 20  
n x 5 = 25  
n x 6 = 30  
n x 7 = 35  
n x 8 = 40  
n x 9 = 45  
n x 10 = 50   


"""

#n = int(input("Numero: "))
#
#multiplo = 1
#
##while multiplo < 11:
##    resultado = n * multiplo
##    print(f" {n} x {multiplo} = {resultado}")
##    multiplo += 1
#    
#
#for i in range(1,11):
#    resultado = n * i
#    print(f" {n} x {i} = {resultado}")


""""
## Ejercicio 039

### Escribir un programa para calcular e imprimir la suma de los números comprendidos entre 42 y 176

"""

#contador = 42
#suma = 0
#
#while contador <= 176:
#    suma += contador
#    contador += 1
#
#    print(suma)


## Ejercicio 040

### Escribir un programa que permita ingresar dos numeros enteros a y b. El programa debe mostrar:

#- La suma de los numeros pares entre a y b.  
#- El producto de los numeros impares entre a y b.



""""

## Ejercicio 040

### Escribir un programa que permita ingresar dos numeros enteros a y b. El programa debe mostrar:

- La suma de los numeros pares entre a y b.  
- El producto de los numeros impares entre a y b.


"""




#n1 = int(input("Numero 1: "))
#n2 = int(input("Numero 2: "))
#
#
#mayor = n1
#menor = n2
#
#suma = 0
#producto = 1
#
#if mayor < menor:
#    mayor, menor = menor, mayor
#
#for i in range (menor, mayor+1):  #Agrego el + 1 para que incluya el ultimo numero tambien
#    if i % 2 == 0:
#        suma += i
#
#    else:
#        producto *= i
#
#    print(suma, producto)

""""
## Ejercicio 041

### Escribir un programa que lea números enteros hasta que se ingrese un 0, y muestre el máximo.


"""

#import random
#
#
#n = 1
#mayor = -float("inf")
#
#while n != 0:
#    n = random.randint(0,100)
#    print(n)
#    for i in range (n):
#        if n > mayor:
#            mayor = n
#
#print(f"El mayor numero fue el {mayor}")


"""
## Ejercicio 042

### Escribir un programa que lea números enteros hasta que se ingrese un 0, y muestre el promedio de los números ingresados.

"""

#import random
#
#
#n = 1
#suma = 0
#mayor = -float("inf")
#contador = 0
#
#while n != 0:
#    n = random.randint(0,100)
#    print(n)
#    for i in range (n):
#        suma += i
#        contador += 1
#
#        promedio = (suma / contador)
#
#print(f"El promedio fue {round(promedio,2)}")


""""
## Ejercicio 043

### Escribir un programa que lea números enteros hasta que se la suma de éstos sea mayor que 100, y muestre la cantidad de números ingresados.

"""

#import random
#
#suma = 0
#contador = 0
#n = random.randint(1,10)
#
#while suma <= 100:
#    print(n)
#    suma += n
#    contador += 1
#    n = random.randint(1,10)
#
#
#print(f"la cantidad de numeros ingresados fue {contador}")


""""
## Ejercicio 044

### Escribir un programa que permita leer dos números A y B (enteros positivos). Calcular el producto A * B por sumas sucesivas e imprimir el resultado.

### Ejemplo:

- 4*3 = 4 + 4 + 4 (4 sumado 3 veces).  
- 3*4 = 3 + 3 + 3 + 3 (3 sumado 4 veces).

"""

#def main():
#    n1 = int(input("Numero 1: "))
#    n2 = int(input("Numero 2: "))
#
#    mayor = n1
#    menor = n2
#
#    if mayor < menor:
#        mayor, menor = menor, mayor
#
#
#    for i in range (menor, mayor):
#        mayor += mayor
#
#    print()
#main()


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

""""
## Ejercicio 045

### Escribir un programa que permita leer dos números naturales A y B. Calcular A elevado a la B mediante productos sucesivos y mostrar el resultado.  

### Ejemplo:  

- 4^3 = 4 * 4 * 4 (4 multiplicado 3 veces).  
- 3^4 = 3 * 3 * 3 * 3 (3 multiplicado 4 veces).

"""
#def potencias(a: int, b: int) -> int:
#    multiplicacion = 1
#    copia_b = b
#    chain = ""
#    for i in range (b):
#        multiplicacion *= a
#        if copia_b != 1:
#            chain += (str(a)+ "*")
#        else:
#            chain += (str(a))
#            
#        copia_b -= 1
#
#        cadena = f"{a} ^ {b} = {chain} = {multiplicacion}"
#
#    return cadena
#
#
#print(potencias(2,3))


"""
## Ejercicio 046

### Escribir un programa que a partir de un número entero cant ingresado por el usuario permita cargar por teclado cant números enteros. 
# La computadora debe mostrar cuál fue el mayor número y en qué posición apareció.

"""

#import random as rd
#
#
#def cant_numeros (n):
#    
#    mayor = -float("inf")
#    lista = []
#
#    while n != 0:
#        numero = rd.randint(1,100)
#        lista.append(numero)
#        if numero > mayor:
#            mayor = numero
#        
#        posicion = lista.index(mayor)   
#
#        n -= 1
#
#    cartel = f"en la lista de numeros {lista} el mayor numero fue {mayor} y esta en la posicion {posicion}"
#
#    return cartel
#
#    
#
#print(cant_numeros(100))


"""
## Ejercicio 047

### Escribir un programa que permita validar la nota de un examen. Se espera que la nota que el usuario ingrese sea un número comprendido entre 0 y 10.  
### La misma debe ser ingresada tantas veces como sea necesario hasta que quede comprendida dentro del rango indicado.


"""

#def main():
#
#    valido = False
#
#    while not valido:
#        nota = int(input("Ingrese una nota: "))
#
#        if nota >= 0 and nota <= 10:
#            valido = True
#            print("Su nota es valida")
#
#        else:
#            print("Su nota no es valida")
# 
#
#main()


""""
## Ejercicio 048

### Escribir un programa que permita realizar varias operaciones matemáticas ingresando un caracter por cada una la operación a realizar (‘+’, ‘-’, ‘*’, ‘/’, ‘F’) y 
# dos números enteros en el caso que no haya elegido ‘F’. La computadora debe mostrar el resultado para la operación ingresada. Considerar que no se puede dividir por cero. 
# Cuando la operación ingresada sea ‘F’ nos indicará que no se desean calcular más operaciones.


"""


#def main():
#
#    validador = False
#    
#    while not validador:
#        
#        a = int(input("Ingrese su numero para la operacion: "))
#        b = int(input("Ingrese su numero para la operacion: "))
#        operacion = input("Ingrese una operacion= (+) (-) (*) (/) y para salir F: ")
#        
#
#        if operacion == 'F' or operacion == "f":
#            print("Usted esta saliendo del programa")
#            validador = False
#
#        if operacion == '+':
#            print(a + b)
#        elif operacion == '-':
#            print(a - b)
#        elif operacion == '/' and b != 0:
#            print(a / b)
#        elif operacion == '*':
#            print(a * b)
#        else:
#            print("Operador incorrecto, por favor cargue nuevamente")
#            
#            
#            
#        
#        
#main()


""""
## Ejercicio 049

### Escribir un programa que permita validar una opción ingresada. Se le preguntará al usuario si desea continuar con alguna operación de la forma "¿Deseás continuar? [S/N]". 
# Se espera que el usuario ingrese una 'S' o una 'N' (incluir las minúsculas). 
# La opción debe ser ingresada tanto como sea necesario hasta que quede comprendida dentro de las posibilidades esperadas.



"""


#ok = False
#
#while not ok:
#
#    operadores = ["+","-","*","/"]
#    OK = False
#
#    
#
#    while not ok:
#        operacion = input("Ingrese una operacion deseada= + ,- , * , /: ")
#        a = int(input("Ingrese un numero: "))
#        b = int(input("Ingrese un numero: "))
#
#        if operacion == "+":
#            resultado = a + b
#            print(resultado)
#            continuar = input("Desea continuar? S/N: ")
#            if continuar == "S" or continuar == "s":
#                ok = False
#            if continuar == "N" or continuar == "n":
#                print("Usted esta saliendo del programa")
#                ok = True
#        elif operacion == "-":
#            resultado = a - b
#            print(resultado)
#            continuar = input("Desea continuar? S/N: ")
#            if continuar == "S" or continuar == "s":
#                ok = False
#            if continuar == "N" or continuar == "n":
#                print("Usted esta saliendo del programa")
#                ok = True
#        elif operacion == "*":
#            resultado = a * b
#            print(resultado)
#            continuar = input("Desea continuar? S/N: ")
#            if continuar == "S" or continuar == "s":
#                ok = False
#            if continuar == "N" or continuar == "n":
#                print("Usted esta saliendo del programa")
#                ok = True
#        elif operacion == "/" and b != 0:
#            resultado = a / b
#            print(round(resultado,2))
#            continuar = input("Desea continuar? S/N: ")
#            if continuar == "S" or continuar == "s":
#                ok = False
#            if continuar == "N" or continuar == "n":
#                print("Usted esta saliendo del programa")
#                ok = True
#        elif operacion == "/" and b == 0:
#            print("No se puede dividir por 0")
#            ok = False
#        else:
#            print("Ingrese un operador correcto por favor (La concha puta de tu hermana)")
#            ok = False
            
        

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
#    valido = True
#
#    while valido:
#        nota = int(input("Ingrese su nota: "))
#
#        if nota == 1 or nota == 3:
#            print("Nota invalida, proba de nuevo mi rey")
#        elif nota == 0:
#            print("Usted estuv0 ausente")
#            valido = False
#        elif nota == 2 or nota >= 4 or nota <= 10:
#            print(f"Usted se ha sacado un {nota}")
#            valido = False
#
#
#main()


""""

## Ejercicio 051

### Escribir un programa que permita al usuario ingresar números hasta que se introduzca un 0.
### La computadora debe mostrar el número máximo y el número mínimo.


"""


#import random
#
#
#def main():
#
#    mayor = -float("inf")
#    menor = float("inf")
#
#    n = 1
#
#    while n != 0:
#        n = random.randint(0,1000)
#
#        if n > mayor and n != 1000:
#            mayor = n
#        if n < menor and n != 0:
#            menor = n
#
#        print(n)
#
#    print(f"El mayor numero fue {mayor} y el minimo fue {menor}")
#
#main()


""""

## Ejercicio 052

### Escribir un programa que permita un programa que permita ingresar la estatura (en metros con decimales) de cada jugador de un equipo de baloncesto. 
# La carga finalizará al ingresar cero. Calcular y mostrar la estatura promedio del equipo.

"""

#import random
#
#
#contador = 0
#estatura = 1.0
#suma = 0
#max_permitido = 1000
#
#while estatura != 0 and contador < max_permitido:
#    estatura = random.uniform(0,3.0)
#    print(round(estatura,2))
#    suma += estatura
#    contador += 1
#
#
#    promedio = round(suma/contador,2)
#
#print(f"Hubo {contador} jugadores y su promedio fue {promedio} y la sumatoria fue {suma}")


""""
## Ejercicio 053

### Escribir un programa que permita ingresar nombre y edad de un grupo de personas (para cada una, nombre y edad).
#  La carga termina cuando en el nombre de la persona se ingresa un asterisco ('*'). Mostrar al final cómo se llama la persona más joven.


"""


#def main():
#    diccionario = {}
#    valido = True
#    n = 1
#    menor = float("inf")
#    name = ""
#
#    while valido:
#        nombre = input("Ingrese su nombre: ")
#        edad = int(input("Ingrese su edad: "))
#
#        if "*" not in nombre:
#            agregar = {"Nombre" + str(n): {nombre}, "Edad" + str(n): {edad}}
#            diccionario.update(agregar)
#            n += 1
#            if edad < menor:
#                menor = edad
#                name = nombre
#        else:
#            valido = False
#
#    print(f"La persona mas joven se llama {name} y tiene {menor} años de edad")
#    print(diccionario)
#main()


""""

## Ejercicio 054

### Escribir un programa que permita controlar con validación el ingreso a un sitio web. Teniendo dos constantes con un nombre de usuario ("admin") y una contraseña ("123456"), 
# el programa debe permitir al usuario ingresar sus credenciales. Si las mismas son erróneas, se volverán a pedir hasta un máximo de 3 intentos. 
# Finalmente, la computadora debe mostrar alguno de los siguientes mensajes según sea el caso: "Acceso concedido" o "Se ha bloqueado la cuenta"

"""
#ADMIN = "admin"
#CONTRASEÑA = "123456"
#max_intentos = 3
#intentos = 0
#acceso = False
#
#while not acceso and intentos <= max_intentos:
#    usuario = input("Ingrese el usuario: ")
#    clave = input("Ingrese su clave: ")
#
#    if intentos == max_intentos:
#        print("Se ha bloqueado la cuenta")
#        acceso = False
#
#    if usuario == ADMIN and clave == CONTRASEÑA:
#        print("Acceso concedido")
#        acceso = False
#
#    else:
#        intentos += 1
#        print("Por favor ingrese de nuevo")
        

""""
## Ejercicio 056

### Escribir un programa que permita Leer números que representan edades de un grupo de personas, finalizando la lectura cuando se ingrese el número 999. 
# Imprimir cuántos son menores de 18 años, cuántos tienen 18 años o más y el promedio de edad de ambos grupos. Descartar valores que no representan una edad válida. 
# (Se considera válido una edad entre 0 y 100)


"""

#import random
#
#
#def main():
#    mayores_18 = []
#    menores_18 = []
#    contador = 0
#    ok = True
#
#    while ok:
#        edad = int(input("Ingrese su edad: "))
#
#        if edad >= 18 and edad <= 100:
#            mayores_18.append(edad)
#        elif edad < 18 and edad > 0:
#            menores_18.append(edad)
#            
#        if edad < 0 or edad > 100:
#            print("Edad invalida, por favor cargue nuevamente")
#
#        if edad == 999:
#            ok = False
#
#        contador +=1
#
#        
#        promedio = (sum(mayores_18) + sum(menores_18)) / contador
#
#    print(f"La cantidad de personas mayores a 18 fueron {len(mayores_18)}, menores de 18 {len(menores_18)} y el promedio de edad fue {round(promedio,2)} ")
#
#main()



""""
## Ejercicio 057

### Escribir un programa que permita ingresar los números de legajo de los alumnos de un curso y su nota de examen final. El fin de la carga se determina ingresando un -1 en el legajo.
### Informar para cada alumno si aprobó o no el examen considerando que se aprueba con nota mayor o igual a 4. Se debe validar que la nota ingresada sea entre 1 y 10. 
# Terminada la carga de datos, informar:
- Cantidad de alumnos que aprobaron (nota >= 4).
- Cantidad de alumnos que desaprobaron el examen (nota < 4).
- Porcentaje de alumnos que están aplazados (nota == 1).


"""



#aprobados = []
#desaprobados = []
#aplazos = []
#legajos = {}
#ok = True
#n = 1
#contador = 0
#
#
#
#while ok:
#
#
#    legajo = int(input("Ingrese su legajo: "))
#    nota = int(input("Ingrese su nota: "))
#
#    if nota > 0 and nota <= 10:
#        agregar = {"Legajo" + " " + str(n): {legajo}, "Nota" + " " + str(n): {nota}}
#        legajos.update(agregar)
#        
#    if nota >= 4 and nota <= 10:
#        aprobados.append(nota)
#
#    if nota < 4 and nota > 1:
#        desaprobados.append(nota)
#
#    if nota == 1:
#        aplazos.append(nota)
#
#    if nota < 0 or nota > 10:
#        print("Ingrese una nota valida")
#
#    if legajo == -1:
#        ok = False
#        
#    n += 1
#    contador +=1
#
#
#print(legajos)
#print(f"la cantidad de alumnos que hicieron el examen fueron {contador} de los cuales los aprobaros fueron: {len(aprobados)}, los desaprobados fueron {len(desaprobados)} y la cantidad de aplazos fue {len(aplazos)}")


""""
## Ejercicio 061

### Escribir un programa que permita ingresar un número entero positivo y mostrar su factorial. 
# El factorial de un número es el producto de todos los números enteros desde 1 hasta el número ingresado. Por ejemplo, el factorial de 5 es 1 * 2 * 3 * 4 * 5 = 120.


"""

#def factorial (n):
#    resultado = 1
#    for i in range(1,n+1):
#        resultado *= i
#
#    return resultado
#
#
#print(factorial(15))
        

""""
## Ejercicio 058

### Una empresa aplica el siguiente procedimiento en la comercialización de sus productos:
- ### Aplica el precio base a la primera docena de unidades.  
- ### Aplica un 10% de descuento a todas las unidades entre 13 y 100.  
- ### Aplica un 25% de descuento a todas las unidades por encima de las 100.
### Por ejemplo, supongamos que vende 230 unidades de un producto cuyo precio base es 100. El cálculo resultante sería:  
100 * 12 + 90 * 88 + 75 * 130 = 18870, y el precio promedio será 18870 / 230 = 82,04  
### Escribir un programa que lea la cantidad solicitada de un producto y su precio base, y muestre el valor total de la venta y el precio promedio por unidad. 
# El fin de carga se determina ingresando -1 como cantidad solicitada.
### Al finalizar informar:  
- a) Cantidad de ventas realizadas total.
- b) Cantidad de ventas que se aplicaron un 10% de descuento.
- c) Cantidad de ventas que SOLO se aplicó el precio base, no se le realizaron descuentos


"""

#import random
#
#
#def solicitar_compra():
#    
#    compra = random.randint(1,200)
#    
#    return compra
#
#
#def precio_base(unidades:int) -> int:
#
#    resultado = (unidades*100) 
#
#    return resultado
#
#
#
#def descuento_10(unidades:int)-> float:
#        
#    resultado = (((unidades - 12)*100) * 0.90) + (12*100) 
#
#    return resultado
#
#
#def descuento_25(unidades:int) -> float:
#
#    resultado = (((unidades - 100) *100) * 0.75) + (100*100)
#
#    return resultado
#
#
#def main():
#
#    contador = 0
#    descuenta10 = []
#    descuento25 = []
#    normal = []
#    suma = 0
#
#
#    while contador < 20:
#
#        unidades = solicitar_compra()
#
#        if unidades >= 13 and unidades < 100:
#            pagar = descuento_10(unidades)
#            descuenta10.append(unidades)
#            suma += unidades
#
#        elif unidades >= 100:
#            pagar = descuento_25(unidades)
#            descuento25.append(unidades)
#            suma += unidades
#
#        else:
#            pagar = precio_base(unidades)
#            normal.append(unidades)
#            suma += unidades
#
#        contador += 1
#
#        print(unidades)
#
#    print(f"el dia de hoy se hicieron {contador} ventas, de las cuales se vendieron {suma} de unidades. Se le aplico el 10% a {len(descuenta10)} unidades , el 25% a {len(descuento25)} y se vendieron {len(normal)} sin descuento")

#main()

    
""""
## Ejercicio 059

### Escribir un programa para un negocio de venta de granos que desea controlar las ventas realizadas. De cada venta ingresa el importe total y un código que indica la forma de pago. Los códigos puede ser:
- C: cheque, 20% de recargo.  
- E: efectivo, 10% de descuento.  
- T: con tarjeta, 12% de recargo.  
### Se debe ingresar una F para finalizar el día de venta y arrojar los siguientes totales.
| Forma de Pago    | Total     |  
| ---------------- | --------- |
| Efectivo en Caja | $ xxxx.xx |  
| Tarjeta/Crédito  | $ xxxx.xx |  
| Cheques          | $ xxxx.xx |  
| Total de Venta   | $ xxxx.xx |  
| Importe del IVA  | $ xxxx.xx |  


"""

#def venta():
#    cantidad = int(input("Cuantos productos vendiste?: "))
#    precio = float(input("A que precio los vendiste?: "))
#    importe_total = cantidad * precio
#
#    
#
#    return importe_total
#
#
#def cheque(importe:float):
#    recargo = importe * 1.20
#
#    return recargo
#
#
#def efectivo (importe:float):
#    recargo = importe * 0.9
#
#    return recargo
#
#def tarjeta(importe:float):
#    recargo = importe * 1.12
#
#    return recargo
#
#
#
#
#def main():
#
#    metodos_permitidos = ["C", "E", "T"]
#
#    efvo = []
#    tarj = []
#    cheq = []
#
#    suma = 0
#
#
#
#
#    ok = True
#
#    while ok:
#
#        metodo_de_pago = input("Elija un metodo de pago (C / E / T): ").upper()
#
#        if metodo_de_pago == "F":
#            print("Cerrando el dia de ventas")
#            ok = False
#
#        if metodo_de_pago not in metodos_permitidos:
#            print("Metodo de pago incorrecto, por favor intente nuevamente")
#            continue # Volver a pedir un método de pago válido
#        #Se usa continue si el método de pago es inválido para evitar procesamientos innecesarios.
#
#    
#        importe = venta()
#
#        
#
#        if metodo_de_pago == "C":
#                ventas = cheque(importe)
#                cheq.append(ventas)
#                
#        elif metodo_de_pago == "E":
#                ventas = efectivo(importe)
#                efvo.append(ventas)
#                
#        elif metodo_de_pago == "T":
#                ventas = tarjeta(importe)
#                tarj.append(ventas)
#
#               
#        suma += ventas
#
#            
#
#    print(f""""
#| Forma de Pago    | Total        
#| ---------------- | ---------  
#| Efectivo en Caja |${round(sum(efvo),2)}  
#| Tarjeta/Crédito  |${round(sum(tarj),2)}  
#| Cheques          |${round(sum(cheq),2)}  
#| Total de Venta   |${round(suma)}              
#| Importe del IVA  |${round((suma*0.21),2)}    
#          """)
#            
#
#main()




""""

## Ejercicio 060

### Escribir un programa para calcular el sueldo final a pagar a cada empleado de una empresa. 
# De cada uno se tiene, sueldo básico, antigüedad, cantidad de hijos y estudios superiores (‘S’ o ‘N’). Además, se conocen los porcentajes de aumento del sueldo que dependen de los siguientes factores:

- Si el empleado tiene más de 10 años de antigüedad: aumento del 10%  
- Si el empleado tiene más de 2 hijos: aumento del 10%, si solo tiene uno 5%  
- Si el empleado posee estudios superiores: aumento del 5%  

### Luego de ingresar los datos de un empleado se debe preguntar si se desea ingresar otro empleado o no. Se termina la carga cuando no se deseen ingresar más empleados.
- Determinar:  
    - a. Por cada empleado: número de empleado, el sueldo básico y el nuevo sueldo.  
    - b. Sueldo nuevo promedio de la empresa.  


"""


#import random
#
#
#class Empleado ():
#    def __init__(self, nombre:str, salario:int, antiguedad:int, hijos:int, estudios:str):
#        self.nombre = nombre
#        self.salario = salario
#        self.antiguedad = antiguedad
#        self.hijos = hijos
#        self.estudios = estudios
#
#    def mostrar_informacion(self):
#        print(f"Nombre: {self.nombre}, Salario: {self.salario}, Antiguedad: {self.antiguedad}, Cantidad de hijos {self.hijos}, Nivel de estudios: {self.estudios}")
#
#
#def aumento_por_antiguedad(salario:int,antiguedad:int)->int:
#    if antiguedad > 10:
#        aumento = salario * 0.10
#    else: 
#        aumento = 0
#
#    return aumento
#
#def aumento_por_hijo(salario:int,cantidad_de_hijos:int)->int:
#    if cantidad_de_hijos == 1:
#        aumento = salario * 0.05
#    elif cantidad_de_hijos == 2:
#        aumento = salario * 0.10
#    else:
#        aumento = salario * 0.15
#
#    return aumento
#
#def aumento_por_estudios(salario:int, estudios:str)->int:
#    if estudios == "Superiores":
#        aumento = salario * 0.05
#    else:
#        aumento = 0
#
#    return aumento
#
#    
#
#def main():
#
#    diccionario = {}
#    diccionario_actualizado = {}
#
#    nombres_posibles = [
#    "Ana", "Beatriz", "Carla", "Diana", "Elena", "Flor", "Gabriela", "Hilda", 
#    "Isabel", "Julia", "Karina", "Luz", "Mónica", "Natalia", "Olga", "Paula", 
#    "Quiela", "Rosa", "Silvia", "Tania", "Úrsula", "Valeria", "Wanda", "Ximena", 
#    "Yolanda", "Zoe", "Alan", "Bruno", "Carlos", "Diego", "Esteban", "Fernando", 
#    "Gabriel", "Hugo", "Iván", "Javier", "Kevin", "Luis", "Marcos", "Nicolás", 
#    "Oscar", "Pablo", "Quintín", "Raúl", "Sergio", "Tomás", "Ulises", "Víctor", 
#    "Walter", "Xavier", "Yago", "Zacarías"]
#
#    nivel_de_estudios = ["Superiores", "Nulos"]
#
#    
#
#    ok = True       
#
#    total_salarios = 0
#    total_nuevo_salarios = 0
#
#    CONTADOR = 0
#
#    
#
#    n = 1
#
#    while ok:
#         
#         nuevo_empleado = input("Desea agregar un nuevo empleado? (S/N): ").strip().lower()
#
#         if nuevo_empleado == "s":
#             
#        
#            nombre = random.choice(nombres_posibles)
#
#            salario = random.randint(1000,10000)
#
#            antiguedad = random.randint(1,20)
#
#            cantidad_de_hijos = random.randint(1,5)
#
#            estudios = random.choice(nivel_de_estudios)
#
#
#            empleado = Empleado(nombre,salario,antiguedad,cantidad_de_hijos,estudios)
#
#            agregar = {
#            f"Empleado {n}": {
#                "Nombre": nombre,
#                 "Salario": salario,
#                    "Antiguedad": antiguedad,
#                    "Cantidad de hijos": cantidad_de_hijos,
#                    "Nivel de estudios": estudios
#                                                }
#                                                    }
#
#            diccionario.update(agregar)
#
#            print(diccionario)
#
#            total_salarios += salario
#            
#
#            nuevo_salario_antiguedad= aumento_por_antiguedad(salario, antiguedad)
#            nuevo_salario_estudios= aumento_por_estudios(salario,estudios)
#            nuevo_salario_hijos= aumento_por_hijo(salario,cantidad_de_hijos)
#
#            nuevo_sueldo = salario + nuevo_salario_antiguedad + nuevo_salario_estudios + nuevo_salario_hijos
#
#            agregar1 = {
#            f"Empleado {n}": {
#                "Nombre": nombre,
#                 "Salario": round(nuevo_sueldo,2),
#                    "Antiguedad": antiguedad,
#                    "Cantidad de hijos": cantidad_de_hijos,
#                    "Nivel de estudios": estudios
#                                                }
#                                                    }
#
#            diccionario_actualizado.update(agregar1)
#
#            print(diccionario_actualizado)
#
#            total_nuevo_salarios += nuevo_sueldo
#            
#            n += 1
#
#            CONTADOR += 1
#
#            salario_promedio = (total_salarios/CONTADOR)
#            salario_promedio_nuevos = (total_nuevo_salarios/CONTADOR)
#
#         elif nuevo_empleado == "n":
#             print("Cerrando app")
#             ok = False
#             
#         else:
#             print("Opcion invalida, por favor intenta nuevamente probando S o N")
#    print(f"El salario promedio antes era de {salario_promedio}. Con los nuevos salarios, el promedio de la empresa es {salario_promedio_nuevos}")
#    
#



#main()



""""
## Ejercicio 062

### Un entrenador le ha propuesto a un atleta recorrer una ruta de cinco kilómetros durante 10 días para determinar si es apto para la prueba de 5 kilómetros que se desarrollará en el Parque. 
# No se sabe si está apto y para eso nos piden que hagamos el siguiente programa.
### Nos ingresan por cada día de entrenamiento tiempo de la prueba en minutos (entero mayor que 0 y menor a 100)
### Para considerarlo apto debe cumplir las siguientes condiciones:
- Que en ninguna de las pruebas haga un tiempo mayor a 20 minutos.
- Que al menos en una de las pruebas realice un tiempo menor de 15 minutos.
- Que su promedio sea menor o igual a 18 minutos.
### Se pide:
- Diseñar un algoritmo para registrar los datos y decidir si es apto para la competencia.
- Sólo en caso de estar apto, informar el promedio y el número de día en el que realizó el
menor tiempo

"""


#import random
#
#
#def main():
#
#    dias_max = 10
#    contador = 0
#    lista = []
#    
#
#    while contador <= dias_max:
#        contador += 1
#        prueba = random.randint(1,25)
#        lista.append(prueba)
#
#    print(lista)
#
#    promedio = round((sum(lista) / contador),2)
#
#    for x in lista:
#        if x > 20:
#            print("No tiene condiciones para seguir")
#            break
#        if x < 15 and promedio < 18:
#            print("Tiene condiciones para seguir")
#            print(f"El promedio de tiempo fue {promedio} y realizo el menor tiempo en el dia {lista.index(min(lista))+1}")  #Le agregue el uno porque el metodo index me inicio la cuenta desde 0 y yo estoy teniendo en consideracion dias
#            break
#
#    
#
#
#main()    

""""
## Ejercicio 063

### Escribir un programa para registrar y obtener información sobre los viajes diarios de un conductor de Uber.
### Cada vez que comienza un viaje se debe ingresar la distancia recorrida, indicando si el viaje fue corto (‘C’), mediano (‘M’), largo (‘L’) o si es el fin de los datos (‘Z’).  
### El día finaliza cuando se llega a los 30 viajes o cuando se ingresa distancia ‘Z’ (fin de los datos).

### Por cada viaje se debe ingresar la siguiente información:

- ### Cantidad de pasajeros (mayor a 0 y menor a 4).
- ### Importe a cobrar, incluyendo la el costo básico ($180).  
- ### Por cada pasajero de ese viaje se debe ingresar:  
    - ### Nombre.
    - ### Edad (mayor a 18 y menor a 120 años).  

### Se desea saber, para cada viaje, cuál es la persona más grande y su nombre.

### Al finalizar el día de trabajo, el programa debe informar:

- ### Cantidad de viajes por cada categoría (‘C’, ‘M’, ‘L’).
- ### Recaudación total.
- ### Valor promedio del viaje.
- ### Porcentaje de viajes cortos.

### Todos los datos ingresados deben ser validados.


"""


#import random
#
#def main():
#
#  mayor = -float("inf")  
#  name = ""
#
#
#    C = []
#    M = []
#    L = []
#    
#    diccionario = {}
#
#    nombres_posibles = [
#    "Ana", "Beatriz", "Carla", "Diana", "Elena", "Flor", "Gabriela", "Hilda", 
#    "Isabel", "Julia", "Karina", "Luz", "Mónica", "Natalia", "Olga", "Paula", 
#    "Quiela", "Rosa", "Silvia", "Tania", "Úrsula", "Valeria", "Wanda", "Ximena", 
#    "Yolanda", "Zoe", "Alan", "Bruno", "Carlos", "Diego", "Esteban", "Fernando", 
#    "Gabriel", "Hugo", "Iván", "Javier", "Kevin", "Luis", "Marcos", "Nicolás", 
#    "Oscar", "Pablo", "Quintín", "Raúl", "Sergio", "Tomás", "Ulises", "Víctor", 
#    "Walter", "Xavier", "Yago", "Zacarías"]
#    
#
#    viajes_posibles = ["C","M","L","Z"]
#
#    viajes = random.choice(viajes_posibles).strip().lower()
#
#    viajes_max = 30
#    viaje = 1
#
#    diccionario.clear()
#
#    
#    while viaje <= viajes_max and viajes != "z":
#        viajes = random.choice(viajes_posibles).strip().lower() #Tengo que agregar esto para que se actualice la funcion
#        pasajeros = random.randint(1,4)
#
#       
#
#        pasajeros_viaje = {}
#        #Se inicializa un diccionario vacío para almacenar los pasajeros del viaje actual.
#        
#        
#        for i in range(1, pasajeros + 1):
#            nombre = random.choice(nombres_posibles)
#            edad = random.randint(18, 120)
#
#            pasajeros_viaje[f"Pasajero {i}"] = {"Nombre": nombre, "Edad": edad}
#
#            # ✅ Comparar la edad de inmediato para evitar recorrer de nuevo
#            if edad > mayor:
#                mayor = edad
#                name = nombre
#
#            """"
#            Se genera un nombre y una edad aleatoria.
#            Se asigna al diccionario pasajeros_viaje con una clave "Pasajero X" y un diccionario anidado con la información de ese pasajero.
#
#            {
#            "Pasajero 1": {"Nombre": "Carlos", "Edad": 78},
#            "Pasajero 2": {"Nombre": "Ana", "Edad": 65}
#            }
#            """
#
#        #Agregar solo este viaje al diccionario principal
#        #Concepto de diccionarios anidados, pasajeros_viaje solo fue un diccionario que utilizamos para que itere, luego se convierte en valores dentro de las claves "viaje" en el diccionario final
#        diccionario[f"Viaje {viaje}"] = pasajeros_viaje
#        # diccionario["Altura"] = 1.85  #Tambien puedo agregar claves valor desde afuera del diccionario
#        #Esto lo aprendi en el curso de Digital House de agregarles claves - valores a los diccionarios
#
#        """"
#        Se agrega pasajeros_viaje como el valor dentro del diccionario principal, usando "Viaje X" como clave.
#    
#        """
#         #EJEMPLO 
#        """"
#        {
#    "Viaje 1": {
#        "Pasajero 1": {"Nombre": "Carlos", "Edad": 78},
#        "Pasajero 2": {"Nombre": "Ana", "Edad": 65}
#    },
#    "Viaje 2": {
#        "Pasajero 1": {"Nombre": "Diego", "Edad": 120},
#        "Pasajero 2": {"Nombre": "Mónica", "Edad": 45},
#        "Pasajero 3": {"Nombre": "Julia", "Edad": 98}
#    }
#}
#        """
#            #NO LO NECESITO PERO ME SIRVE PARA APRENDER LO DE MODIFICAR LA VARIABLE DATOS Y NO LAS VARIABLES POR SEPARADO
#        #for datos in diccionario.values():
#        #    if datos["Edad"] > mayor:
#        #        mayor = datos["Edad"]  #Aca tengo que cambiar LOS VALORES de edad y expresandolo asi, si pongo edad solo no se em actualiza los valores del diccionario
#        #        name = datos["Nombre"] #Aca tengo que cambiar LOS VALORES de nombre y expresandolo asi, si pongo nombre solo no se em actualiza los valores del diccionario
#
#        print(f" en el viaje {viaje} el pasajero de mayor edad tenia {mayor} años y se llamaba {name}")
#
#        if viajes == "c":
#            C.append(viaje)
#        elif viajes == "m":
#            M.append(viaje)
#        elif viajes == "l":
#            L.append(viaje)
#
#        
#        viaje += 1
#
#
#    print(diccionario)
#    print(len(C), len(M), len(L))
#    
#
#
#
#main()

""""
## Ejercicio 064

### Un animal en rehabilitación después de una cirugía requiere ser alimentado y monitoreado en un zoológico. Se alimenta al animal 3 veces al día y se le da de comer hasta que ya no tenga ganas de comer.
### Por cada tanda de comida, se debe ingresar la cantidad de alimento en kg (número entero) que se le dio y se le debe preguntar al animal si quiere seguir comiendo ('S', 'N').
### Se desea conocer:
- ### Cuál de las 3 comidas fue la que el animal comió más cantidad de alimento y cuánto fue esa cantidad.
- ### El total en kg de alimento recibido.
- ### Promedio de alimento por tanda.

"""
#def main():
#    max_comidas = 3
#    ok = True
#    contador = 0
#    kg_lista = []
#
#    while contador < max_comidas and ok:
#        kg = int(input("Ingrese la cantidad de kg que se le dio para comer: "))
#        kg_lista.append(kg)
#
#        while ok:
#            pregunta = input("El animal quiere seguir comiendo? (S/N): ").strip().lower()
#            if pregunta == "s":
#                ok = True
#                break #Tengo que poner el break aca para cortar este bucle, el bucle intermedio
#            elif pregunta == "n":
#                ok = False # Con esta condicion rompo el bucle principal y el bucle intermedio al mismo tiempo (comparten la misma condicion)
#                 
#            else:
#                print("Carga inválida, por favor intente nuevamente!")
#                continue  #Esto es para que vuelva a preguntar
#
#        contador += 1
#
#    if kg_lista:  # Verifica que la lista no esté vacía
#        max_kg = max(kg_lista)
#        indice_max = kg_lista.index(max_kg) + 1  # +1 para que sea más legible (empezando desde 1)
#        print(f"El animal comió un total de {sum(kg_lista)}kg. De los cuales, cuando más comió fue en la comida {indice_max}, equivalente a {max_kg}kg.")
#
#main()


""""

## Ejercicio 065

### Una cadena de comida rápida solicita el desarrollo de una aplicación para sus terminales de autoservicio que permita a los clientes armar su propio menú. Los clientes pueden elegir entre diferentes opciones de combos o pedir por separado la comida, bebida y postre.

### Al iniciar la aplicación, se debe mostrar el siguiente menú de opciones:

- #### 1) Combo 1: Hamburguesa, papas fritas y gaseosa - 1550
- #### 2) Combo 2: Hamburguesa con queso, papas fritas y gaseosa - 1650
- #### 3) Hamburguesa sola - 1300
- #### 4) Hamburguesa con queso - 1400
- #### 5) Gaseosa - 700
- #### 6) Postre - 600
- #### 7) Agregar aderezo - 100
- #### 8) Terminar

### Luego de seleccionar cada ítem, se debe mostrar el subtotal para que el cliente pueda decidir si desea agregar más productos a su pedido antes de terminar.  
### El valor mínimo del pedido debe ser de $1550. Si el cliente elige un combo, se debe sumar el importe total al subtotal. Si el cliente selecciona opciones 3 a 7, se le debe preguntar la cantidad deseada y calcular el valor total antes de sumarlo al subtotal.
### Al finalizar el pedido, se debe mostrar el monto total a pagar, el ítem más caro y, si no se han seleccionado productos, mostrar un mensaje que diga "Pedido cancelado".


"""

productos = {"combo 1": 1500, "combo 2" : 1650, "hamburguesa sola": 1300, "hamburguesa con queso" : 1400, "gaseosa" : 700, "postre": 600, "aderezo" : 100}
lista_pedido = []
lista_productos = []
productos_vendidos = []

ok = True




while ok:
   

    pedido = int(input("""Eliga una de las siguientes opciones!:
1) Combo 1: Hamburguesa, papas fritas y gaseosa - 1550
2) Combo 2: Hamburguesa con queso, papas fritas y gaseosa - 1650
9) Terminar
3) Armar su propio combo: """))
    
    if pedido not in [1,2,3,4,5,6,7,8,9]:
        print("Numero de pedido invalido, por favor intente nuevamente")
        continue
    

    if pedido == 1:
        lista_pedido.append(productos["combo 1"])
        print(f"El subtotal hasta ahora es ${sum(lista_pedido)}")
        
    elif pedido == 2:
        lista_pedido.append(productos["combo 2"])
        print(f"El subtotal hasta ahora es ${sum(lista_pedido)}")


    elif pedido == 9:
        ok = False

    else:
        print("Usted ha decididor armar su propio combo")
        propio_combo = int(input("""
4) Hamburguesa sola - 1300
5) Hamburguesa con queso - 1400
6) Gaseosa - 700
7) Postre - 600
8) Agregar aderezo - 100
9) Terminar: """))
        cantidad = int(input("Ingrese la cantidad que desee: "))

        if propio_combo == 4:
            resultado = productos["hamburguesa sola"] * cantidad
            lista_pedido.append(resultado)
            print(f"El subtotal hasta ahora es ${sum(lista_pedido)}")
        elif propio_combo == 5:
            resultado = productos["hamburguesa con queso"] * cantidad
            lista_pedido.append(resultado)
            print(f"El subtotal hasta ahora es ${sum(lista_pedido)}")
        elif propio_combo == 6:
            resultado = productos["gaseosa"] * cantidad
            print(f"El subtotal hasta ahora es ${sum(lista_pedido)}")
        elif propio_combo == 7:
            resultado = productos["postre"] * cantidad 
            productos_vendidos.append(lista_productos[5])
            print(f"El subtotal hasta ahora es ${sum(lista_pedido)}")
        elif propio_combo == 8:
            resultado = productos["aderezo"] * cantidad
            productos_vendidos.append(lista_productos[6])
            print(f"El subtotal hasta ahora es ${sum(lista_pedido)}")


prod = int(max(lista_pedido))

for clave, valor in productos.items(): #ITERO EN TODOS LOS ITEMAS DEL DICCIONARIO PARA ENCONTRAR EL VALOR MAXIMO
    if valor == prod:
        lista_productos.append(clave)

print(f"El total a pagar es de ${sum(lista_pedido)}. El producto mas caro salio ${max(lista_pedido)} que corresponde a {set(lista_productos)}") #LO TRANSFORME EN SET ASI NO ME GUARDA VALORES REPETIDOS
                  



        




        

        






    












        



