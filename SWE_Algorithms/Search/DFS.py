'''
DFS is an algorithm for traversing a graph. It traverses all the way to the leaf node first (depth) and then recurses back up the graph. We use a stack for DFS. 
Performance: O(V+E)
'''
# Implementation below
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# example graph represented as an adjacency list
graph = {
    1: [2, 4], 
    2: [1, 3, 5], 
    3: [2], 
    4: [1], 
    5: [2], 
}

# start DFS from node 1
print("DFS starting from node 1: ")
dfs(graph, 1)





