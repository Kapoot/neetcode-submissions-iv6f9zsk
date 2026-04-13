class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def dfs(r, sub):
            if not sub:
                return True
            if not r:
                return False
            
            if r.val == sub.val:
                if helper(r, sub):
                    return True
            
            return dfs(r.left, sub) or dfs(r.right, sub)

        
        def helper(r, subr):
            if not r and not subr:
                return True
            elif r and not subr:
                return False
            elif subr and not r:
                return False
            elif subr.val != r.val:
                return False
            else:
                return helper(r.left, subr.left) and helper(r.right, subr.right)
        
        return dfs(root, subRoot)
            
       
        

        

        
        
        