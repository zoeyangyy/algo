# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.arr = []
    def push(self, node):
        # write code here
        self.arr.append(node)
    def pop(self):
        # return xx
        return self.arr.pop(0)

import queue

s = queue.Queue(maxsize=100)

for i in range(0,5):
    s.put(i)

while not s.empty():
    print(s.get())
