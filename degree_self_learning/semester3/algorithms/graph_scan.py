from semester2.data_structures.queue import MyQueue
from semester2.data_structures.linked_list import MyLinkedList

BLUE = 0
RED = 1
INF = -1
WHITE = 9
GRAY = 8
BLACK = 7


def bfs(graph: list, source: int) -> list:
    """
    graph: A nxn Matrix stating 0...n-1 are vertices and graph[i][j]==1 iff IJ is an edge, 0 else.
    source: the index of the vertex from which BFS starts.

    distances: a list of size n in which distances[i] = the distance between i and source,
    or INF(=-1) if there is no route between them.

    This works both for directed and undirected graphs.
    """
    distances = []
    parents = []
    n = len(graph)
    for i in range(n):
        distances.append(INF)
        parents.append(None)
    distances[source] = 0
    q = MyQueue(source)
    while q.size:
        u = q.Dequeue()
        for i in range(n):
            if graph[u][i] == 1 and distances[i] == INF:
                distances[i] = distances[u] + 1
                parents[i] = u
                q.Enqueue(i)
    return distances


"""
Proof of correctness:
    Denote s(v) for each node v as the length of the shortest path from source.
    Lemma 1:
        Let v be a node in the graph; then, for every edge (u,v) in the graph: s(source, v) <= s(source, u) + 1
    Proof:
        by contradiction - assume s(source,v) > s(source,u) + 1. 
        then there is a path from source to u of size s(source, u).
        add the edge (u,v) to the path and get a path from source to v whose size is s(source, u) + 1 < s(source,v).
        this is a contradiction to the fact that s(source,v) is the minimal size of paths from source to v.

    Lemma 2:
        On the end of BFS run, for each node v in the graph, distances[v] >= s(source,v).
    Proof:
        By induction on enqueue operations.
        Base case: 
            when source is added to the queue, all nodes are INF which is either the distance if unreachable
            from source, or bigger than their s(.,.). 
        Inductive step:
            when enqueuing a node u, we have discovered it post dequeuing a node v, such that (v,u) is an edge in the
            graph.
            from the inductive assumption, distances(v) >= s(sources, v)
            We assign distances(u) to be distances(v) + 1, so from lemma 1:
                distances(u) = distances(v) + 1 > s(sources,v) + 1 >= s(sources,u)

    Lemma 3:
        During any step of BFS run, denote the queue members q1, q2, ..., qk. so:
            distances(q1) <= distances(q2) <= ... <= distances(qk)
        and also:
            distances(qk) - distances(q1) <= 1
    Proof:
        By induction on queue operation.
        Base case:
            When source is added to the queue, qk = q1 and so the claim stands.
        Inductive step:
            Dequeue:
                from the inductive assumption, distances(q2) <= ... <= distances(qk), and also:
                    distances(qk) - distances(q2) <= distances(qk) - distances (q1) <= 1
            Enqueue:
                Let v be the node we want to enqueue.
                Let q0 be the last dequeued node.
                Then q0 is v's neighbour, and distances(v) = distances(q0) + 1.
                Denote the last item in the queue qk.
                From the inductive assumption, 0 <= distances(qk)-distances(q0) <= 1.
                Then distances(qk) <= distances(q0) + 1 = distances(v).

                Now, denote q1 the new first element in the queue - next to be dequeued.
                We want to prove distances(v) - distances(q1) <= 1. From the inductive assumption:
                    distances(v) - distances(q1) <= distances(v) - distances(q0) = 1
                Q.E.D.

    Corollary 4:
        if node u is enqueued before node v, then d[u] <= d[v] as v is enqueued.
    Proof:
        distance for u is given once in the whole execution - and it is >= than distances[v], from lemma 3.

    Theorem 5 (Correctness of BFS):
        for each node v in the graph, in the end of bfs runtime:
            1. if v is reachable from source, then bfs discovers it.
            2. distances[v] = s(source, v).
            3. if you take a shortest path from source to parents[v] and add the node (parents[v], v),
                you get a shortest path from source to v.
    Proof:
        5.2. By contradiction.
        Assume, for some node v', distances[v'] > s(source, v') (it isn't the other way around, from lemma 2).
        The set of such nodes is final and as such can be ordered by u' -> s(source, u') and have a minimal - denoted v. 
        We get that v is reachable from source, or else distances[v] > s(source, v) = inf.
        let u be a node connected to s so that s(source,u) + 1 = s(source, v); meaning u precedes v in a shortest path.
        since s(sources, u) < s(sources, v) and the choice of v to have minimal s(sources, u') for wrong distances[u'],
        we get that s(sources, u) = distances(u).
        From that we get:
            ** distances[v] > s(source, v) = s(source, u) + 1 = distances[u] + 1

        Consider the occasion that u is dequeued from q. 
            case 1: assume v was never in the queue.
                then v will be enqueued, and distances[v] will be assigned distances[u] + 1, contradicting **.
            case 2: assume v was already dequeued.
                then by corollary 4, distances[v] < distances[u], contradicting **.
            case 3: assume v is already in the queue.
                then v is before u in the queue, again giving us from corollary 4:
                    distances[v] < distances[u]
                contradicting **.
        A contradiction was reached, which means 5.2 is correct.

        5.1. Assume, for the sake of contradiction, that a node v is reachable from source but not discovered.
        From reachability, s(source, v) is finite. however, distances[v] is infinite.
        However, from 5.2, distances[v] = s(source, v), which gives us the contradiction.

        5.3. for each node v, denote u=parent[v].
        We get that distances[v] = distances[u] + 1, which means s(source, u) + 1 = s(source, v).
        Take a shortest path from source to u; its length will be s(source, u).
        Add the edge (u, v) to its end to make it a path from source to v of size s(source, u) + 1.
        This path is of size s(source, v), which means it is a shortest path.

    for each graph G, the subgraph defined by all the nodes whose parent is not None
     and only edges (u,v) such that parent(u) = v is called the predecessor subgraph.
    The predecessor subgraph is called a Breadth-First Tree if its nodes are all node reachable from source,
     and for each such node v there exists one unique simple path from source to v, and it is a shortest path in G.

    Lemma 6:
        The predecessor subgraph with the list "parent" is a Breadth-First Tree.
    Proof:
        Inside the loop, parent[u] = v iff (u,v) is an edge in the graph,
         and s(source, v)<inf iff v is reachable from source, satisfying the first condition.
        Each node has only one edge connecting it to source, meaning there can be no loops in the graph.
        Combining the last two makes the predecessor graph a tree.

        From being a tree, each path from source is a simple path, and from using theorem 5.3 inductively,
         we get that the path from source to each node is a shortest path.
"""


