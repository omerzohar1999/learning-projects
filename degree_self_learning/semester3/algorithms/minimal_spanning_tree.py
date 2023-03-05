from semester2.data_structures.union_find import MyUnionFind
from semester2.data_structures.fib_heap import MyFibHeap

INF = -1

"""
INTRO


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


"""
PROOF OF CORRECTNESS FOR KRUSKAL
"""


def mst_prim(graph: list, weights: list, root: int):
    pass


"""
PROOF OF CORRECTNESS FOR PRIM
"""