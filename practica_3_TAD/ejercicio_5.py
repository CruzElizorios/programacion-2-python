# Ejercicio 5
# Hace un montón de años había una viejísma sucursal del correo que tenía un cartel que decía "No
# se recibirán más de 5 cartas por persona". O sea que la gente entregaba sus cartas (hasta la
# cantidad permitida) y luego tenía que volver a hacer la cola si tenía más cartas para despachar. Modelar
# una cola de correo generalizada, donde en la inicialización se indica la cantidad (no necesariamente 5)
# de cartas que se reciben por persona.

#  correo = ColaGeneralizada()
#  correo.push(Cliente("Ana", 1))
#  correo.push(Cliente("Facu", 1))
#  correo.push(Cliente("Seba", 2))
#  correo.push(Cliente("Joe", 6))
#  correo.push(Cliente("Pablo", 9))
#  correo.push(Cliente("Ana", 1))
#  correo.push(Cliente("Facu", 1))
#  correo.push(Cliente("Seba", 2))
#  while not correo.isEmpty():
#      correo.remove()
# Debería mostrar:
# Atendido cliente Ana, despachadas 1 cartas
# Atendido cliente Facu, despachadas 1 cartas
# Atendido cliente Seba, despachadas 2 cartas
# Atendido cliente Joe, despachadas 5 cartas
# Atendido cliente Pablo, despachadas 5 cartas
# Atendido cliente Ana, despachadas 1 cartas
# Atendido cliente Facu, despachadas 1 cartas
# Atendido cliente Seba, despachadas 2 cartas
# Atendido cliente Joe, despachadas 1 cartas
# Atendido cliente Pablo, despachadas 4 cartas
class Cliente():
    def __init__(self, nombre: str, cant_cartas: int = 1) -> None:
        self.nombre = nombre
        self.cant_cartas = cant_cartas
    
    def __str__(self) -> str:
        return f"cliente: {self.nombre}, cantidad de cartas: {self.cant_cartas}"

class ColaGeneralizada:
    """Implementar esta clase!!!"""
    def __init__(self, limite_despacho: int = 1) -> None:
        self.elementos = []
        self.limite_despacho = limite_despacho
    
    def push(self, cliente: "Cliente") -> None:
        self.elementos.append(cliente)

    def remove(self) -> None:
        # ARREGLAR CASO VACIO
        atendido = self.elementos.pop(0)
        if atendido.cant_cartas > self.limite_despacho:
            
            cartas_restantes = atendido.cant_cartas - self.limite_despacho
            
            self.push(Cliente(atendido.nombre, cartas_restantes))
            
            print(f"Atendido cliente {atendido.nombre}, despachadas {self.limite_despacho} cartas")
        else:
            print(f"Atendido cliente {atendido.nombre}, despachadas {atendido.cant_cartas} cartas")
    
    def is_empty(self) -> bool:
        return self.elementos == []

    def mostrar(self):
        print("clientes en cola: ")
        for cliente in self.elementos:
            print(cliente)

pablo = Cliente("pablo",3)
correo = ColaGeneralizada(5)
correo.push(pablo)
correo.push(Cliente("Joe", 6))
correo.mostrar()
correo.remove()
print("siguiente..")
correo.mostrar()
correo.remove()
correo.mostrar()
correo.remove()
correo.mostrar()
correo.remove()
