#!usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@Author     : Zoe
@File       : tree_connect.py 
@Time       : 2019-12-03 19:02
"""

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node'):
        if not root:
            return None
        li = [root]
        while li:
            for i in range(len(li)-1):
                li[i].next = li[i+1]
            li = self.traverse(li)
        return root

    def traverse(self, li):
        new_li = []
        for i in li:
            if i.left:
                new_li.append(i.left)
            if i.right:
                new_li.append(i.right)
        return new_li


root = Node(1)
left = Node(2)
right = Node(3)
root.left = left
root.right = right
c = Solution()
c.connect(root)
