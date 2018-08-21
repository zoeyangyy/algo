# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        if n>=0:
            return bin(n)[2:].count("1")
        else:
            return bin(n+2**32)[2:].count("1")


print(Solution().NumberOf1(0))