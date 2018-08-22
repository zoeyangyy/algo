# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        set_pass = set()
        once_li = []
        for one in s:
            if one not in set_pass:
                once_li.append(one)
                set_pass.add(one)
            elif one in once_li:
                once_li.remove(one)
        if len(once_li):
            return s.index(once_li[0])
        return -1

print(Solution().FirstNotRepeatingChar('abcdfabcdu'))
