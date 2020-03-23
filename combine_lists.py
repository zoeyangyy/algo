#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Time        : 2018/8/18 下午6:08
# @Author      : Zoe
# @File        : combine_lists.py
# @Description :

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        if pHead1.val >= pHead2.val:
            head = pHead2
            pHead2 = pHead2.next
        else:
            head = pHead1
            pHead1 = pHead1.next
        next = head
        while pHead1 or pHead2:
            if not pHead1:
                next.next = pHead2
                pHead2 = pHead2.next
                continue
            if not pHead2:
                next.next = pHead1
                pHead1 = pHead1.next
                continue
            if pHead1.val <= pHead2.val:
                next.next = pHead1
                pHead1 = pHead1.next
                next = next.next
                continue
            else:
                next.next = pHead2
                pHead2 = pHead2.next
                next = next.next
        return head



a = ListNode(4)
b = ListNode(5)
a.next = b
c = ListNode(6)
b.next = c

d = ListNode(4)
e = ListNode(5)
d.next = e
f = ListNode(6)
e.next = f


s = Solution()
head = s.Merge(a,d)
while head:
    print(head.val)
    head = head.next