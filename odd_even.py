#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Time        : 2018/8/16 下午10:45
# @Author      : Zoe
# @File        : odd_even.py
# @Description :

class Solution:
    def reOrderArray(self, array):
        # write code here
        odd_array, even_array = [], []
        for data in array:
            if data%2 == 0:
                even_array.append(data)
            else:
                odd_array.append(data)
        return odd_array+even_array

c = Solution()
print(c.reOrderArray([1,2,3,4,5,6,7]))