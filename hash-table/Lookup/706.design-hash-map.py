#
# @lc app=leetcode id=706 lang=python3
# @lcpr version=30403
#
# [706] Design HashMap
#
# https://leetcode.com/problems/design-hashmap/description/
#
# algorithms
# Easy (66.57%)
# Likes:    5438
# Dislikes: 502
# Total Accepted:    771.1K
# Total Submissions: 1.2M
# Testcase Example:  '["MyHashMap","put","put","get","get","put","get","remove","get"]\n' +
  '[[],[1,1],[2,2],[1],[3],[2,1],[2],[2],[2]]'
#
# Design a HashMap without using any built-in hash table libraries.
# 
# Implement the MyHashMap class:
# 
# 
# MyHashMap() initializes the object with an empty map.
# void put(int key, int value) inserts a (key, value) pair into the HashMap. If
# the key already exists in the map, update the corresponding value.
# int get(int key) returns the value to which the specified key is mapped, or
# -1 if this map contains no mapping for the key.
# void remove(key) removes the key and its corresponding value if the map
# contains the mapping for the key.
# 
# 
# 
# Example 1:
# 
# Input
# ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
# [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
# Output
# [null, null, null, 1, -1, null, 1, null, -1]
# 
# Explanation
# MyHashMap myHashMap = new MyHashMap();
# myHashMap.put(1, 1); // The map is now [[1,1]]
# myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
# myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
# myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1],
# [2,2]]
# myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the
# existing value)
# myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
# myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
# myHashMap.get(2);    // return -1 (i.e., not found), The map is now
# [[1,1]]
# 
# 
# 
# Constraints:
# 
# 
# 0 <= key, value <= 10^6
# At most 10^4 calls will be made to put, get, and remove.
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# LC706 手写 HashMap：array + linked list=> separate chaining: 每个 bucket 后面可以挂一条 linked list。
# Python dict / set：array + probing => open addressing: 发生 collision 时，它不会在 bucket 后面挂 linked list，而是在内部数组里继续找别的位置。
# 这样1. 内存更紧凑; 2. cache locality 更好; 不需要为每个 collision 额外创建 linked list node

# 初始化dummy node = ListNode(), 当你写ListNode(), 等价于ListNode(-1, -1, None), 它只是一个占位节点。真实数据节点是这样创建的: ListNode(key, value), 这个就是key-value pair
class ListNode:
   def __init__(self, key = -1, val = -1, next = None):
       self.key = key
       self.val = val
       self.next = next

