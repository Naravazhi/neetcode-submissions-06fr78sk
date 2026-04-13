# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]):

        # dfs approach
        # bfs approach
        if not root:
            return []
        res = []
        q = deque([root])
        index = 0
        while q:
            level = []
            for i in range(len(q)):
                n = q.popleft()
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
                level.append(n.val)
            res.append(level)
            index += 1


        return res





















# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         # q = deque()
#         res = []
#         q = collections.deque()
#         q.append(root)
#         while q:
#             level = []
#             qLen = len(q)
#             for i in range(qLen):
#                 node = q.popleft()
#                 if node:
#                     level.append(node.val)
#                     q.append(node.left)
#                     q.append(node.right)
#             if level:
#                 res.append(level)
#         return res

#         # res = []

#         # def dfs(node, depth):
#         #     if not node:
#         #         return None
#         #     if len(res) == depth:
#         #         res.append([])

#         #     res[depth].append(node.val)
#         #     dfs(node.left, depth + 1)
#         #     dfs(node.right, depth + 1)


#         # dfs(root, 0)
#         # return res




#         # q.append(root)



#         # def dfs(node, traversal):
#         #     if not node:
#         #         return 

#         #     dfs(node.left, traversal)
#         #     traversal.append()


#         # dfs(root, [])


# # class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        