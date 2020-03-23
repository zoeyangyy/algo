#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@Author     : Zoe
@File       : merge_k_link.py 
@Time       : 2019-02-28 19:04
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


import numpy as np
from functools import reduce
import copy

def mergeKLists(lists):
    var = [one.val for one in lists]
    start = lists[np.argmin(var)]
    print(start.val)
    if start.next:
        var[np.argmin(var)] = start.next.val
    else:
        var[np.argmin(var)] = False

    you = reduce(lambda x, y: x | y, var)
    before = start
    while you:
        next1 = lists[np.argmin(var)]
        before.next = next1
        before = next1
        if next1.next:
            var[np.argmin(var)] = next1.next.val
            lists[np.argmin(var)] = next1.next
        else:
            var[np.argmin(var)] = False
        you = reduce(lambda x, y: x | y, var)

    return start


a = ListNode(5)
b = ListNode(6)
c = ListNode(3)
d = ListNode(7)
a.next = b
c.next = d
print(b.next)
ans = mergeKLists([a, c])

while ans:
    print(ans.val)
    ans = ans.next