'''
BFS is an algorithm for traversing a graph. It traverses a graph by level (breadth). We use a queue for BFS. 
Performance: O(V+E)
'''
# Implementation below
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue: # while queue isn't empty
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            # enqueue neighboring nodes that haven't been visited
            queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)

# example graph represented as an adjacency list
graph = {
    1: [2, 4], 
    2: [1, 3, 5], 
    3: [2], 
    4: [1], 
    5: [2], 
}
# start BFS from node 1
print("BFS starting from node 1: ")
bfs(graph, 1)





