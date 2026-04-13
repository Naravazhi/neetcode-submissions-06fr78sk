# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # this is coloring algorithm i think bipartite graph
        # ok so this is just tree dp


        # def rob(node, rob, taken): # this is one rob total and one taken. avoid
        def rob(node): # return two values instead [rob, taken]
            if not node:
                return [0, 0] # take, skip


            left = rob(node.left)
            right = rob(node.right)

            # take
            take = node.val + left[1] + right[1]
            # skip
            skip = max(left[0], left[1]) + max(right[0], right[1])
            # skip = max(left) + max(right)

            return [take, skip]

        return max(rob(root))




