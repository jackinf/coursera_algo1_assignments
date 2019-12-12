from typing import List, Union

from task04.edge import Edge


class Vertex:
    def __init__(self, value: int):
        self.value = value
        self.edges: List[Edge] = []

    def connect(self, other: 'Vertex') -> Union[Edge, None]:
        if self.check_if_connected(other):
            return None
        return Edge(self, other)

    def check_if_connected(self, other: 'Vertex'):
        for other_edge in other.edges:
            if other_edge.a.value == self.value or other_edge.b.value == self.value:
                return True
        return False

    def __str__(self):
        return f'[{self.value}]'

    def __repr__(self):
        return self.__str__()
