# Ejercicio 2
# Crear una clase PilaConMaximo que soporte las operaciones de Pila (push(item) y pop()), y además
# incluya el método obtener_maximo() que devuelva el elemento máximo de la pila sin sacarlo de la
# misma y que funcione en tiempo constante, es decir que su tiempo de ejecución no depende del
# tamaño de la entrada.

# RESOLUCIÓN PROFESOR
class PilaConMaximo():

    def __init__(self) -> None:
        self.elementos = []
        self.maximo = None

    def push(self,elemento: int):
        self.elemntos.append(elemento)
        if elemento is None:
            self.maximo = elemento
        elif elemento > self.maximo:
            self.maximo = elemento
    
    def pop(self):
        elemento = self.elementos.pop()
        if self.maximo == elemento:
            self.maximo = max(self.elementos)
        return elemento
    
    def obtener_maximo(self):
        return self.grande