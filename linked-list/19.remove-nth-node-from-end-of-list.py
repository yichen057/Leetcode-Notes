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
# 删除链表中倒数第 n 个节点。LC 19：Remove Nth Node From End of List
# 1. 为什么用 Dummy + 双指针？因为要删除一个节点，我们通常需要找到它的前一个节点。
# 用两个指针 fast 和 slow，让 fast 先走 n + 1 步，或者让 fast 先走 n 步后再同步走。这里我推荐更容易理解的版本：fast 先走 n 步，然后 slow 和 fast 一起走，最后 slow 停在要删除节点的前一个节点。
# 方法一: fast 和 slow 都从 dummy 出发. 逻辑是：fast 先走 n + 1 步。
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
# 方法二: 推荐! 容易记忆
# fast 先走 n 步，制造出 n 的距离。
# 然后 fast 和 slow 同速前进。
# 当 fast 到 None 时，slow.next 距离末尾正好还有 n 个节点，
# 所以 slow.next 就是倒数第 n 个节点。
# 因为删链表节点时, 需找到它的前一个节点, 所以slow必须停在要删节点的前1个节点

# fast 从 head 开始负责制造 n 的距离；
# slow 从 dummy 开始，是为了最后停在“待删除节点的前一个节点”。
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0) # 如果没有 dummy，删除头节点就要单独处理。
        dummy.next = head

        fast = head
        slow = dummy # 为什么 slow 要从 dummy 开始？因为slow 必须站在“要删除节点的前一个节点”
        # 为什么不是 slow = head？ 然后 fast 先走 n 步，再一起走，最后 slow 会停在要删除的那个节点本身，而不是它前一个节点。
# 初始状态:
# slow
#  ↓
# dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> None
#          ↑
#         fast
        # fast 先走n步
        for _ in range(n):
            fast = fast.next
        
        # fast和slow一起走
        # 当 fast 到 None 时，slow 正好在要删除节点的前一个节点
        while fast:
            fast = fast.next
            slow = slow.next

        # 删除 slow 后面的节点 
        slow.next = slow.next.next

        return dummy.next

# @lc code=end

