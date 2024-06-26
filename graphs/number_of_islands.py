"""
200. Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.
"""

from typing import List
from collections import deque
def bfs(row, col, graph, visited):
    queue = deque()
    queue.append((row, col))
    n = len(graph)
    m = len(graph[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up
    while queue:
        crow, ccol = queue.popleft()
        for dr, dc in directions:
            nrow = crow + dr
            ncol = ccol + dc
            if nrow >=0 and nrow < n and ncol >=0 and ncol < m and graph[nrow][ncol] == "1" and visited[nrow][ncol] == 0:
                visited[nrow][ncol] = 1
                queue.append([nrow, ncol])

def number_of_islands(grid:List[List]) -> int:
    n, m = len(grid), len(grid[0])
    visited = [[0]*m for _ in range(n)]
    # print(visited)
    cnt = 0
    for row in range(n):
        for col in range(m):
            if visited[row][col] == 0 and grid[row][col] == "1":
                bfs(row, col, grid, visited)
                cnt += 1
    return cnt
    

print(number_of_islands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))