#
# @lc app=leetcode id=105 lang=python3
# @lcpr version=30307
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (68.30%)
# Likes:    16534
# Dislikes: 621
# Total Accepted:    1.8M
# Total Submissions: 2.6M
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]\n[-1]\n[-1]'
#
# Given two integer arrays preorder and inorder where preorder is the preorder
# traversal of a binary tree and inorder is the inorder traversal of the same
# tree, construct and return the binary tree.
# 
# 
# Example 1:
# 
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
# 
# 
# Example 2:
# 
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.
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
# 中序和前序可以确定唯一的二叉树, 但是后序和前序不可以构造唯一的二叉树, 因为左右区间找不到分割点, 而中序把左右区间隔开, 天然的分割点
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 第一步: 递归终止条件: 前序数组为空, 前序若为空, 说明中序也为空, 只写前序即可
        if not preorder:
            return None
        
        # 第二步: 前序遍历的第一个元素就是当前的中间节点(根节点元素)
        root_val = preorder[0]
        root = TreeNode(root_val)

        # 第三步: 找中序数组的"中"元素的位置, 并作为切割点
        separator_idx = inorder.index(root_val)

        # 第四步: 切割中序inorder数组, 得到inorder数组的左,右半边
        inorder_left = inorder[:separator_idx]
        inorder_right = inorder[separator_idx+1:]

        # 第五步: 根据中序遍历切割后的长度，去切割前序遍历（Preorder）数组, 得到preorder数组的左,右半边
        # 前序数组的结构是：[根节点, 左子树..., 右子树...]
        #左子树：从索引1开始，长度为 len(inorder_left)，所以应该是 preorder[1 : 1+len(inorder_left)]
        #右子树：从左子树结束后开始到最后，所以应该是 preorder[1+len(inorder_left) :]
        preorder_left = preorder[1:1+len(inorder_left)]
        preorder_right = preorder[1+len(inorder_left): ]

        # 第六步: 递归
        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)

        # 第七步: 返回答案
        return root



# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [3,9,20,15,7]\n[9,3,15,20,7]\n
# @lcpr case=end

# @lcpr case=start
# [-1]\n[-1]\n
# @lcpr case=end

#

