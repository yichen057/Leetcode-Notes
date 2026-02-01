#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (49.61%)
# Likes:    20544
# Dislikes: 875
# Total Accepted:    3.8M
# Total Submissions: 7.5M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given the head of a linked list, remove the n^th node from the end of the
# list and return its head.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# 
# 
# Example 2:
# 
# 
# Input: head = [1], n = 1
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: head = [1,2], n = 1
# Output: [1]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
# 
# 
# 
# Follow up: Could you do this in one pass?
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #“快慢指针”(fast & slow pointers) 的技巧在链表题里非常常见，它的本质是 用两个速度不同的指针遍历链表，来解决涉及「相对位置关系」的问题。
        # 删节点, 操作指针得指向要删元素的前一个, 才能进行删除操作
        # 1) fast先走n+1步, slow不动; 2) slow和fast一起走, 直到fast指向空节点, 此时slow指向要删除元素的前一个; 3) 最后删除节点的操作
        dummyhead = ListNode(0)
        dummyhead.next = head

        slow, fast = dummyhead, dummyhead
        # 1) fast先走n+1步
        for i in range(n+1):
            fast = fast.next
        
        # 2) slow和fast一起移动, 直到fast为空
        while fast: # while fast is not None
            fast = fast.next
            slow = slow.next

        # 3) 删除节点操作
        slow.next = slow.next.next

        return dummyhead.next

# @lc code=end

