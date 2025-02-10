

def main():
    numero_mes = int(input("Mes [1..12]: "))     
    match numero_mes:
            case 1:
                nombre = "Enero"
            case 2:
                nombre = "Febrero"
            case 3:
                nombre = "Marzo"
            case 4:
                nombre = "Abril"
            case 5:
                nombre = "Mayo"
            case 6:
                nombre = "Junio"
            case 7:
                nombre = "Julio"
            case 8:
                nombre =  "Agosto"
            case 9:
                nombre =  "Septiembre"
            case 10:
                nombre =  "Octubre"
            case 11:
                nombre =  "Noviembre"
            case 12:
                nombre =  "Diciembre"
            case _:
                nombre =  None  # Caso por defecto para valores fuera de rango

    print(f"{numero_mes} {nombre}")


main()