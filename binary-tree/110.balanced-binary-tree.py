#
# @lc app=leetcode id=110 lang=python3
# @lcpr version=30307
#
# [110] Balanced Binary Tree
#
# https://leetcode.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (57.71%)
# Likes:    12078
# Dislikes: 834
# Total Accepted:    2.4M
# Total Submissions: 4.1M
# Testcase Example:  '[3,9,20,null,null,15,7]\n[1,2,2,3,3,null,null,4,4]\n[]'
#
# Given a binary tree, determine if it is height-balanced.
# 
# 
# Example 1:
# 
# Input: root = [3,9,20,null,null,15,7]
# Output: true
# 
# 
# Example 2:
# 
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# 
# 
# Example 3:
# 
# Input: root = []
# Output: true
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 5000].
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
# 平衡二叉树: 二叉树里任何一个节点, 它的左右子树的高度差不能超过1, 即<=1
# 高度: 任意一个节点和叶子节点的距离. 求高度要用后序遍历做(左右中). 叶子节点: 左右孩子都为空
# 深度: 任意一个节点和根节点的距离, 求深度要用前序遍历做(中左右)
# 
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.getHeight(root) != -1:
            return True
        else:
            return False
    # 后序递归遍历法求高度
    def getHeight(self, root: Optional[TreeNode]) -> int: # 1) 递归函数的返回类型为int, 参数是二叉树的根节点
        # 2) 递归的终止条件 Base Case
        if not root:
            return 0
        # 3) 单层递归处理逻辑: 后序遍历(左右中)
        # 左
        leftHeight = self.getHeight(root.left) # Note: python里调用函数要加self.
        if leftHeight == -1:
            return -1
        # 右
        rightHeight = self.getHeight(root.right)
        if rightHeight == -1:
            return -1
        # 中: 此时左右子树都符合平衡二叉树的条件, 就比较高度差即可
        if abs(rightHeight - leftHeight) >1:
            return -1
        else: #此时高度差也符合条件: 即左右子树的高度差<=1, 那么当前父节点的高度 = 1+左右子树高度的最大值, +1表示父节点本身的高度
            return 1 + max(rightHeight, leftHeight)
# 以下为递归法精简版:
class Solution:
    def isBalanced(self, root:Optional[TreeNode]) -> bool:
        return self.getHeight(root) != -1
    def getHeight(self, node):
        if not node:
            return 0
        leftHeight = self.getHeight(node.left)
        rightHeight = self.getHeight(node.right)
        if leftHeight == -1 or rightHeight == -1 or abs(rightHeight - leftHeight) > 1:
            return -1
        else:
            return 1+ max(leftHeight, rightHeight)
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,2,3,3,null,null,4,4]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

