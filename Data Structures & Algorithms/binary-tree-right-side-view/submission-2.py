# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return []
        q = deque([root])
        while q:
            level = []
            for i in range(len(q)):
                n = q.popleft()
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
                level.append(n.val)
            res.append(level[-1])
        
        return res
        # res = []
        # def dfs(node):
        #     if not node: 
        #         return None
            
        #     res.append(node.val)
        #     dfs(node.left)
        #     dfs(node.right)
        #     # if node.right:
        #     #     node = node.right

        # dfs(root)
        # return res

