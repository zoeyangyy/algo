# -*- coding:utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if not pre or not tin:
            return None
        root = TreeNode(pre.pop(0))
        index = tin.index(root.val)
        root.left = self.reConstructBinaryTree(pre, tin[:index])
        root.right = self.reConstructBinaryTree(pre, tin[index+1:])
        return root



        # if not pre or not tin:
        #     return None
        # root = TreeNode(pre.pop(0))
        # index = tin.index(root.val)
        # root.left = self.reConstructBinaryTree(pre, tin[:index])
        # root.right = self.reConstructBinaryTree(pre, tin[index + 1:])
        # return root

