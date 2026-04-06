# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# class TreeNode:
#     def __init__(self, val = 0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Iterative DFS
        # instead of call stack use actual stack
        if not root:
            return None
        stack = [root]

        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root







        # BFS
        # if not root:
        #     return None

        # q = deque([root])

        # while q:
        #     node = q.popleft()
        #     node.left, node.right = node.right, node.left
        #     if node.left:
        #         q.append(node.left)
        #     if node.right:
        #         q.append(node.right)

        # return root        
        
        # Recursive DFS
        # if not root:
        #     return None

        # left = root.left
        # root.left = root.right
        # root.right = left
        
        # self.invertTree(root.left)
        # self.invertTree(root.right)

        # return root














# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

#         def dfs(node):

#             if not node:
#                 return 

#             left = node.left
#             node.left = node.right
#             node.right = left
#             return node

#         return dfs(root)

















        # if not root:
        #     return None

        # root.left, root.right = root.right, root.left

        # self.invertTree(root.left)
        # self.invertTree(root.right)

        # reutrn root

        # # if not root:
        # #     return None

        # # queue = deque([root])

        # # while queue:
        # #     node = queue.popleft()
        # #     node.left, node.right = node.right, node.left

        # #     if node.left:
        # #         queue.append(node.left)

        # #     if node.right:
        # #         queue.append(node.right)

    
        # # return root
