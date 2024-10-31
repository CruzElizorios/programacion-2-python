class pila():
    def __init__(self):
        self.data = []
    
    def push(self, elemento):
        self.data.append(elemento)
    
    def pop(self):
        return self.data.pop()
    
    def isEmpty(self):
        if self.data == []:
            return True
        return False

p = pila()
#pruebas para saber si la pila funciona
# p.push(2)
# p.push(4)
# p.push(7)
# print(p.data)
# p.pop()
# print(p.data)
# print(p.isEmpty())

class colaCon2Pila():
    def __init__(self):
        self.pila1 = pila()
        self.pila2 = pila()
    
    def push(self, elemento):
        self.pila1.push(elemento)
    
    def pop(self):
        if self.pila2.isEmpty():
            #si la pila1 no está vacía entra en el ciclo
            while not self.pila1.isEmpty():
                elemento_pila1 = self.pila1.pop()
                self.pila2.push(elemento_pila1)     
        return self.pila2.pop()
    
    def isEmpty(self):
        if self.data == []:
            return True
        return False
    
c = colaCon2Pila()
c.push(2)
c.push(3)
c.push(5)
print(f"almacenado en: pila1 = {c.pila1.data} - pila2 = {c.pila2.data}")
print(c.pop())
print(f"almacenado en: pila1 = {c.pila1.data} - pila2 = {c.pila2.data}")
print(c.pop())
c.push("z")
print(f"almacenado en: pila1 = {c.pila1.data} - pila2 = {c.pila2.data}")
print(c.pop())
print(c.pop())
# print(c.pop())
# c.push(10)
# c.push(15)
# print(c.pila1.data, c.pila2.data)
# print(c.pop())
# print(c.pila2.data)
