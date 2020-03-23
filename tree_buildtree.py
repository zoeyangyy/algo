#!usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@Author     : Zoe
@File       : tree_buildtree.py 
@Time       : 2019-11-24 20:42
"""
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def in_post_buildTree(self, inorder, postorder):
        if inorder:
            root_index = inorder.index(postorder[-1])
            left_root = self.in_post_buildTree(inorder[:root_index], postorder[:root_index])
            right_root = self.in_post_buildTree(inorder[root_index+1:], postorder[root_index:-1])
            root = TreeNode(postorder[-1])
            root.left = left_root
            root.right = right_root
            return root
        else:
            return None


    def pre_in_buildTree(self, preorder, inorder):
        if preorder:
            root = TreeNode(preorder[0])
            root_index = inorder.index(preorder[0])
            left_root = self.pre_in_buildTree(preorder[1:1+root_index], inorder[:root_index])
            right_root = self.pre_in_buildTree(preorder[1+root_index:], inorder[root_index+1:])
            root.left = left_root
            root.right = right_root
            return root
        else:
            return None


preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
# 无右子树
# inorder = [2,1]
# postorder = [2,1]
# [2,3,1]
# [3,2,1]
# 无左子树
# inorder = [1,2]
# postorder = [2,1]

c = Solution()
print(c.in_post_buildTree(inorder, postorder))
print(c.pre_in_buildTree(preorder, inorder))
