# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # do a bfs level by level search and carry down the maximum value seen so far down that path
        # issue is max will be carried down level which is not good amongst split
        # iguess dfs works best here
        good_count = 0
        def dfs(node, curr_max): # we need to know a way to have max so far given so carry max with you
            nonlocal good_count
            if not node:
                return None
            if node.val >= curr_max:
                curr_max = node.val
                good_count += 1
            dfs(node.left, curr_max)
            dfs(node.right, curr_max)


        dfs(root, root.val)
        return good_count