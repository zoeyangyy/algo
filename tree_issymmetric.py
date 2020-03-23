#!usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@Author     : Zoe
@File       : tree_issymmetric.py 
@Time       : 2019-11-19 17:14
层次遍历的想法
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode):
        def level(q):
            length = len(q)
            li = []
            flag = 0
            for i in q[:length]:
                if not i:
                    li.append("null")
                else:
                    li.append(i.val)
                    flag = 1
                    q.append(i.left)
                    q.append(i.right)
            if flag == 0:
                return [], li
            else:
                return q[length:], li

        def issym(li):
            length = len(li)
            for i in range(int(length/2)):
                if li[i]!=li[length-i-1]:
                    return False
            return True

        if not root:
            return True
        queue = [root]
        while queue:
            queue, answer_li = level(queue)
            if not issym(answer_li):
                return False
        return True

class Solution2:
    def isSymmetric(self, root: TreeNode):
        def check_binary(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            return check_binary(left.right, right.left) and check_binary(left.left, right.right)

        if not root:
            return True
        return check_binary(root.left,root.right)



root = TreeNode(5)
left = TreeNode(4)
right = TreeNode(4)
left_right = TreeNode(3)
right_right = TreeNode(3)
root.left = left
root.right = right
# left.right = left_right
# right.right = right_right
s = Solution2()
print(s.isSymmetric(root))
