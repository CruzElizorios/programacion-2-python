class Laberinto():
    def __init__(self,matriz) -> None:
        self.matriz = matriz
    

class Personaje():
    def __init__(self,nombre, posicion) -> None:
        self.nombre = nombre
        self.posicion = posicion
    
    def mover(self,letra):
        pass
    # def moverIzquierda(self):
    #     pass
    # def moverArriba(self):
    #     pass    
    # def moverAbajo(self):
    #     pass

nivel_1=[
    [1,1,0,1], # lista 0
    [1,1,0,1], # lista 1
    [1,1,0,1], # lista 2
    [1,1,0,1]  # lista 3
]