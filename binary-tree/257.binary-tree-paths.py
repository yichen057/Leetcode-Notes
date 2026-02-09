#
# @lc app=leetcode id=257 lang=python3
# @lcpr version=30307
#
# [257] Binary Tree Paths
#
# https://leetcode.com/problems/binary-tree-paths/description/
#
# algorithms
# Easy (68.07%)
# Likes:    7185
# Dislikes: 342
# Total Accepted:    980.2K
# Total Submissions: 1.4M
# Testcase Example:  '[1,2,3,null,5]\n[1]'
#
# Given the root of a binary tree, return all root-to-leaf paths in any order.
# 
# A leaf is a node with no children.
# 
# 
# Example 1:
# 
# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]
# 
# 
# Example 2:
# 
# Input: root = [1]
# Output: ["1"]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 100].
# -100 <= Node.val <= 100
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
# 递归法 + 回溯
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = [] # result是string字符串数组用来记录字符串结果
        path=[] # path是int整数数组用来记录单条路径的
        if not root:
            return result
        self.traversal(root,path, result)
        return result
    # 递归前序遍历: 只有这样才能自上而下让父节点指向左右子节点 (中左右)
    # 本题还引入了"回溯", 一个递归一个回溯, 一体化
    def traversal(self, cur, path, result) -> None: # cur: 根节点; 当没有返回值时写None, 而不是void
        # 中. 此处中的处理过程放base case前面, 是为了在进入左右子树递归前, append当前节点的值, 同时为了让叶子节点的值可以加入path里, 否则如果直接return了, 叶子节点都还没加入到result里
        path.append(cur.val)
        # base case: 到达叶子节点(左右孩子都为空)就结束并记录和返回路径, 没必要遍历到空节点
        if not cur.left and not cur.right:
            # 将path整数数组转为字符串数组, 并用->拼接
            sPath = '->'.join(map(str, path)) #  join 函数只能连接字符串列表, 用 `'->'.join(...)` 把这些字符串用箭头连起来; 用 map(str, path) 把路径里的数字全变字符串
            # 在 Python 里，`map(function, iterable)` 函数的作用是将指定的 `function`（函数）依次作用于 `iterable`（可迭代对象，如列表、元组）的每一个元素上。
            # str：是 Python 的内置类型转换函数，可以将数字转为字符串。
            # path：是一个整数列表，例如 [1, 2, 3]
            # map(str, path) 会把列表里的每个数字都变成字符串，得到类似 `['1', '2', '3']` 的效果。
            result.append(sPath) #注意: 这里append的可不是path, 而是从数字转换为字符串的sPath
            return
        # 左
        if cur.left:
            self.traversal(cur.left, path, result) # 递归函数内部的第一步是append当前节点
            path.pop() # 回溯, 弹出左子树的元素. 只有退出了当前的左子树pop, path才能进入右子树
        # 右
        if cur.right:
            self.traversal(cur.right, path, result) # 递归
            path.pop() # 回溯
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [1,2,3,null,5]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

