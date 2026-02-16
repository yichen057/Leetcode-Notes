#
# @lc app=leetcode id=129 lang=python3
# @lcpr version=30307
#
# [129] Sum Root to Leaf Numbers
#
# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
#
# algorithms
# Medium (69.52%)
# Likes:    8606
# Dislikes: 157
# Total Accepted:    1.2M
# Total Submissions: 1.8M
# Testcase Example:  '[1,2,3]\n[4,9,0,5,1]'
#
# You are given the root of a binary tree containing digits from 0 to 9 only.
# 
# Each root-to-leaf path in the tree represents a number.
# 
# 
# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# 
# 
# Return the total sum of all root-to-leaf numbers. Test cases are generated so
# that the answer will fit in a 32-bit integer.
# 
# A leaf node is a node with no children.
# 
# 
# Example 1:
# 
# Input: root = [1,2,3]
# Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.
# 
# 
# Example 2:
# 
# Input: root = [4,9,0,5,1]
# Output: 1026
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 1000].
# 0 <= Node.val <= 9
# The depth of the tree will not exceed 10.
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
#         self.right = na
class Solution:
# 在主函数初始化：每次调用函数都会重置清零, 这样最保险，绝对不会出现“跨用例污染”。
# 如果在 __init__ 初始化, 如果 LeetCode 跑完第一个用例没销毁对象，直接跑第二个用例，self.result 里就还留着上一个用例的结果. 主函数里还需要做重置清零
# 遵循标准的面向对象（OOP）规范
# 在标准的 Python 开发中，__init__ 是构造函数，专门负责初始化对象的状态。
# 如果你在主函数（如 pathSum）里临时创建 self.total_sum，虽然 Python 允许这样做，但在严谨的工程实践中，这叫“动态绑定属性”，有时会让代码变得难以维护（因为别人不知道这个对象到底有多少属性，得翻遍所有函数才知道）。
# 因此，代码随想录 的示例通常遵循标准的 OOP 风格，先在 __init__ 里“报到”，再在函数里使用。

# 递归+显示回溯代码:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # 在主函数里定义 self.xxx，相当于在每次“发令起跑”前清零
        self.total_sum = 0
        self.current_num = 0
        if not root:
            return 0
        # 处理根节点 (手动处理第一步)
        self.current_num = root.val
        self.traversal(root)
        return self.total_sum
    
    def traversal(self, cur: Optional[TreeNode]) -> None:
        # base case: binary tree reaches to leaf node
        if not cur.left and not cur.right:
            # 当且仅当到达叶子节点, 才把这个分支的数字加起来总和
            self.total_sum += self.current_num
            return
        
        # 单层逻辑处理
        if cur.left:
            # 递归前创建了一个全新的数字作为参数传给下一层, 当前这一层的current_num依然是原来的值没变
            self.current_num = self.current_num * 10 + cur.left.val
            self.traversal(cur.left) # 进入递归
            self.current_num = (self.current_num - cur.left.val) // 10 # 回溯
        
        if cur.right:
            self.current_num = self.current_num * 10 + cur.right.val
            self.traversal(cur.right)
            self.current_num = (self.current_num - cur.right.val) // 10


# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [4,9,0,5,1]\n
# @lcpr case=end

#

