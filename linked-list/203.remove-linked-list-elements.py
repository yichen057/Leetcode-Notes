#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#
# https://leetcode.com/problems/remove-linked-list-elements/description/
#
# algorithms
# Easy (52.52%)
# Likes:    8823
# Dislikes: 280
# Total Accepted:    1.4M
# Total Submissions: 2.7M
# Testcase Example:  '[1,2,6,3,4,5,6]\n6'
#
# Given the head of a linked list and an integer val, remove all the nodes of
# the linked list that has Node.val == val, and return the new head.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
# 
# 
# Example 2:
# 
# 
# Input: head = [], val = 1
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: head = [7,7,7,7], val = 7
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [0, 10^4].
# 1 <= Node.val <= 50
# 0 <= val <= 50
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val # 节点存的值
        self.next = next # 指向下一个节点的指针
# 所以每次写 ListNode(...)，就是在创建一个新节点。
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        #虚拟头节点法. 这是“哑结点 / 虚拟头结点（dummy head）”技巧，解决以下问题：
        # 1) 方便删除第一个节点：
        # 如果要删头节点 [1]，直接让 dummy_head.next = head.next 就行，不用单独判断“是不是头节点”。
        # 2) 统一代码逻辑：
        # 删除/插入操作都能写成「找到要操作节点的前驱 → 修改指针」，不用对头节点做特殊处理。 
        
        dummy_head = ListNode(next = head) # 只传了 next 参数，没有传 val，所以 val 会用默认值 0。创建了一个值为 0、next 指向原链表头的虚拟节点。它本身不存有效数据，只是一个辅助节点，常用于简化链表操作（特别是删除/插入头节点时）
        # 遍历列表并删除值为val的节点
        cur = dummy_head
        while cur.next: # 等价于while cur.next is not None:, 只是左边的更简洁
            # cur.next → 下一个节点对象
            # cur.next.val → 下一个节点里存储的值
            # 删除节点 / 查找目标值时，应该写 cur.next.val == val。
            # 注意是 .val；cur.next == val 永远 False
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy_head.next # 返回新的头（链表入口）
    
# @lc code=end

