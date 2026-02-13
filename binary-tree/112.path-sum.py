#
# @lc app=leetcode id=112 lang=python3
# @lcpr version=30307
#
# [112] Path Sum
#
# https://leetcode.com/problems/path-sum/description/
#
# algorithms
# Easy (54.35%)
# Likes:    10629
# Dislikes: 1212
# Total Accepted:    2.1M
# Total Submissions: 3.8M
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,null,1]\n22\n[1,2,3]\n5\n[]\n0'
#
# Given the root of a binary tree and an integer targetSum, return true if the
# tree has a root-to-leaf path such that adding up all the values along the
# path equals targetSum.
# 
# A leaf is a node with no children.
# 
# 
# Example 1:
# 
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true
# Explanation: The root-to-leaf path with the target sum is shown.
# 
# 
# Example 2:
# 
# Input: root = [1,2,3], targetSum = 5
# Output: false
# Explanation: There are two root-to-leaf paths in the tree:
# (1 --> 2): The sum is 3.
# (1 --> 3): The sum is 4.
# There is no root-to-leaf path with sum = 5.
# 
# 
# Example 3:
# 
# Input: root = [], targetSum = 0
# Output: false
# Explanation: Since the tree is empty, there are no root-to-leaf paths.
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000
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
# 递归法: 前中后序都可, 因为不涉及中节点的处理. 没必要遍历所有节点, 只要找到一条符合的路径, 直接原地返回即可, 所有返回类型bool
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None: # 注意, 得先判断root是否为空. 因为如果root为空又先访问root.left, 会报错
            return False
        return self.traversal(root, targetSum - root.val) # target减去当前节点的值, 把根节点（root）处理掉，然后开启递归.traversal 接收到的 count 已经是扣除 root 后的“余额”了
    # 根节点没有爸爸，所以由主函数负责扣除。子节点都有爸爸，所以由它们的父节点在递归前负责扣除。
    # 这样一来，每个节点都在它作为“孩子”被拉进递归的那一刻被扣除且仅被扣除一次
    def traversal(self, cur:TreeNode, count:int) -> bool:
        # 递归的终止条件: 遇到叶子节点+遇到一个节点就做减法, 到叶子节点时余额已被减为0 (说明沿路节点相加=targetSum)
        if not cur.left and not cur.right and count == 0 :
            return True
        if not cur.left and not cur.right and count != 0:# 遇到叶子节点但余额不为0则返回False
            return False
       
       # 单层递归逻辑: 
       # 左
        if cur.left:
            count -= cur.left.val 
            if self.traversal(cur.left, count): # 递归, 此时的count是减掉了父节点和左节点的值
                return True # 左方向有符合条件的路径, 要把true继续向上返回, 直到根节点
            count += cur.left.val # 回溯, 回到原target-root.val的值. 之所以用回溯, 是因为后面还要用这个变量
        # 右
        if cur.right:
            count -= cur.right.val
            if self.traversal(cur.right, count): # 递归
                return True
            count += cur.right.val # 回溯
            # if traversal(cur.right, count-cur.right.val): return True # 精简语句, 包含了回溯, 未改变count的值
        return False

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [5,4,8,11,null,13,4,7,2,null,null,null,1]\n22\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n5\n
# @lcpr case=end

# @lcpr case=start
# []\n0\n
# @lcpr case=end

#

