"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def dfs(node, hashmap):
            if not node:
                return node
            if node in hashmap:
                return hashmap[node]
            
            hashmap[node] = Node(node.val)

            for n in node.neighbors:
                cloned = dfs(n, hashmap)
                hashmap[node].neighbors.append(cloned)

            return hashmap[node]

        return dfs(node, {})