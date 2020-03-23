# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return None
        head = RandomListNode(pHead.label)
        head.next = pHead.next
        head.random = pHead.random
        head.next = self.Clone(pHead.next)
        return head

