# Problem: https://leetcode.com/problems/set-matrix-zeroes
# Status   / Language / Runtime / Memory  /  Time
# Accepted / Python   /  75ms   / 14.16MB /  a few seconds ago

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        m = len(matrix)
        n = len(matrix[0])

        rows = []
        columns = []

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.append(i)
                    columns.append(j)
                
        for row in rows:
            for j in range(n):
                matrix[row][j] = 0

        for column in columns:
            for i in range(m):
                matrix[i][column] = 0