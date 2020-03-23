# -*- coding:utf-8 -*-
class Solution:
    def convert(self, s, numRows):
        if numRows >= len(s):
            return s

        L = [''] * numRows
        index, flag = 0, 1

        for one in s:
            L[index] += one
            if index == 0:
                flag = 1
            elif index == numRows - 1:
                flag = -1
            index += flag
        return ''.join(L)


s = Solution()
s.convert("paypalishiring", 3)