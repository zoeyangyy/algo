# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if not array:
            return 0
        res = array[0]
        for index,data in enumerate(array):
            res = max(res, self.end_with(index, array))
        return res

    def end_with(self,index, array):
        if index == 0:
            return array[0]
        return max(self.end_with(index-1,array)+array[index], array[index])


print(Solution().FindGreatestSumOfSubArray([6,-3,-2,7,-15,1,2,2]))
