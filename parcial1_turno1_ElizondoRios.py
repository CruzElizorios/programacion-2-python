# Programacion 2 (TUIA)
# Examen 1 - Turno 1
# 24/09/2024

# COMPLETAR
# nombre, Elizondo Rios
# Ejercicio 1: Defina la siguiente funcion en forma recursiva.

def enumerar(lista:list[str]) -> str:
    """
    Recibe una lista de cadenas y devuelve una cadena con los elementos
    de la lista separados por coma y finalizados por punto.

    Ejemplos:
    >>> enumerar([])
    ''

    >>> enumerar(['Hola'])
    'Hola.'

    >>> enumerar(['Hola', 'Chau'])
    'Hola, Chau.'

    >>> enumerar(['Hola', 'Chau', 'Adios'])
    'Hola, Chau, Adios.'
    """
    if len(lista) == 0:
        return ""
    elif len(lista) == 1:
        return f"{lista[0]}."
    
    return f"{lista[0]}" + ", " + enumerar(lista[1:])

print(enumerar([]))
print(enumerar(['Hola']))
print(enumerar(['Hola', 'Chau']))
print(enumerar(['Hola', 'Chau', 'Adios']))

# Ejercicio 2: Defina la clase Pila.
class Pila:
    def __init__(self) -> None:
        self.elementos = []

    def push(self, elemento:any) -> None:
        self.elementos.append(elemento)
    
    def pop(self):
        if not self.is_empty():
            return self.elementos.pop()
        else:
            print("la pila no tiene elementos")
    
    def is_empty(self):
        return self.elementos == []
    
    def mostrar(self):
        #no era necesario, con hacer un print(p.elementos)
        #se obtenia el mismo resultado
        print(self.elementos)

p = Pila()
p.push(8)
p.push(3)
#print(p.elementos)
print(p.is_empty())
p.mostrar()
p.pop()
p.mostrar()
p.pop()
p.pop()

# Ejercicio 3: Defina una clase Caja que represente una caja registradora.
# Asegurese de mantener en su representacion interna la cantidad de
# billetes de cada denominacion.
class Caja:
    def __init__(self) -> None:
        self.contenido: dict[int, int] = {}

    def agregar(self, billete: int, cantidad: int) -> None:
        """Agrega a la caja la cantidad de billetes indicada
        de una determinada denominacion."""
        #si el billete ya se encuentra, le sumo la nueva cantidad de billetes
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
    
    def mostrar(self):
        """muestra el diccionario interno"""
        print(self.contenido)
    
    def __str__(self) -> str:
        """Representa el contenido de la caja de la siguiente manera:
        Cantidad de billetes de $10: XXX.
        Cantidad de billetes de $20: XXX.
        Cantidad de billetes de $50: XXX.
        Cantidad de billetes de $100: XXX.
        Cantidad de billetes de $500: XXX.
        Cantidad de billetes de $1000: XXX.
        Cantidad de billetes de $2000: XXX.
        Cantidad de billetes de $10000: XXX.
        Total: $XXX.
        """
        info = ""
        for clave,valor in self.contenido.items():
            info += f"Cantidad de billetes de ${str(clave)}: {str(valor)}. \n"
        return info + f"Total: ${str(self.total())}."

caja_registradora = Caja()
caja_registradora.agregar(100,2)
caja_registradora.agregar(50,2)
caja_registradora.agregar(20,1)
caja_registradora.agregar(20,4)
caja_registradora.agregar(100,3)
caja_registradora.mostrar()
print(caja_registradora)



