#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Time        : 2018/11/5 5:06 PM
# @Author      : Zoe
# @File        : 1_n.py
# @Description :

class Solution:
    def __init__(self):
        self.sum = 0

    def Sum_Solution(self, n):
        # write code here
        def qiusum(n):
            self.sum += n
            n -= 1
            return n > 0 and self.Sum_Solution(n)

        qiusum(n)
        return self.sum


s = Solution()
print(s.Sum_Solution(5))