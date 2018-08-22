# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        count = 0
        for i in range(len(data)-1):
            for j in range(i, len(data)):
                if data[i] > data[j]:
                    count+=1
        return count % 1000000007

print(Solution().InversePairs([1,2,3,4,5,6,7,0]))