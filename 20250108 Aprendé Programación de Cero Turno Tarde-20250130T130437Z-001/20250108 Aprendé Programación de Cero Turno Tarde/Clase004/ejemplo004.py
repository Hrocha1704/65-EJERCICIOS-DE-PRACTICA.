
"""
Generar 3 numeros. mostrar mayor,medio,menor
"""



import random as rd


n1 = rd.randint(1,10) # 1
n2 = rd.randint(1,10) # 2
n3 = rd.randint(1,10) # 10
n4 = rd.randint(1,10) # 10

mayor = n1
medio = n2
menor = n3

if n2 > mayor:
    mayor = n2
    medio = n1
    menor = n3 

if n3 > mayor:
    mayor = n3
    medio = n1
    menor = n2 

if menor > medio:
    # normal
    auxiliar = menor
    menor = medio
    medio = auxiliar
#    1      5      1     5
    menor,medio = medio,menor


print(f"[{n1},{n2},{n3}]  ==> {mayor} , {medio} , {menor}")

print(mayor,' ',medio,' ',menor)
x = mayor,medio,menor
print(x)


