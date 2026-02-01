#
# @lc app=leetcode id=199 lang=python3
# @lcpr version=30307
#
# [199] Binary Tree Right Side View
#
# https://leetcode.com/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (69.26%)
# Likes:    13288
# Dislikes: 1083
# Total Accepted:    2.1M
# Total Submissions: 3.1M
# Testcase Example:  '[1,2,3,null,5,null,4]\n[1,2,3,4,null,null,null,5]\n[1,null,3]\n[]'
#
# Given the root of a binary tree, imagine yourself standing on the right side
# of it, return the values of the nodes you can see ordered from top to
# bottom.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,3,null,5,null,4]
# 
# Output: [1,3,4]
# 
# Explanation:
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: root = [1,2,3,4,null,null,null,5]
# 
# Output: [1,3,4,5]
# 
# Explanation:
# 
# 
# 
# 
# Example 3:
# 
# 
# Input: root = [1,null,3]
# 
# Output: [1,3]
# 
# 
# Example 4:
# 
# 
# Input: root = []
# 
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 100].
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

# 层序遍历的时候，判断是否遍历到单层的最后面的元素，如果是，就放进result数组中，随后返回result就可以了。
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = collections.deque([root])
        result = []
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                cur = queue.popleft() # 此时queue的长度会随着popleft()而变短
        
                if i == level_size -1: # 注意📢: 这里不能直接使用len(queue), 因为它是在循环过程中实时计算的
                    result.append(cur.val)

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return result



        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [1,2,3,null,5,null,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,null,null,null,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,null,3]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

