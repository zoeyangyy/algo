# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        res = self.fun2(pRootOfTree)
        if len(res) == 1:
            return pRootOfTree
        if len(res) == 0:
            return None
        res[0].left = None
        res[0].right = res[1]
        res[-1].left = res[-2]
        res[-1].right = None
        for i in range(1,len(res)-1):
            res[i].left = res[i-1]
            res[i].right = res[i+1]
        return res[0]

    def fun2(self, pRoot):
        if not pRoot:
            return []
        return self.fun2(pRoot.left) + [pRoot] + self.fun2(pRoot.right)


a = TreeNode(4)
b = TreeNode(2)
c = TreeNode(5)
d = TreeNode(1)
e = TreeNode(3)

a.left = b
a.right = c
b.left = d
b.right = e

s = Solution()
print(s.Convert(a).val)