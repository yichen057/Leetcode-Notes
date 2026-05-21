#
# @lc app=leetcode id=705 lang=python3
# @lcpr version=30403
#
# [705] Design HashSet
#
# https://leetcode.com/problems/design-hashset/description/
#
# algorithms
# Easy (68.03%)
# Likes:    4049
# Dislikes: 329
# Total Accepted:    578.2K
# Total Submissions: 849.9K
# Testcase Example:  '["MyHashSet","add","add","contains","contains","add","contains","remove","contains"]\n' +
  '[[],[1],[2],[1],[3],[2],[2],[2],[2]]'
#
# Design a HashSet without using any built-in hash table libraries.
# 
# Implement MyHashSet class:
# 
# 
# void add(key) Inserts the value key into the HashSet.
# bool contains(key) Returns whether the value key exists in the HashSet or
# not.
# void remove(key) Removes the value key in the HashSet. If key does not exist
# in the HashSet, do nothing.
# 
# 
# 
# Example 1:
# 
# Input
# ["MyHashSet", "add", "add", "contains", "contains", "add", "contains",
# "remove", "contains"]
# [[], [1], [2], [1], [3], [2], [2], [2], [2]]
# Output
# [null, null, null, true, false, null, true, null, false]
# 
# Explanation
# MyHashSet myHashSet = new MyHashSet();
# myHashSet.add(1);      // set = [1]
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(1); // return True
# myHashSet.contains(3); // return False, (not found)
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(2); // return True
# myHashSet.remove(2);   // set = [1]
# myHashSet.contains(2); // return False, (already removed)
# 
# 
# Constraints:
# 
# 
# 0 <= key <= 10^6
# At most 10^4 calls will be made to add, remove, and contains.
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# LeetCode explanation 里的 set = [1, 2] 只是展示集合内容
# Python 真正的 set 写法是 {1, 2}。
# 空 set 要写 set()，不能写 {}。
# @lc code=start
#  HashSet 的 node 只需要 key; 而HashMap的node需要key和value
class ListNode:
    def __init__(self, key=-1, next = None):
        self.key = key
        self.next = next
class MyHashSet:

    # preallocate the memory for the array, ListNode(0) is a dummy node
    def __init__(self):
        self.set = [ListNode() for i in range(10 ** 4)]
        # 注意1: 这里场景一个长度为xx的array, 不可以直接写成[ListNode(0) * 10** 4], 因为这样会copy the exact same value in every position. 
        # It's not going to create a new list node for every position. It's going to copy the same one.
        # 注意2: 10^4 在 Python 里不是 10 的 4 次方。是 bitwise XOR 位运算，结果是：14. 应该写成：10 ** 4
        # 注意3: ListNode(0) 表示dummy node的key是0, 0本身也是合法key
    def add(self, key: int) -> None:
        index = key % len(self.set)
        cur = self.set[index]
        # skip the current node(dummy node), so here using while cur.next
        while cur.next:
            # before shift the pointer, we can detect the duplicate and then stop and return 
            if cur.next.key == key:
                return 
            cur = cur.next
        # 此时cur是last node of the linked list
        cur.next = ListNode(key)

    def remove(self, key: int) -> None:
        index = key % len(self.set)
        cur = self.set[index]
        # skip the current node(dummy node)
        while cur.next:
            # before shift the pointer, we can detect the duplicate and then stop and return 
            if cur.next.key == key:
                # shift the next pointer to the pointer after that and then return 
                cur.next = cur.next.next
                return 
            cur = cur.next
  
    def contains(self, key: int) -> bool:
        index = key % len(self.set)
        cur = self.set[index]
        # skip the current node(dummy node)
        while cur.next:
            # before shift the pointer, we can detect the duplicate and then stop and return True
            if cur.next.key == key:
                return True
            cur = cur.next
        # 此时cur是last node of the linked list
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# ["MyHashSet","add","add","contains","contains","add","contains","remove","contains"]\n[[],[1],[2],[1],[3],[2],[2],[2],[2]]\n
# @lcpr case=end

#

