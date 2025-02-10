import funciones_int as fi


def main():
    f1 = fi.crear_fecha_random(2025)
    print(fi.str_fecha_corta(f1))

    f2 = fi.crear_fecha_random(2025)
    print(fi.str_fecha_corta(f2))

    for cantidad_dias in range(1,365):
        f3 = fi.sumar_dias(f1,cantidad_dias)
        print(fi.str_fecha_corta(f3))
main()








