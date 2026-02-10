#
# @lc app=leetcode id=404 lang=python3
# @lcpr version=30307
#
# [404] Sum of Left Leaves
#
# https://leetcode.com/problems/sum-of-left-leaves/description/
#
# algorithms
# Easy (62.33%)
# Likes:    5769
# Dislikes: 323
# Total Accepted:    773.8K
# Total Submissions: 1.2M
# Testcase Example:  '[3,9,20,null,null,15,7]\n[1]'
#
# Given the root of a binary tree, return the sum of all left leaves.
# 
# A leaf is a node with no children. A left leaf is a leaf that is the left
# child of another node.
# 
# 
# Example 1:
# 
# Input: root = [3,9,20,null,null,15,7]
# Output: 24
# Explanation: There are two left leaves in the binary tree, with values 9 and
# 15 respectively.
# 
# 
# Example 2:
# 
# Input: root = [1]
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 1000].
# -1000 <= Node.val <= 1000
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
# 本题采用后序递归遍历, 代码相对间接. 为了层层自下而上返回. 收集了左子树的左叶子之和A, 及右子树的左叶子之和B, 然后返回给上一层父节点的左叶子之和: A+B
# 要注意的是, 本题不能遍历到最底层的叶子节点, 因为无法知道它是不是左叶子, 只能判断是不是叶子节点, 所以只能遍历到倒数第二层, 它的left才是左叶子
# 你不需要保证它们在同一层。**递归法是通过“分治”思想**，把整棵树拆成左、右两部分分别计算，最后把两部分的结果**加在一起**。只要每个子树都正确计算了自己内部的左叶子，总和就一定是正确的。
# 即如何准确抓住“左叶子”？本题递归法并不是在进入子节点后才知道它是左叶子，而是在父节点层级进行判断的。only when the current node is a parent can it be checked if its child is a left leaf. 
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int: # 函数返回类型是int, 参数是需要处理的节点
        
        # 递归的终止条件 Base case. 本题有两个base case, 第二个可以不写
        if not root:
            return 0
        if not root.left and not root.right: # This line is optional: omitting it would not affect the result, but it would cause the recursion to go one layer deeper.Define the logic for a single level of recursion
            return 0 # 遇到叶子节点返回0是因为它收集的是左子树之和0与右子树之和0的相加, 返回给这个叶子节点(即根节点), 此时根节点为0. if the current node traversed is a leaf node, then its left leaf must also be 0. 
        
        # 单层递归: 左右中. 递归会自动深入到每一层。
        # 左, leftSum: 代表左子树里所有的左叶子之和. 在处理左子树时，它只会找左子树范围内的左叶子
        if root.left is not None and root.left.left is None and root.left.right is None: # Left subtree is a left leaf
            leftSum = root.left.val
        else:
            leftSum = self.sumOfLeftLeaves(root.left)
        # 右, rightSum: 代表右子树里所有的左叶子之和
        rightSum = self.sumOfLeftLeaves(root.right)
        # 中 Root
        sum = leftSum + rightSum
        return sum


        
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

