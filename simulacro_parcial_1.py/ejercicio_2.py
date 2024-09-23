#  EJERCICIO 2
# Dada la siguiente clase completar:
# class Tarea:
#     def __init__(self, titulo, descripcion):
#         self.titulo = titulo
#         self.descripcion = descripcion
# a) Agregar a la clase Tarea un método para transformar la tarea en un string.
# b) Permitir unir dos tareas en una con el + concatenando sus titulos y descripciones.
# c) Crear una nueva clase TareaPrioritaria la cual hereda los métodos de Tarea pero en este caso permite guardar la prioridad de cada tarea siendo la 0 la más alta.
# d) Agregar un método a TareaPrioritaria que las compare por prioridad. Una tarea antecede a otra si su prioridad es más alta.


class Tarea():
    def __init__(self, titulo: str, descripcion: str):
        self.titulo = titulo
        self.descripcion = descripcion
    
    def tareaToString(self) -> str:
        return f"tarea: {self.titulo}, descripción: {self.descripcion}; "
    
    def tareaConcatenada(self, other: "Tarea") -> str:
        # tarea1= f"tarea: {self.titulo}, descripción: {self.descripcion}; "
        # tarea2= f"tarea: {other.titulo}, descripción: {other.descripcion} "
        # return tarea1 + tarea2
        return self.tareaToString() + other.tareaToString()


matematica = Tarea("mate", "calcular radio")
print(matematica.tareaToString())
lengua = Tarea("lengua", "hacer un cuento")
# tarea1 = lengua.tareaToString()
# tarea2 = matematica.tareaToString()
# print(tarea1 + tarea2)

tareasJuntas = matematica.tareaConcatenada(lengua)
print(tareasJuntas)

class TareaPrioritaria(Tarea):
    """ es una clase hija de la clase Tarea, tiene un atributo extra llamado prioridad que permite indicar la tarea con más prioridad
    """
    def __init__(self, titulo, descripcion, prioridad: int) -> None:
        super().__init__(titulo,descripcion)
        self.prioridad = prioridad
    
    def ordenDePrioridad(self, other: "TareaPrioritaria") -> str:
        if self.prioridad < other.prioridad:
            return f"'{self.titulo}' es más prioritaria que: '{other.titulo}'"
        elif self.prioridad > other.prioridad:
            return f"'{other.titulo}' es más prioritaria que: '{self.titulo}'"
        return f"'{other.titulo}' y '{self.titulo}' tienen el mismo orden de prioridad"

dibujo = TareaPrioritaria("dibujo","pintar un cuadro",0)
compras = TareaPrioritaria("ir a mercado","comprar papas",2)
print(dibujo.ordenDePrioridad(compras))
# modifico el atributo prioridad del objeto dibujo
dibujo.prioridad = 2 # compras prioridad=2 y dibujo prioridad=2
print(dibujo.ordenDePrioridad(compras))
dibujo.prioridad = 3 # compras prioridad=2 y dibujo prioridad=3 
print(dibujo.ordenDePrioridad(compras))