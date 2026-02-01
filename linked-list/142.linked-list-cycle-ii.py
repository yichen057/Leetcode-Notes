#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#
# https://leetcode.com/problems/linked-list-cycle-ii/description/
#
# algorithms
# Medium (55.73%)
# Likes:    14699
# Dislikes: 1054
# Total Accepted:    1.8M
# Total Submissions: 3.2M
# Testcase Example:  '[3,2,0,-4]\n1'
#
# Given the head of a linked list, return the node where the cycle begins. If
# there is no cycle, return null.
# 
# There is a cycle in a linked list if there is some node in the list that can
# be reached again by continuously following the next pointer. Internally, pos
# is used to denote the index of the node that tail's next pointer is connected
# to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as
# a parameter.
# 
# Do not modify the linked list.
# 
# 
# Example 1:
# 
# 
# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the
# second node.
# 
# 
# Example 2:
# 
# 
# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail connects to the
# first node.
# 
# 
# Example 3:
# 
# 
# Input: head = [1], pos = -1
# Output: no cycle
# Explanation: There is no cycle in the linked list.
# 
# 
# 
# Constraints:
# 
# 
# The number of the nodes in the list is in the range [0, 10^4].
# -10^5 <= Node.val <= 10^5
# pos is -1 or a valid index in the linked-list.
# 
# 
# 
# Follow up: Can you solve it using O(1) (i.e. constant) memory?
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 方法一: 快慢指针:时间复杂度O(n), 空间复杂度O(1)
        # 1) 阶段1: 寻找相遇点. 快慢指针部分.最多走 n 步（n = 链表长度）就能相遇(要么在无环情况下退出，要么在环内追上)，快指针就会到达链表尾部（无环）或者在环内追上慢指针。所以这一步时间复杂度是 O(n)。
        fast = head
        slow = head
        while fast and fast.next: # 因为fast是两步两步的走, 第二步需要确认不能为空
            fast = fast.next.next # fast一次走两个节点
            slow = slow.next # slow一次走一个节点
            if fast == slow: # 环中相遇, 说明找到了环. 如果有环，快指针会一点点“追上”慢指针，最终在环中相遇。因为相对速度差 = 1，所以追赶过程不会超过环长 y+z 步，而 y+z ≤ n。
                index1 = fast # index1在环形中的相遇点meet
                index2= head  # index2在链表的head
                
                # 2) 阶段2: 寻找环入口.利用数学关系x=z+(n-1)(y+z)推导出x=z, 找到环的入口. 两个同步指针会在entry相遇:一个指针从head出发走x步, 一个指针从meet出发走z步
                # 相遇后，一个指针从头出发，一个指针从相遇点出发，同时一步步走。最多也就走 n 步（实际上 ≤ 非环部分长度 a + 环长 L）。所以这一步的时间复杂度也是 O(n)。
                while index1 != index2: # 循环的结束条件: index1 = index2在入口处相遇
                    index1 = index1.next # index1和index2两个指针同步走, 一次一步
                    index2 = index2.next
                return index1 # 利用数学关系, 推导见下,目的是找到环形入口
        return None
    # 假设head→entry=x, entry→meet=y, meet→entry=z, 
    # slow走的总步数= x+y,此处无需加n(y+z), 因为slow还没转完一圈就会和fast相遇
    # fast走的总步数= x+y+n(y+z),其中y+z是环形总长, n表示相遇时fast在环形里转了几圈.n>=1即fast至少走一圈才可能和slow相遇
    # 由于快指针是慢指针的两倍速度, 因为代入即为2(x+y)=x+y+n(y+z) -> x=n(y+z)-y = (n-1)(y+z)+z -> 当n=1时, x=z, 在环形入口处相遇 ->即“head 到 entry 的距离” = “相遇点到 entry 的距离”。

    # 方法二: 哈希表解法: 时间复杂度为O(n),每个节点最多访问一次;空间复杂度为O(n)需要额外集合存储节点
    # 遍历链表时，把访问过的节点存到集合里；如果某个节点已经出现过，那它就是环的入口。
    # 哈希表解法：好理解，但额外空间 O(n)
        visited = set()
        cur = head
        while cur:
            if cur in visited: # 如果当前节点已经出现过
                return cur     # 说明是环的入口
            visited.add(cur)   # 把当前节点加入集合
            cur = cur.next     # 移动指针
        return None

# 哈希表解法：好理解，但额外空间 O(n)
# 快慢指针法：不需要额外空间，空间 O(1)，是面试最优解

# @lc code=end

