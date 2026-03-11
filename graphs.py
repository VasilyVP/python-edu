import numpy as np
from scipy.sparse.csgraph import (
    connected_components,
    dijkstra,
    floyd_warshall,
    bellman_ford,
    depth_first_order,
    breadth_first_order,
)
from scipy.sparse import csr_matrix

# Create a sample adjacency matrix for a graph
arr = np.array([[0, 1, 2], [1, 0, 0], [2, 0, 0]])
newarr = csr_matrix(arr)

print("Connected Components:", connected_components(newarr))
print(
    "Dijkstra (shortest weighted path):",
    dijkstra(newarr, return_predecessors=False, indices=0),
)
print(
    "Floyd-Warshall (all pairs shortest path):\n",
    floyd_warshall(newarr, return_predecessors=False),
)


arr = np.array([[0, -1, 2], [1, 0, 0], [2, 0, 0]])
newarr = csr_matrix(arr)

print(
    "Bellman-Ford (shortest path with negative weights):",
    bellman_ford(newarr, return_predecessors=False, indices=0),
)

arr = np.array([[0, 1, 0, 1], [1, 1, 1, 1], [2, 1, 1, 0], [0, 1, 0, 1]])
newarr = csr_matrix(arr)

print("Depth-First Order:", depth_first_order(newarr, 1, return_predecessors=False))
print("Breadth-First Order:", breadth_first_order(newarr, 1, return_predecessors=False))
