import numpy as np

adj_matrix = np.loadtxt("l2-1.txt")

num_vertices = adj_matrix.shape[0]

stack = [0]

euler_cycle = []

while stack:
    curr_vertex = stack[-1]
    
    if any(adj_matrix[curr_vertex]):
        next_vertex = np.where(adj_matrix[curr_vertex] != 0)[0][0]
        
        adj_matrix[curr_vertex][next_vertex] = 0
        adj_matrix[next_vertex][curr_vertex] = 0
        
        stack.append(next_vertex)
    else:
        euler_cycle.append(stack.pop())
        
euler_cycle.reverse()

print("The Euler cycle in the graph is:", euler_cycle)