
"""Depth First Algorithm."""
from typing import List
def dfs(adj_matrix: List[List[int]], node_label: int) -> List[int]:
    """Depth-First Search (DFS) graph traversal using recursion
      on a graph represented by an adjacency matrix."""
    visited: List[int] = []

    def traverse(node):
        # Mark the current node as visited
        visited.append(node)

        # Check all potential target nodes in the adjacency matrix
        for neighbor, connected in enumerate(adj_matrix[node]):
            # If an edge exists and the neighbor has not been visited yet
            if connected == 1 and neighbor not in visited:
                traverse(neighbor)

    traverse(node_label)
    return visited
