#
# @lc app=leetcode id=160 lang=python3
# @lcpr version=30403
#
# [160] Intersection of Two Linked Lists
#
# https://leetcode.com/problems/intersection-of-two-linked-lists/description/
#
# algorithms
# Easy (63.76%)
# Likes:    16678
# Dislikes: 1501
# Total Accepted:    2.4M
# Total Submissions: 3.8M
# Testcase Example:  '8\n' +
  '[4,1,8,4,5]\n' +
  '[5,6,1,8,4,5]\n' +
  '2\n' +
  '3\n' +
  '2\n' +
  '[1,9,1,2,4]\n' +
  '[3,2,4]\n' +
  '3\n' +
  '1\n' +
  '0\n' +
  '[2,6,4]\n' +
  '[1,5]\n' +
  '3\n' +
  '2'
#
# Given the heads of two singly linked-lists headA and headB, return the node
# at which the two lists intersect. If the two linked lists have no
# intersection at all, return null.
# 
# For example, the following two linked lists begin to intersect at node c1:
# 
# The test cases are generated such that there are no cycles anywhere in the
# entire linked structure.
# 
# Note that the linked lists must retain their original structure after the
# function returns.
# 
# Custom Judge:
# 
# The inputs to the judge are given as follows (your program is not given these
# inputs):
# 
# 
# intersectVal - The value of the node where the intersection occurs. This is 0
# if there is no intersected node.
# listA - The first linked list.
# listB - The second linked list.
# skipA - The number of nodes to skip ahead in listA (starting from the head)
# to get to the intersected node.
# skipB - The number of nodes to skip ahead in listB (starting from the head)
# to get to the intersected node.
# 
# 
# The judge will then create the linked structure based on these inputs and
# pass the two heads, headA and headB to your program. If you correctly return
# the intersected node, then your solution will be accepted.
# 
# 
# Example 1:
# 
# Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA =
# 2, skipB = 3
# Output: Intersected at '8'
# Explanation: The intersected node's value is 8 (note that this must not be 0
# if the two lists intersect).
# From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as
# [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are
# 3 nodes before the intersected node in B.
# - Note that the intersected node's value is not 1 because the nodes with
# value 1 in A and B (2^nd node in A and 3^rd node in B) are different node
# references. In other words, they point to two different locations in memory,
# while the nodes with value 8 in A and B (3^rd node in A and 4^th node in B)
# point to the same location in memory.
# 
# 
# Example 2:
# 
# Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3,
# skipB = 1
# Output: Intersected at '2'
# Explanation: The intersected node's value is 2 (note that this must not be 0
# if the two lists intersect).
# From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as
# [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node
# before the intersected node in B.
# 
# 
# Example 3:
# 
# Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# Output: No intersection
# Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it
# reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0,
# while skipA and skipB can be arbitrary values.
# Explanation: The two lists do not intersect, so return null.
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes of listA is in the m.
# The number of nodes of listB is in the n.
# 1 <= m, n <= 3 * 10^4
# 1 <= Node.val <= 10^5
# 0 <= skipA <= m
# 0 <= skipB <= n
# intersectVal is 0 if listA and listB do not intersect.
# intersectVal == listA[skipA] == listB[skipB] if listA and listB
# intersect.
# 
# 
# 
# Follow up: Could you write a solution that runs in O(m + n) time and use only
# O(1) memory?
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 换头双指针方法:不需要修改链表。
    # pA 先走链表 A，走完后再走链表 B; pB 先走链表 B，走完后再走链表 A. 
    # 即pA 走 A整条链表+ B的独有部分, pB 走 B整条链表 + A的独有部分
    # 如果有交点，它们会在交点相遇；如果没有交点，它们最终都会变成 None。
    # TC: O(m + n)
    # SC: O(1)
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # 应该在 cur.next 为空时停下来，而不是走到 cur 自己为空。否则最后一轮变量 cur 此时已经是 None，但是你还想执行 cur.next = headB。None 不是链表节点，它没有 .next 属性，所以程序报错。
        #  while cur: 适合访问每一个节点, 直到链表结束, 结束后cur = None
        # while cur.next: 适合找到最后一个节点 / tail node, 结束后cur = 最后一个节点

        # 如何区分什么是修改链表连接关系, 什么是改变两个遍历指针: 看赋值号左边
        # 左边是 某个节点变量 = ...：通常只是在移动指针。
        # 左边是 某个节点.next = ...：是在修改链表连接关系。
        # 举例:
        # cur = cur.next, 表示变量cur从当前节点移动到下一个节点, 链表本身未变
        # cur.next = some_node, 表示cur指向some_node, 修改了链表结构
        # cur = head, 表示让cur跳到head, 不会修改链表
        pA = headA
        pB = headB

        while pA != pB:
            if pA:
                pA = pA.next # 继续沿着链表 A 往后走, 一直走到pA = None
            else:
                pA = headB # pA已经把链表A走完，改为从链表B 的头部开始走
                # 注意：这并不是让链表 A 的尾巴真的连接到链表 B，而只是让指针变量 pA 在走完 A 后，重新指向 headB。
            pB = pB.next if pB else headA # 本句话的展开可参考上述pA. 只是改变两个遍历指针，并没有改变链表的任何连接关系。
        return pA # 此时pA = pB


# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# 8\n[4,1,8,4,5]\n[5,6,1,8,4,5]\n2\n3\n
# @lcpr case=end

# @lcpr case=start
# 2\n[1,9,1,2,4]\n[3,2,4]\n3\n1\n
# @lcpr case=end

# @lcpr case=start
# 0\n[2,6,4]\n[1,5]\n3\n2\n
# @lcpr case=end

#

