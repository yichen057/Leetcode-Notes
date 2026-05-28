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
# 求环入口方法: 当slow和fast相遇后, 把其中一个指针挪到起点, 然后两个指针匀速前进都走1步, 当他们相遇时即找到了环的入口!
# A straightforward solution is to use a hash set to record visited nodes, which takes O(n) time and O(n) space. 
# Since we want constant extra space, I will use Floyd’s fast and slow pointer algorithm.
# Let:
# x = distance from head to cycle entrance
# y = distance from cycle entrance to meeting point
# z = distance from meeting point back to cycle entrance
# L = y + z, the cycle length
#
# At the first meeting point:
# slow travels x + y steps
# fast travels 2 * (x + y) steps
#
# Since fast travels whole extra cycles:
# 2(x + y) - (x + y) = kL
# x + y = kL
# x = kL - y = (k - 1)L + z
#
# Therefore, a pointer starting from head and a pointer starting
# from the meeting point will meet at the cycle entrance
# if both move one step at a time.

 # Floyd's Cycle Detection Algorithm 推荐!
    # TC: O(n)
    # SC: O(1)
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 方法一: 快慢指针:时间复杂度O(n), 空间复杂度O(1)
        # 1) 阶段1: 寻找相遇点. 快慢指针部分.最多走 n 步（n = 链表长度）就能相遇(要么在无环情况下退出，要么在环内追上)，快指针就会到达链表尾部（无环）或者在环内追上慢指针。所以这一步时间复杂度是 O(n)。
        fast = head
        slow = head
        # Phase 1: Find a meeting point if a cycle exists.
        while fast and fast.next: # 因为fast是两步两步的走, 第二步需要确认不能为空
            fast = fast.next.next # fast一次走两个节点
            slow = slow.next # slow一次走一个节点
            if slow == fast: # 环中相遇, 说明找到了环. 如果有环，快指针会一点点“追上”慢指针，最终在环中相遇。因为相对速度差 = 1，所以追赶过程不会超过环长 y+z 步，而 y+z ≤ n。
               # 如果没有环, fast会最终会走到None, 如果有环fast进入环后会不断追赶slow最终二者相遇
               # slow 和 fast 会在环中的某个节点相遇，但这个节点不一定是入口。
               # Phase 2: Find the cycle entrance.
               slow = head
                
                # 2) 阶段2: 寻找环入口.利用数学关系x=z+(n-1)(y+z)推导出x = (k - 1)L + z, 找到环的入口. 两个同步指针会在entry相遇:一个指针从head出发走x步, 一个指针从meet出发走z步
                # 相遇后，一个指针从头出发，一个指针从相遇点出发，同时一步步走。最多也就走 n 步（实际上 ≤ 非环部分长度 a + 环长 L）。所以这一步的时间复杂度也是 O(n)。
                # 让 slow 回到 head, fast 保留在相遇点, 然后两个指针都每次走 1 步, 再次相遇的位置就是环入口
                while slow != fast: # 循环的结束条件: 两个指针相等在入口处相遇
                    slow = slow.next # 两个指针同步走, 一次一步
                    fast = fast.next
                return slow # 利用数学关系, 推导见下,目的是找到环形入口
        return None
    # 假设head→entry=x, entry→meet=y, meet→entry=z, 
    # slow走的总步数= x+y,此处无需加n(y+z), 因为slow还没转完一圈就会和fast相遇
    # fast走的总步数= x+y+n(y+z),其中y+z是环形总长, n表示相遇时fast在环形里转了几圈.n>=1即fast至少走一圈才可能和slow相遇
    # 由于快指针是慢指针的两倍速度, 因为代入即为2(x+y)=x+y+n(y+z) -> x=n(y+z)-y = (n-1)(y+z)+z -> 当n=1时, x=z, 在环形入口处相遇 ->即“head 到 entry 的距离” = “相遇点到 entry 的距离”。

    # 快慢指针的方法二, 不推荐写, 因为while...else语法还需要额外解释, 容易吧讨论重点从算法转移到语法
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        
        # Step 1: find meeting point
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        # Python 的 while...else 语法: 如果 while 正常结束，没有被 break 打断，就执行 else
        else:
            return None
        # Step 2: find cycle entrance
        # 当 slow 和 fast 在环里第一次相遇后：从 head 和相遇点同时出发
        # 让一个指针从 head 出发, 让另一个指针从相遇点出发. 两个都每次走 1 步. 它们再次相遇的位置，就是环入口
        # fast 比 slow 多走的距离，刚好是环长度的整数倍。因此 slow 在相遇点到入口的距离，和 head 到入口的距离，可以同步抵消。
        p1 = head
        p2 = slow
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next

        return p1


    # 方法二: 哈希表解法: 
    # 时间复杂度为O(n),每个节点最多访问一次;空间复杂度为O(n)需要额外集合存储节点
    # 遍历链表时，把访问过的节点存到set集合里；第一次遇到已经访问过的节点，它就是环入口
    # 哈希表解法：好理解，但额外空间 O(n)
class Solution:
    # TC: O(n)
    # SC: O(n)
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        current = head

        while current:
            if current in visited: # 如果当前节点已经出现过
                return current # 说明是环的入口

            visited.add(current) # 把当前节点加入集合
            current = current.next # 移动指针

        return None

# 哈希表解法：好理解，但额外空间 O(n)
# 快慢指针法：不需要额外空间，空间 O(1)，是面试最优解

# @lc code=end

