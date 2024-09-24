# Ejercicio 2
# Crear una clase PilaConMaximo que soporte las operaciones de Pila (push(item) y pop()), y además
# incluya el método obtener_maximo() que devuelva el elemento máximo de la pila sin sacarlo de la
# misma y que funcione en tiempo constante, es decir que su tiempo de ejecución no depende del
# tamaño de la entrada.

class PilaConMaximo():

    def __init__(self) -> None:
        self.datos = []
        self.grande = 0 # hay que inicializar con valor None para que no 
        # de error al tener una lista con negativos

    def push(self,item: int):
        self.datos.append(item)
        self.grande = max(self.datos)
    
    def pop(self) -> int:
        if self.is_empty():
            print("No hay elementos")
            return
        borrado = self.datos.pop()
        self.grande = max(self.datos)
        return borrado
    
    def obtener_maximo(self) -> int:
        return self.grande
    
    def is_empty(self) -> bool:
        return self.datos == []
    
    def mostrar(self):
        print(self.datos)

p = PilaConMaximo()
p.pop()
p.push(7)
p.mostrar()
print(p.obtener_maximo())
p.push(10)
p.push(15)
p.mostrar()
print(p.obtener_maximo())
p.pop()
print(p.obtener_maximo())
p.mostrar()

