#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Time        : 2018/8/16 上午10:03
# @Author      : Zoe
# @File        : end_start_list.py
# @Description :

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        return_list = []
        if listNode:
            while listNode.next:
                return_list.append(listNode.val)
                listNode = listNode.next
            return_list.append(listNode.val)
        return return_list[::-1]


a = ListNode(4)
b = ListNode(5)
a.next = b


c = Solution()
print(c.printListFromTailToHead({}))