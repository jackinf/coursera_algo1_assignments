import random

import networkx as nx
import matplotlib.pyplot as plt
from typing import Dict


class Vertex:
    def __init__(self, value: int):
        self.value = value
        self.vertices = []

    def connect(self, vertex: 'Vertex'):
        self.vertices.append(vertex)
        vertex.vertices.append(self)

    def disconnect(self, vertex):
        for next_vertex in vertex.vertices:
            # if vertex in next_vertex.vertices:
            next_vertex.vertices.remove(vertex)
        # if self in vertex.vertices:
        vertex.vertices.remove(self)

    # https://en.wikipedia.org/wiki/Karger%27s_algorithm
    def contract(self):
        if len(self.vertices) == 0:
            print('Cannot contract - no connections')
            return

        target = random.choice(self.vertices)
        next_vertices = target.vertices
        self.disconnect(target)
        for next_vertex in next_vertices:
            if next_vertex not in self.vertices:
                self.vertices.append(next_vertex)


    def __str__(self):
        return f'[{self.value}]'

    def __repr__(self):
        return self.__str__()


with open('coursera-algo-task4.txt', 'r') as f:
    lines = f.readlines()
    first_values = [int(x.split('\t')[0]) for x in lines]
    unique_vertices: Dict[int, Vertex] = {x: Vertex(x) for x in first_values}

    # connect vertices between each-other
    for line in lines:
        items = [int(x) for x in line.split('\t')]
        target: Vertex = unique_vertices[items[0]]
        vertices = [unique_vertices[x] for x in items[1:]]
        for vertex in vertices:
            target.connect(vertex)

plt.ion()
while True:
    g = nx.Graph()

    chosen = random.choice(unique_vertices)
    chosen.contract()
    for k, vs in unique_vertices.items():
        server_id = 'server_%s' % k

        for v in vs.vertices:
            g.add_edge(server_id, v)

    nx.draw(g)
    plt.pause(0.1)
    plt.clf()
    plt.show()
