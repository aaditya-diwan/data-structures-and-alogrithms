"""
547. Number of Provinces

There are n cities. Some of them are connected, while some are not.
If city a is connected directly with city b, and city b is connected directly with city c, 
then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 
if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
"""

from typing import List

class Solution:
    def dfs_list(self, adj_list, i, visited):
        visited[i] = 1
        for j in adj_list[i]:
            if visited[j] == 0:
                self.dfs(adj_list, j, visited)

    def dfs_matrix(self, isConnected, i, visited):
        visited[i] = 1
        for j in range(len(isConnected)):
            if isConnected[i][j] == 1 and visited[j] == 0:
                self.dfs(isConnected, j, visited)
    
    def findCircleNumUsingAdjMatrix(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [0]*n
        cnt = 0
        for i in range(n):
            if visited[i] == 0:
                self.dfs_matrix(isConnected, i, visited)
                cnt += 1
        return cnt
            
    def findCircleNumUsingAdjList(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        adj_list = {i: [] for i in range(1, n+1)}
        # Creating an adjacency list from a matrix
        for node in range(n):
            for edge in range(n):
                if isConnected[node][edge] == 1 and node != edge:
                    adj_list[node + 1].append(edge + 1)
        visited = [0]*(n+1)
        cnt = 0
        for i in range(1, n + 1):
            if visited[i] == 0:
                self.dfs_list(adj_list, i, visited)
                cnt += 1
        return cnt        
        

sol = Solution()
print(sol.findCircleNumUsingAdjList([[1,0,0],[0,1,0],[0,0,1]]))
print(sol.findCircleNumUsingAdjMatrix([[1,0,0],[0,1,0],[0,0,1]]))
