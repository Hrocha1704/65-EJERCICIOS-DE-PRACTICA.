
"""
n! ==>  n <= 1 = 1
        n * (n-1)!
            (n-1) * (n-2)!
                    (n-2) * (n-3)!
"""

def main():
    numero = int(input("Numero: "))
    factorial = 1

    if numero <= 1:   
        factorial = 1
    else:
        while numero >= 1:
            factorial *= numero
            numero -= 1 
    
    print(factorial)
    cadena = str(factorial)
    cantidad_caracteres = len(cadena)
    print(f"Cantidad de caracteres: {cantidad_caracteres}")
main()
