# EJERCICIO 6
# Escriba una función recursiva que tome un numero natural n e imprima todos los números 
# desde n hasta 1
def mostrar_numeros(n):
    if n < 0:
        print(n)
        return mostrar_numeros(n+1)
    elif n == 0:
        return
    print(n)
    return mostrar_numeros(n-1)

mostrar_numeros(5)
mostrar_numeros(-4)