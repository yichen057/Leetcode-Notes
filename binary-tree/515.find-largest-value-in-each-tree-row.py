#
# @lc app=leetcode id=515 lang=python3
# @lcpr version=30307
#
# [515] Find Largest Value in Each Tree Row
#
# https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/
#
# algorithms
# Medium (66.28%)
# Likes:    4121
# Dislikes: 130
# Total Accepted:    511.2K
# Total Submissions: 771.3K
# Testcase Example:  '[1,3,2,5,3,null,9]\n[1,2,3]'
#
# Given the root of a binary tree, return an array of the largest value in each
# row of the tree (0-indexed).
# 
# 
# Example 1:
# 
# Input: root = [1,3,2,5,3,null,9]
# Output: [1,3,9]
# 
# 
# Example 2:
# 
# Input: root = [1,2,3]
# Output: [1,3]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree will be in the range [0, 10^4].
# -2^31 <= Node.val <= 2^31 - 1
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
# 思路: 层序遍历，取每一层的最大值
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = collections.deque([root])
        result = []
        while queue:
            max_val = float('-inf') # 初始值为最小值
            # 为了保证这一层里任何值都能比初始值大，尤其当节点值可能是负数时。如果用 0 做初始值，遇到全是负数的一层，最大值就会被错误地保留成 0。
            #float('-inf') 表示负无穷，比任何实数都小，所以第一次比较一定会被当前节点值替换掉。
            #这里用浮点数只是表示“负无穷”的一种写法，和 int 混用比较没问题。如果想用整数也可以写成 -10**9 或 -sys.maxsize，但 -inf 更通用、语义更清晰

            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur.val > max_val:# 注意: 此处比较的是节点的值, 而不是node节点, 因为max_val就是数值而不是node
                    max_val = cur.val
                # max_val = max(max_val, cur.val) # 本句话可以拆分为上面两句话, 等同效果比大小

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            result.append(max_val)
            # 每一层遍历完了, 把最大值添加到result里, 本题无需存储每层所有的值 
        return result
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [1,3,2,5,3,null,9]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

#

