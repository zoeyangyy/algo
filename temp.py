import json

def func1():
    n, m = [int(one) for one in input().split()]
    li = input().split()
    count = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if int(li[i]) ^ int(li[j]) > m:
                count += 1
    print(count)

def func2():
    from itertools import combinations
    n,m = map(int, input().split())
    com = combinations(list(map(int,input().split())),2)
    f = filter(lambda x:x > m, map(lambda x:x[0]^x[1], com))
    print(len(list(f)))


n,m = map(int, input().split())
li = [str(one) for one in range(1, n+1)]
print(int(sorted(li)[m-1]))
