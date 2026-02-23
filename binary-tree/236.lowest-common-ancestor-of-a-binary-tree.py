#
# @lc app=leetcode id=236 lang=python3
# @lcpr version=30400
#
# [236] Lowest Common Ancestor of a Binary Tree
#
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
#
# algorithms
# Medium (68.73%)
# Likes:    18535
# Dislikes: 487
# Total Accepted:    2.5M
# Total Submissions: 3.6M
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n' +
  '5\n' +
  '1\n' +
  '[3,5,1,6,2,0,8,null,null,7,4]\n' +
  '5\n' +
  '4\n' +
  '[1,2]\n' +
  '1\n' +
  '2'
#
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes
# in the tree.
# 
# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes p and q as the lowest node in T that has both p
# and q as descendants (where we allow a node to be a descendant of
# itself).”
# 
# 
# Example 1:
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
# 
# 
# Example 2:
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant
# of itself according to the LCA definition.
# 
# 
# Example 3:
# 
# Input: root = [1,2], p = 1, q = 2
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [2, 10^5].
# -10^9 <= Node.val <= 10^9
# All Node.val are unique.
# p != q
# p and q will exist in the tree.
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
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 本题需要看代码随想录网站, 看图解更清晰https://programmercarl.com/0236.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%9C%80%E8%BF%91%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88.html#%E6%80%9D%E8%B7%AF
# 这道题目刷过的同学未必真正了解这里面回溯的过程，以及结果是如何一层一层传上去的。那么我给大家归纳如下三点：
# 求最小公共祖先，需要从底向上遍历，那么二叉树，只能通过后序遍历（即：回溯）实现从底向上的遍历方式。
# 在回溯的过程中，必然要遍历整棵二叉树，即使已经找到结果了，依然要把其他节点遍历完，因为要使用递归函数的返回值（也就是代码中的left和right）做逻辑判断。
# 要理解如果返回值left为空，right不为空为什么要返回right，为什么可以用返回right传给上一层结果。
# 可以说这里每一步，都是有难度的，都需要对二叉树，递归和回溯有一定的理解。
# 本题没有给出迭代法，因为迭代法不适合模拟回溯的过程。理解递归的解法就够了
# 本题的已知三个重要条件: 1) 所有节点的值都唯一不重复 2) p/q为不同节点且一定存在于给定的二叉树中 3) LCA可以为节点本身
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode': # 本题递归函数有返回值是因为遍历了搜索整个树，直接用一个变量left、right接住返回值，这个left、right后序还有逻辑处理的需要，也就是后序遍历中处理中间节点的逻辑（也是回溯）。
        # 遍历整棵树
        # base case
        if root is None:
            return root # 或者返回None也可以
        if root == p or root == q:# 只要发现目标，就原地交卷并向上汇报。至于我是不是最终答案，让上面的节点去比对.
            # 对于父节点来说，它只需要知道 left 或 right 返回的是一个非空值。只要是非空，就意味着那棵子树里涵盖了目标。至于具体是哪一个，会在父节点的“中”逻辑里结合两边的返回结果统一判断。
            return root
        # 单层后序遍历递归: 自下向上找, 左右中, 天然的回溯过程
        # 左
        left = self.lowestCommonAncestor(root.left, p, q) # left和right是TreeNode type
        # 右
        right = self.lowestCommonAncestor(root.right, p, q)
        # 中
        if left is not None and right is not None: # 不是左子树有p/q就是右子树有p/q
            return root
        
        if left is None and right is not None: #如果left为空(left无p or q)，right不为空(right有p or q)，就返回right，说明目标节点是通过right返回的，反之依然。
            return right
        elif left is not None and right is None:
            return left
        else: # 如果left和right都为空，则返回left或者right都是可以的，也就是返回空。
            return None
        
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [3,5,1,6,2,0,8,null,null,7,4]\n5\n1\n
# @lcpr case=end

# @lcpr case=start
# [3,5,1,6,2,0,8,null,null,7,4]\n5\n4\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n1\n2\n
# @lcpr case=end

#

