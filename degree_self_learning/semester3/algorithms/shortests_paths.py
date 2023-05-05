from graph_scan import topological_sort
from semester2.data_structures.binom_heap import MyBinomialHeap
from semester2.data_structures.linked_list import MyLinkedList


def initialize_sssp(n: int, s: int):
    d = [float('inf') for i in range(n)]
    pi = [None for i in range(n)]
    d[s] = 0
    return d, pi


def b_f_relax(i: int, j: int, weights: list, d: list, pi: list):
    if d[j] is None or weights[i][j] < d[j]:
        d[j] = weights[i][j]
        pi[j] = i


def bellman_ford(graph: list, weights: list, s: int):
    n = len(graph)
    d, pi = initialize_sssp(n, s)
    for iteration in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][j]:
                    b_f_relax(i, j, weights, d, pi)
    for i in range(n):
        for j in range(n):
            if d[j] > d[i] + weights[i][j]:
                return False, [], []
    return True, d, pi


def bellman_ford_dag(graph: list, weights: list, s: int):
    n = len(graph)
    d, pi = initialize_sssp(n, s)
    ll = topological_sort(graph)
    ptr = ll.head
    while ptr:
        while ptr.value != s:
            ptr = ptr.next
        node = ptr.value
        for target in range(n):
            if graph[node][target]:
                b_f_relax(node, target, weights, d, pi)
        ptr = ptr.next
    return True, d, pi


def dijkstra_add_nodes(
        graph: list, weights: list, d: list, pi: list, i: int, priority_queue: MyBinomialHeap, heap_nodes: list
):
    for j in range(len(graph[i])):
        if graph[i][j]:
            path_len = d[i] + weights[i][j]
            if path_len < d[j]:
                if heap_nodes[j]:
                    priority_queue.decrease_key(heap_nodes[j], path_len)
                else:
                    heap_nodes[j] = priority_queue.insert(path_len, j)
                pi[j] = i


def dijkstra(graph: list, weights: list, s: int):
    priority_queue = MyBinomialHeap()
    n = len(graph)
    d, pi = initialize_sssp(n, s)
    heap_nodes = [None for i in range(n)]
    dijkstra_add_nodes(graph, weights, d, pi, s, priority_queue, heap_nodes)
    while not priority_queue.is_empty():
        new_node = priority_queue.pop_min()
        dijkstra_add_nodes(graph, weights, d, pi, new_node, priority_queue, heap_nodes)
    return d, pi


def dijkstra_dial_add_nodes(graph: list, weights: list, d: list, pi: list, i: int, priority_queue: list[MyLinkedList]):
    for j in range(len(graph[i])):
        if graph[i][j]:
            path_len = d[i] + weights[i][j]
            if path_len < d[j]:
                if j in priority_queue[d[j]]:
                    priority_queue[d[j]].delete(j)
                priority_queue[path_len].insert_last(j)
                pi[j] = i


def dijkstra_dial(graph: list, weights: list, s: int, max_weight: int):
    """
    Here, assuming for each edge we get 0<=w(e)<=max_weight and w(e) is integer, we get linear complexity.
    """
    n = len(graph)
    d, pi = initialize_sssp(n, s)
    priority_queue = [MyLinkedList() for i in range(max_weight * (n-1))]
    ptr_min = 0
    while ptr_min < len(priority_queue):
        if not priority_queue[ptr_min].is_empty():
            new_node = priority_queue[ptr_min].pop_first()
            dijkstra_dial_add_nodes(graph, weights, d, pi, new_node, priority_queue)
        else:
            ptr_min += 1
    return d, pi
