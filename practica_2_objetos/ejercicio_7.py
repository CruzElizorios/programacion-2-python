# EJERCICIO 7
# Encontrar los errores en el siguiente código y proponer soluciones:
# class Cosa:
#     def __init__(self, valor):
#         self.valor = valor
# class Coleccion:
#     def __init__(self):
#         self.coleccion = []
#     def agregar_cosa(cosa: Cosa):
#         coleccion.append(cosa)

class Cosa:
    def __init__(self, valor):
        self.valor = valor

class Coleccion:
    def __init__(self):
        self.coleccion = []
    def agregar_cosa(self, cosa: Cosa): # falta el self para poder acceder a coleccion
        self.coleccion.append(cosa)
    def mostrar(self):
        print(self.coleccion)

cosa = Cosa(3) # necesita un valor
coleccion = Coleccion()
coleccion.agregar_cosa(cosa)
coleccion.mostrar()