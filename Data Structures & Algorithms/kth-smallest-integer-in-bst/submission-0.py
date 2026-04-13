class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.res = 0

        def dfs(node):
            if not node:
                return
            dfs(node.left)

            self.k -= 1          # "visit" this node in sorted order
            if self.k == 0:
                self.res = node.val
                return            # found it, start unwinding

            dfs(node.right)

        dfs(root)
        return self.res



        