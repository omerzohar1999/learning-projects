from linked_list import MyLinkedList


class Edge:
    def __init__(self, src: int, dst: int, weight: int):
        self.src = src
        self.dst = dst
        self.weight = weight


class Graph:
    def __init__(self, num_of_nodes: int):
        self.n = num_of_nodes
        self.edges = [MyLinkedList() for i in range(self.n)]

    def add_edge(self, i: int, j: int, w: int, is_directed: bool):
        new_edge = Edge(i, j, w)
        self.edges[i].insert_last(new_edge)
        if not is_directed:
            self.edges[j].insert_last(new_edge)

    def remove_edge(self):
        pass  # TODO
