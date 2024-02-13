'''
Implementation for **Bellman Ford's Algorithm** in Python. It finds the shortest path from a starting node to all other nodes in the graph. The graph can be directed/undirected, and can tolerate negative weights.
No negative cycles allowed. Unlike Dijkstra which is greedy, Bellman-Ford is not greedy.
Each iteration we examine all the edges, giving the VE time complexity. 
Algorithm takes at MOST V-1 iterations.
Performance: O(VE)
'''
# Implementation below

def bellman_ford(graph, source):
    # prepare the distance and predecessor for each node
    distance = {vertex: float('infinity') for vertex in graph}
    predecessor = {vertex: None for vertex in graph}

    # set source node distance to 0
    distance[source] = 0

    # update the shortest paths cycling through the V-1 iterations
    for _ in range(len(graph) - 1):
        for vertex in graph:
            for neighbor in graph[vertex]:
                if distance[vertex] + graph[vertex][neighbor] < distance[neighbor]:
                    distance[neighbor] = distance[vertex] + graph[vertex][neighbor]
                    predecessor[neighbor] = vertex

    # check for negative weight cycles
    # OPTIONAL PIECE OF CODE, assuming this doesn't exist in the problem
    for vertex in graph:
        for neighbor in graph[vertex]:
            if distance[vertex] + graph[vertex][neighbor] < distance[neighbor]:
                print("Graph contains a negative weight cycle")
                return None

    return distance, predecessor

# example
graph = {
    'A': {'B': -1, 'C': 4},
    'B': {'C': 3, 'D': 2, 'E': 2},
    'C': {},
    'D': {'B': 1, 'C': 5},
    'E': {'D': -3}
}

source = 'A'
distance, predecessor = bellman_ford(graph, source)
if distance: # given no neg weight cycle
    print("Distance from source:", distance)
    # print("Predecessor in path:", predecessor)