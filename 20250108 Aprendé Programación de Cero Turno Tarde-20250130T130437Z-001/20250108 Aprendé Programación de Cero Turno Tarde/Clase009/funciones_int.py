"""
Módulo para manejar fechas y realizar operaciones como obtener componentes de la fecha,
verificar si un año es bisiesto, generar fechas aleatorias, y convertirlas a formato de texto.
Este módulo utiliza el formato numérico AAAAMMDD para representar las fechas.

Incluye funciones para:
- Extraer el día, mes y año de una fecha numérica.
- Generar una cadena de texto de la fecha en formato DD/MM/AAAA.
- Verificar si un año es bisiesto.
- Obtener la cantidad de días en un mes específico.
- Crear fechas aleatorias basadas en un año.

Requiere:
- La biblioteca `random` para la generación de números aleatorios.
"""

import random as rd

def obtener_dia(aaaammdd: int) -> int:
    """
    Extrae el día de una fecha en formato numérico AAAAMMDD.
    
    Parámetros:
        aaaammdd (int): Fecha en formato AAAAMMDD.
        
    Retorna:
        int: Día de la fecha (1-31).
    """
    dia = aaaammdd % 100
    return dia

def obtener_anio(aaaammdd: int) -> int:
    """
    Extrae el año de una fecha en formato numérico AAAAMMDD.
    
    Parámetros:
        aaaammdd (int): Fecha en formato AAAAMMDD.
        
    Retorna:
        int: Año de la fecha (por ejemplo, 2025).
    """
    anio = aaaammdd // 10000
    return anio

def obtener_mes(aaaammdd: int) -> int:
    """
    Extrae el mes de una fecha en formato numérico AAAAMMDD.
    
    Parámetros:
        aaaammdd (int): Fecha en formato AAAAMMDD.
        
    Retorna:
        int: Mes de la fecha (1-12).
    """
    mes = (aaaammdd // 100) % 100
    return mes

def str_fecha_corta(aaaammdd: int) -> str:
    """
    Convierte una fecha numérica AAAAMMDD en una cadena de texto en formato DD/MM/AAAA.
    
    Parámetros:
        aaaammdd (int): Fecha en formato AAAAMMDD.
        
    Retorna:
        str: Cadena en formato DD/MM/AAAA.
    """
    dia = obtener_dia(aaaammdd)
    mes = obtener_mes(aaaammdd)
    anio = obtener_anio(aaaammdd)
    cadena = f"{dia:02}/{mes:02}/{anio:04}"
    return cadena


def el_nombre_del_mes(mes:int) -> str:
    pass

def str_fecha_larga(aaaammdd: int) -> str:
    """
    Convierte una fecha numérica AAAAMMDD en una cadena de texto en formato:

    dd de nombre_mes de aaaa.
    
    Parámetros:
        aaaammdd (int): Fecha en formato AAAAMMDD.
        
    Retorna:
        str: Cadena en formato dd de nombre_mes de aaaa.
    """
    dia = obtener_dia(aaaammdd)
    mes = obtener_mes(aaaammdd)
    anio = obtener_anio(aaaammdd)
    nombre = el_nombre_del_mes(mes)
    cadena = f"{dia:02} de {nombre} de {anio:04}"
    return cadena

def isbisiesto(anio: int) -> bool:
    """
    Determina si un año es bisiesto.
    
    Un año es bisiesto si:
    - Es divisible por 4.
    - No es divisible por 100, excepto si también es divisible por 400.
    
    Parámetros:
        anio (int): Año a evaluar.
        
    Retorna:
        bool: True si el año es bisiesto, False en caso contrario.
    """
    return (anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0))


def obtener_los_dias_del_mes(mes: int, anio: int) -> int:
    """
    Obtiene la cantidad de días de un mes específico, considerando si el año es bisiesto.
    
    Parámetros:
        mes (int): Mes del año (1-12).
        anio (int): Año correspondiente al mes.
        
    Retorna:
        int: Número de días en el mes (28, 29, 30 o 31).
    """
    cantidad = 31

    if mes in (4, 6, 9, 11):  # Meses con 30 días.
        cantidad = 30
    elif mes == 2:  # Febrero.
        if isbisiesto(anio):
            cantidad = 29
        else:
            cantidad = 28

    return cantidad


def crear_fecha(dia:int,mes:int,anio:int) -> int:
    return (anio * 10000) + (mes * 100) + dia  # Construye la fecha en formato AAAAMMDD.

def crear_fecha_random(anio: int) -> int:
    """
    Genera una fecha aleatoria en un año específico en formato AAAAMMDD.
    
    Parámetros:
        anio (int): Año en el que se generará la fecha.
        
    Retorna:
        int: Fecha aleatoria en formato AAAAMMDD.
    """
    mes = rd.randint(1, 12)  # Selecciona un mes aleatorio (1-12).
    cantidad_de_dias = obtener_los_dias_del_mes(mes, anio)  # Días posibles en el mes.
    dia = rd.randint(1, cantidad_de_dias)  # Selecciona un día aleatorio válido.

    return crear_fecha(dia,mes,anio)


def restar_dias(aaaammdd:int,cantidad_dias:int)->int:
    pass

def comparar(aaaammdd1:int,aaaammdd2:int) -> int:
    """
    >  0 ==> aaaammdd1 > aaaammdd2
    == 0 ==> aaaammdd1 == aaaammdd2
    <  0 ==> aaaammdd1 < aaaammdd2
    """
    return aaaammdd1 - aaaammdd2

def sumar_dias(aaaammdd:int,cantidad_dias:int)->int:
    dia = obtener_dia(aaaammdd)
    mes = obtener_mes(aaaammdd)
    anio = obtener_anio(aaaammdd)

    while cantidad_dias > 0:
        dia += 1
        if dia > obtener_los_dias_del_mes(mes,anio):
            dia = 1
            mes += 1
            if mes > 12:
                mes = 1
                anio += 1
        cantidad_dias -= 1
    
    return crear_fecha(dia,mes,anio)

def test():
    """
    Función principal que genera una fecha aleatoria en el año 2025
    y la imprime en formato DD/MM/AAAA.
    """
    # Genera una fecha aleatoria para el año 2025.
    fecha = crear_fecha_random(2025)

    # Muestra la fecha en formato corto.
    print(str_fecha_corta(fecha))




# Llamada al programa principal.
# main()

if __name__ == '__main__':
    test()



