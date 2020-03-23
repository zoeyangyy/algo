#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Time        : 2018/8/9 下午10:14
# @Author      : Zoe
# @File        : sort.py
# @Description :


li = [4,7,3,8,2,9,5,1,0]
# 冒泡排序

def bubbling(li):
    for i in range(0,len(li)-1):
        for j in range(0, len(li)-i-1):
            if li[j+1] < li[j]:
                li[j], li[j+1] = li[j+1], li[j]
    return li

# print(bubbling(li))

def select(li):
    for i in range(0, len(li)-1):
        min = i
        for j in range(i, len(li)):
            if li[j]<li[min]:
                min = j
        li[i], li[min] = li[min], li[i]
    return li

# print(select(li))

def insert(li):
    for i in range(1, len(li)):
        base = li[i]
        j = i-1
        while li[j]>base and j>=0:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = base
    return li

# print(insert(li))

def quick(li, start, end):
    if start < end:
        base = li[start]
        i, j = start, end
        while i < j:
            while j>i and li[j]>base:
                j -= 1
            li[i] = li[j]
            while i<j and li[i]<base:
                i += 1
            li[j] = li[i]
        li[i] = base
        quick(li, start, i-1)
        quick(li, j+1, end)
    return li

# print(quick(li, 0, len(li)-1))

def heap(li):
    def sift_down(start, end):
        root = start
        while True:
            child = root*2+1
            if child > end:
                break
            if child+1 <=end and li[child] < li[child+1]:
                child += 1
            if li[root] < li[child]:
                li[root], li[child] = li[child], li[root]
                root = child
            else:
                break

    for i in range(len(li)//2-1, -1, -1):
        sift_down(i, len(li)-1)

    for end in range(len(li)-1, 0, -1):
        li[end], li[0] = li[0], li[end]
        sift_down(0, end-1)

    return li

# print(heap(li))


def merge(li):
    if len(li)==1:
        return li
    half = len(li)//2
    left, right = merge(li[:half]), merge(li[half:])
    new_li = []
    while len(new_li) < len(li):
        if not left:
            new_li += right
            break
        if not right:
            new_li += left
            break
        if left[0] <= right[0]:
            new_li.append(left.pop(0))
        else:
            new_li.append(right.pop(0))
    return new_li

# print(merge(li))


def quick_2(list, start, end):
    if start == end:
        return [list[start]]
    if start>end:
        return []
    one = list[start]
    left, right = start, end
    while left < right:
        for m in range(right,left,-1):
            if list[m]<one:
                list[left] = list[m]
                break
            right -= 1
        for n in range(left, right):
            if list[n]>one:
                list[right] = list[n]
                break
            left += 1
    list[left] = one
    return quick_2(list, start, left-1) + [one] + quick_2(list, left+1, end)

def quick(li, start, end):
    if start < end:
        base = li[start]
        i, j = start, end
        while i < j:
            while j>i and li[j]>base:
                j -= 1
            li[i] = li[j]
            while i<j and li[i]<base:
                i += 1
            li[j] = li[i]
        li[i] = base
        quick(li, start, i-1)
        quick(li, j+1, end)
    return li

