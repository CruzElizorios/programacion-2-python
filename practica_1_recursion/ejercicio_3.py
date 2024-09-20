# EJERCICIO 3

def misterio(a: int) -> int:
    if a == 0:
        return a
    return 1 + misterio(a - 1)

print(misterio(10))

def new_misterio(a:int) -> int:
    return a 

def new_misterio2(a:int) -> int:
    for num in range(a):
        p = num + 1
    return p

print(new_misterio2(10))