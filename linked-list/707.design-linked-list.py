#
# @lc app=leetcode id=707 lang=python3
#
# [707] Design Linked List
#
# https://leetcode.com/problems/design-linked-list/description/
#
# algorithms
# Medium (29.28%)
# Likes:    2934
# Dislikes: 1666
# Total Accepted:    439K
# Total Submissions: 1.5M
# Testcase Example:  '["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]\n' +
  '[[],[1],[3],[1,2],[1],[1],[1]]'
#
# Design your implementation of the linked list. You can choose to use a singly
# or doubly linked list.
# A node in a singly linked list should have two attributes: val and next. val
# is the value of the current node, and next is a pointer/reference to the next
# node.
# If you want to use the doubly linked list, you will need one more attribute
# prev to indicate the previous node in the linked list. Assume all nodes in
# the linked list are 0-indexed.
# 
# Implement the MyLinkedList class:
# 
# 
# MyLinkedList() Initializes the MyLinkedList object.
# int get(int index) Get the value of the index^th node in the linked list. If
# the index is invalid, return -1.
# void addAtHead(int val) Add a node of value val before the first element of
# the linked list. After the insertion, the new node will be the first node of
# the linked list.
# void addAtTail(int val) Append a node of value val as the last element of the
# linked list.
# void addAtIndex(int index, int val) Add a node of value val before the
# index^th node in the linked list. If index equals the length of the linked
# list, the node will be appended to the end of the linked list. If index is
# greater than the length, the node will not be inserted.
# void deleteAtIndex(int index) Delete the index^th node in the linked list, if
# the index is valid.
# 
# 
# 
# Example 1:
# 
# 
# Input
# ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get",
# "deleteAtIndex", "get"]
# [[], [1], [3], [1, 2], [1], [1], [1]]
# Output
# [null, null, null, null, 2, null, 3]
# 
# Explanation
# MyLinkedList myLinkedList = new MyLinkedList();
# myLinkedList.addAtHead(1);
# myLinkedList.addAtTail(3);
# myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
# myLinkedList.get(1);              // return 2
# myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
# myLinkedList.get(1);              // return 3
# 
# 
# 
# Constraints:
# 
# 
# 0 <= index, val <= 1000
# Please do not use the built-in LinkedList library.
# At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and
# deleteAtIndex.
# 

# @lc code=start
# Singly linked list单链表法
# 节点类定义:
class ListNode:
   def __init__(self, val=0, next=None):
      self.val = val    # 节点存储的数据
      self.next = next  # 指向下一个节点的指针
      # ListNode 就是链表里的节点。val 是节点存的值，默认是 0。next 是指针，指向下一个节点，默认是 None。

# 链表类初始化 
class MyLinkedList:
    def __init__(self):
        self.dummy_head = ListNode() # 定义成员变量为虚拟头节点, 它的作用是简化操作（特别是插入/删除头节点）。
        self.size = 0 # 链表长度,用来记录链表当前有多少元素，方便边界判断。
#self 代表当前对象实例。
# self.dummy_head 表示这个对象的“成员变量”。如果你只写 dummy_head，那会被当成本地变量（函数内部临时变量），而不是对象里的属性。
    def get(self, index: int) -> int: # 返回一个 int
        #如果越界, 返回-1
        if index < 0 or index >= self.size:
           return -1
        
        current = self.dummy_head.next # 链表真正的第一个节点
        for i in range(index): # 往后走index步, 找到对应位置的节点
           current = current.next

        return current.val
    
    def addAtHead(self, val: int) -> None: #-> None 表示这个函数没有返回值。
       self.dummy_head.next=ListNode(val, self.dummy_head.next) # 新节点，它的 next 指向原来的第一个节点。
       
       self.size += 1 # 更新长度
        
    def addAtTail(self, val: int) -> None:
        current = self.dummy_head
        while current.next: # 找到最后一个节点
           current = current.next
        current.next = ListNode(val)  # 新节点挂在最后. 创建了一个新的节点 ListNode，存储的值就是传进来的 val。然后把这个新节点挂在链表的最后。
        self.size += 1 # 更新长度

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
           return -1
        
        current = self.dummy_head
        for i in range(index): # 找到index的前驱节点
           current = current.next
        current.next = ListNode(val, current.next) # 本句包含以下两行代码, 且顺序不能颠倒, 先接后继, 再改前驱
        # newnode.next = current.next   # 新节点指向后继,在前; current.next = newnode # 前驱指向新节点, 在后
        # 如果先写 current.next = newnode，那么链表会变成：current → newnode, 原来的 current.next（即原后继节点）就没法找回了。
        # 另一种写法:newnode = SListNode(val, prev.next)   # 先接后继 ;prev.next = newnode                   # 再改前驱
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
       if index < 0 or index >= self.size:
          return -1
       
       current = self.dummy_head
       for i in range(index): # 遍历到目标节点的前驱节点current
          current = current.next
       current.next = current.next.next #修改指针, 跳过目标节点
       self.size -= 1 # 更新长度

