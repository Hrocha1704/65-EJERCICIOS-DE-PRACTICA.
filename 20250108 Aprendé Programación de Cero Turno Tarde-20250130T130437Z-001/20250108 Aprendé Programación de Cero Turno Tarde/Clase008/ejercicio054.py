"""
Ejercicio 054

Escribir un programa que permita controlar con validación el ingreso a un sitio web. 

Teniendo dos constantes con un nombre de usuario ("admin") y una contraseña ("123456"), 
el programa debe permitir al usuario ingresar sus credenciales. 
Si las mismas son erróneas, se volverán a pedir hasta un máximo de 3 intentos. 

Finalmente, la computadora debe mostrar alguno de los siguientes mensajes según sea el caso: 
"Acceso concedido" o "Se ha bloqueado la cuenta"
"""
USUARIO = "admin"
CONTRASENA = "1234"
MAXIMA_CANTIDAD_INTENTOS = 3


def ingresar_las_credenciales() -> bool:
    ingreso_ok = False
    intento = 0
    while intento < MAXIMA_CANTIDAD_INTENTOS and ingreso_ok == False:
        usuario = input("Usuario: ")
        contrasena = input("Contraseña: ")
        intento += 1
        ingreso_ok = (USUARIO == usuario) and (CONTRASENA == contrasena)

    return ingreso_ok

    


def main():
    ingreso_ok = ingresar_las_credenciales()
    if ingreso_ok:
        print("Acceso concedido")
    else:
        print("Se ha bloqueado la cuenta")
        
    

    
    



main()



