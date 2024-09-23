class Laberinto():
    def __init__(self,matriz,entrada, salida) -> None:
        self.matriz = matriz
        self.entrada = entrada
        self.salida = salida
    

class Personaje():
    def __init__(self, x:int,y:int) -> None:
        self.x = x
        self.y = y
        
    def mover(self,letra):
        if letra == "a":
            self.posicion

elmo = Personaje()
nivel_1=[
    [(1,1),(1,2),(1,3),(2,3),(2,4),(3,1),(3,2),(3,4),(3,1),(3,2),(3,4)]
]