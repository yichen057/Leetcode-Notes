#
# @lc app=leetcode id=463 lang=python3
# @lcpr version=30400
#
# [463] Island Perimeter
#
# https://leetcode.com/problems/island-perimeter/description/
#
# algorithms
# Easy (74.24%)
# Likes:    7276
# Dislikes: 427
# Total Accepted:    808.5K
# Total Submissions: 1.1M
# Testcase Example:  '[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]\n[[1]]\n[[1,0]]'
#
# You are given row x col grid representing a map where grid[i][j] = 1
# represents land and grid[i][j] = 0 represents water.
# 
# Grid cells are connected horizontally/vertically (not diagonally). The grid
# is completely surrounded by water, and there is exactly one island (i.e., one
# or more connected land cells).
# 
# The island doesn't have "lakes", meaning the water inside isn't connected to
# the water around the island. One cell is a square with side length 1. The
# grid is rectangular, width and height don't exceed 100. Determine the
# perimeter of the island.
# 
# 
# Example 1:
# 
# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.
# 
# 
# Example 2:
# 
# Input: grid = [[1]]
# Output: 4
# 
# 
# Example 3:
# 
# Input: grid = [[1,0]]
# Output: 4
# 
# 
# 
# Constraints:
# 
# 
# row == grid.length
# col == grid[i].length
# 1 <= row, col <= 100
# grid[i][j] is 0 or 1.
# There is exactly one island in grid.
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# 题目大意给定一个n*m 的二维网格 grid，其中 1 代表陆地，0 代表水域。网格中恰好只有一个岛屿。
# 岛屿内部没有“湖泊”（即岛屿内没有被陆地完全包围的水域）。每个格子是边长为 1 的正方形。你需要计算这个岛屿的总周长。
# 减法逻辑（最推荐)
# 假设每块陆地都是独立的：如果一块陆地周围全是水，它的周长贡献是 4
# 处理相邻关系：如果两块陆地相邻，它们接触的那条边就消失了，不再是周长。
# 关键点：每有一对相邻的陆地，总周长就要 减去 2（因为这条重合边本属于两块陆地）。
# 算法步骤：
# 遍历整个矩阵。
# 如果当前格子是陆地 (grid[i][j] == 1)：
# 周长基础值 ans += 4。先给全额，再按需扣减的倒扣逻辑。
# 检查它的上方是否也是陆地。如果是，ans -= 2。
# 检查它的左边是否也是陆地。如果是，ans -= 2。
# 为什么只检查左和上？ 因为我们是从左往右、从上往下遍历的，这样可以确保每对相邻关系只被计算（和扣除）一次。
# 时间复杂度：O(n * m)。我们需要遍历矩阵中的每一个格子。空间复杂度：O(1)。我们只需要一个变量来存储结果。
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid) # len(grid)指的是矩阵有多少行。在 Python 中，二维矩阵实际上是一个**大列表**，里面装了很多个**小列表**。大列表**代表整个矩阵。每个小列表**代表矩阵的一行。当你对一个列表执行 `len()` 时，Python 只会数这个列表里直接装了多少个“东西”。
        cols = len(grid[0]) # Python 的二维列表（即矩阵）时，`grid[0]` 指的是该矩阵的**第一行（Row）**。
        perimeter = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: # 如果当前格子是陆地 (grid[i][j] == 1)：它的周长贡献是 4
                    # 基础周长先给全额，假设每块陆地都是独立的, 再按需扣减的倒扣逻辑。
                    perimeter += 4

                    # 处理相邻关系：如果两块陆地相邻，它们接触的那条边就消失了，不再是周长。
                    # 关键点：每有一对相邻的陆地，总周长就要 减去 2（因为这条重合边本属于两块陆地）
                    # 检查左边是否有邻居
                    if c > 0 and grid[r][c-1] == 1:
                        perimeter -= 2
                    # 检查上边是否有邻居
                    if r >0 and grid[r-1][c] == 1:
                        perimeter -= 2

        return perimeter
                    
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,0]]\n
# @lcpr case=end

#

