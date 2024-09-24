#Ejercicio 9
# Complete la funcionalidad de la clase Jugador, implementando los siguientes métodos:
# •golpeado: quita vida al jugador.
# •golpear: quita vida al enemigo y lo agrega a la lista de enemigos golpeados.
# class Entidad:
#     def __init__(self, vida_inicial: int):
#         self.vida = vida_inicial
# class Enemigo(Entidad):
#     pass
# class Jugador(Entidad):
#     def __init__(self, vida_inicial: int):
#         super().__init__(vida_inicial)
#         self.enemigos_golpeados = []
#     def golpeado(self, cuanto):
#         """Completar."""
#         pass
#     def golpear(self, enemigo, cuanto):
#         """Completar."""
#         pass
class Entidad:
    def __init__(self, vida_inicial: int, nombre: str):
        self.nombre = nombre
        self.vida = vida_inicial

class Enemigo(Entidad):
    def __init__(self, vida_inicial: int, nombre: str):
        super().__init__(vida_inicial, nombre)

        pass

class Jugador(Entidad):
    def __init__(self, vida_inicial: int, nombre: str):
        super().__init__(vida_inicial, nombre)
        self.enemigos_golpeados = []

    def golpeado(self, cuanto: int):
        self.vida = self.vida - cuanto
        if self.vida <= 0:
            print(f"{self.nombre} ha muerto, vida = {self.vida}")

    def golpear(self, enemigo: Enemigo, cuanto: int):
        enemigo.vida = enemigo.vida - cuanto
        print(f"{self.nombre} golpea a {enemigo.nombre}")
        
        if enemigo.vida <= 0:
            print(f"{enemigo.nombre} ha muerto, vida = {enemigo.vida}")
        if enemigo not in self.enemigos_golpeados:
            self.enemigos_golpeados.append(enemigo)

maria = Jugador(100,"maria")
pedro = Enemigo(100,"pedro")
maria.golpeado(20)
print(maria.vida)
maria.golpear(pedro,50)
print(pedro.vida)
maria.golpear(pedro,50)


