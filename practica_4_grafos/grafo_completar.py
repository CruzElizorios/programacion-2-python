from typing import Any, Self

class Graph:
    def __init__(self: Self, name: str = "") -> None:
        self.name: str = name
        self.nodes: set[Any] = set()
        self.edges: set[tuple[Any, Any]] = set()
        self.adj: dict[Any, set[Any]] = {}
        self.degree: dict[Any, int] = {}
        self.weight: dict[tuple[Any, Any], int] = {}

    def add_node(self: Self, node: Any) -> None:
        """Agrega un vertice aislado al grafo."""
        self.nodes.add(node)
        # setdefault agrega al diccionario una clave y un valor si la clave no existe
        self.adj.setdefault(node, set())
        self.degree.setdefault(node, 0)

    def add_edge(self: Self, node1: Any, node2: Any, weight: int = 0) -> None:
        """Agrega la arista (node1, node2) al grafo."""
        self.add_node(node1)
        self.add_node(node2)
        self.edges.add((node1, node2))
        self.weight[(node1, node2)] = weight
        self.adj[node1].add(node2)
        self.adj[node2].add(node1)
        # .get() devuelve el valor para una clave, el segundo
        # parametro es para devolver un valor si no existe la clave 
        # get(<key>, <default_valor>)
        self.degree[node1] = self.degree.get(node1, 0) + 1
        self.degree[node2] = self.degree.get(node2, 0) + 1

    def __str__(self: Self) -> str:
        """Devuelve una cadena el nombre, vertices y aristas del grafo."""
        return f"Nombre: {self.name}\n"     \
               f"Vertices: {self.nodes}.\n" \
               f"Aristas: {self.edges}."

    def __eq__(self: Self, other: object) -> bool:
        """Determina si dos grafos son iguales."""
        # primero me fijo que tengan la misma cantidad de nodos y aristas,
        # Si no cumple => no son iguales
        if len(self.nodes) == len(other.nodes) and len(self.edges) == len(other.edges):
            
            for nodo in self.nodes:
                # si el nodo no está dentro del otro grafo
                if nodo not in other.nodes:
                    return False
            for arista in self.edges:
                # si la arista no está dentro del otro grafo
                if arista not in other.edges:
                    return False
            return True
                    
        return False


    def __le__(self: Self, other: Self) -> bool:
        """Determina si el grafo es subgrafo de otro. sobreescribe el operador <= """
        # para que el grafo actual sea subgrafo de Otro, self debe estar contenido en Otro
        
        # primer codigo
        # for nodo in self.nodes:
        #     # si el nodo no está dentro del otro grafo
        #     if nodo not in other.nodes:
        #         return False
        # for arista in self.edges:
        #     # si la arista no está dentro del otro grafo
        #     if arista not in other.edges:
        #         return False
        # return True
        
        #El método .issubset() verifica si todos los elementos de un conjunto (set) están contenidos en otro conjunto
        return self.nodes.issubset(other.nodes) and self.edges.issubset(other.edges)

    def is_regular(self: Self) -> bool:
        """Determina si el grafo es k-regular, para algun k."""
        # grafo regular: es un grafo en el que cada vértice tiene el mismo número de vecinos;
        # es decir, cada vértice tiene el mismo grado
        
        # for nodo in self.nodes:
        #     for nodo2 in self.nodes:
        #         if self.degree[nodo] != self.degree[nodo2]:
        #             return False
        # return True

        # tomo los valores de los grados
        grados = list(self.degree.values())
        for grado in grados:
            # comparo el primer valor con cada uno de los valores de los grados
            # si no son iguales significa que no es regular
            if grados[0] != grado:
                return False
        return True

    def is_eulerian(self: Self) -> bool:
        """Determina si el grafo tiene un circuito euleriano."""
        # es un ciclo cerrado que recorre cada arista exactamente una vez.
        # el grafo debe ser conexo y todos los nodos deben tener grado par.
        
        # verifico que el grado sea par
        for grado in self.degree.values():
            if grado % 2 != 0:
                return False
        # falta verificar que es conexo
        return True
         

    def is_complete(self: Self) -> bool:
        """Deterima si es un grafo completo."""
        # para ser completo el grado de todos los nodos debe ser n-1,
        # donde n es la cantidad de nodos

        cant_nodos = len(self.nodes)
        for grado in self.degree.values():
            if grado != cant_nodos - 1:
                return False
        return True

    def remove_node(self: Self, node: Any) -> None:
        """Elimina un vertice del grafo."""
        if node in self.nodes:
            self.nodes.remove(node)
            # no puedo modificar el conjunto y recorrerlo al mismo tiempo,
            # por eso creo una lista de las aristas
            
            lista_aristas = list(self.edges)
            for arista in lista_aristas:
                if arista[0] == node or arista[1] == node:
                    self.edges.remove(arista)
            
            self.adj.pop(node,None)
            self.degree.pop(node,None)
            # se actualizan los nodos adyacentes
            for nodo in self.adj:
                # similar al remove(elemento) pero si no está => no da error
                self.adj[nodo].discard(node)
                self.degree[nodo] = len(self.adj[nodo])
            
            # elimino las aristas con pesos que contengan a 'node'
            lista_aristas_pesos = list(self.weight) # solo me quedo con las claves
            for arista in lista_aristas_pesos:
                if arista[0] == node or arista[1] == node:
                    self.weight.pop(arista) 

    def remove_edge(self: Self, node1: Any, node2: Any) -> None:
        """Elimina la arista (node1, node2) del grafo."""
        arista = (node1,node2)
        arista2 = (node2,node1)
        if arista in self.edges or arista2 in self.edges:
            self.edges.discard(arista)
            self.edges.discard(arista2)
        
        # borro las aristas con pesos
        lista_aristas_pesos = list(self.weight) # solo me quedo con las claves
        for arista_p in lista_aristas_pesos:
            if arista_p == arista or arista_p == arista2:
                self.weight.pop(arista, None)
                self.weight.pop(arista2,None)
        # actualizo vecinos
        if node1 in self.adj and node2 in self.adj[node1]:
            self.adj[node1].remove(node2)
        if node2 in self.adj and node1 in self.adj[node2]:
            self.adj[node2].remove(node1)
        # actualizo grados
        for nodo in self.adj:
            self.degree[nodo] = len(self.adj[nodo])

    def adjacency(self: Self) -> list[list[int]]:
        """Devuelve la matriz de adyacencia que representa el grafo."""
        matriz_adj = []
        contador = 0
        for nodo_adj in self.adj.keys():
            matriz_adj.append([])
            
            for nodo in self.nodes:
                if nodo in self.adj[nodo_adj]:
                    matriz_adj[contador].append(1)
                else:
                    matriz_adj[contador].append(0)
            contador += 1
        return matriz_adj

    def incidence(self: Self) -> list[list[int]]:
        """Devuelve la matriz de incidencia que representa el grafo."""

    def induced(self: Self, nodes: set[Any]) -> Self:
        """Devuelve el grafo inducido por el conjunto de vertices nodes."""

    def complement(self: Self) -> Self:
        """Devuelve el grafo complemento."""

    def dijkstra(self: Self, a: Any, z: Any) -> list[tuple[Any, Any]]:
        """Si el grafo es conexo y tiene pesos no negativos en las aristas,
           devuelve el camino de menor peso desde node1 hasta node2.

           Tenga en cuenta que la arista (x, y) debe ser considerada en
           ambos sentidos."""
        

