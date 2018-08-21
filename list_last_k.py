#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Time        : 2018/8/16 下午10:54
# @Author      : Zoe
# @File        : list_last_k.py
# @Description :

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        l=[]
        while head!=None:
            l.append(head)
            head=head.next
        if k>len(l) or k<1:
            return
        return l[-k]


a = ListNode(4)
b = ListNode(5)
a.next = b
c = ListNode(6)
b.next = c

s = Solution()
print(s.FindKthToTail({},1))
