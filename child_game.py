#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Time        : 2018/11/5 4:24 PM
# @Author      : Zoe
# @File        : child_game.py
# @Description :

class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n==0 or m==0:
            return -1
        flag = [True]*n
        li = range(n)
        # print(map(lambda x:if(x==True), flag))
        while flag.count(True) > 1:
            if len(li) >= m:
                flag[li[m-1]] = False
                li = li[m:]
            if len(li) < m:
                for i,d in enumerate(flag):
                    if d == True:
                        li.append(i)

        return flag.index(True)

c = Solution()
print(c.LastRemaining_Solution(7, 4))