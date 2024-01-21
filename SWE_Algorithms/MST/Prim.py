'''
A **Minimum Spanning Tree (MST)** is a subset of edges of an undirected connected graph that forms a tree and contains all the vertices of the original graph. It connects all the vertices with a minimum possible total edge weight sum.
If the original graph has n nodes, the tree has n-1 edges. 
Prim's Algorithm gives a MST of a connected graph. Start with a random node. Then, find all its neighboring edges. Pick the smallest edge that connects to an unvisited node (including edges from the new visited node).
Performance: O((V+E)log V)
'''
# Implementation below
import heapq

def prims_alg(graph, start_vertex):
    mst = []
    visited = set([start_vertex])
    edges = [(cost, start_vertex, to) for to, cost in graph[start_vertex].items()] # all neighboring edges from start node
    heapq.heapify(edges)

    while edges:
        cost, from_vertex, to_vertex = heapq.heappop(edges)
        if to_vertex not in visited:
            visited.add(to_vertex)
            mst.append((from_vertex, to_vertex, cost))

            for to_next, cost_next in graph[to_vertex].items():
                if to_next not in visited:
                    heapq.heappush(edges, (cost_next, to_vertex, to_next))
                
    return mst

# example
graph = {
    'A': {'B': 2, 'D': 3},
    'B': {'A': 2, 'D': 1, 'E': 4},
    'C': {'E': 2, 'F': 5},
    'D': {'A': 3, 'B': 1, 'E': 3},
    'E': {'B': 4, 'D': 3, 'C': 2, 'F': 3},
    'F': {'C': 5, 'E': 3}
}

minimum_spanning_tree = prims_alg(graph, 'A')
print("Minimum Spanning Tree:", minimum_spanning_tree)




