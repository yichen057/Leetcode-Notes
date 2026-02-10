#
# @lc app=leetcode id=222 lang=python3
# @lcpr version=30307
#
# [222] Count Complete Tree Nodes
#
# https://leetcode.com/problems/count-complete-tree-nodes/description/
#
# algorithms
# Easy (71.91%)
# Likes:    9421
# Dislikes: 606
# Total Accepted:    1.1M
# Total Submissions: 1.6M
# Testcase Example:  '[1,2,3,4,5,6]\n[]\n[1]'
#
# Given the root of a complete binary tree, return the number of the nodes in
# the tree.
# 
# According to Wikipedia, every level, except possibly the last, is completely
# filled in a complete binary tree, and all nodes in the last level are as far
# left as possible. It can have between 1 and 2^h nodes inclusive at the last
# level h.
# 
# Design an algorithm that runs in less than O(n) time complexity.
# 
# 
# Example 1:
# 
# Input: root = [1,2,3,4,5,6]
# Output: 6
# 
# 
# Example 2:
# 
# Input: root = []
# Output: 0
# 
# 
# Example 3:
# 
# Input: root = [1]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 5 * 10^4].
# 0 <= Node.val <= 5 * 10^4
# The tree is guaranteed to be complete.
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
# 满二叉树: 每一层都必须排满, 除了根节点外, 每一层的节点数一定是偶数: 2^n-1, n为深度
# 完全二叉树: 1) 层数: 除了最后一层外, 其他层都是满状态节点数达到最大值; 2) 排列: 最后一层的节点必须从左至右连续排列, 中间不能有空隙, 对最后一层的节点数无要求
# 完全二叉树求节点数量, 用后序递归遍历法. 时间复杂度虽然依然是O(n), 但是未遍历所有节点, 中检侧的节点都未遍历, 值遍历了左右两侧的节点计算深度. 如果左右外侧的高度相同说明是满二叉树, 用满二叉树的公式计算数的节点数2^n-1
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # Base Case 1
        if not root:
            return 0
        # Base Case 2: 左右两侧高度相同说明是满二叉树, 无需每个节点都遍历, 中间侧的节点无需遍历
        # 通过判断子树外侧的节点数,若左右侧深度相等则直接用满二叉树的公式2^n-1,其中n表示深度,返回子树的节点数给父节点
        # 最终的叶子节点一定是满二叉树, 高度为1, 节点数=2^n-1 = 2-1 = 1
        left = root.left
        right = root.right
        leftDepth = 1 # 初始化改为1而不是0, 指的是初始化就包含根节点root本身这一层
        rightDepth = 1
        # 左侧遍历统计左侧深度
        while left:
            left = left.left
            leftDepth += 1
        # 计算右侧深度
        while right:
            right = right.right
            rightDepth += 1
        if leftDepth == rightDepth: # 说明是一个满二叉树, 可利用公式计算子树的节点数量
            return (1 << leftDepth) - 1 # 即表示(1*2^leftDepth) -1, 符合满二叉树的节点个数公式2^n-1, n为深度
        
        # 单层递归逻辑(后序遍历): 此时左右外侧高度不相等, 不是满二叉树, 需要向下遍历继续递归. 该逻辑放在单层处理递归逻辑内, 不属于base case 2 
        # left
        leftNum= self.countNodes(root.left) # root.left是直接从当前节点root身上取出的左孩子节点. 无论前面的局部变量left怎么变，root.left始终指向当前节点的左孩子
        # right
        rightNum = self.countNodes(root.right)
        # middle
        result = leftNum + rightNum + 1 
        return result

# 对于普通二叉树的计算节点数, 可用后序递归遍历. 时间复杂度为O(n), 每个节点都遍历了一遍
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # Base Case
        if not root:
            return 0
        # 单层递归逻辑 (后序遍历: 左右中)
        leftNum = getNum(root.left) # left
        rightNum = getNum(root.right) # right
        result = leftNum + rightNum + 1 # middle, +1表示根节点本身的层高
        return result
    
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [1,2,3,4,5,6]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

