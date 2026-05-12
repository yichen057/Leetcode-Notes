#
# @lc app=leetcode id=538 lang=python3
# @lcpr version=30403
#
# [538] Convert BST to Greater Tree
#
# https://leetcode.com/problems/convert-bst-to-greater-tree/description/
#
# algorithms
# Medium (71.63%)
# Likes:    5420
# Dislikes: 183
# Total Accepted:    357.6K
# Total Submissions: 499.3K
# Testcase Example:  '[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]\n[0,null,1]'
#
# Given the root of a Binary Search Tree (BST), convert it to a Greater Tree
# such that every key of the original BST is changed to the original key plus
# the sum of all keys greater than the original key in BST.
# 
# As a reminder, a binary search tree is a tree that satisfies these
# constraints:
# 
# 
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.
# 
# 
# 
# Example 1:
# 
# Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
# Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
# 
# 
# Example 2:
# 
# Input: root = [0,null,1]
# Output: [1,null,1]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 10^4].
# -10^4 <= Node.val <= 10^4
# All the values in the tree are unique.
# root is guaranteed to be a valid binary search tree.
# 
# 
# 
# Note: This question is the same as 1038:
# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
# from common.node import *

# 递归法：
# TC: O(n)
# SC: O(h)  栈里最多存一条从根到叶子的路径，h 是树的高度。来自系统递归调用栈
# 具体看树形:
# Balanced BST: h = log n，所以空间 O(log n)
# Skewed BST: h = n，所以空间 O(n)

# 迭代法：
# TC: O(n)
# SC: O(h)  来自手动 stack
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 由于累加树的要求是“每个节点的新值 = 大于等于它的所有节点值之和”，而在 BST 中，比当前节点大的值都在右边。因此，我们需要按照 “右 -> 中 -> 左” 的顺序来遍历。
# 递归法DFS, reverse in-order traversal:
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.curSum = 0 # curSum是记录前一个节点的数值, global variable
        # curSum要在所有递归调用之间共享, 递归过程中需要“持续累计/共享”的变量，不能放在递归函数内部初始化。
        # curSum = 0 不能直接写在 traversal 里面，原因是：递归每进入一次 traversal，都会重新执行一遍 pre = 0，这样累计和会被重置，结果就错了。

        def traversal(cur): # 遍历整个二叉树, 遍历过程中更新节点数. 无返回值
            if cur is None:
                return 
      
            # post-order: right->mid->left
            # starting from right: because every value in the right subtree is greater than the root (Due to the definition of a BST)
            # right
            traversal(cur.right) 

            # mid
            cur.val += self.curSum # 既然用了 self.curSum，那就全程用 self.curSum. 如果不用self.curSum就得声明nonlocal curSum
            self.curSum = cur.val # curSum要把cur.val记录下以便于cur指向下一个节点, pre能指向它的前一个节点的数值

            # left
            traversal(cur.left) 

        traversal(root)
        return root

# 迭代法
# class Solution:
#     def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         stack = []
#         cur = root
#         pre = 0 # 记录前一个累加后的数值. 依次类推，pre 永远带着“所有比当前节点大的值之和

#         while cur or stack: # 只要当前还有节点可走，或者栈里还有没处理的节点，就继续。
#             # cur 负责“继续往右/左走", stack 负责“回来处理之前路过的节点”
#             # 遍历真正结束是当 cur is None 且 stack 为空
#             # 1. go to the right path, and add all the node to the stack, the bottom node is the smaller one, stack top is the biggest node
#             # every value in the right subtree is greater than the root (Due to the definition of a BST)
#             if cur: # 只是一路压栈，往右走，不处理节点
#                 stack.append(cur)
#                 cur = cur.right # right
#             # pop out the node and then process 
#             else: # 右边走到底了，cur已经一路向右走到None了, 说明该回到上一个节点处理root了. 弹出并处理节点，处理完才去左边
#                 # at the top of the stack, the node is the biggest one. 刚开始pop的第一个节点是整棵树的最大值
#                 cur = stack.pop() # mid

#                 cur.val += pre # 当前值= 原值+ 之前所有比我大的值的和
#                 pre = cur.val # update pre, 对于本题pre 的更新属于“处理当前节点”, 供下一个节点使用
#                 # 处理完当前节点后, 才转向左子树
#                 cur = cur.left # left

#         return root




# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]\n
# @lcpr case=end

# @lcpr case=start
# [0,null,1]\n
# @lcpr case=end

#

