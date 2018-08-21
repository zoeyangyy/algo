# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        li = [0, 1, 2]
        if number <= 2:
            return li[number]
        for i in range(3, number+1):
            li.append(sum(li)+1)
        return li[-1]


c = Solution()
print(c.jumpFloorII(5))