# EJERCICIO 4
# Basándose en el TAD de Cola, implementar una clase Queue con listas de Python

class Queue:
    def __init__(self) -> None:
        self.elementos = []
    
    def push(self, item):
        """sirve para agregar un elemento a la cola"""
        self.elementos.append(item)
    
    def is_empty(self) -> bool:
        """devuelve True si no hay elementos en la cola"""
        return self.elementos == []
    
    def pop(self):
        """devuelve y borra el primer elemento de la cola"""
        if not self.is_empty() :
            return self.elementos.pop(0)
        else:
            print("No hay elementos que borrar")
    
    def cantidad(self) -> int:
        """devuelve la cantidad de elementos que hay dentro de la cola"""
        return len(self.elementos)
    
    def mostrar(self) -> None:
        print(self.elementos)

c = Queue()
c.push(4)
c.push("hola")
c.mostrar()
print("cantidad elementos:", c.cantidad())
print(c.is_empty())
c.pop()
c.mostrar()
c.pop()
c.mostrar()
c.pop()
