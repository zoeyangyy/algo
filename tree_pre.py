#!usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@Author     : Zoe
@File       : tree_pre.py 
@Time       : 2019-11-18 17:55
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode):
        li = []
        if root:
            li.extend(self.append_li(root))
        return li

    def append_li(self, root):
        li = []
        if root:
            li.extend([root.val])
            if root.left:
                li.extend(self.append_li(root.left))
            if root.right:
                li.extend(self.append_li(root.right))
        return li

root = TreeNode(5)
left = TreeNode(4)
right = TreeNode(6)
root.left = left
root.right = right
s = Solution()
print(s.preorderTraversal(root))