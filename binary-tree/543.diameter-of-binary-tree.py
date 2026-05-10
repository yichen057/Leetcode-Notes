#
# @lc app=leetcode id=543 lang=python3
# @lcpr version=30403
#
# [543] Diameter of Binary Tree
#
# https://leetcode.com/problems/diameter-of-binary-tree/description/
#
# algorithms
# Easy (65.46%)
# Likes:    15729
# Dislikes: 1251
# Total Accepted:    2.5M
# Total Submissions: 3.8M
# Testcase Example:  '[1,2,3,4,5]\n[1,2]'
#
# Given the root of a binary tree, return the length of the diameter of the
# tree.
# 
# The diameter of a binary tree is the length of the longest path between any
# two nodes in a tree. This path may or may not pass through the root.
# 
# The length of a path between two nodes is represented by the number of edges
# between them.
# 
# 
# Example 1:
# 
# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
# 
# 
# Example 2:
# 
# Input: root = [1,2]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 10^4].
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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0 # 记录全局最大直径, 是目前为止见过的最大直径。

        def depth(node): # 返回：当前节点往下的最大深度, 返回以 node 为根节点的这棵子树的最大深度
            if not node:
                return 0
            
            left = depth(node.left) # left = 当前节点左子树的最大深度
            right = depth(node.right) # right = 当前节点右子树的最大深度

            self.ans = max(self.ans, left + right) # 更新的是直径
            # 当前节点左边能走多深 + 右边能走多深，就是“经过当前节点”的最长路径。拿它和已经记录的最大直径比较，保留更大的。
            # 这里是在给 ans 重新赋值。不是修改原来的整数对象。整数 int 在 Python 里是不可变的，不能像 list 一样 append。所以需要：nonlocal ans 或者用self.ans
            
            return max(left, right) + 1 # 返回给父节点的也就是“从当前节点往下走的最大深度”。不能返回 left + right, 因为不能同时走左边和右边。
            # 返回给父节点时，只能选择左边或右边更深的一条路，再加上当前节点。
            # 一棵树的最大深度就是: 左子树最大深度 和 右子树最大深度 里更大的那个 + 当前节点这一层
        depth(root)
        return self.ans
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

#

