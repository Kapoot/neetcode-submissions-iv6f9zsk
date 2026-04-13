# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        queue = collections.deque()
        queue.append([root, float("-inf"), float("inf")])

        while queue:
            node, lower, upper = queue.popleft()
            if node.val <= lower or node.val >= upper:
                return False
            if node.left:
                queue.append([node.left, lower, min(upper, node.val)])
            if node.right:
                queue.append([node.right, max(lower, node.val), upper])
                
        return True