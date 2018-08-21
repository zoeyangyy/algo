#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Time        : 2018/8/21 下午9:42
# @Author      : Zoe
# @File        : count_1.py
# @Description :

class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        sum = 0
        for i in range(n+1):
            sum += self.count_one(i)
        return sum

    def count_one(self, num):
        return len(list(filter(lambda x:x=='1', [i for i in str(num)])))


print(Solution().NumberOf1Between1AndN_Solution(13))