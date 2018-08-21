#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Time        : 2018/8/16 下午10:27
# @Author      : Zoe
# @File        : exponent.py
# @Description :

# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        result = base
        if exponent == 0:
            return 1
        elif exponent > 0:
            for i in range(exponent-1):
                result *= base
            return result
        else:
            for i in range(-exponent-1):
                result *= base
            return 1/result

c = Solution()
print(c.Power(2,-3))