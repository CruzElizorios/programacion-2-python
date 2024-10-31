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
        self.degree[node1] = self.degree.get(node1, 0) + 1
        self.degree[node2] = self.degree.get(node2, 0) + 1

    def __str__(self: Self) -> str:
        """Devuelve una cadena el nombre, vertices y aristas del grafo."""
        return f"Nombre: {self.name}\n"     \
               f"Vertices: {self.nodes}.\n" \
               f"Aristas: {self.edges}."

    def __eq__(self: Self, other: object) -> bool:
        """Determina si dos grafos son iguales."""

    def __le__(self: Self, other: Self) -> bool:
        """Determina si el grafo es subgrafo de otro."""

    def is_regular(self: Self) -> bool:
        """Determina si el grafo es k-regular, para algun k."""

    def is_eulerian(self: Self) -> bool:
        """Determina si el grafo tiene un circuito euleriano."""

    def is_complete(self: Self) -> bool:
        """Deterima si es un grafo completo."""

    def remove_node(self: Self, node: Any) -> None:
        """Elimina un vertice del grafo."""

    def remove_edge(self: Self, node1: Any, node2: Any) -> None:
        """Elimina la arista (node1, node2) del grafo."""

    def adjacency(self: Self) -> list[list[int]]:
        """Devuelve la matriz de adyacencia que representa el grafo."""

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

# Defina el grafo completo K5.
k5: Graph = Graph("K5")
print(k5)

# Defina el grafo bipartito K3,3.
k33: Graph = Graph("K3,3")
print(k33)

# Defina el grafo de Petersen.
# https://es.wikipedia.org/wiki/Grafo_de_Petersen
petersen: Graph = Graph("Petersen")
print(petersen)
