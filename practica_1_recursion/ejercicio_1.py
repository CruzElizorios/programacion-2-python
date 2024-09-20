#forma recursiva
#ejercicio 1.1
def repite_hola(n: int)-> None:
    if n == 1:
        return print("Hola")
    print("Hola")
    return repite_hola(n-1)

# repite_hola(5)
# print("nuevo llamado abajo")
# repite_hola(2)

#ejercicio 1.2
def repite_hola_concatenado(n: int) -> str:
    if n == 1:
        return "hola"
    return "hola " + repite_hola_concatenado(n-1) 

print(repite_hola_concatenado(3))