# -*- coding:utf-8 -*-
import itertools
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        return sorted(list(set(map(''.join, itertools.permutations(ss)))))


li = 'abc'
print(Solution().Permutation(li))