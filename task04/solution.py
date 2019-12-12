import random

import networkx as nx
import matplotlib.pyplot as plt
from typing import Dict, List

from task04.edge import Edge
from task04.vertex import Vertex

# test case 1: expected result: 2, number of cuts are [(1,7), (4,5)]
# test case 2: expected result: 2, number of cuts are [(1,7), (4,5)]
# test case 3: expected result: 1, cut is [(4,5)]
# test case 4: expected result: 1, cut is [(4,5)]
# test case 5: expected result: 3


def collect_input():
    edges = []
    with open('task04/test-case-1.txt', 'r') as f:
        lines = f.readlines()
        first_values = [int(x.split(' ')[0]) for x in lines]
        unique_vertices: Dict[int, Vertex] = {x: Vertex(x) for x in first_values}

        # connect vertices between each-other
        for line in lines:
            items = [int(x) for x in line.split(' ')]
            target: Vertex = unique_vertices[items[0]]
            vertices = [unique_vertices[x] for x in items[1:]]
            for vertex in vertices:
                edge = target.connect(vertex)
                if edge is not None:
                    edges.append(edge)
    return edges


def draw(edges_arg, **kwargs):
    g = nx.Graph()
    for edge in edges_arg:
        g.add_edge(edge.a, edge.b)

    if "contract" in kwargs and kwargs["contract"] is True:
        chosen_edge = next(x for x in edges_arg if x.a.value == 7 and x.b.value == 1 or x.a.value == 1 and x.b.value == 7)
        chosen_edge.contract()
        edges_arg.remove(chosen_edge)
        g.remove_edge(chosen_edge.a, chosen_edge.b)

    nx.draw(g, with_labels=True)
    plt.show()


def update_and_draw(edges_arg: List[Edge]):
    plt.ion()
    g = nx.Graph()
    for edge in edges_arg:
        g.add_edge(edge.a, edge.b)
    while True:
        chosen_edge = random.choice(edges_arg)
        chosen_edge.contract()
        edges_arg.remove(chosen_edge)
        g.remove_edge(chosen_edge.a, chosen_edge.b)

        nx.draw(g, with_labels=True)
        plt.pause(3)
        plt.clf()
        plt.show()


edges = collect_input()
print(edges)
draw(edges)
draw(edges, contract=True)
# update_and_draw(edges)




