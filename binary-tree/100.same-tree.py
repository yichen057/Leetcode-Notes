#
# @lc app=leetcode id=100 lang=python3
# @lcpr version=30307
#
# [100] Same Tree
#
# https://leetcode.com/problems/same-tree/description/
#
# algorithms
# Easy (66.51%)
# Likes:    12751
# Dislikes: 294
# Total Accepted:    3.3M
# Total Submissions: 4.9M
# Testcase Example:  '[1,2,3]\n[1,2,3]\n[1,2]\n[1,null,2]\n[1,2,1]\n[1,1,2]'
#
# Given the roots of two binary trees p and q, write a function to check if
# they are the same or not.
# 
# Two binary trees are considered the same if they are structurally identical,
# and the nodes have the same value.
# 
# 
# Example 1:
# 
# Input: p = [1,2,3], q = [1,2,3]
# Output: true
# 
# 
# Example 2:
# 
# Input: p = [1,2], q = [1,null,2]
# Output: false
# 
# 
# Example 3:
# 
# Input: p = [1,2,1], q = [1,1,2]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in both trees is in the range [0, 100].
# -10^4 <= Node.val <= 10^4
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
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q: return False
        if p and q is None: return False
        if p is None and q is None: return True
        # 此时p 和 q都为有值的情况了, 只需判断值是否相等
        if p.val != q.val: return False
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        result = left and right
        return result
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [1,2,3]\n[1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n[1,null,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,1]\n[1,1,2]\n
# @lcpr case=end

#

