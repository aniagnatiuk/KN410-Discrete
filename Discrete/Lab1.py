import sys
import heapq

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[py] < self.rank[px]:
            self.parent[py] = px
        else:
            self.parent[px] = py
            self.rank[py] += 1
        return True

def kruskal(graph):
    edges = []
    for i in range(len(graph)):
        for j in range(i + 1, len(graph)):
            if graph[i][j] != 0:
                edges.append((graph[i][j], i, j))
    edges.sort()
    dsu = DisjointSet(len(graph))
    for w, u, v in edges:
        if dsu.union(u, v):
            yield (u, v, w)

def read_graph(filename):
    with open(filename, 'r') as f:
        n = int(f.readline())
        graph = [[int(x) for x in f.readline().split()] for i in range(n)]
    return graph

def display_step(step):
    print(f"Step {step}")
    input("Press K to continue...")

def main():
    filename = "l1-1.txt"
    graph = read_graph(filename)
    step = 0
    for u, v, w in kruskal(graph):
        step += 1
        print(f"{step}: ({u}, {v}) - weight {w}")
        display_step(step)

if __name__ == "__main__":
    main()
