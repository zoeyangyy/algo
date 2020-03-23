#!usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@Author     : Zoe
@File       : tree_maxdepth.py 
@Time       : 2019-11-19 17:05
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode):
        if not root:
            return 0
        left, right = 1, 1
        if root.left:
            left = self.maxDepth(root.left)+1
        if root.right:
            right = self.maxDepth(root.right)+1
        return max(left, right)

root = TreeNode(5)
left = TreeNode(4)
right = TreeNode(6)
root.left = left
root.right = right
s = Solution()
print(s.maxDepth(root))