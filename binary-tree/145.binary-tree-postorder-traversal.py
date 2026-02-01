#
# @lc app=leetcode id=145 lang=python3
# @lcpr version=30307
#
# [145] Binary Tree Postorder Traversal
#
# https://leetcode.com/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Easy (77.41%)
# Likes:    7710
# Dislikes: 222
# Total Accepted:    1.9M
# Total Submissions: 2.4M
# Testcase Example:  '[1,null,2,3]\n[1,2,3,4,5,null,8,null,null,6,7,9]\n[]\n[1]'
#
# Given the root of a binary tree, return the postorder traversal of its nodes'
# values.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,null,2,3]
# 
# Output: [3,2,1]
# 
# Explanation:
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
# 
# Output: [4,6,7,5,2,9,8,3,1]
# 
# Explanation:
# 
# 
# 
# 
# Example 3:
# 
# 
# Input: root = []
# 
# Output: []
# 
# 
# Example 4:
# 
# 
# Input: root = [1]
# 
# Output: [1]
# 
# 
# 
# Constraints:
# 
# 
# The number of the nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
# 
# 
# 
# Follow up: Recursive solution is trivial, could you do it iteratively?
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

# 二叉树的后序遍历: 顺序为左右中
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            dfs(node.right)
            result.append(node.val)
        
        dfs(root)
        return result
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [1,null,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5,null,8,null,null,6,7,9]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

