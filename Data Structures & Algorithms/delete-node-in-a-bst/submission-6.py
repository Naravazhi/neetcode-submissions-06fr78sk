# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # def find_min(node):
        #     while node.left:
        #         node = node.left
        #     return node
        def find_min(node):
            while node.left:
                node = node.left
            return node

        def delete_successor(node, val):
            if not node:
                return None
            if node.val < val:
                node.right = delete_successor(node.right, val)
            elif node.val > val:
                node.left = delete_successor(node.left, val)
            else:
                # successor might still have right node so return that
                return node.right
            return node
        #     return node
        # def delete_successor(node, val):
        #     if not node:
        #         return None
        #     if node.val < val:
        #         node.right = delete_successor(node.right, val)
        #     elif node.val > val:
        #         node.left = delete_successor(node.left, val)
        #     elif node.val == val:
        #         # found node.val == val
        #         return node.right
        #     return node
            
        
        def dfs(node):
            if not node:
                return None

            if node.val == key:
                # do something
                # no children
                if not node.left and not node.right:
                    return None # just remove
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                #both nodes exist
                # have to make sure subtree of node chosen is organized correctly
                # forgot about inorder successor and predecessor
                successor = find_min(node.right)
                node.val = successor.val
                node.right = delete_successor(node.right, successor.val)
                return node
                # successor = find_min(node.right)
                # node.val = successor.val
                # node.right = delete_successor(node.right, successor.val)
                # return node

            elif node.val < key:
                node.right = dfs(node.right)
            else:
                # node.val > key
                node.left = dfs(node.left)

            return node
        return dfs(root)
# class Solution:
#     def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        