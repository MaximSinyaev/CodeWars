""""
Description:
The class Graph represents an undirected graph of vertices named 0 through
V - 1. It supports 2 primary operations:

    add an edge to the graph
    iterate over all of the vertices adjacent to a vertex.

And provides a way for returning the number of vertices V and the number of
edges E. Parallel edges and self-loops are permitted. Self-loop v-v appears in
the adjacency list of v twice.
"""


class IllegalArgumentError(Exception):
    pass


class Graph:
    def __init__(self, v):
        # Initialize an empty graph with v vertices(V) and 0 edges(E).
        # Raise IllegalArgumentError unless 0 <= v
        self.V = v
        self.E = 0
        self.adj = [[] for _ in range(v)]

    def add_edge(self, v, w):
        # Add the undirected edge v-w to this graph.
        # Raise IllegalArgumentError unless both 0 <= v < V and 0 <= w < V
        if not (0 <= v < self.V) or not (0 <= w < self.V):
            raise IllegalArgumentError
        self.adj[v].append(w)
        self.adj[w].append(v)
        self.E += 1


if __name__ == "__main__":
    z = Graph(3)
    z.add_edge(2, 2)
    z.add_edge(0, 1)

    # Test.assert_equals(z.V, 3)
    # Test.assert_equals(z.E, 2)
    # Test.assert_equals(z.adj, [[1], [0], [2, 2]])
