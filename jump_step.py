# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 0:
            return 0
        if number == 1:
            return 1
        li = [1,1]
        for i in range(2, number+1):
            li.append(li[i-1] + li[i-2])
        return li[-1]


c = Solution()
print(c.jumpFloor(2))