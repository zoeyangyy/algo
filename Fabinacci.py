# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        if n == 1:
            return 1
        one, two = 0, 1
        for i in range(n//2):
            one = one + two
            two = one + two
        if n % 2 == 0:
            return one
        else:
            return two