# Grafo completo K2
k2: Graph = Graph("K2")
k2.add_edge(1, 2)
print(k2)

# Grafo completo K3
k3: Graph = Graph("K3")
k3.add_edge(1, 2)
k3.add_edge(2, 3)
k3.add_edge(3, 1)
print(k3)
print(5 in k3.nodes)

h2: Graph = Graph("h2")
h2.add_edge(1, 2)
h2.add_edge(2, 3)
h2.add_edge(3, 1)
h2.add_edge(3, 4)
print(h2)

h6: Graph = Graph("h6 copia de k3")
h6.add_edge(1, 2)
h6.add_edge(2, 3)
h6.add_edge(3, 1)
print(h6)
# # comprobando método __eq__()
# print("k3 es igual a h6:",k3 == h6)
# # comprobando método __le__()
# print("k2 es subgrafo h6:",k2 <= h6)
# # comprobando método is_regular()
# print("k3 es regular:", k3.is_regular())
# print("h2 es regular:", h2.is_regular())
# # comprobando método is_complete()
# print("k3 es completo:", k3.is_complete())
# print("h2 es completo:", h2.is_complete())
# comprobando método remove_node()
#print("borrando nodo 2 de h2:", h2.remove_node(2))
# comprobando método remove_edge()
print("borrando nodo 2 de h2:", h2.remove_edge(1,2))
print(k3.adjacency())


# # Defina el grafo completo K5.
# k5: Graph = Graph("K5")
# print(k5)

# # Defina el grafo bipartito K3,3.
# k33: Graph = Graph("K3,3")
# print(k33)

# Defina el grafo de Petersen.
# https://es.wikipedia.org/wiki/Grafo_de_Petersen
# petersen: Graph = Graph("Petersen")
# print(petersen)
