#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Time        : 2018/8/16 上午12:46
# @Author      : Zoe
# @File        : blankspace_replace.py
# @Description :

class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code
        result = ''
        for i in s:
            if i==" ":
                result += '%20'
            else:
                result += i
        return result

c = Solution()
print(c.replaceSpace(" are happy"))