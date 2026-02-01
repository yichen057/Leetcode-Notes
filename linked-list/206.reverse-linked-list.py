#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (79.58%)
# Likes:    23602
# Dislikes: 550
# Total Accepted:    5.7M
# Total Submissions: 7.1M
# Testcase Example:  '[1,2,3,4,5]'
#
# Given the head of a singly linked list, reverse the list, and return the
# reversed list.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# 
# 
# Example 2:
# 
# 
# Input: head = [1,2]
# Output: [2,1]
# 
# 
# Example 3:
# 
# 
# Input: head = []
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
# 
# 
# 
# Follow up: A linked list can be reversed either iteratively or recursively.
# Could you implement both?
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: # Optional[ListNode] = ListNode | None用来表示链表可能为空，不是强制语法，而是类型提示（方便可读性和 IDE 检查）。
        # 方法一: 双指针法
        # 初始化
        cur = head
        pre = None
        while cur:
            temp = cur.next # 暂存后继. 变量赋值，不改变链表，把 cur.next 这个节点赋值给 temp 变量, 只是让 temp 变量指向了和cur.next一样的节点
            cur.next = pre # 修改链表指针方向，改变结构: 把当前节点 cur 的 next 指针指向 pre, 让链表走向发生变化. 常见场景：反转链表。
            # 右移一位, 更新pre和cur
            pre = cur
            cur = temp
        return pre # 因为遍历终止时, pre指向的是链表反转后的head(原先是tail)  
       
        # 方法二: 递归法(其实就是把 while 循环展开，每次递归调用负责处理一步)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverse(head, None) # 调用入口, 从第一个头节点开始处理, 因为head还没有前驱, 所以pre应该是None
   
    def reverse(self, cur:ListNode, pre:ListNode) -> ListNode: # 递归reverse(cur, pre)里 就是「执行一次 while 循环」,递归的每一层就是 while 的一次迭代。
        if cur is None: #递归终止条件
            return pre #返回新头结点（pre）
        
        temp = cur.next
        cur.next = pre
        return self.reverse(temp, cur) # 把下一个节点交给递归, 进入下一层递归


# @lc code=end

