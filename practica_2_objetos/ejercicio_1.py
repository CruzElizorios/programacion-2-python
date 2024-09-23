
# Considere las clases Point y Rectangle que vimos en la clase de teoría.
# 1. Defina métodos __str__ y __eq__ apropiados para Rectangle.
# 2. Defina una función llamada mover_rectángulo que tome un rectángulo y dos parámetros dx y
# dy. Esta función debería cambiar de posición el rectángulo sumando dx a la coordenada x de la
# esquina superior izquierda y del mismo modo sumar dy a la coordenada y de la esquina superior
# izquierda. Haga las dos versiones, una función pura y una función modificadora.
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
    
class Rectangle:
    def __init__(self, width: float, height: float, corner: Point) -> None:
        self.width = width
        self.height = height
        self.corner = corner

    def __str__(self) -> str:
        return f"({str(self.width)}, {str(self.height)}, {str(self.corner)})"

    def __eq__(self, other: 'Rectangle') -> bool:
        return self.width == other.width and self.height == other.height and self.corner == other.corner

#funcion modificadora
def mover_rectangulo( rectang:Rectangle,dx:float,dy:float) -> None:
    # rectang.corner[0] = rectang.corner[0] + dx --esto no funciona porque no se puede modificar una tupla
    # rectang.corner[1] = rectang.corner[1] + dy -- entonces sobreescribo el valor
    rectang.corner = (rectang.corner[0] + dx, rectang.corner[1] + dy)
#funcion pura
def mover_rectangulo_pura( rectang:Rectangle,dx:float,dy:float) -> Rectangle:
    # rectang.corner[0] = rectang.corner[0] + dx --esto no funciona porque no se puede modificar una tupla
    # rectang.corner[1] = rectang.corner[1] + dy -- entonces sobreescribo el valor
    x = rectang.corner[0] + dx
    y = rectang.corner[1] + dy
    return Rectangle(rectang.width,rectang.height, (x,y))


a = Rectangle(10,5,(8,4))
b = Rectangle(10,5,(8,4))
#print(a)
#print(a==b)
c = Rectangle(10,5,(10,5))
#print(a==c)

d = Rectangle(4,6,(3,2))
print(mover_rectangulo_pura(d,2,2)) # devuelve otro rectangulo con los valores cambiados
mover_rectangulo(d,2,2) # modifica los valores del rectangulo d
print(d)



