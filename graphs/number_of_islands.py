"""
200. Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.
"""

from typing import List
from collections import deque
def bfs(row, col, graph, visited):
    queue = deque(list())
    queue.append([row, col])
    n = len(graph)
    m = len(graph[0])
    
    while queue:
        ele = queue.popleft()
        crow = ele[0]
        ccol = ele[1]
        
        for i in range(-1, 2):
            for j in range(-1, 2):
                nrow = crow + i
                ncol = ccol + j
                if nrow >=0 and nrow < n and ncol >=0 and ncol < m and graph[nrow][ncol] == "1" and visited[nrow][ncol] == 0:
                    visited[nrow][ncol] = 1
                    queue.append([nrow, ncol])

def number_of_islands(graph:List[List]) -> int:
    n, m = len(graph), len(graph[0])
    visited = [[0]*m]*n
    # print(visited)
    cnt = 0
    for row in range(n):
        for col in range(m):
            if visited[row][col] == 0 and graph[row][col] == "1":
                cnt += 1
                bfs(row, col, graph, visited)
    print(f"The number of islands in the grid are - {cnt}")
    

number_of_islands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])