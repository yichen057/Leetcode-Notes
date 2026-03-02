#
# @lc app=leetcode id=235 lang=python3
# @lcpr version=30400
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
#
# algorithms
# Medium (70.07%)
# Likes:    12203
# Dislikes: 357
# Total Accepted:    2.2M
# Total Submissions: 3.1M
# Testcase Example:  '[6,2,8,0,4,7,9,null,null,3,5]\n' +
  '2\n' +
  '8\n' +
  '[6,2,8,0,4,7,9,null,null,3,5]\n' +
  '2\n' +
  '4\n' +
  '[2,1]\n' +
  '2\n' +
  '1'
#
# Given a binary search tree (BST), find the lowest common ancestor (LCA) node
# of two given nodes in the BST.
# 
# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes p and q as the lowest node in T that has both p
# and q as descendants (where we allow a node to be a descendant of
# itself).”
# 
# 
# Example 1:
# 
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
# 
# 
# Example 2:
# 
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant
# of itself according to the LCA definition.
# 
# 
# Example 3:
# 
# Input: root = [2,1], p = 2, q = 1
# Output: 2
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
# p and q will exist in the BST.
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

class Solution:
    # 方法一: 递归法: 有左右遍历即可, 这里不涉及中
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode': # 返回值是最近公共祖先LCA
        # Base case
        if root is None:
            return None
        # 单层递归 Single layer recursion, 利用bts的有序性: 遍历的节点比p和q都大, LCA在左子树里, 向左遍历; 反之LCA在右子树, 向右遍历
        # 在 BST 中，从根节点到 LCA 的路径是唯一的：如果当前节点值比 $p, q$ 都大，LCA 必在左边。如果当前节点值比 $p, q$ 都小，LCA 必在右边。
        # 一旦不满足上述两条（即当前值在 $[p, q]$ 之间），当前节点就是 LCA，直接返回。具体原因见底部.
        # 这就意味着，如果你进入了左子树（left = traversal(cur.left, p, q)），并且它返回了一个非空值，说明它在左子树的深处已经触发了第 3 条规则（找到了终点）。根据递归的特性，这个结果会像回声一样直接传回来。
        # left
        if root.val > p.val and root.val > q.val: # 向左子树搜索找LCA, 因为递归函数有返回值, 所以得有变量接住
            left = self.lowestCommonAncestor(root.left, p, q) # left和right的数据类型是TreeNode
            if left is not None: # 搜索一条边的写法，遇到递归函数的返回值，如果不为空，立刻返回。
                return left # 左子树找到了LCA
        # right
        if root.val < p.val and root.val < q.val:
            right = self.lowestCommonAncestor(root.right, p, q)
            if right is not None:
                return right
        # 剩下的情况: 当前节点一定在p和q之间, 当p<root<q时, root一定是p和q的LCA
        # 因为p在root的左子树, q在root的右子树里. 如果继续向左遍历, 那么root将错过q; 如果继续向右遍历, 那么root将错过p. 所以只有root才能链接p和q, 此时root是p和q的LCA
        return root

    # 方法二: 迭代法
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode': # 返回值是最近公共祖先LCA
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root
        return None # 在技术上是有必要写的，但从业务逻辑上几乎永远不会被执行到。
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [6,2,8,0,4,7,9,null,null,3,5]\n2\n8\n
# @lcpr case=end

# @lcpr case=start
# [6,2,8,0,4,7,9,null,null,3,5]\n2\n4\n
# @lcpr case=end

# @lcpr case=start
# [2,1]\n2\n1\n
# @lcpr case=end

#

