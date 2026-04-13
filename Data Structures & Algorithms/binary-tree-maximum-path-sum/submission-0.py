# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # path can stop abruptly
        # there can be negative values


        # im thinking there is a dynamic programming aspect to this problem
        # we need to store max num of groups of nodes
        # but we cannot store this information in one single value etc.
        # we also cannot every single combination of nodes sum so i think 
        # there has to be a selection criteria to cast away certain nodes
        # so i guess either adding or not adding that node


        # some insights is that you return max(child) or 0 if it is negative cause we dont need that
        # left contribution + node + right contribution
        # i guess for this approach dont go with reutrning up with sum
        # so have nonlocal max_sum within dfs
        max_sum = float("-inf")
        def dfs(node):
            nonlocal max_sum
            if not node:
                return 0
            left_part = max(dfs(node.left), 0)
            right_part = max(dfs(node.right), 0)
            curr_path_sum = left_part + node.val + right_part
            max_sum = max(max_sum, curr_path_sum)
            return node.val + max(left_part, right_part)
        dfs(root)
        return max_sum





        # max_sum = float("-inf")

        # def dfs(node):
        #     nonlocal max_sum
        #     if not node:
        #         return 0
            
        #     left_contribution = max(dfs(node.left), 0)
        #     right_contribution = max(dfs(node.right), 0)

        #     # this is to check if we include this node so that the path goes through it
        #     curr_path = node.val + left_contribution + right_contribution
        #     max_sum = max(max_sum, curr_path)
        #     # here we take max because we can take ONE of left and right so that it doesnt become a fork
        #     return node.val + max(left_contribution, right_contribution)


        # dfs(root)
        # return max_sum