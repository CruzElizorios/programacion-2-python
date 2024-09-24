# Ejercicio 10
# Escriba una función recursiva que reciba 2 enteros n y b y devuelva True si n es potencia de b
# ejemplos:
# es_potencia(8, 2) -> True
# es_potencia(64, 4) -> True
# es_potencia(70, 10) -> False

def es_potencia(n:int,b:int) -> bool:
    # caso base
    if n == 1:
        #print("soy potencia")
        return True
    if n < b:
        return False
    #print(n)
    # el resto de n dividido b debe ser cero para q n sea potencia de b
    if n % b == 0:
        return es_potencia(n/b,b)
    else:
        return False
print(es_potencia(15,3))
print(es_potencia(8, 2))
print(es_potencia(64, 4))
print(es_potencia(70, 10)) 

# Ejercicio 10.1
# Escribe una función recursiva que calcule la potencia de un número dado. La función debe recibir dos parámetros: la base y el exponente.
# si b^e -> e = 0  b^e = 1
def potencia(base:int, exponente:int) -> bool:
    # caso base
    if exponente == 0:
        #print("soy potencia")
        return 1
    if exponente > 0:
        return base * potencia(base, exponente-1)
    else:
        return("exponente no admite negativo")

print(potencia(2,3))
print(potencia(10,4))
print(potencia(3,-1))
