class Pila:
    def __init__(self):
        self.datos = []
    
    def push(self,elemento):
        self.datos.append(elemento)

    def pop(self):
        """Este método no se puede llamar si la pila esta vacía"""
        return self.datos.pop()

    def is_empty(self) -> bool:
        return self.datos==[]
    
# p= Pila()
# print(p.is_empty())
# p.push(1)
# p.push(2)
# p.push(3)
# print(p.pop())
# print(p.is_empty())

class Cola:
    def __init__(self):
        self.datos = []
    
    def push(self,elemento):
        self.datos.append(elemento)

    def pop(self):
        """Este método no se puede llamar si la pila esta vacía"""
        return self.datos.pop(0)

    def is_empty(self) -> bool:
        return self.datos==[]
    
    
c= Cola()
c.push(5)
c.push(2)
c.push(6)
c.push(10)
print(c.pop())
print(c.datos)
c.pop()
print(c.datos)



    
        

