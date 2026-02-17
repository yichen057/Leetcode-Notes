#
# @lc app=leetcode id=617 lang=python3
# @lcpr version=30307
#
# [617] Merge Two Binary Trees
#
# https://leetcode.com/problems/merge-two-binary-trees/description/
#
# algorithms
# Easy (78.98%)
# Likes:    9059
# Dislikes: 322
# Total Accepted:    887.6K
# Total Submissions: 1.1M
# Testcase Example:  '[1,3,2,5]\n[2,1,3,null,4,null,7]\n[1]\n[1,2]'
#
# You are given two binary trees root1 and root2.
# 
# Imagine that when you put one of them to cover the other, some nodes of the
# two trees are overlapped while the others are not. You need to merge the two
# trees into a new binary tree. The merge rule is that if two nodes overlap,
# then sum node values up as the new value of the merged node. Otherwise, the
# NOT null node will be used as the node of the new tree.
# 
# Return the merged tree.
# 
# Note: The merging process must start from the root nodes of both trees.
# 
# 
# Example 1:
# 
# Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
# Output: [3,4,5,5,4,null,7]
# 
# 
# Example 2:
# 
# Input: root1 = [1], root2 = [1,2]
# Output: [2,2]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in both trees is in the range [0, 2000].
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
# 合并二叉树, 本题考察一起操作两个二叉树的能力
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]: # 1. 参数是两个数的根节点, 返回值是合并后的根节点
        # 2. 递归终止条件
        if not root1:
            return root2
        if not root2:
            return root1 
        # 上面的递归终止条件保证了代码执行到这里root1, root2都非空
        # 3. 单层递归, 此处用前序遍历, 中序和后序也可做
        # 方法一: 前序+修改root1: 本方法直接改tree1的结构, 无需重新定义tree, 合并后的二叉树直接用tree1的结构
        # root1.val += root2.val # 中
        # root1.left = self.mergeTrees(root1.left, root2.left) # 左
        # root1.right = self.mergeTrees(root1.right, root2.right) # 右

        # return root1 #  注意: 本题我们重复使用了题目给出的节点而不是创建新节点. 节省时间, 空间. 
    
        # 方法二: 前序+新建root
        root = TreeNode() # 创建新节点. 当你写 TreeNode() 时：你没有传参数，Python 自动使用了默认值 val=0。所以此处括号里可以不写0
        # 永远不要提前创建一个“空壳”节点，而是等拿到了正确的数值后，再通过 TreeNode(correct_val) 把它生出来。
        root.val += root1.val+root2.val # 中
        root.left = self.mergeTrees(root1.left, root2.left) # 左
        root.right = self.mergeTrees(root1.right, root2.right) # 右

        return root  #注意: 本题我们创建了新节点. 


# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [1,3,2,5]\n[2,1,3,null,4,null,7]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n[1,2]\n
# @lcpr case=end

#

