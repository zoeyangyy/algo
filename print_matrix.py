# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        result = []
        m = len(matrix)
        n = len(matrix[0])
        # if m == 1:
        #     return matrix[0]
        # if n == 1:
        #     return [matrix[one][0] for one in range(m)]
        for k in range((min(m, n)+1)//2):
            for j in range(k,n-k):
                result.append(matrix[k][j])
            for i in range(k+1,m-k):
                result.append(matrix[i][n-1-k])
            for j in range(n-2-k, k-1, -1):
                result.append(matrix[m-k-1][j])
            for i in range(m-k-2,k,-1):
                result.append(matrix[i][k])
        return result[:m*n]


s = Solution()
print([[one] for one in range(1,6)])
print(s.printMatrix([[one] for one in range(1,6)]))