# 双链表法Doubly linked list
class ListNode:
   def __init__(self, val=0, prev=None, next=None):
      self.val = val
      self.prev = prev
      self.next = next
 
class MyLinkedList:
   def __init__(self):
      self.head = None
      self.tail = None
      self.size = 0

   def get(self, index:int) -> int:
      if index <0 or index >= self.size: #越界检查，若 index 无效返回 -1。
         return -1
      
      if index < self.size // 2:
         current = self.head
         for i in range(index):
            current = current.next
      else:
         current = self.tail
         for i in range(self.size - index -1):
            current = current.prev
        # 如果 index 在前半部分，就从 头节点 head 开始往后找；
        # 如果 index 在后半部分，就从 尾节点 tail 开始往前找。
        # 这样平均只要走一半的链表长度，效率更高。
      return current.val
   
   def addAtHead(self, val:int) -> None:
      new_node = ListNode(val, None, self.head) #创建一个新节点 new_node：值为 val，前驱 None，后继指向原来的 head。
      if self.head:#如果链表非空，原来的 head 节点要更新 prev，指向新节点。
         self.head.prev = new_node
      else: #如果链表为空，说明这是第一个节点 
         self.tail = new_node
      self.head = new_node # → 同时更新 head 和 tail。最后更新 head = 新节点，长度 +1。
      self.size += 1

   def addAtTail(self, val:int) -> None:
      new_node = ListNode(val, self.tail, None) # 新节点的 prev 指向旧的尾结点，next=None。
      if self.tail:
         self.tail.next = new_node
      else:
         self.head = new_node
      self.tail = new_node
      self.size += 1
      # 如果链表非空，旧尾节点的 next 要更新为新节点。
      # 如果链表为空，说明新节点同时是 head 和 tail。
      # 最后更新 tail = 新节点，长度 +1。

   def addAtIndex(self, index: int, val: int) -> None:
      if index < 0 or index > self.size:#越界检查：index 必须在 [0, size] 之间。
         return #按题意（LC707）是 void，越界时应该“啥也不做”，不是 return -1
      
      if index == 0:
         self.addAtHead(val)
      elif index == self.size: # 链表末尾+1的index
         self.addAtTail(val)
      else:
         if index < self.size // 2:
            current = self.head
            for i in range(index - 1): #插入：找到 index的前置节点 → size - index
               current = current.next
         else:
            current = self.tail
            for i in range(self.size - index): #插入：找到 index的前置节点 → size - index
               current = current.prev
         new_node = ListNode(val, current, current.next) # (val, prev, next)这一句已包含以下两句: newnode.next = current.next # 新节点指向后继; newnode.prev = current # 新节点指向前驱
         # Python 总是先算右边，再赋值给左边。所以这里会先把新节点初始化好，再让 new_node 指向它。
         current.next.prev = new_node
         current.next = new_node
         self.size += 1
        # 指针四步的心法：一定要先保存/处理好原来的 current.next，否则它丢失后，你没法更新 prev。所以推荐还是「先处理 newnode.next / newnode.prev，再更新 current.next / 后继.prev」。
        # new.prev = current         新节点指向前驱
        # new.next = current.next    新节点指向后驱
        # current.next = new         前驱指向新节点
        # current.next.prev = new    后继指向新节点

   def deleteAtIndex(self, index: int) -> None:
      if index < 0 or index >= self.size:
         return 
      
      if index == 0: #删除首元素
         self.head = self.head.next
         if self.head:
            self.head.prev = None
         else:
            self.tail = None
         
      elif index == self.size - 1: #删除尾元素
            self.tail = self.tail.prev
            if self.tail:
               self.tail.next = None
            else:
               self.head = None
      else: # 删除中间元素
         if index < self.size // 2: # 删除中间前半部分的元素
            current = self.head
            for i in range(index): # 删除：找到要删元素的位置
               current = current.next
         else: # 删除中间后半部分中间的元素
            current = self.tail
            for i in range(self.size - index -1): # 删除：找到要删元素的位置
               current = current.prev
         current.prev.next = current.next
         current.next.prev = current.prev
      self.size -= 1
                  
# addAtHead：O(1)
# addAtTail：O(n)（单链表只能遍历找到尾）
# addAtIndex：O(n)
# deleteAtIndex：O(n)
# 使用 dummy_head，使得所有插入/删除操作都能统一成「找到前驱节点 → 修改指针」。避免了对“头节点”的特殊处理。      

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

