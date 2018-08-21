#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Time        : 2018/8/18 下午5:47
# @Author      : Zoe
# @File        : reverse_list.py
# @Description :

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead

        last = None
        while pHead:
            tmp = pHead.next
            pHead.next = last
            last = pHead
            pHead = tmp
        return last

a = ListNode(4)
b = ListNode(5)
a.next = b
c = ListNode(6)
b.next = c

s = Solution()
print(s.ReverseList(a))