#
# @lc app=leetcode id=637 lang=python3
# @lcpr version=30307
#
# [637] Average of Levels in Binary Tree
#
# https://leetcode.com/problems/average-of-levels-in-binary-tree/description/
#
# algorithms
# Easy (74.69%)
# Likes:    5543
# Dislikes: 351
# Total Accepted:    721.1K
# Total Submissions: 965.5K
# Testcase Example:  '[3,9,20,null,null,15,7]\n[3,9,20,15,7]'
#
# Given the root of a binary tree, return the average value of the nodes on
# each level in the form of an array. Answers within 10^-5 of the actual answer
# will be accepted.
# 
# Example 1:
# 
# Input: root = [3,9,20,null,null,15,7]
# Output: [3.00000,14.50000,11.00000]
# Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5,
# and on level 2 is 11.
# Hence return [3, 14.5, 11].
# 
# 
# Example 2:
# 
# Input: root = [3,9,20,15,7]
# Output: [3.00000,14.50000,11.00000]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 10^4].
# -2^31 <= Node.val <= 2^31 - 1
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 本题就是层序遍历的时候把一层求个总和再取一个均值。
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        queue = collections.deque([root])
        result = []
        while queue:
            level = []
            level_sum = 0
            level_size = len(queue)
            for i in range(level_size):
                cur = queue.popleft()
                level.append(cur.val)
                level_sum += cur.val # 注意: 此处每层的sum是加node的值,  而不是加1
                # if i == level_size-1: # 算每层的平均值, 不用判断是否是最后一个值, 而是直接在一层遍历完后算平均值即可!
                #     level_avg = level_sum / level_size
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            #result.append(level_avg)
            result.append(level_sum/level_size)
        return result
    

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here


#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [3,9,20,15,7]\n
# @lcpr case=end

#

