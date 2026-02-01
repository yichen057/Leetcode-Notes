#
# @lc app=leetcode id=94 lang=python3
# @lcpr version=30307
#
# [94] Binary Tree Inorder Traversal
#
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Easy (79.60%)
# Likes:    14744
# Dislikes: 886
# Total Accepted:    3.5M
# Total Submissions: 4.4M
# Testcase Example:  '[1,null,2,3]\n[1,2,3,4,5,null,8,null,null,6,7,9]\n[]\n[1]'
#
# Given the root of a binary tree, return the inorder traversal of its nodes'
# values.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,null,2,3]
# 
# Output: [1,3,2]
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
# Output: [4,2,6,5,7,1,3,9,8]
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
# The number of nodes in the tree is in the range [0, 100].
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
# 二叉树的中序遍历: 顺序是左中右
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node):
            if node is None:
                return
            
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)
        
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