def is_bipartite(graph: list) -> bool:
    distances = bfs(graph, 0)
    colors = []
    n = len(graph)
    for i in range(n):
        colors.append(RED if distances[i] % 2 == 0 else BLUE)

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 and colors[i] == colors[j]:
                return False
    return True


def dfs(
        graph: list,
        do_when_detect=lambda x: None,
        do_when_finish=lambda x: None,
        order_of_neighbors=lambda x: x,
        reverse_order_of_neighbors=False
):
    n = len(graph)
    colors = [WHITE for i in range(n)]
    parents = [None for i in range(n)]
    detections = [None for i in range(n)]
    finishes = [None for i in range(n)]
    forest_roots = []
    timer = 0

    def dfs_visit(node: int):
        colors[node] = GRAY
        nonlocal timer
        timer += 1
        detections[node] = timer
        do_when_detect(node)
        neighbors = [i for i in range(n) if graph[node][i]]
        sorted(neighbors, key=order_of_neighbors, reverse=reverse_order_of_neighbors)
        for i in neighbors:
            if graph[node][i] and colors[i] == WHITE:
                parents[i] = node
                dfs_visit(i)
        colors[node] = BLACK
        timer += 1
        finishes[node] = timer
        do_when_finish(node)
    graph_nodes = [i for i in range(n)]
    graph_nodes.sort(key=order_of_neighbors, reverse=reverse_order_of_neighbors)
    for graph_node in graph_nodes:
        if colors[graph_node] == WHITE:
            forest_roots.append(graph_node)
            dfs_visit(graph_node)
    return parents, detections, finishes, forest_roots


