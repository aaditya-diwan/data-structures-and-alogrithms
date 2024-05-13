from typing import List
"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

[      0  1  2
    0 [1, 1, 1],
    1 [1, 0, 1],
    2 [0, 1, 1],
]
"""
class Solution:
    def setZeroesBruteForce(self, matrix: List[List[int]]) -> None:
        def setRow(row, noOfCols, matrix):
            for i in range(noOfCols):
                matrix[row][i] = -1
    
        def setColumn(col, noOfRows, matrix):
            for i in range(noOfRows):
                matrix[i][col] = -1

        row = len(matrix)    
        col = len(matrix[0])
        
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    setRow(i, col, matrix)
                    setColumn(j, row, matrix)
        
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == -1:
                    matrix[i][j] = 0
        print(matrix)
    
    def setZeroesBetter(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)    
        cols = len(matrix[0])
        row = [1] * len(matrix)
        col = [1] * len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    row[i] = 0
                    col[j] = 0
        for i in range(rows):
            for j in range(cols):
                if row[i] == 0 or col[j] == 0:
                    matrix[i][j] = 0
        print(matrix)
    
    def setZeroesOptimalSolution(self, matrix: List[List[int]]) -> None:
        """
        if you want to improve the space complexity, 
        can do so by using the first row and the first column of the matrix to keep track of the rows and columns that should be set to zero. 
        This approach requires constant space, but you need to be careful to handle the first row and the first column separately in case they
        themselves need to be set to zero.
        """
        m, n = len(matrix), len(matrix[0])
        first_row_has_zero = 0 in matrix[0]
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(m))

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0

        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0

        
    


s = Solution()

# s.setZeroesBruteForce([[1,1,1],[1,0,1],[1,1,1]])
# s.setZeroesBetter([[1,1,1],[1,0,1],[1,1,1]])
s.setZeroesOptimalSolution([[1,1,1],[1,0,1],[1,1,1]])