#
# @lc app=leetcode id=304 lang=python3
# @lcpr version=30403
#
# [304] Range Sum Query 2D - Immutable
#
# https://leetcode.com/problems/range-sum-query-2d-immutable/description/
#
# algorithms
# Medium (58.39%)
# Likes:    5422
# Dislikes: 371
# Total Accepted:    487.6K
# Total Submissions: 835.1K
# Testcase Example:  '["NumMatrix","sumRegion","sumRegion","sumRegion"]\n' +
  '[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]'
#
# Given a 2D matrix matrix, handle multiple queries of the following
# type:
# 
# 
# Calculate the sum of the elements of matrix inside the rectangle defined by
# its upper left corner (row1, col1) and lower right corner (row2, col2).
# 
# 
# Implement the NumMatrix class:
# 
# 
# NumMatrix(int[][] matrix) Initializes the object with the integer matrix
# matrix.
# int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the
# elements of matrix inside the rectangle defined by its upper left corner
# (row1, col1) and lower right corner (row2, col2).
# 
# 
# You must design an algorithm where sumRegion works on O(1) time
# complexity.
# 
# 
# Example 1:
# 
# Input
# ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
# [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0,
# 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
# Output
# [null, 8, 11, 12]
# 
# Explanation
# NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2,
# 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
# numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
# numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green
# rectangle)
# numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue
# rectangle)
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 200
# -10^4 <= matrix[i][j] <= 10^4
# 0 <= row1 <= row2 < m
# 0 <= col1 <= col2 < n
# At most 10^4 calls will be made to sumRegion.
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.sumMat = [[0] * (COLS + 1) for r in range(ROWS + 1)] # list comprehension
        # [0] * (cols+1): 创建一行长度为 cols+1, 全部初始化为0
        # for r in range(rows+1): 循环rows+1次
        # 目的就是初始化一个长度为cols+1, 有rows+1行的值全为0的二维数组, 这是后面存二维 Prefix Sum 的容器。
        # 即创建一个(rows+1) × (cols+1)的二维数组, 全部初始化为0
        # sumMat比matrix多一圈0的目的是防止index=-1越界, 不需要任何 if row1 == 0 或 if col1 == 0 的特殊处理。
        # sumMat[r][c]表示从matrix左上角(0,0)到(r-1, c-1)的矩形总和
# eg: matrix真实数据, 大小 = ROWS × COLS
#       0   1
# 0     1   2
# 1     3   4
# eg: sumMat辅助数据, 大小 = (ROWS+1) × (COLS+1)
#       0   1   2
# 0     0   0   0
# 1     0   1   3
# 2     0   4  10
# 如图matrix[0][0]对应sumMat[1][1], sumMat[1][2]表示从matrix(0,0)到(0,1)的矩形和即[1, 2], 所以sumMat[1][2]=3
# sumMat[2][2]表示matrix中1234整个矩形和=10, sumMat[2][1]表示matrix中的(0,0)到(1,0)区域和即[1, 3], 即4
        for r in range(ROWS): # 是在遍历 matrix。
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c] # prefix表示当前这一行从最左边到当前位置的行前缀和
                above = self.sumMat[r][c+1] # 取当前位置正上方所有行组成的大矩形和, 而不是取正上方那个格子
                self.sumMat[r+1][c+1] = prefix + above # 这句是在写入 prefix matrix。
                # 当前行累计和prefix+上方所有行的总和above
                # sumMat[r+1][c+1]表示matrix中(0,0)到(r,c)的矩形和
                # 上述公式等价于:
                # sumMat[r+1][c+1] =matrix[r][c]+ sumMat[r][c+1]+ sumMat[r+1][c]- sumMat[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1+1, col1+1, row2+1, col2+1 # matrix坐标+1是为了把 matrix坐标映射到sumMat坐标。
        bottomRight = self.sumMat[r2][c2] # 表示从左上角到右下角整个大矩形
        above = self.sumMat[r1 - 1][c2] # 表示当前位置上方所有行行成的大矩形面积, above必须由r1决定, 因为要删到query上边界为止
        left = self.sumMat[r2][c1-1] # 表示左侧整个矩形面积, left必须由c1决定, 因为要删到query左边界为止
        # 因为我们是在根据 Query 的左上角边界(row1,col1) 来切掉不要的区域，而不是根据右下角边界(row2,col2)。
        topLeft = self.sumMat[r1 - 1][c1 - 1] # 表示左上角重叠矩形面积
        return bottomRight - above - left + topLeft 

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# ["NumMatrix","sumRegion","sumRegion","sumRegion"]\n[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]\n
# @lcpr case=end

#

