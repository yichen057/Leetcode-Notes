#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
# https://leetcode.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (67.72%)
# Likes:    12769
# Dislikes: 495
# Total Accepted:    1.7M
# Total Submissions: 2.5M
# Testcase Example:  '[1,2,3,4]'
#
# Given a linked list, swap every two adjacent nodes and return its head. You
# must solve the problem without modifying the values in the list's nodes
# (i.e., only nodes themselves may be changed.)
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4]
# 
# Output: [2,1,4,3]
# 
# Explanation:
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: head = []
# 
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: head = [1]
# 
# Output: [1]
# 
# 
# Example 4:
# 
# 
# Input: head = [1,2,3]
# 
# Output: [2,1,3]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# “引用”不是“前一个节点”，而是“有没有办法能继续找到这个节点”。变量或字段（比如 .next）保存了某个节点的地址，从而能找到那个节点。
# 每个节点本质上有两个部分：
# val → 节点存储的值
# next → 指向下一个节点的“指针”（也就是引用）
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyhead = ListNode(0)# 此处0指的是value, next 默认为 None. dummyhead 指向一个已经存在的 节点对象（不为空）就不会是 None，也就不会“空”
        dummyhead.next = head # 真正的链表结果是从 dummyhead.next 开始的。
        cur = dummyhead # cur指针目前在dummyhead
        # 遍历结束条件:
        # 奇数个数: cur.next.next is not null, 剩一个数没有交换, 此处cur指针在它前面, 这个数指向null
        # 偶数个数: cur.next is not null, 刚好两两成对交换, 最后一对数指向null, cur指针在这对数第二个数的位置, 即指向链表的末尾
        while cur.next is not None and cur.next.next is not None:# 注意此处不能颠倒这两个条件的顺序, 否则会在cur.next.next中如果cur.next为空的话, 会出现空指针异常的报错
            temp = cur.next # 临时记录节点1
            temp1 = cur.next.next.next # 临时记录节点3
            # 节点1和节点3必须保存 → 否则一旦 cur.next 改了，你就找不到它。
            # 节点2不必额外保存 → 因为交换前你能通过 cur.next.next 找到它，交换后它又是新的 cur.next，始终有引用。
            cur.next = cur.next.next # dummyhead指向2
            cur.next.next = temp # 改变指针方向, 2指向1, 注意易错点:此时cur指针依旧指向dummyhead, 2还是得按cur.next.next表示
            temp.next = temp1 # 1指向3
            # 此时要移动指针cur, 从dummyhead的位置往后移动2位, 移动到能找到下一对要处理的节点, 也就是移动到它的前一个节点(即此时1的位置)
            cur= cur.next.next
        return dummyhead.next # 返回链表的入口
        
# @lc code=end

