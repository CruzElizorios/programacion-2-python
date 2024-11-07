from typing import Any, Self, Optional
import copy

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
        #print(self.data, data)
        if self.data == data:
            return True
        if self.left != None:
            if self.left.__contains__(data):
                return True
            
        if self.right != None:
            if self.right.__contains__(data):
                return True
            
        return False



    def max(self: Self) -> Any:
        """Devuelve el elemento maximo del arbol."""
        if self.data == None:
            return 
        leftmax = 0
        rightmax = 0
        
        if self.left != None:
            leftmax = self.left.max()
            #leftmax = max(self.data,self.left.max())
        if self.right != None:
            # rightmax = max(self.data,self.right.max())
            rightmax = self.right.max()
        
        return max(self.data,leftmax,rightmax)

    def min(self: Self) -> Any:
        """Devuelve el elemento minimo del arbol."""
        if self.data == None:
            return 
        leftmin = self.data
        rightmin = self.data
        
        if self.left != None:
            leftmin = self.left.min()
            #leftmax = max(self.data,self.left.max())
        if self.right != None:
            # rightmax = max(self.data,self.right.max())
            rightmin = self.right.min()
        
        return min(self.data,leftmin,rightmin)

    def height(self: Self) -> int:
        """Devuelve la altura del arbol."""
        left_height = 0
        right_height = 0
        #si es hoja altura cero
        if self.left == None and self.right == None:
            return 0
        #calculo la altura de los subárboles izquierdo y derecho
        if self.left != None:
            left_height = 1 + self.left.height()
            
        if self.right != None:
            right_height = 1 + self.right.height()
        
        return max(left_height,right_height) 

    def is_balanced(self: Self) -> bool:
        """Determina si es un arbol binario balanceado."""

    def __len__(self: Self) -> int:
        """Devuelve la cantidad de datos almacenados en el arbol."""

def copia(tree: BinaryTree) -> BinaryTree:
    """Devuelve una copia de un arbol. Debe importar el modulo copy, escribir: import copy"""
    return copy.deepcopy(tree)

def copiaV2(tree: BinaryTree) -> BinaryTree:
    """Devuelve una copia de un arbol."""
    if tree is None:
        return None
    new_tree = BinaryTree(tree.data)
    new_tree.left = copiaV2(tree.left)
    new_tree.right = copiaV2(tree.right)

    return new_tree

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
    if tree == None:
        return
    inOrder(tree.left,f)
    f(tree)
    inOrder(tree.right,f)

def postOrder(tree: BinaryTree, f: callable) -> None:
    """Aplica la funcion 'f' a todos los elementos del arbol, siguiendo un
    recorrido post-orden."""
    if tree == None:
        return
    postOrder(tree.left,f)
    postOrder(tree.right,f)
    f(tree)

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
# Verificación de funcionamiento correcto de los métodos:
#print(d3.is_complete())

# print(7 in i2)
# preOrder(i2,print)

# print("valor max:",izquierda.max())
# print("valor min:",izquierda.min())
# print("arbol 'izquierda' abajo")
# preOrder(izquierda,print)

# print("altura:",raiz.height())
# preOrder(raiz,print)

# nuevoArbol= copia(i3) # raiz 7, hijo izq: 5 -> hijo izq:4 hijo der:5
# nuevoArbol.left.data = 33
# preOrder(i3,print) # como i3 no se modifico, significa que la copia se realizo correctamente
# print("copia abajo") # ya que apuntan a espacios de memorias distintos
# preOrder(nuevoArbol,print) # raiz 7, hijo izq: 33 -> hijo izq:4 hijo der:5

nuevoTree = copiaV2(i3)
nuevoTree.left.data = 26
preOrder(i3,print)
print("copia abajo")
preOrder(nuevoTree,print)

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
