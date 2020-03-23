#!usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@Author     : Zoe
@File       : tree_haspathsum.py 
@Time       : 2019-11-20 11:39
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int):
        def hasnum(node, num):
            if not node.left and not node.right and node.val == num:
                return True
            if node.left and hasnum(node.left, num-node.val):
                return True
            if node.right and hasnum(node.right, num-node.val):
                return True
            return False
        if not root:
            return False
        ans = hasnum(root, sum)
        return ans

class Solution2:
    def hasPathSum(self, root: TreeNode, sum: int):
        if not root:
            return False
        if not root.left and not root.right and root.val == sum:
            return True
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)

root = TreeNode(5)
left = TreeNode(4)
right = TreeNode(4)
root.left = left
root.right = right
s = Solution2()
print(s.hasPathSum(root,8))


