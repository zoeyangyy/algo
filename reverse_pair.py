# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.count = 0

    def InversePairs(self, data):
        # write code here
        self.merge(data)
        return self.count % 1000000007

    def merge(self, li):
        if len(li) == 1:
            return li
        half = len(li) // 2
        left, right = self.merge(li[:half]), self.merge(li[half:])
        new_li = []
        while len(left)>0 and len(right)>0:
            if left[0] > right[0]:
                new_li.append(right.pop(0))
                self.count += len(left)
            else:
                new_li.append(left.pop(0))
        new_li += left
        new_li += right
        return new_li


class Solution:
    def InversePairs(self, data):
        # write code here
        if not data:
            return 0
        temp = [i for i in data]
        return self.mergeSort(temp, data, 0, len(data) - 1) % 1000000007

    def mergeSort(self, temp, data, low, high):
        if low >= high:
            temp[low] = data[low]
            return 0
        mid = (low + high) / 2
        left = self.mergeSort(data, temp, low, mid)
        right = self.mergeSort(data, temp, mid + 1, high)

        count = 0
        i = low
        j = mid + 1
        index = low
        while i <= mid and j <= high:
            if data[i] <= data[j]:
                temp[index] = data[i]
                i += 1
            else:
                temp[index] = data[j]
                count += mid - i + 1
                j += 1
            index += 1
        while i <= mid:
            temp[index] = data[i]
            i += 1
            index += 1
        while j <= high:
            temp[index] = data[j]
            j += 1
            index += 1
        return count + left + right

    
print(Solution().InversePairs([1,2,3,4,5,6,7,0]))