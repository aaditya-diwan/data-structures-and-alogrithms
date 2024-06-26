"""
1557. Minimum Number of Vertices to Reach All Nodes

Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where 
edges[i] = [fromi, toi] represents a directed edge from node fromi to node toi.

Find the smallest set of vertices from which all nodes in the graph are reachable. 
It's guaranteed that a unique solution exists.

Notice that you can return the vertices in any order.
"""

from collections import defaultdict
from typing import List
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incoming = defaultdict(list)
        for frm, to in edges:
            incoming[to].append(frm)
        result = []
        for i in range(n):
            if not incoming[i]:
                result.append(i)
        return result
