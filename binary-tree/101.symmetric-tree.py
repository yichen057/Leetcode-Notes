#
# @lc app=leetcode id=101 lang=python3
# @lcpr version=30307
#
# [101] Symmetric Tree
#
# https://leetcode.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (60.60%)
# Likes:    16693
# Dislikes: 449
# Total Accepted:    2.8M
# Total Submissions: 4.6M
# Testcase Example:  '[1,2,2,3,4,4,3]\n[1,2,2,null,3,null,3]'
#
# Given the root of a binary tree, check whether it is a mirror of itself
# (i.e., symmetric around its center).
# 
# 
# Example 1:
# 
# Input: root = [1,2,2,3,4,4,3]
# Output: true
# 
# 
# Example 2:
# 
# Input: root = [1,2,2,null,3,null,3]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100
# 
# 
# 
# Follow up: Could you solve it both recursively and iteratively?
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.compare(root.left, root.right)
    # 本题采用后续递归法,即左右中, 这里的中与普通的单树遍历有所不同
#     在标准的后序遍历中，顺序是：左子树处理 -> 右子树处理 -> 中间节点处理。
# 对于这道题，我们要判断的是以两个节点（左节点 `left` 和右节点 `right`）为根的子树是否对称：
# - **左：** 先递归比较“外侧”是否对称（`left->left` 和 `right->right`）。
# - **右：** 再递归比较“内侧”是否对称（`left->right` 和 `right->left`）。
# - **中：** 最后根据外侧和内侧的比较结果，**得出当前这两个节点的整体对称结论**并向上层返回。
    # 递归条件1: 确定递归函数的参数和返回值
    def compare(self, left, right):
    # 递归条件2: 确定递归终止条件: 节点为空, 分左右子节点
    # 条件1: 左为空, 右不空, false
    # 条件2: 左不空, 右空, false
    # 条件3: 左空, 右空, true
    # 条件4: 左不空, 右不空, 且值不相等, false
    # 条件5: 左不空, 右不空, 且值相等, 向下递归遍历, 看子孩子是否相等
        if left is None and right: return False
        if left and right is None: return False
        if left is None and right is None: return True
        if left and right and left.val != right.val: return False
    # 此时就是左右节点都不为空, 且数值相同的情况, 此时再做递归, 做下一层的判断
    # 递归条件3: 处理递归单层里的逻辑--比较内外侧节点值
        outside = self.compare(left.left, right.right) #左子树：左、 右子树：右
        inside = self.compare(left.right, right.left)  #左子树：右、 右子树：左
        result = outside and inside #左子树：中、 右子树：中 （逻辑处理）
        return result
# 在 Python 中，以下情况都会被 `if not` 判定为 `True`：

# - `None`
# - `False`
# - 数字 `0`
# - 空字符串 `""`
# - 空列表 `[]`、空字典 `{}` 等
# ### 在二叉树题目中，为什么大家常用 `if not left`？

# 在算法题（如 LeetCode）中，二叉树的节点通常是一个对象 `TreeNode`。
# - 如果节点存在，它是一个对象，布尔值为 `True`。
# - 如果节点不存在，它是 `None`，布尔值为 `False`。
# **结论：** 因为二叉树节点不会变成数字 `0` 或空字符串，所以 `if not left` 等价于检查它是不是 `None`。**这种写法更简洁，符合 Python 之禅（Pythonic）。**
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [1,2,2,3,4,4,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,2,null,3,null,3]\n
# @lcpr case=end

#