class MyHashMap:

    # 创建整个array, 创建之后它有1000个位置, 每个位置都已经放了一个ListNode, 他们初始化都是dummy head node, 即self.map[index]是这个bucket的dummy head node
    # 所以array得每个value是一条linked list的入口
    # 三个注意事项: self.map 是整个数组, 它不是普通地直接存value, 它是一个bucket array。每个bucket里面放一个linked list
    # self.map[index] 是某一个 bucket。
    # self.map[index] 里面放的是 linked list 的 dummy head。dummy node 是 linked list 的假头节点，用来简化插入和删除操作。
    def __init__(self): 
       self.map = [ListNode() for i in range(1000)] # initialize every array index with a dummy node

    # hash function can convert a key into an array index(index = hash key % array_size)
    def hash(self, key):
       return key % len(self.map)
    
    # get the index, and start map at the head of linked list
    # 例如put(1, 10)步骤:
    # 1) 先算index = 1 % 1000 = 1
    # 2) 找到bucket1: cur = self.map[1]
    # 3) 一开始是index 1: dummy -> None
    # 4) while cur.next不成立因为dummy.next是None, 所以执行cur.next = ListNode(1, 10), 即变成index 1: dummy -> (1, 10) -> None
    # 5) 再执行put(1001, 20), index = 1001 % 1000 = 1. 此时发生hash collision, 即不同key得到同一个index
    # 6) 所以还是进入bucket1: index 1: dummy -> (1, 10) -> None
    # 7) 开始遍历 cur = dummy, cur.next是(1, 10), cur.next.key是1, 不是1001, 所以继续cur = cur.next, 现在cur是(1, 10), cur.next是None, while结束
    # 8) 然后插入新节点 cur.next = ListNode(1001, 20), 变成dummy -> (1, 10) -> (1001, 20) -> None. 
    # separate chaining: multiple keys go to the same index, store them in a linked list at that index. 每个bucket后面挂个linked list
    def put(self, key: int, value: int) -> None: # insert or update
        index = self.hash(key) # 先通过 hash 找到 key 应该去哪个 bucket。
        cur = self.map[index] # 这个cur节点也可以视作bucket, 然后从这个 bucket 的 linked list 开始找。
        # we want current node to be pointing at the last node instead of point at null, so here: while cur.next instead of while cur
        # cur node start from the start of the linked list which is going to be a dummy node, so here: if cur.next.key == key instead of if cur.key
        while cur.next: # cur 永远停在“目标节点的前一个节点”。
            if cur.next.key == key: # which mean the key already exist, we can just update its value (当key已经存在,只需要更新value)
                cur.next.val = value # 注意等号前面是cur.next.val, 而不是cur.val
                return 
            cur = cur.next # 当key不存在时插入一个新的node
        # when we at the end of linked list and then, cur.next = null, so we can insert a new list node
        # 到linkedlist的end后要执行下面这句话, 新增一个key-value pair
        cur.next = ListNode(key, value)

    # get the head of linked list, that key maps to get its value
    # Start from the dummy node to check
    # eg: 调用get(1001), 流程如下:
    # index = 1001 % 1000 = 1, 去index1: dummy -> (1, 10) -> (1001, 20)
    # cur = dummy, dummy.key = -1, not 1001, cur = cur.next = (1, 10). 
    # cur.key = 1, not 1001, cur = cur.next = (1001, 20)
    # 因为此时cur.key = key 1001, 找到了, 因此return 20
    def get(self, key: int) -> int: # 查找key对应的value
        cur = self.map[self.hash(key)]
        while cur:
            if cur.key ==key:
                return cur.val
            cur = cur.next
        return -1

    # start at the dummy node cus we need to do some pointer manipulation
    # we need to stop prior to the node we want to delete
    # 删除linked list节点时, 需要知道目标节点的前一个节点
    # eg: dummy -> (1, 10) -> (1001, 20) -> (2001, 30), 如果要删除 1001，你需要让：(1, 10).next = (2001, 30), 即cur.next = cur.next.next. 所以 cur 要停在被删除节点的前一个节点。
    #  dummy node 的好处：删除第一个真实节点也不需要特殊处理。
    def remove(self, key: int) -> None: # 删除key-value pair
        cur = self.map[self.hash(key)]
        while cur and cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next


# 以下为英文带注释版
class ListNode:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next


class MyHashMap:

    def __init__(self):
        # Create 1000 buckets.
        # Each bucket starts with a dummy head node.
        self.map = [ListNode() for _ in range(1000)]

    def hash(self, key):
        # Convert key into an array index.
        return key % len(self.map)

    def put(self, key: int, value: int) -> None:
        index = self.hash(key)

        # cur starts at the dummy node of this bucket.
        cur = self.map[index]

        # Search the linked list.
        # We check cur.next because cur is the previous node.
        while cur.next:
            if cur.next.key == key:
                # Key already exists, update value.
                cur.next.val = value
                return
            cur = cur.next

        # Key does not exist, insert a new node at the end.
        cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = self.hash(key)

        # Start from the first real node, skipping dummy.
        cur = self.map[index].next

        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next

        return -1

    def remove(self, key: int) -> None:
        index = self.hash(key)

        # Start from dummy because we need previous node to delete.
        cur = self.map[index]

        while cur.next:
            if cur.next.key == key:
                # Delete cur.next
                cur.next = cur.next.next
                return
            cur = cur.next
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# ["MyHashMap","put","put","get","get","put","get","remove","get"]\n[[],[1,1],[2,2],[1],[3],[2,1],[2],[2],[2]]\n
# @lcpr case=end

#

