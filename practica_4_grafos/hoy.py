#from typing import any

class Graph:
    def __init__ (self) ->None:
        self.nodes:set[any] =set()
        self.edges: set [tuple[any,any]] =set()
        self.adj: dict[any, set[any]] ={}
        self.degree: dict[any,int] = {}

    def add_nodes(self, node:any) -> None:
        self.nodes.add(node)

    def add_edge (self, node1: any, node2: any)->None:
        if not node1 in self.nodes:
             self.nodes.add(node1)
        if not node2 in self.nodes:
             self.nodes.add(node2)   
        self.edges.add((node1,node2))

R=Graph()
R.add_nodes("x") 
R.add_nodes("y")
R.add_nodes("z")

print(R.nodes)

R.add_edge("x","y")
R.add_edge("z","t")
print(R.edges)

print(R.nodes)





