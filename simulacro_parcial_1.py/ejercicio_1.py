# Cada número de Lucas se define como la suma de sus dos inmediatos
# anteriores, formando así una secuencia de enteros. Los dos primeros números de Lucas son a y b.
# Dada la siguiente ley:
#             [ a                         si n = 0,
# L(a,b,n) =  | b                         si n = 1,
#             [ L(a,b,n-1) + L(a,b,n-2)   si n > 1.
# Definir en python la función lucas(...) que permita calcular el n-esimo número de forma
# recursiva.

def lucas(a:int, b:int, n:int) -> int:
    if n >= 0:
        if n == 0:
            return a
        elif n == 1:
            return b
        return lucas(a,b, n-1) + lucas(a,b, n-2)
    
print(lucas(2,3,-1)) # 2
print(lucas(2,3,1)) # 3
print(lucas(2,3,2)) # 5
print(lucas(2,3,3)) # 8 porque va a retornar (a,b,3-1) -> (a,b,2) = 5
                    #                        (a,b,3-2) -> (a,b,1) = 3    

# lucasV2 no funciona para negativos
def lucasV2(a:int, b:int, n:int) -> int:
    if n > 1:
        return lucas(a,b, n-1) + lucas(a,b, n-2)
    elif n == 1:
        return b
    return a
print("v2")
print(lucasV2(2,3,0))
print(lucasV2(2,3,1))
print(lucasV2(2,3,2))
print(lucasV2(2,3,-1)) # siempre va a devolver a y no es correcto
print(lucas(2,3,-1))   # se vuelve bucle infinito tampoco es correcto, por eso es necesario verificar antes que n no es negativo
