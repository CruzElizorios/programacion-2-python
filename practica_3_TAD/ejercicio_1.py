# Práctica 2: Tipos Abstractos de Datos 
# Ejercicio 1
# Basándose en el TAD de Pila, implementar una clase Stack con listas de Python.

class Stack():
    def __init__(self) -> None:
        self.datos = []
    
    def push(self,lista:list):
        """ sirve para agregar una lista a Stack"""
        if type(lista) is list:
            self.datos.append(lista)
            print(self.datos)

    def pop(self):
        """ No se puede llamar a este método si esta vacia, debe antes verificar con el 
        método is_empty"""
        return self.datos.pop()

    def is_empty(self) -> bool:
        """verifica que el stack no se encuentre vacio"""
        return self.datos == []
    
p = Stack()

p.push(["A", "b"])
p.push([8, 5, 9])
#print(p)
p.push([1,2])
print(p.pop())
print(p.is_empty()) #devuelve false porque tiene dos listas dentro de la lista datos
p.pop()
p.pop()
print(p.is_empty()) # la lista ahora esta vacia