"""
Properties of DFS:

Theorem 1: Parenthesis Theorem:
    For any graph, and for any two vertices u,v, exactly one of the following happens:
        - detections[u] < finishes[u] < detections[v] < finishes[v] or replace u and v. 
            means neither is ancestor of the second in the list "parents".
        - detections[v] < detections[u] < finishes[u] < finishes[v] - meaning v is ancestor of u in parents.
        - detections[u] < detections[v] < finishes[v] < finishes[u] - meaning u is ancestor of v in parents.
Proof:
    case 1: assume detections[u] < detections[v].
        case 1.1: assume detections[v] < finishes[u].
            So v was discovered when u was gray.
            This means u is v's ancestor.
            Since v was discovered after u, all of v's outgoing edges were discovered before finishing v,
                which happens before finishing u.
            This means finishes[v] < finishes[u].
        case 1.2: assume finishes[u] < detections[v].
            Since for every node n, detections[n] < finishes[n], we get:
                detections[u] < finishes[u] < detections[v] < finishes[v].
    The second case is symmetric by replacing u and v's positions.
    
From this theorem, we get that for each nodes v and u, v is an ancestor of u in the list "parents" if and only if:
    detections[u] < detections[v] < finishes[v] < finishes[u]

Theorem 2: The White Path Theorem:
    In the graph defined by "parents", node u is ancestor of node v if and only if in time d[u], there is a white path
        from u to v.
Proof:
    ->:
    Assume u is ancestor of v. let w be a node on the path from u to v. then d[u]<d[w], hence in time d[u], w is white.
    <-:
    Assume, for the sake of contradiction, that in time d[u] there is a white path from u to v but u is not ancestor
    of v in "parents".
        Assume without loss of generality that any other node n in the path gets u as ancestor;
        otherwise let v be the closest n that doesn't.
             let w be v's predecessor in the white path (it might also be u itself).
                We then get that finishes[w] <= finishes[u] (equality when w=u).
                We also get that v must be detected after u's detection, but before finishing w, hence:
                    detections[u] < detections[v] < finishes[w] <= finishes[u]
                which gives is from the parenthesis theorem that:
                    detections[u] < detections[v] < finishes[v] < finishes[u]
                Which means, u is ancestor of v in "parents".

Types of edges in the graph:
    1. Tree edges - edges (u,v) such that parents[v]=u, meaning v was discovered by checking (u,v).
    2. Back edges - edges (u,v) such that v is an ancestor of u.
    3. Forward edges - edges (u,v) which aren't tree edges, but u is ancestor of v.
    4. Cross edges - any other edge.

During DFS, when checking the edge (u,v):
    - if v is white, (u,v) is a tree edge:
        given that v is white, we assign parents[v]=u.
    - if v is gray, (u,v) is a back edge:
        given v is gray, it means detections[v]<detections[u]<finishes[v] which means v is ancestor of u.
    - if v is black, (u,v) is forward or cross edge (anything else).
    
Theorem 3:
    In a non-directed graph G after DFS, every edge in G is tree edge or back edge.
Proof:
    Let (u,v) be an edge in G.
    Assume without loss of generality that detections[u]<detections[v] (otherwise look at (v,u)).
        then v's detection and end of check must end before finishing checking u, since v is in u's neighbors list:
            detections[v]<finishes[v]<finishes[u]
        if we first check (u,v) from u to v:
            then (u,v) is a tree edge.
        otherwise:
            we check (u,v) from v to u, but detections[u]<detections[v] meaning u is gray;
            which means (u,v) is a back node.
"""


def topological_sort(graph):
    lst = MyLinkedList()
    dfs(graph, do_when_finish=(lambda x: lst.insert_first(x)))
    return lst


"""
Proof of correctness for topological_sort.

Lemma:
    A directed graph G has circles if and only if DFS(G) provides back edges.
Proof:
    <-: Assume there is a back edge (u,v).
        Then v is ancestor of u - there is a path from v to u, then an edge from u to v - added together, a circle.
    ->: Assume there is a circle in G.
        Let v be the first node discovered in the circle, and let u be its former node in the circle.
            In time detections[v], the whole circle besides v wasn't discovered;
            this means there is a white path from v to u, meaning v is u's ancestor in the DFS forest;
            making (u,v) a back edge.

Theorem:
    topological_sort(G) gives a topological sort for any directed acyclic graph G.
Proof:
    Assume we do DFS for a given DAG G to determine "finishes".
    It's enough to show that for any nodes u,v, if there's an edge (u,v) then finishes[v]<finishes[u].
    Let (u,v) be an edge checked by DFS(G).
        v cannot be gray during the check, since that would mean, by the former lemma, that the graph isn't DAG.
        So v must be black or white.
        If v is white, then parents[v]=u, making finishes[v]<finishes[u].
        If v is black, then we are past finishes[v] but before finishes[u], satisfying finishes[v]<now<finishes[u].
"""


def test():
    graph = [[0, 1, 1, 1, 0], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [0, 1, 1, 1, 0]]
    print(bfs(graph, 0))
    print(is_bipartite(graph))
    print(dfs(graph))
    dag = [  # CLRS graph for Professor Bumstead's dressing routine
        [0, 0, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    print(topological_sort(dag))  # Returns a different topological sort than the CLRS solution, but still valid


test()
