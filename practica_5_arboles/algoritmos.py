from typing import Any
import networkx as nx
import matplotlib.pyplot as plt

def plot_graph(G: nx.Graph) -> None:
    """Dibuja un grafo en la pantalla."""
    edge_labels = { (u,v) : d.get('weight', '') for u,v,d in G.edges(data=True) }

    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    nx.draw(G, pos, edge_cmap=plt.cm.Reds)

    plt.axis('off')
    plt.show()

def nearest_neighbour(G: nx.Graph) -> list[Any]:
    """Devuelve un recorrido hamiltoniano."""

def kruskal(G: nx.Graph) -> nx.Graph:
    """Dado un grafo conexo, devuelve un arbol recubridor minimo.
    Tenga en cuenta la función has_path del modulo nx."""

def prim(G: nx.Graph) -> nx.Graph:
    """Dado un grafo conexo, devuelve un arbol recubridor minimo.
    Tenga en cuenta la función has_path del modulo nx."""

def dijkstra(G: nx.Graph, a: Any, z: Any) -> list[tuple[Any, Any]]:
    """Si el grafo es conexo y tiene pesos no negativos en las aristas,
       devuelve el camino de menor peso desde a hasta z."""

g1 = nx.Graph()
g1.add_edge("A", "C", weight=5)
g1.add_edge("A", "B", weight=3)
g1.add_edge("B", "D", weight=4)
g1.add_edge("C", "D", weight=12)
g1.add_edge("D", "E", weight=9)
g1.add_edge("D", "H", weight=8)
g1.add_edge("E", "H", weight=1)
g1.add_edge("E", "G", weight=5)
g1.add_edge("E", "F", weight=4)
g1.add_edge("F", "G", weight=6)
g1.add_edge("H", "G", weight=20)
