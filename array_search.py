#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Time        : 2018/8/14 下午11:12
# @Author      : Zoe
# @File        : array_search.py
# @Description :

class Solution:
    # array 二维列表
    def Find(self, target, array):
        row, column = len(array), len(array[0])
        x,y = row-1, 0

        while x>=0 and y<=column-1:
            base = array[x][y]
            if base == target:
                return True
            if base > target:
                x -= 1
            elif base < target:
                y += 1
        return False





c = Solution()
print(c.Find(11,[[1,2,9],[4,7,10],[5,8,12]]))
