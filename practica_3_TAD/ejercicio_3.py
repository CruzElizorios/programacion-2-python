# Ejercicio 3
# Escribir una función que recibe una expresión matemática (en forma de cadena) y devuelve True si los
# paréntesis (), corchetes [] y llaves {} están correctamente balanceados, False en caso contrario.
# Nota: Una secuencia de caracteres está correctamente balanceada con respecto a los paréntesis (),
# corchetes [] y llaves {} si el número de aperturas de cada símbolo coincide con el de cierre y además
# se cierran en el orden correcto.
# Ejemplos:
# validar('(x+y)/2') -> True
# validar('[8*4(x+y)]+{2/5}') -> True
# validar('(x+y]/2') -> False
# validar('1+)2(+3') -> False

class Pila():
    def __init__(self) -> None:
        self.datos = []
    
    def push(self,lista):
        self.datos.append(lista)
        print(self.datos)

    def pop(self):
        return self.datos.pop()

    def is_empty(self) -> bool:
        """verifica que la pila no se este vacia"""
        return self.datos == []

def validar(cadena:str) -> bool:
    p = Pila()
    for letra in cadena:
        if letra in ["(", "{","["]: #["(", ")", "{", "}","[", "]"]
            p.push(letra)
        elif letra == ")":    # [ "[", "("  ]
            if "(" == p.pop():
                pass
        elif letra == "}":
                if "(" p.pop()
                    pass
        elif letra == "]":
                if "(" p.pop()
                    pass

    return p.is_empty()

validar("[(a+b)]")
             