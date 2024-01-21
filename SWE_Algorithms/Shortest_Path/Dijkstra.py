'''
Implementation for **Dijkstra's Algorithm** in Python. It finds the shortest path from a starting node to all other nodes in the graph. The graph can be directed/undirected, but no negative weights allowed. 
Performance: O(E+Vlog V)
'''
# Implementation below
import heapq

def dijkstra(graph, start):
    # initialize distances as infinity and the distance to start node as 0
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # initialize a priority queue and add the start node
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        # nodes can get added to the priority queue multiple times
        # we only process a vertex the first time we remove it from the priority queue
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            # only consider this new path if it's better than any path we've already found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# example
graph = {
    'A': {'B': 1, 'C': 4}, 
    'B': {'A': 1, 'C': 2, 'D': 5}, 
    'C': {'A': 4, 'B': 2, 'D': 1}, 
    'D': {'B': 5, 'C': 1}
}
# graph['A']['E'] = 6 this is if you wanted to connect another node E to A with dist 6

print(dijkstra(graph, 'A'))




