#ejercicio 2.1
def repite_saludo(n: int, saludo: str) -> None:
    if n == 1:
        return print(f"{saludo}")
    print(f"{saludo}")
    return repite_saludo(n-1, saludo)

repite_saludo(2, "banana")
repite_saludo(4, "casa")

#ejercicio 2.2
def repite_saludo_concatenado(n: int, saludo: str) -> str:
    if n == 1:
        return f"{saludo}"
    return f"{saludo} " + repite_saludo_concatenado(n-1, saludo) 

def repite_saludo_concatenado2(n: int, saludo: str) -> str:
    if n == 1:
        return saludo
    return saludo + " " + repite_saludo_concatenado(n-1, saludo) 

print(repite_saludo_concatenado2(2,"hola"))
print(repite_saludo_concatenado(6,"tree"))