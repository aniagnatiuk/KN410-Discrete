def read_graph(filename):
    with open(filename) as f:
        n = int(f.readline().strip())
        graph = []
        for i in range(n):
            row = list(map(int, f.readline().strip().split()))
            graph.append(row)
        return graph

def bfs(graph, source, sink, parent):
    n = len(graph)
    visited = [False] * n
    queue = []
    queue.append(source)
    visited[source] = True
    while queue:
        u = queue.pop(0)
        for v in range(n):
            if visited[v] == False and graph[u][v] > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u
                if v == sink:
                    return True
    return False

def edmonds_karp(graph, source, sink):
    n = len(graph)
    parent = [-1] * n
    max_flow = 0
    while bfs(graph, source, sink, parent):
        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
    return max_flow

graph = read_graph('l4-1.txt')
source, sink = 0, len(graph)-1
max_flow = edmonds_karp(graph, source, sink)
print(f"Maximum Flow: {max_flow}")


