# def potencia(n:int,pot:int) -> int:
#     if(pot == 0):
#         return 1
#     return n * potencia(n, pot -1)

# var = potencia(5,3)
# print(var)

# EJERCICIO 7
def recursiva(t: int, k: int) -> int:
    #print(t)
    if t >= 100:
        return k
    else:
        return recursiva(t + k, k + 1)

print("resultado recursivo: ",recursiva(10,4))

def no_recursiva(t: int, k: int) -> int:
    while t < 100:
        #print(t)
        t = t + k
        k = k + 1
    return k

print("iterativo abajo")
print("resultado iterativo: ",no_recursiva(10,4))

# HACER TESTING CON PYTEST, DE FORMA MANUAL
def test_funciones():
    for t in range(50):
        for k in range(50):
            assert no_recursiva(t,k) == recursiva(t,k)
    assert 3 == 1
test_funciones()