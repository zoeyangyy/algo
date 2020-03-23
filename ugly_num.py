# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <= 0:
            return 0
        ugly_li = [1]
        index2, index3, index5 = 0, 0, 0
        for i in range(index-1):
            new_ugly = min(ugly_li[index2]*2, ugly_li[index3]*3, ugly_li[index5]*5)
            ugly_li.append(new_ugly)
            if new_ugly % 2 == 0:
                index2 += 1
            if new_ugly % 3 == 0:
                index3 += 1
            if new_ugly % 5 == 0:
                index5 += 1
        return ugly_li[-1]


print(Solution().GetUglyNumber_Solution(7))