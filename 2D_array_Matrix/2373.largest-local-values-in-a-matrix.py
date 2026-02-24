#
# @lc app=leetcode id=2373 lang=python3
# @lcpr version=30400
#
# [2373] Largest Local Values in a Matrix
#
# https://leetcode.com/problems/largest-local-values-in-a-matrix/description/
#
# algorithms
# Easy (87.72%)
# Likes:    1318
# Dislikes: 182
# Total Accepted:    197.2K
# Total Submissions: 224.8K
# Testcase Example:  '[[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]\n' +
#  '[[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]'
#
# You are given an n x n integer matrix grid.
# 
# Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such
# that:
# 
# 
# maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid
# centered around row i + 1 and column j + 1.
# 
# 
# In other words, we want to find the largest value in every contiguous 3 x 3
# matrix in grid.
# 
# Return the generated matrix.
# 
# 
# Example 1:
# 
# Input: grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
# Output: [[9,9],[8,6]]
# Explanation: The diagram above shows the original matrix and the generated
# matrix.
# Notice that each value in the generated matrix corresponds to the largest
# value of a contiguous 3 x 3 matrix in grid.
# 
# Example 2:
# 
# Input: grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
# Output: [[2,2,2],[2,2,2],[2,2,2]]
# Explanation: Notice that the 2 is contained within every contiguous 3 x 3
# matrix in grid.
# 
# 
# 
# Constraints:
# 
# 
# n == grid.length == grid[i].length
# 3 <= n <= 100
# 1 <= grid[i][j] <= 100
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
#from common.node import *

# @lc code=start
# 二维矩阵滑动窗口问题
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        # 1. Initialize the matrix , matrix size: (n-2)*(n-2)
        # Create a matrix of all zeros using list comprehension. 使用列表推导式创建一个全 0 矩阵
        res = [[0]*(n-2) for _ in range(n-2)]

        # 2. Traverse each cell (i, j) in the result matrix
        for i in range(n-2):
            for j in range(n-2):

                # 3. examine the original grid for each res[i][j]
                # The two inner loops are responsible for searching for the maximum value within a 3x3 area.
                current_max = 0 # initialize the max value
                for x in range(i, i+3):
                    for y in range(j, j+3):
                        if grid[x][y] > current_max:
                            current_max = grid[x][y]

                # 4.Insert the maximum value found into the result.
                res[i][j] = current_max
        
        return res

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    # 测试一下 Example 1
    grid1 = [
        [9, 9, 8, 1],
        [5, 6, 2, 6],
        [8, 2, 6, 4],
        [6, 2, 2, 2]
    ]
   # 调用时需要加上 solution.
    result = solution.largestLocal(grid1)
    print(f"Result: {result}")
    # 进阶：使用 assert 自动校验
    expected1 = [[9, 9], [8, 6]]
    assert solution.largestLocal(grid1) == expected1, "测试用例 1 失败！"
    print("✅ 所有测试通过！")



# @lcpr case=start
# [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]\n
# @lcpr case=end

#

