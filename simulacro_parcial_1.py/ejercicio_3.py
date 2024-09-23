# EJERCICIO 3 
# Crear una clase ColaConPromedio que soporte las operaciones de Cola
# incluya el método obtener_promedio() que devuelva el promedio de los elementos de la cola y
# funciona en tiempo constante.

class ColaConPromedio():
    def __init__(self) -> None:
        self.lista = []
        self.suma = 0
    
    def push(self,valor: int):
        self.lista.append(valor)
        self.suma += valor
        print(self.suma)
    
    def delete(self):
        borrado = self.lista.pop(0)
        self.suma -= borrado
        print(self.suma)
    
    def obtener_promedio(self) -> float:
        return self.suma / len(self.lista)
    
    def __str__(self) -> str:
        datos = "["
        for index in range(len(self.lista)):
            if index == 0:
                datos = datos + str(self.lista[index])
            elif index > 0:    
                datos = datos + ", " + str(self.lista[index])
        return datos +"]"
    
    def mostrar(self):
        print(self.lista)
    
cola = ColaConPromedio()
cola.push(11)
cola.push(7)
cola.push(6)
print(cola)
print("promedio: ", cola.obtener_promedio())
cola.delete()
print(cola)
cola.mostrar()
print("promedio: ", cola.obtener_promedio())
