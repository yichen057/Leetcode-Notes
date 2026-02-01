#
# @lc app=leetcode id=107 lang=python3
# @lcpr version=30307
#
# [107] Binary Tree Level Order Traversal II
#
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
#
# algorithms
# Medium (67.47%)
# Likes:    5136
# Dislikes: 333
# Total Accepted:    803.9K
# Total Submissions: 1.2M
# Testcase Example:  '[3,9,20,null,null,15,7]\n[1]\n[]'
#
# Given the root of a binary tree, return the bottom-up level order traversal
# of its nodes' values. (i.e., from left to right, level by level from leaf to
# root).
# 
# 
# Example 1:
# 
# Input: root = [3,9,20,null,null,15,7]
# Output: [[15,7],[9,20],[3]]
# 
# 
# Example 2:
# 
# Input: root = [1]
# Output: [[1]]
# 
# 
# Example 3:
# 
# Input: root = []
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
# from common.node import *

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 易混淆点：[::-1] vs .reverse()

# 虽然效果一样，但它们有个小区别：
# 写法	作用	是否改变原列表？
# b = a[::-1]	创建一个新的倒序列表，赋值给 b	不会。原列表 a 保持不变。
# a.reverse()	直接把 a 自己给翻转了	会。原列表 a 变了，且这个方法不返回新列表。
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return [] # 注意, 这里不能返回None, 因为函数的定义：-> List[List[int]]。这就承诺了函数一定会返回一个列表。None 不是列表
        queue = collections.deque([root])
        result = []
        while queue:
            level = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            result.append(level)
        return result[::-1] # 创建一个新的倒序列表, 将列表（List）倒序（反转）. [::-1] 的字面意思就是：“从后往前，一步一步地把所有元素取出来，组成一个新的列表。
        # .reverse(): 翻转原列表, 且这个方法不返回新列表

            



# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

