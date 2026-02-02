#
# @lc app=leetcode id=116 lang=python3
# @lcpr version=30307
#
# [116] Populating Next Right Pointers in Each Node
#
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/
#
# algorithms
# Medium (66.73%)
# Likes:    10365
# Dislikes: 326
# Total Accepted:    1.3M
# Total Submissions: 2M
# Testcase Example:  '[1,2,3,4,5,6,7]\n[]'
#
# You are given a perfect binary tree where all leaves are on the same level,
# and every parent has two children. The binary tree has the following
# definition:
# 
# struct Node {
# ⁠ int val;
# ⁠ Node *left;
# ⁠ Node *right;
# ⁠ Node *next;
# }
# 
# 
# Populate each next pointer to point to its next right node. If there is no
# next right node, the next pointer should be set to NULL.
# 
# Initially, all next pointers are set to NULL.
# 
# 
# Example 1:
# 
# Input: root = [1,2,3,4,5,6,7]
# Output: [1,#,2,3,#,4,5,6,7,#]
# Explanation: Given the above perfect binary tree (Figure A), your function
# should populate each next pointer to point to its next right node, just like
# in Figure B. The serialized output is in level order as connected by the next
# pointers, with '#' signifying the end of each level.
# 
# 
# Example 2:
# 
# Input: root = []
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 2^12 - 1].
# -1000 <= Node.val <= 1000
# 
# 
# 
# Follow-up:
# 
# 
# You may only use constant extra space.
# The recursive approach is fine. You may assume implicit stack space does not
# count as extra space for this problem.
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# given a perfect binary tree where all leaves are on the same level, and every parent has two children. 本题和117题思路一致
# 本题依然是层序遍历，只不过在单层遍历的时候记录一下本层的头部节点，然后在遍历的时候让前一个节点指向本节点就可以了
# 注意: 本题要求的返回值类型是 Node（即修改后的根节点）
# 在数据结构中，root 确实是一个节点，但它是整棵树的入口。即使循环结束了，root 所指向的那个对象已经不是最初的那个“孤零零”的 root 了，它的子孙后代们的 next 指针全都已经被你在线下“偷偷”连好了。
# 我们在循环里做的 node.next = ...，实际上是在给珍珠之间加新的连线。当我们加完所有的 next 连线后，从 root 出发，判题系统就能顺着 left/right 往下走，顺着 next 往右走，从而检查整棵树的连接是否正确。
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root # 如果 root 为空，queue 就是 [None], 注意: 此处返回的是节点, 不是list
        queue = collections.deque([root])
        # 注意: 本题不用新创建result数组, 题目要求的返回值类型是 Node（即修改后的根节点）, 看清楚题目要求

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                # 弹出当前节点
                cur = queue.popleft()

                # 判断是否为当前层的最后一个节点
                if i < level_size - 1:
                    # 如果不是最后一个，它的 next 就在当前队列的最前面
                    cur.next = queue[0]
                else:
                    # 如果是最后一个，next 指向 None（初始默认也是 None）
                    cur.next = None
                # cur.next = queue[0] if i < level_size - 1 else None # [三元表达式Ternary operator]如果不是最后一个，指向 queue[0]，否则指向 None

                # 将cur的子节点加入队列queue
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return root
            
# @lc code=end

if __name__ == '__main__': 
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [1,2,3,4,5,6,7]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

