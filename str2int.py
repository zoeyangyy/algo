#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Time        : 2018/11/5 9:31 PM
# @Author      : Zoe
# @File        : str2int.py
# @Description :

# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        if not s:
            return 0
        flag = 1
        if s[0] == '+':
            flag = 1
            s = s[1:]
        elif s[0] == '-':
            flag = -1
            s = s[1:]
        if not s:
            return 0
        Sum = 0
        multiple = 1
        for i in s[::-1]:
            if i not in ['1','2','3','4','5','6','7','8','9','0']:
                return 0
            Sum += multiple*int(i)
            multiple *= 10
        return Sum*flag

c = Solution()
print(c.StrToInt('+'))