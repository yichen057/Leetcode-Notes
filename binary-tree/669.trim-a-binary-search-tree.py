#
# @lc app=leetcode id=669 lang=python3
# @lcpr version=30403
#
# [669] Trim a Binary Search Tree
#
# https://leetcode.com/problems/trim-a-binary-search-tree/description/
#
# algorithms
# Medium (66.71%)
# Likes:    6106
# Dislikes: 266
# Total Accepted:    348.7K
# Total Submissions: 522.6K
# Testcase Example:  '[1,0,2]\n1\n2\n[3,0,4,null,2,null,null,1]\n1\n3'
#
# Given the root of a binary search tree and the lowest and highest boundaries
# as low and high, trim the tree so that all its elements lies in [low, high].
# Trimming the tree should not change the relative structure of the elements
# that will remain in the tree (i.e., any node's descendant should remain a
# descendant). It can be proven that there is a unique answer.
# 
# Return the root of the trimmed binary search tree. Note that the root may
# change depending on the given bounds.
# 
# 
# Example 1:
# 
# Input: root = [1,0,2], low = 1, high = 2
# Output: [1,null,2]
# 
# 
# Example 2:
# 
# Input: root = [3,0,4,null,2,null,null,1], low = 1, high = 3
# Output: [3,2,null,1]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 10^4].
# 0 <= Node.val <= 10^4
# The value of each node in the tree is unique.
# root is guaranteed to be a valid binary search tree.
# 0 <= low <= high <= 10^4
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# 如果不对递归有深刻的理解，本题有点难 单纯移除一个节点那还不够，要修剪！
# 修剪二叉搜索树
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
''' 
UMPIRE template

  # Understand
inputs:root of binary search tree
outputs:trimed root of binary search tree, so that each node.val within the range [low, high]
constraints:
edge cases:if root is None, return None

  # Match (any problems this reminds you of, any helpful patters to solve this e.g. two pointer technique, any data structures this reminds you of )
BST, left < root < right
DFS recursion, pre-order: root->left->right
  # Plan (pseudocode)
1) edge case
2) Recursion: 
root: check its value and utilize the characteristics of BST: 
    < low: its right children maybe within the range(> low), return right; 
    > high: its left children maybe within the range(< high), return left.
left: traversal(root.left, low, high)
right: traversal(root.right, low, high)
3) finally return root
  # Implement (python code)

  # Review (dry run of your code)

  # Evaluate (time and space complexity)
  For the recursion method, the complexity is as follows:
  TC: O(n), where n is the number of nodes in the tree. In the worst case, we visit every node once.
  SC: O(H), where H is the height of the tree. In the "worst case" for a tree's height is when it is completely skewed (essentially becoming a linked list).
•	Skewed Tree: If every node only has a left child, the height H equals N. The recursion stack will push N function calls onto the stack before hitting the None base case. Thus, Space = O(N).
•	Balanced Tree: In a best-case/average-case scenario where the tree is balanced, H = log N. Thus, Space = O(log N).

The space complexity is O(H) due to the call stack. If we were worried about stack depth, we could implement this iteratively to bring the space down to O(1). 
This shows you know both without wasting time writing the more complex version unless they ask for it.
'''
# Recursion method
# class Solution:
#     def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
#         # 1. edge case
#         if root is None:
#             return None
#         # recursion (trim BST):pre-order: root->left->right
#         # root recursion:
#         # 移除不满足条件的节点, 但其对应的左右孩子不能移除, 需要继续判断
#          # 2. If root value is less than low, the entire left subtree is out of range.
#         # We discard root and its left child, then return the result of trimming the right child.
#         if root.val < low:
#             right = self.trimBST(root.right, low, high)
#             return right 
#         # 注意这里不能直接return root.right, 因为节点的右孩子不一定都符合区间内

#          # 3. If root value is greater than high, the entire right subtree is out of range.
#         # We discard root and its right child, then return the result of trimming the left child.
#         if root.val > high:
#             left = self.trimBST(root.left, low, high)
#             return left # 即A的左孩子返回给A的父节点, 因此将A删除, 即root的右孩子A变成了None
        
#         # 4. If root is within [low, high], we recursively trim its left and right children.
#         # left and right recursion
#         root.left = self.trimBST(root.left, low, high)
#         root.right = self.trimBST(root.right, low, high)

#         return root

# Iteration method: no recursion and no extra stack, making it O(1) space complexity
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        
         # 1. Find the new root that is within [low, high]
        while root and (root.val < low or root.val >high):
            if root.val < low:
                root = root.right
            else:
                root = root.left

         # 2. 此时root已经在[L, R] 范围内，处理左孩子元素小于low的情况, skip the too-small node. Trim the left subtree
        curr = root
        while curr:
            while curr.left and curr.left.val < low:
                curr.left = curr.left.right # skip the too-small node
            curr = curr.left # move the curr pointer

         # 3. 此时root已经在[L, R] 范围内，处理右孩子大于high的情况, skip the too-large node. Trim the right subtree
        curr = root
        while curr: 
            while curr.right and curr.right.val > high:
                curr.right = curr.right.left # skip the too-large node
            curr = curr.right # move the curr pointer
        
        return root

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [1,0,2]\n1\n2\n
# @lcpr case=end

# @lcpr case=start
# [3,0,4,null,2,null,null,1]\n1\n3\n
# @lcpr case=end

#

