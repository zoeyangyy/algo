#!usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@Author     : Zoe
@File       : reverse_int.py 
@Time       : 2019-11-06 13:57

给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
输入: 120
输出: 21
注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
"""
class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            x = int(str(x)[::-1])
            if x>=2**31:
                return 0
            else:
                return x
        elif x<0:
            x = int(str(x)[1:][::-1])
            if x>2**31:
                return 0
            else:
                return -x
        else:
            return x

c = Solution()
print(c.reverse(123))
