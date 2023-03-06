import math

from semester2.data_structures.union_find import MyUnionFind
from semester2.data_structures.binom_heap import MyBinomialHeap


"""
INTRO:



PSEUDO-CODE FOR GENERAL ALGORITHM:

GENERIC-MST(GRAPH, WEIGHTS):
    A = EMPTY_GRAPH()
    WHILE A IS NOT SPANNING TREE:
        FIND (u,v) SAFE FOR A
        ADD (u,v) TO A
    RETURN A



PROOF OF CORRECTNESS:


"""


def get_edges_from_graph(graph: list):
    n = len(graph)
    edges = []
    for i in range(n):
        for j in range(n):
            if graph[i][j]:
                edges.append((i, j))
    return edges


def mst_kruskal(graph: list, weights: list):
    ret = []
    n = len(graph)
    union_finds = [MyUnionFind(i) for i in range(n)]
    edges = get_edges_from_graph(graph)
    edges.sort(key=lambda x: weights[x[0]][x[1]])
    for edge in edges:
        if union_finds[edge[0]].find() is not union_finds[edge[1]].find:
            ret.append(edge)
            union_finds[edge[0]].union(union_finds[edge[1]])


def mst_prim(graph: list, weights: list, root: int):
    n = len(graph)
    nodes_min_heap = MyBinomialHeap()
    nodes = []
    parents = [None for i in range(n)]
    for i in range(n):
        nodes.append(nodes_min_heap.insert(math.inf, i))
    nodes_min_heap.delete(nodes[root])
    nodes_min_heap.insert(0, root)
    while not nodes_min_heap.is_empty():
        new_node = nodes_min_heap.pop_min()[1]
        nodes[new_node] = None
        for i in range(n):
            if graph[new_node][i] and nodes[i] is not None and weights[new_node][i] < nodes[i].key:
                parents[i] = new_node
                nodes_min_heap.decrease_key(nodes[i], weights[new_node][i])
    return parents
