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


def collect_input() -> Dict[int, Vertex]:
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
                target.connect(vertex)
        return unique_vertices


def get_all_edges(all_vertices: Dict[int, Vertex]) -> List[Edge]:
    all_edges = []
    for k, v in all_vertices.items():
        all_edges += v.edges
    return all_edges


def build_graph(g: nx.Graph, vertices: Dict[int, Vertex]):
    edges_arg: List[Edge] = get_all_edges(vertices)
    for edge in edges_arg:
        g.add_edge(edge.a, edge.b)


def draw(vertices: Dict[int, Vertex], **kwargs):
    g = nx.Graph()

    build_graph(g, vertices)

    if "contract" in kwargs and kwargs["contract"] is True:
        edges_arg = get_all_edges(vertices)
        chosen_edge = next(x for x in edges_arg if x.a.value == 7 and x.b.value == 1 or x.a.value == 1 and x.b.value == 7)

        vertex_to_remove = chosen_edge.contract()
        g.remove_edge(chosen_edge.a, chosen_edge.b)

        vertices.pop(vertex_to_remove.value)
        g.remove_node(vertex_to_remove)

    nx.draw(g, with_labels=True)
    plt.show()


def update_and_draw(vertices: Dict[int, Vertex]):
    plt.ion()
    g = nx.Graph()

    build_graph(g, vertices)

    while True:
        edges_arg: List[Edge] = get_all_edges(vertices)

        chosen_edge = random.choice(edges_arg)
        chosen_edge.contract()
        edges_arg.remove(chosen_edge)
        g.remove_edge(chosen_edge.a, chosen_edge.b)

        nx.draw(g, with_labels=True)
        plt.pause(3)
        plt.clf()
        plt.show()


vertices = collect_input()
print(vertices)
edges = get_all_edges(vertices)
print(edges)
draw(vertices)
draw(vertices, contract=True)
# update_and_draw(edges)
