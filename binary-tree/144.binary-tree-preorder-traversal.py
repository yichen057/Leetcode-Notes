#
# @lc app=leetcode id=144 lang=python3
# @lcpr version=30307
#
# [144] Binary Tree Preorder Traversal
#
# https://leetcode.com/problems/binary-tree-preorder-traversal/description/
#
# algorithms
# Easy (74.90%)
# Likes:    8784
# Dislikes: 233
# Total Accepted:    2.3M
# Total Submissions: 3.1M
# Testcase Example:  '[1,null,2,3]\n[1,2,3,4,5,null,8,null,null,6,7,9]\n[]\n[1]'
#
# Given the root of a binary tree, return the preorder traversal of its nodes'
# values.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,null,2,3]
# 
# Output: [1,2,3]
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
# Output: [1,2,4,5,6,7,3,8,9]
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
#         self.left = left # 左指针, 默认为空
#         self.right = right # 右指针, 默认为空
# 递归法三步走: 1) 确定递归函数的参数和返回值; 本题无返回值, 结果放参数里了, 参数表示每一层递归需要处理的当前的节点
#             2) 确定终止条件: 如果 node 为 None，则停止。如果你传的是数值，数值无法判断是否为“空节点”。
#             3) 确定单层递归逻辑： 在每一层取当前节点的 val，然后把左右孩子（作为新的节点）交给下一层处理。
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        # dfs函数传递的参数是节点而不是数值. 参数： 每一层递归需要处理的是“当前的节点”
        # 如果只传了 node.left.val（一个具体的数字），下一层递归就再也找不到它的左右子节点了，递归就此中断。
        def dfs(node): # node: 代表当前正在处理的整棵树的根节点
            if node is None:
                return
            
            # 前序的顺序: 中左右
            result.append(node.val) # node.value: 获取当前这棵树根节点的值
            dfs(node.left) # node.left: 代表当前节点的左子树
            dfs(node.right)
        # 调用函数
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

