#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Time        : 2018/8/21 下午10:34
# @Author      : Zoe
# @File        : arrange_min.py
# @Description :

# class Solution:
#     def PrintMinNumber(self, numbers):
#         # write code here
#         str_li = [str(one) for one in numbers]
#         sort = self.quick(str_li, 0, len(str_li)-1)
#         return ''.join(sort)
#
#     def quick(self, li, start, end):
#         if start < end:
#             base = li[start]
#             i, j = start, end
#             while i < j:
#                 while j > i and self.compare(li[j],base):
#                     j -= 1
#                 li[i] = li[j]
#                 while i < j and self.compare(base, li[i]):
#                     i += 1
#                 li[j] = li[i]
#             li[i] = base
#             self.quick(li, start, i - 1)
#             self.quick(li, j + 1, end)
#         return li
#
#     def compare(self, A, B):
#         if int(A+B) > int(B+A):
#             return True # A>=B
#         return False


class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ""
        lmb = lambda n1, n2:int(str(n1)+str(n2))-int(str(n2)+str(n1))
        array = sorted(numbers, cmp=lmb)
        return ''.join([str(i) for i in array])


print(Solution().PrintMinNumber([3,321,4,45,43]))
