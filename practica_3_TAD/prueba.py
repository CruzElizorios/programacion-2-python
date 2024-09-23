from copy import deepcopy
lista = [5,6,1,10,5]
lista2 = lista
lista2.sort()
print(lista)
print(lista2)
print(id(lista2),
id(lista))

