# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(tree1_node, tree2_node):
            if not tree1_node and not tree2_node:
                return True
            if not tree1_node:
                return False
            if not tree2_node:
                return False

            if tree1_node.val != tree2_node.val:
                return False
            # recurse
            left = dfs(tree1_node.left, tree2_node.left)
            # if tree1_node.val != tree2_node.val:
            #     return False
            right = dfs(tree1_node.right, tree2_node.right)
            return left and right
        return dfs(p, q)



        

# class Solution:
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        