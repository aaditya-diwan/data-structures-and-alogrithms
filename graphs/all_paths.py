"""
    Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, 
    find all possible paths from node 0 to node n - 1 and return them in any order.
    The graph is given as follows:
    graph[i] is a list of all nodes you can visit from node i 
    (i.e., there is a directed edge from node i to node graph[i][j]).
    
    Input: graph = [[1,2],[3],[3],[]]
    Output: [[0,1,3],[0,2,3]]
    Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
"""
from typing import List


class Solution:
    """
    A helper method dfs is used to perform the DFS. 
    The path list is passed to the recursive call of dfs to keep track of the current path. 
    When the target node is reached, the current path is added to the results list. 
    The path + [neighbor] creates a new list for each path, ensuring that paths don't share the same list.
    """
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        results = []
        self.dfs(graph, 0, target, [0], results)
        return results

    def dfs(self, graph, current, target, path, results):
        if current == target:
            results.append(path)
            return
        for neighbor in graph[current]:
            self.dfs(graph, neighbor, target, path + [neighbor], results)