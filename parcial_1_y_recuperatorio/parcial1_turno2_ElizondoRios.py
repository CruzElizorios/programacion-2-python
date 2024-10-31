# Programacion 2 (TUIA)
# Examen 1 - Turno 2
# 24/09/2024

# COMPLETAR
# Nombre, Apellido
# DNI

# Ejercicio 1: Defina la siguiente funcion en forma recursiva.
def aplanar(lista: list[list[int]]) -> list[int]:
    """
    Recibe una lista de lista de enteros y devuelve una unica lista con
    el contenido de todas.

    Ejemplos:
    >>> aplanar([])
    []

    >>> aplanar([[1]])
    [1]

    >>> aplanar([[1], [2]])
    [1, 2]

    >>> aplanar([[1], [2], [3, 4]])
    [1, 2, 3, 4]
    """
    if lista == []:
        return []
    return lista[0] + aplanar(lista[1:])

print(aplanar([]))
print(aplanar([[1]]))
print(aplanar([[1], [2]]))
print(aplanar([[1], [2], [3, 4]]))

# Ejercicio 2: Defina la clase Cola.
class Cola:
    def __init__(self) -> None:
        self.elementos = []

    def push(self, elemento:any) -> None:
        self.elementos.append(elemento)
    
    def pop(self):
        if not self.is_empty():
            return self.elementos.pop(0)
        else:
            print("la pila no tiene elementos")
    
    def is_empty(self):
        return self.elementos == []

p = Cola()
p.push(8)
p.push(3)
print(p.is_empty())
print(p.elementos)
p.pop()
print(p.elementos)
p.pop()
p.pop() # muestra la pila no tiene elementos
    

# Ejercicio 3: Defina una clase Caja que represente una caja registradora.
# Asegurese de mantener en su representacion interna la cantidad de
# billetes de cada denominacion.
class Caja:
    def __init__(self) -> None:
        self.contenido: dict[int, int] = {}

    def agregar(self, billete: int, cantidad: int) -> None:
        """Agrega a la caja la cantidad de billetes indicada
        de una determinada denominacion."""
        if billete in self.contenido.keys():
            self.contenido[billete] = self.contenido[billete] + cantidad 
        else:
            #si el billete no se encuentra, lo agrego al dic
            self.contenido[billete] = cantidad

    def total(self) -> int:
        """Devuelve el importe total almacenado en la caja."""
        total = 0
        for clave,valor in self.contenido.items():
            total += valor*clave
        return total
    
    def __add__(self, other) -> "Caja":
        """Dadas dos cajas, devuelve una nueva con el contenido de ambas."""
        nueva = Caja()

        for billete, cantidad in self.caja.items():
            nueva.agregar(billete,cantidad)

        for billete, cantidad in other.caja.items():
            nueva.agregar(billete,cantidad)
        return nueva
    
c=Caja()
c.agregar(1000,2)
c.agregar(100,3)
print(c.contenido)
print(c)
