#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#
# https://leetcode.com/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (73.76%)
# Likes:    6764
# Dislikes: 277
# Total Accepted:    727.8K
# Total Submissions: 984.4K
# Testcase Example:  '3'
#
# Given a positive integer n, generate an n x n matrix filled with elements
# from 1 to n^2 in spiral order.
# 
# 
# Example 1:
# 
# 
# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]
# 
# 
# Example 2:
# 
# 
# Input: n = 1
# Output: [[1]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 20
# 
# 
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # # 方法一: 定义四个边界法
        # a = [[0] * n for _ in range(n)] # 初始化 n×n 矩阵，全 0
        # top, bottom = 0, n - 1 # 定义上下边界
        # left, right = 0, n - 1 # 定义左右边界
        # x = 1 # 将要写入的数字，从 1 到 n^2

        # while left <= right and top <= bottom:
        #     # 1. 上边: 从左到右填满left -> right
        #     for i in range(left, right + 1): # j取值范围[left, right]
        #         a[top][i] = x  # 把x写到(top,j)
        #         x += 1 # 数字+1
        #     top += 1   # 上边界下移一行

        #     # 2. 右边: 从上top+1到下填bottom: top -> bottom
        #     for i in range(top, bottom + 1): # i取值范围[top+1, bottom](top是在前面已下移的)
        #         a[i][right] = x # 把x写到(i, right)
        #         x += 1
        #     right -= 1 # 右边界左移一列

        #     # 3. 下边: 从右right-1到左填left: right -> left
        #     if top <= bottom: # 画下边前：确保还有“可画的行”, 避免最后一圈重复某条边或访问越界。
        #         for i in range(right, left -1, -1): # j取值范围[right-1, left]
        #             a[bottom][i] = x
        #             x += 1
        #         bottom -= 1 #下边界上移一列

        #     # 4. 左边: 从下bottom-1到上填top+1: bottom -> top
        #     if left <= right: # 画左边前：确保还有“可画的列”, 避免最后一圈重复某条边或访问越界。
        #         for i in range(bottom, top-1, -1): # i取值范围[bottom-1, top+1], 
        #             # bottom: bottom-1是上一轮减过的, 所以本轮不用减1
        #             # top-1: 由于之前在上边时已将top处理成top+1, 所以top这里能取到的值是top-1+1=top, 实际是原始的top+1, 正好避开左上角
        #             a[i][left] = x
        #             x += 1
        #         left += 1 # 左边界右移一列

        # return a
        # # 奇数 n：最后只剩中心一个格子，仍由上边/右边的流程自然覆盖，无需特判。
        
        # 方法二: 圈数循环 + 偏移量法
        nums = [[0] * n for _ in range(n)] # 初始化 n×n 矩阵，全 0
        startx, starty = 0, 0 # 起始点
        loop, mid = n // 2, n // 2 # 迭代次数, n为奇数时, 矩阵有唯一中心点(偶数阶矩阵没有“唯一中心点)
        count = 1 # 将要写入的数字，从 1 到 n^2

        for offset in range(1, loop + 1): # 每转一圈循环一层偏移量加1，偏移量从1开始
            for i in range(starty, n-offset): # 从左至右到右边倒数第二个点，左闭右开
                nums[startx][i] = count
                count += 1
            for i in range(startx, n-offset): # 从上至下
                nums[i][n-offset] = count
                count += 1
            for i in range(n-offset, startx, -1): # 从右至左
                nums[n-offset][i] = count
                count += 1
            for i in range(n-offset, starty, -1): # 从下至上
                nums[i][starty] = count
                count += 1
            startx += 1 # 更新起始点
            starty += 1

        if n % 2 != 0: # n为奇数时，填充中心点
            nums[mid][mid]= count
        
        return nums
            

# @lc code=end

