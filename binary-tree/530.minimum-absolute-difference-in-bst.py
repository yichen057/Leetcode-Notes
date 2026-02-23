#
# @lc app=leetcode id=530 lang=python3
# @lcpr version=30400
#
# [530] Minimum Absolute Difference in BST
#
# https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/
#
# algorithms
# Easy (59.20%)
# Likes:    4726
# Dislikes: 272
# Total Accepted:    595.5K
# Total Submissions: 1M
# Testcase Example:  '[4,2,6,1,3]\n[1,0,48,null,null,12,49]'
#
# Given the root of a Binary Search Tree (BST), return the minimum absolute
# difference between the values of any two different nodes in the tree.
# 
# 
# Example 1:
# 
# Input: root = [4,2,6,1,3]
# Output: 1
# 
# 
# Example 2:
# 
# Input: root = [1,0,48,null,null,12,49]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [2, 10^4].
# 0 <= Node.val <= 10^5
# 
# 
# 
# Note: This question is the same as 783:
# https://leetcode.com/problems/minimum-distance-between-bst-nodes/
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
# 方法一: 双指针递归法: 二叉搜索树利用中序递增, 找到该树最小差值. 好处是无需转数组开辟空间
class Solution:
    def __init__(self):
        self.result = float('inf') # result记录相邻节点差值的最小值, 一开始作为基准是, 要想找比他还小的, 可以默认result初始化为最大值, 这样任意值都比它小
        self.pre = None # 定义cur的前一个指针

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.traversal(root)
        return self.result
    # 递归函数需要有返回值的情况: 返回布尔值/整数等, 返回的二叉树是否符合某一特性或返回某一节点数值或无需遍历整个二叉树, 仅遍历某一条特定路径或搜索某个节点
    def traversal(self, cur: Optional[TreeNode]) -> None: # 本题要遍历整棵二叉树且记录结果的过程中用全局变量记录, 所以无需递归函数有返回值
        # Base case
        if cur is None:
            return
        self.traversal(cur.left) # 左
        # 中: 比较相邻节点差值, result记录最小差值
        if self.pre is not None:
            self.result = min(self.result, cur.val - self.pre.val)
        self.pre = cur # 如何让pre紧跟cur, 使pre指向cur的前一个节点: 此时pre==None时, 把第一个节点cur给pre, 第一个节点无需左两个节点的相减
        self.traversal(cur.right) # 右

# 方法二: 创建数组递归法, 二叉搜索树利用中序递增. 本题不是要求相邻最小, 但用中序转成数组后肯定相邻最小, 因为数组是有序递增的. 又因为是递增的, 所以不用管绝对值的问题, 因为当前值-前一位的值的大小一定大于0
class Solution: 
    def __init__(self):
        self.vec = []
    
    def traversal(self, root) -> None:
        if root is None: 
            return
        self.traversal(root.left) # 左
        self.vec.append(root.val) # 中, 将二叉搜索树转换为有序数组
        self.traversal(root.right) # 右
    
    def getMinimumDifference(self, root) ->int:
        result = float('inf') # result 记录相邻节点差值的最小值, 作为基准数, 因此设最大值
        self.vec = [] # 清空数组

        self.traversal(root) # 先进行中序遍历填充数组
        # 遍历完后再判断长度, 根据题意, 树中至少有2个节点, 此步可不写写了更严谨
        if len(self.vec) < 2: # 注: 这一步容易漏掉, 1. 求最小绝对差, 不能少于两个元素; 2. 必须先调用traversal()函数使得vec内有值, 才能判断数组的长度
            return 0
        # 此时vec是有序升序数组, 直接计算相邻差值
        for i in range(1, len(self.vec)): # 从1开始是因为后面要[i-1]求前一位的值, 不能越界
            result = min(result, self.vec[i] - self.vec[i-1])

        return result

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [4,2,6,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,0,48,null,null,12,49]\n
# @lcpr case=end

#

