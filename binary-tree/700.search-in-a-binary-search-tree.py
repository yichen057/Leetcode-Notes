#
# @lc app=leetcode id=700 lang=python3
#
# [700] Search in a Binary Search Tree
#
# https://leetcode.com/problems/search-in-a-binary-search-tree/description/
#
# algorithms
# Easy (82.02%)
# Likes:    6536
# Dislikes: 217
# Total Accepted:    1.3M
# Total Submissions: 1.6M
# Testcase Example:  '[4,2,7,1,3]\n2'
#
# You are given the root of a binary search tree (BST) and an integer val.
# 
# Find the node in the BST that the node's value equals val and return the
# subtree rooted with that node. If such a node does not exist, return null.
# 
# 
# Example 1:
# 
# 
# Input: root = [4,2,7,1,3], val = 2
# Output: [2,1,3]
# 
# 
# Example 2:
# 
# 
# Input: root = [4,2,7,1,3], val = 5
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 5000].
# 1 <= Node.val <= 10^7
# root is a binary search tree.
# 1 <= val <= 10^7
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Binary search tree二叉搜索树是一个有序树: 若左子树不空+根节点要比左子树的所有节点的数值都要大, 若右子树不空+根节点要比右子树的所有节点的数值都要小; 同样,左子树和右子树分别为二叉搜索树
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]: # 递归函数的参数传入的就是根节点和要搜索的数值，返回的就是以这个搜索数值所在的节点。
        # 方法一: 层序法: 本题利用了二叉搜索树的特性, 确定了遍历顺序, 无需遍历整棵树, 推荐!
        # while root:
        #     if val < root.val: # 向左搜索
        #         root = root.left
        #     elif val > root.val: # 向右搜索
        #         root = root.right
        #     else: # 此时 val = root.val
        #         return root
        # return None # 当未搜到目标值val时, 返回None
        
        # 方法二: 递归法: 二叉搜索树天然自带顺序, 其有序性决定了遍历顺序, 不涉及前中后序
        # base case : 如果root为空，或者找到这个数值了，就返回root节点。
        if not root or root.val == val: # 注: 不能写成root == val, 左边不能是node, 得是integer
            return root
        # 单层递归遍历
        result = TreeNode()
        if val < root.val:
            result = self.searchBST(root.left, val) # 注: 这里不能直接写self.searchBST(root.left, val), 此处递归函数有返回值, 得有变量(result)接返回值
        if val > root.val:
            result = self.searchBST(root.right, val)
        return result
# 方法三, 简易递归, 推荐!:
class Solution3:
    def searchBST(self, root, val):
        if not root or root.val == val:
            return root

        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

# @lc code=end

