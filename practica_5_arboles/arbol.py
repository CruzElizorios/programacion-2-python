from typing import Any, Self, Optional

class BinaryTree:
    """Arbol binario."""

    def __init__(self: Self, data: Any, left: Optional[Self] = None, right: Optional[Self] = None) -> None:
        self.data = data
        self.left = left
        self.right = right

    def __str__(self: Self) -> str:
        """Devuelve la representacion del dato almacenado, como una cadena."""
        return str(self.data)

    def is_complete(self: Self) -> bool:
        """Determina si es un arbol binario completo."""
        if self.left == None and self.right == None:
            return True

        if self.left != None and self.right != None:
            return self.left.is_complete() and self.right.is_complete()
        
        return False
 

    def __contains__(self: Self, data: Any) -> bool:
        """Determina si el arbol almacena el elemento 'data'. sobreescribe el in"""
        print(self.data, data)
        if self.data == data:
            return True
        # if self.left != None and self.right != None:
        #     self.left.__contains__(data)
        #     self.right.__contains__(data)
        # if self.left == None and self.right != None:
        #     self.right.__contains__(data)
        # if self.left != None and self.right == None:
        #     print("entre izquierdo")
        #     #print(self.data,data)
        #     self.left.__contains__(data)
        # if self.left == None and self.right.__contains__(data):
        #     print("lo encontre")
        #     return
        
        # if self.left.__contains__(data)  and self.right == None:
        #     print(f"lo encontre por izquierda {self.data, data}")
        #     return True
        if self.left != None:
            self.left.__contains__(data)
        if self.right != None:
            self.right.__contains__(data)

        return False



    def max(self: Self) -> Any:
        """Devuelve el elemento maximo del arbol."""

    def min(self: Self) -> Any:
        """Devuelve el elemento minimo del arbol."""

    def height(self: Self) -> int:
        """Devuelve la altura del arbol."""

    def is_balanced(self: Self) -> bool:
        """Determina si es un arbol binario balanceado."""

    def __len__(self: Self) -> int:
        """Devuelve la cantidad de datos almacenados en el arbol."""

def copy(tree: BinaryTree) -> BinaryTree:
    """Devuelve una copia de un arbol."""

def preOrder(tree: BinaryTree, f: callable) -> None:
    """Aplica la funcion 'f' a todos los elementos del arbol, siguiendo un
    recorrido pre-orden."""
    if tree == None:
        return
    f(tree)
    preOrder(tree.left,f)
    preOrder(tree.right,f)


def inOrder(tree: BinaryTree, f: callable) -> None:
    """Aplica la funcion 'f' a todos los elementos del arbol, siguiendo un
    recorrido in-orden."""

def postOrder(tree: BinaryTree, f: callable) -> None:
    """Aplica la funcion 'f' a todos los elementos del arbol, siguiendo un
    recorrido post-orden."""

class BSTree(BinaryTree):
    """Arbol binario de busqueda."""

    def __contains__(self: Self, data: Any) -> bool:
        """Determina si el arbol almacena el elemento 'data'."""

    def max(self: Self) -> Any:
        """Devuelve el elemento maximo del arbol."""

    def min(self: Self) -> Any:
        """Devuelve el elemento minimo del arbol."""

    def insert(self: Self, data: Any) -> None:
        """Inserta el elemento 'data' en el lugar correspondiente."""

# Dibuje el siguiente arbol:
i1 = BinaryTree(3)
i5 = BinaryTree(4)
i6 = BinaryTree(5)
i4 = BinaryTree(5, i5, i6)
i3 = BinaryTree(7, i4)
i2 = BinaryTree(9, i3)
izquierda = BinaryTree(4, i1, i2)

d1 = BinaryTree(15)
d5 = BinaryTree(17)
d2 = BinaryTree(20)
d4 = BinaryTree(16, d5)
d3 = BinaryTree(18, d4, d2)
derecha = BinaryTree(15, d1, d3)

raiz = BinaryTree(14, izquierda, derecha)

#print(d3.is_complete())
print(7 in i2)
# preOrder(raiz,print)

# Cree un arbol binario de busqueda identico al anterior utilizando el metodo
# insert.
bst = BSTree(14)

# Complete el arbol del mundial 2022.
octavos1 = BinaryTree(("Holanda", "USA"))
octavos2 = BinaryTree(("Argentina", "Australia"))
octavos3 = BinaryTree(("Japon", "Croacia"))
octavos4 = BinaryTree(("Brasil", "Corea"))
octavos5 = BinaryTree(("Inglaterra", "Senegal"))
octavos6 = BinaryTree(("Francia", "Polonia"))
octavos7 = BinaryTree(("Marruecos", "España"))
octavos8 = BinaryTree(("Portugal", "Suiza"))
