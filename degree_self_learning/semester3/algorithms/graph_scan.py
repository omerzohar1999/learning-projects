import sys
sys.path[0] = sys.path[0][:-21]
sys.path.insert(0, '..')
from semester2.data_structures.queue import MyQueue
from semester2.data_structures.stack import MyStack

BLUE = 0
RED = 1
INF = -1


def dfs_directed():
    pass


def dfs_undirected():
    pass


def bfs(graph: list, source: int) -> list:
    """
    graph: A nxn Matrix stating 0...n-1 are vertices and graph[i][j]==1 iff IJ is an edge, 0 else.
    source: the index of the vertex from which BFS starts.

    distances: a list of size n in which distances[i] = the distance between i and source,
    or INF(=-1) if there is no route between them.
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



def test():
    graph = [[0,1,0,1],[1,0,1,0],[0,1,0,1], [1,0,1,0]]
    print(bfs(graph, 0))
    print(is_bipartite(graph))

test()
