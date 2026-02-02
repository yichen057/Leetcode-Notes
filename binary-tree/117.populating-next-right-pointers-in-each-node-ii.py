#
# @lc app=leetcode id=117 lang=python3
# @lcpr version=30307
#
# [117] Populating Next Right Pointers in Each Node II
#
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/
#
# algorithms
# Medium (56.99%)
# Likes:    6171
# Dislikes: 341
# Total Accepted:    821.2K
# Total Submissions: 1.4M
# Testcase Example:  '[1,2,3,4,5,null,7]\n[]'
#
# Given a binary tree
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
# Input: root = [1,2,3,4,5,null,7]
# Output: [1,#,2,3,#,4,5,7,#]
# Explanation: Given the above binary tree (Figure A), your function should
# populate each next pointer to point to its next right node, just like in
# Figure B. The serialized output is in level order as connected by the next
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
# The number of nodes in the tree is in the range [0, 6000].
# -100 <= Node.val <= 100
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
# 这道题目说是二叉树(Given a binary tree)，但116题目说是完整二叉树，其实没有任何差别，一样的代码一样的逻辑一样的味道#
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        queue = collections.deque([root])
    
        # 方法一: 引入prev前节点
        # while queue:
        #     prev = None # prev 变量的作用是追踪当前行中上一个处理的节点, 在处理新的一层前，先清空前驱节点记录. 处理每一层刚开始都需要重置, 所以必须在每一层循环开始时清空
        #     # prev的创建如果放在 while 外面：会导致树的结构变乱，每一层的结尾会连向下一层的开头; 而放在while 里面：确保 next 指针只在同层节点之间建立连接。
        #     level_size = len(queue)
        #     for i in range(level_size):
        #         cur = queue.popleft()

        #         if prev:
        #             prev.next = cur 
        #         prev = cur

        #         if cur.left:
        #             queue.append(cur.left)
        #         if cur.right:
        #             queue.append(cur.right)
        # return root
    
        # 方法二: 直接用当前cur节点判断
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                cur = queue.popleft()
                if i < level_size - 1:
                    cur.next = queue[0] # 如果不是最后一个，它的 next 就在当前队列的最前面
                else:
                    cur.next = None # 如果是最后一个，next 指向 None（初始默认也是 None）

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
# [1,2,3,4,5,null,7]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

