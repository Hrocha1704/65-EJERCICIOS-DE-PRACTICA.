"""
Ejercicio 066c

La biblioteca de la ciudad necesita organizar y hacer un recuento 
de los libros que tiene en sus estantes. 

Para cada uno de los estantes (usando 'F' para indicar el fin del estante), 
se deben ingresar los libros, y para cada libro, se debe ingresar:
nombre (usando 'FIN' si no hay más libros para ese estante), 
género (usando 'I' para Infantil, 'N' para Novela, o 'H' para Historia), y 
cantidad de páginas (mayor a 0). 


Una vez que se han ingresado los datos de 1 estante, se debe mostrar por 
pantalla el nombre del libro con la mayor cantidad de páginas y su 
cantidad correspondiente. 

Al finalizar el ingreso de datos de todos los estantes, se deben mostrar 
la cantidad de libros por género y el promedio de libros por estante.
"""

def main():
    cantidad_estantes = 0
    cantidad_historia = 0
    cantidad_infantil = 0
    cantidad_novela = 0
    cantidad_libros = 0
    numero_estante = input("Numero de estante [F para terminar]: ").upper()
    while numero_estante != 'F':
        # PARA CADA ESTANTE
        mayor = -float('inf')
        libro_mayor = ""
        nombre_libro = input("Nombre del libro: ").title()
        while nombre_libro != "Fin":
            # PARA CADA LIBRO DE CADA ESTANTE
            genero = input("Genero ['I'/Infantil 'N'/Novela 'H'/Historia]:  ").upper()
            cantidad_paginas = int(input("Cantidad de paginas: "))

            if genero == 'I':
                cantidad_infantil += 1
            elif genero == 'H':
                cantidad_historia += 1
            elif genero == 'N':
                cantidad_novela += 1                

            cantidad_libros += 1

            if cantidad_paginas > mayor:
                mayor = cantidad_paginas
                libro_mayor = nombre_libro


            # LEO EL NOMBRE DEL SIG. LIBRO ==> PUEDE HACER TERMINAR EL ESTANTE
            nombre_libro = input("Nombre del libro: ").title()
        # fin while ==> se terminaron los libros de un estante
        cantidad_estantes += 1
        
        if mayor == -float('inf'):
            cadena = f"Estante: {numero_estante} No tiene libros"
        else:            
            cadena = f"Estante: {numero_estante} Libro con mas paginas: {libro_mayor} con {mayor} cantidad de paginas."
        print(cadena)
        numero_estante = input("Numero de estante [F para terminar]: ").upper()
    # fin del for ==> fin de datos
    print(f"""
            Historia: {cantidad_historia}
            Novela:   {cantidad_novela}
            Infantil: {cantidad_infantil}
          """)
    promedio = cantidad_libros / cantidad_estantes
    print(f"Promedio: {promedio:.2f}")
main()
