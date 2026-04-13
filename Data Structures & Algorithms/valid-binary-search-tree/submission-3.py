# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, leftBound, rightBound):
            if not node:
                return True

            
            # i know i have to check every node against its parent and an 
            # ancestor node above parent?
            if leftBound >= node.val or node.val >= rightBound:
                return False

            return (dfs(node.left, leftBound, node.val) and 
            dfs(node.right, node.val, rightBound))

        # return (dfs(root.left, 0, root.val) and
        # dfs(root.right, root.val, float("inf")))
        return dfs(root, float("-inf"), float("inf"))


        