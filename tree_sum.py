# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        if not root.right and not root.left and root.val == expectNumber:
            return [[root.val]]
        res = []
        left = self.FindPath(root.left, expectNumber-root.val)
        right = self.FindPath(root.right, expectNumber-root.val)
        for i in left+right:
            res.append([root.val]+i)
        return res

a = TreeNode(4)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(1)
e = TreeNode(3)

a.left = b
a.right = c
b.left = d
b.right = e

s = Solution()
print(s.FindPath(a, 7))