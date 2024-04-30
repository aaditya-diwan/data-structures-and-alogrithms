def has_path(graph, current, destination):
    stack = [current]
    visited = set()
    while stack:
        current = stack.pop()
        visited.add(current)
        if current == destination:
            return True
        stack.extend(node for node in graph[current] if node not in visited)
    return False
    


graph  = {
    'f': ['i', 'g'],
    'i': ['k'],
    'g': ['h'],
    'k': [],
    'h': [],
    'j': ['i']
}

print(f"Is the path present in the graph - ", has_path(graph, 'f', 'h'))