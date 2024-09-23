# ejercicio de tarea para 03/09/24:
#     crear una clase diccionario que tenga el método insertar y buscar;debe tener una clave y un valor, 
#     además debe comportarse como uno sin serlo (utilizar tuplas o listas por ejemplo) 

class Diccionario_propio:
    def __init__(self, lista: list = []):
        self.lista = lista

    def insertar(self, clave, valor):
        # tupla = (clave, valor)
        for tupla in self.lista:
            # verifico si ya existe la clave en el dic
            if tupla[0] == clave:
                # se elimina la tupla para poder actualizar el nuevo valor
                self.lista.remove(tupla)
                self.lista.append((clave, valor))
                return             
        self.lista.append((clave, valor)) 

    #  [('maria', 20), ('juan', 36)]
    def buscar(self, clave):
        print(self.lista)
        for tupla in self.lista:
            if tupla[0] == clave:
                return tupla[1]
        else:
            print("no existe la clave")

dic2 = Diccionario_propio()
dic2.insertar("maria", 20)
dic2.insertar("juan", 36)
print(dic2.buscar("maria"))
dic2.insertar("maria", 150)
dic2.insertar("maria", 463)
dic2.insertar("maria", 500)
print(dic2.buscar("maria"))
dic2.insertar("ana", 1050)
print(dic2.buscar("maria"))

# dic = {
#     "papa": 20,
#     "manzana": 5
# }
# dic["manzana"]=10

# print(dic)