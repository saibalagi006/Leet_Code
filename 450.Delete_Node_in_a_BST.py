"""
https://leetcode.com/problems/delete-node-in-a-bst/

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def min1(self,root):
        if(root.left is None):
            return root.val
        return self.min1(root.left)
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if(root is None):
            return None
        elif(key<root.val):
            if(root.left is not None):
                root.left = self.deleteNode(root.left,key)
        elif(key>root.val):
            if(root.right is not None):
                root.right = self.deleteNode(root.right,key)
        
        else:

            if(root.left is None and root.right is None):
                return None
            elif(root.left is None):
                return root.right 
            elif(root.right is None):
                return root.left 
            else:
                min1 = self.min1(root.right)
                root.val = min1
                root.right = self.deleteNode(root.right,min1)
        return root
                
        