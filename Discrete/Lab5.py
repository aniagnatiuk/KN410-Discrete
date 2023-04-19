from collections import defaultdict

def load_graph(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    graphs = []
    graph = defaultdict(list)
    for line in lines:
        if line == "\n":
            graphs.append(graph)
            graph = defaultdict(list)
            continue
        node, neighbors = line.strip().split(":")
        neighbors = list(map(int, neighbors.strip().split()))
        graph[int(node)] = neighbors
    graphs.append(graph)
    return graphs

def weisfeiler_lehman(graph):
    labels = {}
    for node in graph:
        labels[node] = frozenset(graph[node])
    while True:
        new_labels = {}
        for node in graph:
            neighbors = graph[node]
            neighbor_labels = [labels[neighbor] for neighbor in neighbors]
            new_labels[node] = frozenset(neighbor_labels)
        if labels == new_labels:
            break
        labels = new_labels
    return labels

def is_isomorphic(graph1, graph2):
    labels1 = weisfeiler_lehman(graph1)
    labels2 = weisfeiler_lehman(graph2)
    return labels1 == labels2

if __name__ == '__main__':
    graphs = load_graph('l5.txt')
    graph1 = graphs[0]
    graph2 = graphs[1]
    if is_isomorphic(graph1, graph2):
        print("Graphs are isomorphic")
    else:
        print("Graphs are not isomorphic")
