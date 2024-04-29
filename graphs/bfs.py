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

    def bfs(self, root):
        visited = []
        queue = deque()
        queue.append(root)
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.append(vertex)
                queue.extend(node for node in self.graph[vertex] if node not in visited)
        return visited


g = Graph(5)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 5)
print(g.bfs(1))