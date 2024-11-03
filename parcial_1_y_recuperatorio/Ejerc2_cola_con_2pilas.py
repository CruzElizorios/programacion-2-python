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
        #si hay elementos en la pila2, saco elementos de la 2da pila
        #si la pila2 está vacía, tengo q llenarla con elementos de la pila1
        if self.pila2.isEmpty():
            #si la pila1 no está vacía entra en el ciclo
            while not self.pila1.isEmpty():
                elemento_pila1 = self.pila1.pop()
                self.pila2.push(elemento_pila1)     
        return self.pila2.pop()
    
    def isEmpty(self):
        return self.pila1.isEmpty() and self.pila2.isEmpty()
    
c = colaCon2Pila()
c.push(2)
c.push(3)
c.push(5)
print(f"almacenado en: pila1 = {c.pila1.data} - pila2 = {c.pila2.data}")
print(c.pop())
print(f"almacenado en: pila1 = {c.pila1.data} - pila2 = {c.pila2.data}")
print(c.isEmpty())
print(c.pop())
c.push("z")
print(f"almacenado en: pila1 = {c.pila1.data} - pila2 = {c.pila2.data}")
print(c.pop())
print(c.pop())
print(c.isEmpty())

# print(c.pop())
# c.push(10)
# c.push(15)
# print(c.pila1.data, c.pila2.data)
# print(c.pop())
# print(c.pila2.data)

class colaCon2Pila_V2():
    #más simple pero menos eficiente
    def __init__(self):
        self.pila1 = pila()
        self.pila2 = pila()
    
    def push(self, elemento):
        self.pila1.push(elemento)
    
    def pop(self):
        #todos los elementos de la 1ra pila van a la 2da pila
        while not self.pila1.isEmpty():
            elemento_pila1 = self.pila1.pop()
            self.pila2.push(elemento_pila1)     
        #la 2da pila, tiene todos los elementos en orden inverso a la 1ra pila
        #se quita el último elemento, que a su vez es el primero que entró a la cola
        ultimo_elemento = self.pila2.pop()
        #todos los elementos de la 2da pila vuelven a la 1ra pila
        while not self.pila2.isEmpty():
            elemento_pila2 = self.pila2.pop()
            self.pila1.push(elemento_pila2) 
        return ultimo_elemento
    
    def isEmpty(self):
        return self.pila1.isEmpty() and self.pila2.isEmpty()
cola_V2 = colaCon2Pila_V2()
cola_V2.push(2)
cola_V2.push(3)
cola_V2.push(5)
print(f"almacenado en: pila1 = {cola_V2.pila1.data} - pila2 = {cola_V2.pila2.data}")
print(cola_V2.pop())
print(f"almacenado en: pila1 = {cola_V2.pila1.data} - pila2 = {cola_V2.pila2.data}")