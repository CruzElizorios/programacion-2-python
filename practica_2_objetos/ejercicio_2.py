from math import sqrt
# Defina, en la clase Point, un método distancia() que nos de la distancia euclídea entre dos puntos.
# Nota: Recordar que la distancia euclídea entre dos puntos A = (x1, y1) y B = (x2, y2) se calcula como:
# d = raiz((x2 - x1)^2 + (y2 - y1)^2 )

class Point:
    """ representación de un punto en un plano cartesiano 2D """
    
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return '(' + str(self.x) + ', ' + str(self.y) + ')'
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y
    
    def __add__(self, other: 'Point') -> 'Point':
        return Point(self.x + other.x, self.y + other.y)
    
    def distancia(self, other: 'Point') -> float:
        return sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
    
puntoA = Point(4,6)
puntoB = Point(6,8)

print(puntoA.distancia(puntoB))



