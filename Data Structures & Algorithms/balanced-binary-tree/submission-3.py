# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        checkBalance = True

        def search(node):
            nonlocal checkBalance
            if not node:
                return 0
            leftHeight = search(node.left)
            rightHeight = search(node.right)
            if abs(rightHeight - leftHeight) > 1:
                checkBalance = False
            return 1 + max(leftHeight, rightHeight)
        search(root)
        return checkBalance
