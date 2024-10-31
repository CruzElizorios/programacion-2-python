from typing import Any, Self, Optional

class BinaryTree:
    """Árbol binario."""

    def __init__(self: Self, data: Any, left: Optional[Self] = None,
                 right: Optional[Self] = None) -> None:
        self.data = data
        self.left = left
        self.right = right

    def __str__(self: Self) -> str:
        """Devuelve la representacion del dato almacenado, como una cadena."""
        return str(self.data)

    def is_complete(self: Self) -> bool:
        """Determina si es un árbol binario completo."""

    def __contains__(self: Self, data: Any) -> bool:
        """Determina si el árbol almacena el elemento 'data'."""

    def max(self: Self) -> Any:
        """Devuelve el elemento maximo del árbol."""

    def min(self: Self) -> Any:
        """Devuelve el elemento minimo del árbol."""

    def height(self: Self) -> int:
        """Devuelve la altura del árbol."""

    def is_balanced(self: Self) -> bool:
        """Determina si es un árbol binario balanceado."""

    def __len__(self: Self) -> int:
        """Devuelve la cantidad de datos almacenados en el árbol."""

    def reflex(self: Self) -> None:
        """Refleja el árbol con respecto a la raíz."""

def preOrder(tree: BinaryTree, f: callable) -> None:
    """Aplica la funcion 'f' a todos los elementos del árbol, siguiendo un
    recorrido pre-orden."""

def inOrder(tree: BinaryTree, f: callable) -> None:
    """Aplica la funcion 'f' a todos los elementos del árbol, siguiendo un
    recorrido in-orden."""

def postOrder(tree: BinaryTree, f: callable) -> None:
    """Aplica la funcion 'f' a todos los elementos del árbol, siguiendo un
    recorrido post-orden."""

def copy(tree):
    """Devuelve una copia de un árbol."""

class BSTree(BinaryTree):
    """Árbol binario de búsqueda."""

    def __contains__(self: Self, data: Any) -> bool:
        """Determina si el árbol almacena el elemento 'data'."""

    def max(self: Self) -> Any:
        """Devuelve el elemento maximo del árbol."""

    def min(self: Self) -> Any:
        """Devuelve el elemento minimo del árbol."""

    def insert(self: Self, data: Any) -> None:
        """Inserta el elemento 'data' en el lugar correspondiente."""

    def __add__(self: Self, other: Self) -> Self:
        """Devuelve un nuevo árbol binario de búsqueda,
        con el contenido de ambos."""

# Dibuje el siguiente arbol:
i1 = BinaryTree(3)
i5 = BinaryTree(5)
i6 = BinaryTree(6)
i4 = BinaryTree(6, i5, i6)
i3 = BinaryTree(7, i4)
i2 = BinaryTree(9, i3)
izquierda = BinaryTree(4, i1, i2)

d1 = BinaryTree(17)
d5 = BinaryTree(31)
d2 = BinaryTree(41)
d4 = BinaryTree(29, None, d5)
d3 = BinaryTree(33, d4, d2)
derecha = BinaryTree(20, d1, d3)

raiz = BinaryTree(12, izquierda, derecha)

# Cree un arbol binario de busqueda identico al anterior utilizando el metodo
# insert.
bst = BSTree(12)

# Complete el arbol del mundial 2022.
octavos1 = BinaryTree(("Holanda", "USA"))
octavos2 = BinaryTree(("Argentina", "Australia"))
octavos3 = BinaryTree(("Japon", "Croacia"))
octavos4 = BinaryTree(("Brasil", "Corea"))
octavos5 = BinaryTree(("Inglaterra", "Senegal"))
octavos6 = BinaryTree(("Francia", "Polonia"))
octavos7 = BinaryTree(("Marruecos", "España"))
octavos8 = BinaryTree(("Portugal", "Suiza"))
