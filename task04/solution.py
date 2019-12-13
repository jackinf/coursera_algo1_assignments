import random
import copy
from typing import List, Dict, Tuple


class Node:
    def __init__(self, value: int):
        self.value = value
        self.nodes: List['Node'] = []

    def __str__(self):
        return f'[{self.value}]'

    def __repr__(self):
        return self.__str__()

    def add(self, node: 'Node'):
        self.nodes.append(node)

    def is_same(self, node: 'Node'):
        return self.value == node.value

    def change_to(self, node: 'Node'):
        self.value = node.value
        self.nodes = node.nodes


class KargerMinCutAlgo:
    """
    https://en.wikipedia.org/wiki/Karger%27s_algorithm
    """

    def run(self, nodes_input: List[Node], iterations: int) -> int:
        results = []
        for _ in range(iterations):
            nodes = copy.deepcopy(nodes_input)
            while len(nodes) > 2:
                source, target = self.step1_choose_random_edge(nodes)
                self.step2_copy_nodes_from_source_to_target(source, target)
                self.step3_replace_target_nodes_with_source_nodes(source, target)
                self.step4_remove_sources_selfloops(source)
                nodes = self.step5_remove_target_node(nodes, target)
            result = self.step6_get_min_cuts(nodes)
            results.append(result)
        return min(results)

    def step1_choose_random_edge(self, nodes: List[Node]) -> Tuple[Node, Node]:
        source: Node = random.choice(nodes)
        target = random.choice(source.nodes)
        return source, target

    def step2_copy_nodes_from_source_to_target(self, source: Node, target: Node):
        source.nodes += target.nodes

    def step3_replace_target_nodes_with_source_nodes(self, source: Node, target: Node):
        for target_node in target.nodes:
            for i in range(len(target_node.nodes)):
                if target_node.nodes[i].is_same(target):
                    target_node.nodes[i] = source

    def step4_remove_sources_selfloops(self, source: Node):
        source.nodes = [x for x in source.nodes if not x.is_same(source)]

    def step5_remove_target_node(self, nodes: List[Node], target) -> List[Node]:
        return list(filter(lambda x: not x.is_same(target), nodes))

    def step6_get_min_cuts(self, nodes: List[Node]):
        return len(nodes[0].nodes)


def collect_input() -> Dict[int, Node]:
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        first_values = [int(x.split(' ')[0]) for x in lines]
        unique_nodes: Dict[int, Node] = {x: Node(x) for x in first_values}

        # connect vertices between each-other
        for line in lines:
            items = [int(x) for x in line.split(' ')]
            target_node: Node = unique_nodes[items[0]]
            nodes = [unique_nodes[x] for x in items[1:]]
            for node in nodes:
                target_node.add(node)
        return unique_nodes


def progam():
    """
    test-case-0.txt: expected result: 2
    test-case-1.txt: expected result: 2, number of cuts are [(1,7), (4,5)]
    test-case-2.txt: expected result: 2, number of cuts are [(1,7), (4,5)]
    test-case-3.txt: expected result: 1, cut is [(4,5)]
    test-case-4.txt: expected result: 1, cut is [(4,5)]
    test-case-5.txt: expected result: 3 (actually, I think that it is 4)
    input.txt: expected result: 17      P.S: in case of , it will run for awhile - about 10-15 sec
    """

    nodes_dict = collect_input()
    nodes = list(nodes_dict.values())
    result = KargerMinCutAlgo().run(nodes, 10)
    print(result)


progam()