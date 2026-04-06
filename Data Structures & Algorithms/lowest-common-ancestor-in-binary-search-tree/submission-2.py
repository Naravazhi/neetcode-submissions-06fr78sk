# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # wait this lowkey easy as shit if you understand that if curr val
        # is greater than or less than both p and q then it is the LCA
        curr = root
        while curr:
            if curr.val > q.val and curr.val > p.val:
                curr = curr.left
            elif curr.val < q.val and curr.val < p.val:
                curr = curr.right
            else:
                return curr
        # if not root or not p or not q:
        #     return None

        # if (max(p.val, q.val) < root.val):
        #     return self.lowestCommonAncestor(root.left, p, q)

        # elif (min(p.val, q.val) > root.val):
        #     return self.lowestCommonAncestor(root.right, p, q)
        # else:
        #     return root



