#!usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@Author     : Zoe
@File       : tree_levelorder.py 
@Time       : 2019-11-19 15:16
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode):
        li = []
        queue = []
        if root:
            queue.append(root)
            while queue:
                new_li, queue = self.traverse(queue)
                li.append(new_li)
        return li

    def traverse(self, queue):
        new_li = []
        length = len(queue)
        for i in queue[:length]:
            new_li.append(i.val)
            if i.left:
                queue.append(i.left)
            if i.right:
                queue.append(i.right)
        queue = queue[length:]
        return new_li, queue

class Solution2:
    def levelOrder(self, root: TreeNode):
        #bfs
        res = []
        def helper(pnode:TreeNode,levels:int):
            if not pnode:
                return
            if len(res) == levels:
                res.append([])
            res[levels].append(pnode.val)
            helper(pnode.left,levels+1)
            helper(pnode.right,levels+1)
        helper(root,0)
        return res

root = TreeNode(5)
left = TreeNode(4)
right = TreeNode(6)
root.left = left
root.right = right
s = Solution()
print(s.levelOrder(root))

