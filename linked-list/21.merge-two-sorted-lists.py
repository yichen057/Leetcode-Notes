#
# @lc app=leetcode id=21 lang=python3
# @lcpr version=30403
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (68.24%)
# Likes:    25027
# Dislikes: 2449
# Total Accepted:    6.3M
# Total Submissions: 9.2M
# Testcase Example:  '[1,2,4]\n[1,3,4]\n[]\n[]\n[]\n[0]'
#
# You are given the heads of two sorted linked lists list1 and list2.
# 
# Merge the two lists into one sorted list. The list should be made by splicing
# together the nodes of the first two lists.
# 
# Return the head of the merged linked list.
# 
# 
# Example 1:
# 
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# 
# 
# Example 2:
# 
# Input: list1 = [], list2 = []
# Output: []
# 
# 
# Example 3:
# 
# Input: list1 = [], list2 = [0]
# Output: [0]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0) # dummy提供一个固定的假头节点, 方便返回结果, 永远往tail后接节点
        tail = dummy # tail是新链表的尾巴, 负责往后接节点, 永远指向新链表的最后一个节点
        while list1 and list2: # 表示两个原链表当前还没处理的节点. list1和List2各自指向头节点
            if list1.val < list2.val: # 每轮比较当前节点
                tail.next = list1 # 把更小的结果接到新链表后tail.next, 保持最终链表的有序
                # 谁被接走, 谁就往后移动, tail也往后移动
                list1 = list1.next # list1往后移动一个节点
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next # 让tail往后移动
            tail.next = list1 or list2 # 哪个不None就接哪个, 如果俩都是None, 接哪个都可, 反正最后都是None
        
        return dummy.next
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [1,2,4]\n[1,3,4]\n
# @lcpr case=end

# @lcpr case=start
# []\n[]\n
# @lcpr case=end

# @lcpr case=start
# []\n[0]\n
# @lcpr case=end

#

