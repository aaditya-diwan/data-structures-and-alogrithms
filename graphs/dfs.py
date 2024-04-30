from collections import deque

class Graph:
    def __init__(self, num_of_vertices):
        self.num_of_vertices = num_of_vertices
        self.graph = {i: [] for i in range(1, num_of_vertices + 1)}

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def print_graph(self):
        for i in range(1, self.num_of_vertices + 1):
            print(f"Adjacency list of vertex {i}: {self.graph[i]}")

    def dfs(self, root):
        visited = []
        stack = deque()
        stack.append(root)
        
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.append(current)
                stack.extend(node for node in self.graph[current] if node not in visited)
        return visited
    

adj_list = {
    'a': ['b', 'c'],
    'b': ['e'],
    'c': ['d'],
    'd': [],
    'e': ['f'],
    'f': ['d']
}

def dfs_recursive(graph, current, visited = None):
    if visited is None:
        visited = list()
    visited.append(current)
    for neighbors in graph[current]:
        if neighbors not in visited:
            dfs_recursive(graph, neighbors, visited);
    return visited

print(dfs_recursive(adj_list, 'a'))

# g = Graph(5)
# g.add_edge(1, 2)
# g.add_edge(1, 3)
# g.add_edge(2, 4)
# g.add_edge(3, 5)
# print(g.dfs(1))