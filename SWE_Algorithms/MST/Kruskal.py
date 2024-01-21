'''
A **Minimum Spanning Tree (MST)** is a subset of edges of an undirected connected graph that forms a tree and contains all the vertices of the original graph. It connects all the vertices with a minimum possible total edge weight sum. 
If the original graph has n nodes, the tree has n-1 edges. 
Kruskal's Algorithm gives a MST of a connected graph. Sorting all the edges take Elog E time. 
Performance: O(Elog E)
'''
# Implementation below
class DisjointSet:
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            return self.find(self.parent[item])
        
    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                if self.rank[root1] == self.rank[root2]:
                    self.rank[root2] += 1

def kruskal(graph):
    mst = set()
    edges = sorted(graph['edges'], key=lambda item: item[2]) # sort the edges by edge weight
    ds = DisjointSet(graph['vertices'])

    for edge in edges:
        v1, v2, weight = edge
        if ds.find(v1) != ds.find(v2): # if they are not in the same connected component
            ds.union(v1, v2) # connect the nodes
            mst.add(edge) # add the edge to the mst
    
    return sorted(mst)

# example usage
graph = {
    'vertices': ['A', 'B', 'C', 'D', 'E'], 
    'edges': set([
        ('A', 'B', 3),
        ('A', 'D', 4), 
        ('B', 'C', 1), 
        ('B', 'D', 2),
        ('C', 'D', 4),
        ('C', 'E', 5),
        ('D', 'E', 6)
    ])
}

print(kruskal(graph))



