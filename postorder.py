# -*- coding:utf-8 -*-

# BST的后序序列的合法序列是，对于一个序列S，最后一个元素是x （也就是根），如果去掉最后一个元素的序列为T，
# 那么T满足：T可以分成两段，前一段（左子树）小于x，后一段（右子树）大于x，
# 且这两段（子树）都是合法的后序序列。完美的递归定义 : ) 。


class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        else:
            return self.fun2(sequence)

    def fun2(self, sequence):
        if len(sequence) == 1 or not sequence:
            return True
        root = sequence.pop()
        cut = 0
        while cut < len(sequence) and sequence[cut] < root:
            cut += 1
        for i in sequence[cut:]:
            if i < root:
                return False
        return self.fun2(sequence[:cut]) and self.fun2(sequence[cut:])


s = Solution()
print(s.VerifySquenceOfBST([2,4,3,6,8,9,5]))