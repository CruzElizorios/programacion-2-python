# Ejercicio 13
# Escriba una función recursiva para replicar los elementos de una lista 
# una cantidad n de veces. Por ejemplo:
# replicar([1, 3, 3, 7], 2) -> ([1, 1, 3, 3, 3, 3, 7, 7])

def replicar(lista:list, repeticion: int) -> list:

    if len(lista) == 1:
        return lista * repeticion 
    
    return [lista[0]]*repeticion + replicar(lista[1:],repeticion)
    
print(replicar([1, 3, 3, 7],2))
    