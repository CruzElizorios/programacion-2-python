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
        print(self.datos)
    
    def pop(self):
        borrado = self.datos.pop()
        self.grande = max(self.datos)
        return borrado
    
    def obtener_maximo(self) -> int:
        return self.grande

inten = PilaConMaximo()
inten.push(7)
print(inten.obtener_maximo())
inten.push(10)
inten.push(15)
print(inten.obtener_maximo())
inten.pop()
print(inten.obtener_maximo())

