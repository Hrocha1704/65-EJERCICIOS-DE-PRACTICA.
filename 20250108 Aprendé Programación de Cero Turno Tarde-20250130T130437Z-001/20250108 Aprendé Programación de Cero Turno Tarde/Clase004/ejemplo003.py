"""
Generar 3 numeros y mostrar el mayor.

"""


from random import randint


n1 = randint(1,10) # 1
n2 = randint(1,10) # 2
n3 = randint(1,10) # 10
n4 = randint(1,10) # 10

"""
    no nos gusta !!!!!

if n1 > n2:
    # True n1 > n2
    if n1 > n3:
        # True n1 > n3
        cartel = f"mayor {n1}"
    else:    
        cartel = f"mayor {n3}"
else:
    if n2 > n1:
"""        

mayor = n1

if n2 > mayor:
    mayor = n2

if n3 > mayor:
    mayor = n3

if n4 > mayor:
    mayor = n4

print(f"{n1},{n2},{n3},{n4} Mayor es {mayor}")    



