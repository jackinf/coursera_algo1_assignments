class Edge:
    def __init__(self, a: 'Vertex', b: 'Vertex'):
        a.edges.append(self)
        b.edges.append(self)
        self.a = a
        self.b = b

    def contract(self) -> 'Vertex':
        """
        https://en.wikipedia.org/wiki/Karger%27s_algorithm
        """

        # a node disappears (= merges into b)
        self.b.edges += self.a.edges
        while self in self.b.edges:
            self.b.edges.remove(self)

        return self.a

    def __str__(self):
        return f'{self.a}--{self.b}'

    def __repr__(self):
        return self.__str__()
