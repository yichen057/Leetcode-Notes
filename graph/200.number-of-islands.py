#
# @lc app=leetcode id=200 lang=python3
# @lcpr version=30403
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (64.15%)
# Likes:    25029
# Dislikes: 619
# Total Accepted:    4.2M
# Total Submissions: 6.5M
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]\n' +
  '[["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]'
#
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and
# '0's (water), return the number of islands.
# 
# An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically. You may assume all four edges of the grid are all
# surrounded by water.
# 
# 
# Example 1:
# 
# Input: grid = [
# ⁠ ["1","1","1","1","0"],
# ⁠ ["1","1","0","1","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","0","0","0"]
# ]
# Output: 1
# 
# 
# Example 2:
# 
# Input: grid = [
# ⁠ ["1","1","0","0","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","1","0","0"],
# ⁠ ["0","0","0","1","1"]
# ]
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
''' UMPIRE template

  # Understand
inputs:2D grid of characters grid(注意: 题目里输入是字符"1"和"0", 并非数字1和0)
"1" for land, "0" for water
outputs: int: # of islands
constraints:
grid boudaries are surrounded by water
horizontal and vertical connections only
edge cases:
empty grid
grid with only water or only land

  # Match (any problems this reminds you of, any helpful patters to solve this e.g. two pointer technique, any data structures this reminds you of )
    DFS, Flood fill: once we find land, we sink it to avoid counting the same island twice
  # Plan (pseudocode)
 1. initialize count = 0
 2. iterate through every cell (r, c) in the grid
 3. if grid[r][c] == "1": increment count ; start a dfs(r,c) to turn all connected "1"s into "0"s.
 4. return count

  # Implement (python code)

  # Review (dry run of your code)
  Dry Run: For a 2 * 2 grid [["1","1"],["0","0"]], the first '1' triggers DFS, sinks both '1's, and the loop finishes with count = 1.

  # Evaluate (time and space complexity)
  Time Complexity: O(M * N), where M is rows and N is columns. Every cell is visited at most once.
  Space Complexity: O(M * N) in the worst case (all land) due to the recursion stack.
'''
# method 1: DFS with Implicit Marking (Modifying Input)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
      
       # nested function: 想把 dfs 写成主函数内部的一个辅助函数，你必须把它挪到 for 循环之前
        def dfs (r, c):
            # base case: out of bounds or water/already visited
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c]=="0":
                return
            # sink the land to water
            grid[r][c] = "0"

            # recursion: check neighbors
            dfs(r + 1, c) # down
            dfs(r - 1, c) # up
            dfs(r, c + 1) # right
            dfs(r, c - 1) # left
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)
        return count

# 如果你想“先调用后定义”该怎么办？
# 在 Python 中，唯一能实现“视觉上的先调用、后定义”的方法是将 dfs 定义为类的一个独立方法。
# 因为 Python 在执行类的方法时，会先加载整个类的内容。只要 dfs 是 self 的一个方法，调用的顺序就不受限制了。
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    self.dfs(grid, r, c) # 调用类方法必须加 self.
        return count
    # class method
    def dfs (self, grid, r, c):
        # 注意：这里不能直接用 rows/cols，需要动态获取或从参数传入
        rows, cols = len(grid), len(grid[0])

        # base case: out of bounds or water/already visited
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c]=="0":
            return
        
        # mark as visited (sink the land to water)
        grid[r][c] = "0"

        # recursion: check neighbors. 必须全部加上 self. 否则 Python 找不到这个函数
        self.dfs(grid, r + 1, c) # down
        self.dfs(grid, r - 1, c) # up
        self.dfs(grid, r, c + 1) # right
        self.dfs(grid, r, c - 1) # left
# Method 2: DFS with Explicit visited Set (No Modification) 
'''
# Understand
Same as above, but with a strict constraint: Do not modify the input grid.

# Match
Pattern: DFS with a State Tracker.

Data Structure: A Set or a Boolean Matrix to keep track of visited coordinates.

# Plan
1. Initialize count = 0 and visited = set().

2. Iterate through the grid.

3. If grid[r][c] == '1' and (r, c) is not in visited:

    Increment count.

    Run dfs(r, c) to add all connected land coordinates to visited.

    
# Evaluate
Time Complexity: O(M * N).
Space Complexity: O(M * N). We now use O(M * N) extra space for the visited set in addition to the recursion stack.

'''
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        count = 0
        
        def dfs(r, c):
            if r < 0 or if c < 0 or r >= rows or c >= cols or grid[r][c] =="0" or (r, c) in visited:
                return
            
            # mark as visited
            visited.add((r, c))

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    count += 1
                    dfs(r, c)

        return count
# I implemented Method 1 because it's highly space-efficient by utilizing In-place modification, avoiding the $O(M \times N)$ overhead of an auxiliary visited structure. However, in a production environment where the input grid might be used by other services or requires thread-safety, I would opt for Method 2 to ensure the input remains immutable and free of side effects."
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]\n
# @lcpr case=end

# @lcpr case=start
# [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]\n
# @lcpr case=end

#

