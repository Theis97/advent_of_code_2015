class Graph:
    """A basic implementation of a weighted graph."""
    def __init__(self):
        self.graph: dict[str, dict[str, int]] = {}

    def add_vertex(self, label: str) -> None:
        self.graph[label] = {}

    def add_edge(self, from_vertex: str, to_vertex: str, weight: int) -> None:
        self.graph[from_vertex][to_vertex] = weight
