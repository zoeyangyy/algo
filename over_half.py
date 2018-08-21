# -*- coding:utf-8 -*-
import collections
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        max_num = collections.Counter(numbers).most_common(1)
        if max_num[0][1] > len(numbers)/2:
            return max_num[0][0]
        else:
            return 0
        # write code here


print(Solution().MoreThanHalfNum_Solution([1,2,3,2,2,2,5,4,2]))