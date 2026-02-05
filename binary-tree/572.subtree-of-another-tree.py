#
# @lc app=leetcode id=572 lang=python3
# @lcpr version=30307
#
# [572] Subtree of Another Tree
#
# https://leetcode.com/problems/subtree-of-another-tree/description/
#
# algorithms
# Easy (51.14%)
# Likes:    8834
# Dislikes: 595
# Total Accepted:    1.2M
# Total Submissions: 2.4M
# Testcase Example:  '[3,4,5,1,2]\n[4,1,2]\n[3,4,5,1,2,null,null,null,null,0]\n[4,1,2]'
#
# Given the roots of two binary trees root and subRoot, return true if there is
# a subtree of root with the same structure and node values of subRoot and
# false otherwise.
# 
# A subtree of a binary tree tree is a tree that consists of a node in tree and
# all of this node's descendants. The tree tree could also be considered as a
# subtree of itself.
# 
# 
# Example 1:
# 
# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true
# 
# 
# Example 2:
# 
# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the root tree is in the range [1, 2000].
# The number of nodes in the subRoot tree is in the range [1, 1000].
# -10^4 <= root.val <= 10^4
# -10^4 <= subRoot.val <= 10^4
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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # 只要 root 没了，就必须 return，不能让它往下走
        # 下面两句等价于:
        # if root is None:
        #   if subRoot is None:
        #     return True
        # else:
        #     return False
        #或者等价于:
        # if root is None and subRoot is None:
        #     return True
        # if root is None: # 走到这里说明 subRoot 肯定不是 None
        #     return False
        if root is None:
            return subRoot is None 
        # 此时root不为空. 先判断自己: 以当前root作为起点的二叉树, 是否和subRoot相同
        if self.isSameTree(root, subRoot):
            return True
        # 如果自己不是, 就去左子树里找有没有符合要求的, 还没找到就去右子树里找
        # root.left 不是完全等于 subRoot，但 root.left 的某个更深节点处有一棵子树等于 subRoot。
        # isSameTree(root.left, subRoot) 会直接返回 False，而 isSubtree(root.left, subRoot) 会继续往下找。
        # 所以这里必须递归调用 isSubtree，而不是 isSameTree。
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool: # 可以简写为: def isSameTree(self, p: TreeNode, q: TreeNode)
        if p is None and q is None:# 这里判断了 p 和 q 同时为空的情况 # 这里如果同一个节点被共享, 那么q is q, 所以这句也可以写成if p is q: # 同一个对象（包含两个都是 None）
            return True
        if p is None or q is None: # 这里判断了 p 和 q 其中一个为空的情况: p为空, q不空;p不空, q为空
            return False
        # 此时p and q 是不为空的
        if p.val != q.val:
            return False
        # 此时p and q不为空且值相等,向下遍历判断左子和右子节点是否相同
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [3,4,5,1,2]\n[4,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,4,5,1,2,null,null,null,null,0]\n[4,1,2]\n
# @lcpr case=end

#

