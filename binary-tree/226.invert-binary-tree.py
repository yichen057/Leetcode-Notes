#
# @lc app=leetcode id=226 lang=python3
# @lcpr version=30307
#
# [226] Invert Binary Tree
#
# https://leetcode.com/problems/invert-binary-tree/description/
#
# algorithms
# Easy (79.76%)
# Likes:    15104
# Dislikes: 252
# Total Accepted:    2.9M
# Total Submissions: 3.7M
# Testcase Example:  '[4,2,7,1,3,6,9]\n[2,1,3]\n[]'
#
# Given the root of a binary tree, invert the tree, and return its root.
# 
# 
# Example 1:
# 
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
# 
# 
# Example 2:
# 
# Input: root = [2,1,3]
# Output: [2,3,1]
# 
# 
# Example 3:
# 
# Input: root = []
# Output: []
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:# 1)确定递归函数的参数和返回值: 参数就是要传入节点的指针，不需要其他参数了，通常此时定下来主要参数，如果在写递归的逻辑中发现还需要其他参数的时候，随时补充。返回值的话其实也不需要，但是题目中给出的要返回root节点的指针，可以直接使用题目定义好的函数，所以就函数的返回类型为TreeNode。
        # 方法一: 层序法
        # if not root:
        #     return root
        # queue = collections.deque([root])
        # while queue:
        #     cur = queue.popleft()
        #     cur.left, cur.right = cur.right, cur.left # 交换root的两个子节点
        #     if cur.left:
        #         queue.append(cur.left)
        #     if cur.right:
        #         queue.append(cur.right)
        # return root
        # 方法二: 递归法(本题适合用前序或后序遍历, 不适合用中序, 因为中序在处理时会写成左中左, 而不是左中右, 比较麻烦)
        # 此处用前序法(中左右)
        # 2) 递归终止条件: 碰到空节点停止遍历
        if not root:
            return root
        # 3) 确定单层递归的逻辑
        root.left, root.right = root.right, root.left # 中
        self.invertTree(root.left) # 左
        self.invertTree(root.right) # 右
        return root

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [4,2,7,1,3,6,9]\n
# @lcpr case=end

# @lcpr case=start
# [2,1,3]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

