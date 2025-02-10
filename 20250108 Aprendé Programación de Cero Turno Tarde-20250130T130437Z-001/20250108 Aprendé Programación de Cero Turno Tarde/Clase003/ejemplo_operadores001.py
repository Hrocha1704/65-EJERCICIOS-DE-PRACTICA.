

# AAAAMMDD
fecha = 19631216

# AAAAMM | ==> DD
dia = fecha%100


# AAAA <== | MMDD
anio = fecha//10000

# AAAAMM <== | DD
anio_mes = fecha // 100

# AAAA | ==> MM
mes = anio_mes%100

# AAAA | ==> MM <== | DD
mes = (fecha//100)%100

# DD/MM/AAAA
cadena = f"{dia}/{mes}/{anio}"

print(cadena)












