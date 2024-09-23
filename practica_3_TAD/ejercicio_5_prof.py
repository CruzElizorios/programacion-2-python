# RESOLUCIÓN PROFESOR
# Ejercicio 5
# Hace un montón de años había una viejísma sucursal del correo que tenía un cartel que decía "No
# se recibirán más de 5 cartas por persona". O sea que la gente entregaba sus cartas (hasta la
# cantidad permitida) y luego tenía que volver a hacer la cola si tenía más cartas para despachar. Modelar
# una cola de correo generalizada, donde en la inicialización se indica la cantidad (no necesariamente 5)
# de cartas que se reciben por persona.
class Cliente():
    def __init__(self, nombre: str, cant_cartas: int = 1) -> None:
        self.nombre = nombre
        self.cant_cartas = cant_cartas

class ColaGeneralizada:
    def __init__(self, cant_cartas: int = 5) -> None:
        self.elementos:list[Cliente] = []
        self.cant_cartas = cant_cartas
    
    def push(self, cliente: Cliente):
        self.elementos.append(cliente)
    
    def is_empty(self) -> bool:
        return len(self.elementos) == 0
    
    def remove(self) -> None:
        cliente = self.elementos.pop(0)
        cant_cartas = min( cliente.cant_cartas, self.cant_cartas) #devuelve el minimo que puede procesar
        # if cliente.cant_cartas <= self.cant_cartas:
        #     print(f"Atendido cliente: {cliente.nombre} despachadas {cliente.cant_cartas}")
        print(f"Atendido cliente: {cliente.nombre} despachadas {cliente.cant_cartas} cartas")

        cliente.cant_cartas -= cant_cartas
            
