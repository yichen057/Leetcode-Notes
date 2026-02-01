# LeetCode Day 3 笔记：链表01 - 203 / 707 / 206

*最后更新：2025-09-23*

------

## 目录

- [203. Remove Linked List Elements（移除链表元素）](#203-remove-linked-list-elements移除链表元素)
- [707. Design Linked List（设计链表）](#707-design-linked-list设计链表)
  - [单向链表实现（dummy head + size）](#单向链表实现dummy-head--size)
  - [双向链表实现（head/tail）](#双向链表实现headtail)
  - [索引步数与边界一把过](#索引步数与边界一把过)
  - [常见坑位清单](#常见坑位清单)
- [206. Reverse Linked List（反转链表）](#206-reverse-linked-list反转链表)
  - [双指针（迭代）](#双指针迭代)
  - [递归 = 把 while 拆开](#递归--把-while-拆开)
- [类型注解 & 语法点](#类型注解--语法点)
- [小抄：数组 vs 链表 & 单链 vs 双链](#小抄数组-vs-链表--单链-vs-双链)

------

## 203. Remove Linked List Elements（移除链表元素）

**题意**：删除链表中所有值等于 `val` 的节点，返回新的头结点。

**思路（推荐）**：`dummy` + 前驱指针扫描。用 `dummy = ListNode(0, head)`，指针 `cur` 指向**前驱**；若 `cur.next.val == val`，跳过它；否则 `cur = cur.next`。

```python
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
```

**常见疑问点**

- `if cur.next == val` ❌：这是把**节点对象**和整数比较；应写 `cur.next.val == val`。
- `while cur.next:` 与 `while cur.next != None` 等价（Python 对象的真值语义）。
- 为什么只返回头结点就够：**头 = 入口**，顺着 `next` 能访问整条链。
- 删除最后一个和中间节点是否不同：
  - 单链表尾删必须先找前驱 O(n)。
  - 删除中间（已知前驱）O(1)。
  - 双向链表若维护 `tail`，尾删 O(1)。

------

## 707. Design Linked List（设计链表）

### 单向链表实现（dummy head + size）

统一用「**找到前驱，再改指针**」。

```python
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
```

> 插入顺序必须是 `node.next = prev.next` → `prev.next = node`，否则丢失后继。

------

### 双向链表实现（head/tail）

维护 `head/tail/size`，头尾操作均 O(1)。

```python
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
```

------

### 索引步数与边界一把过

- **tail 的下标** = `size - 1`
- 从 **dummy** 出发找“index 的前驱” → 走 `index` 步
- 从 **head** 出发 → 走 `index - 1` 步
- 从 **tail** 出发：
  - 找 index 的前驱 → 走 `size - index` 步
  - 找 index 本身 → 走 `size - index - 1` 步

> 核心：**想清楚要停在谁身上（前驱 or 本身），就能自己推出步数**。

------

### 常见坑位清单

- `addAtIndex` 是 void：`index > size` 不插；`index <= 0` 当作头插。
- `pre = cur.next` 只是变量换指向；`cur.next = pre` 改链结构。
- `new_node = DListNode(val, prev, prev.next)` 会先构造右侧，再赋值给左侧。
- 返回头结点就够：**头 = 链表入口**。

------

## 206. Reverse Linked List（反转链表）

### 双指针（迭代）

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
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
```

------

### 递归 = 把 while 拆开

```python
class Solution:
    # 方法二: 递归法(其实就是把 while 循环展开，每次递归调用负责处理一步)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverse(head, None) # 调用入口, 从第一个头节点开始处理, 因为head还没有前驱, 所以pre应该是None
   
    def reverse(self, cur:ListNode, pre:ListNode) -> ListNode: # 递归reverse(cur, pre)里 就是「执行一次 while 循环」,递归的每一层就是 while 的一次迭代。
        if cur is None: #递归终止条件
            return pre #返回新头结点（pre）
        
        temp = cur.next
        cur.next = pre
        return self.reverse(temp, cur) # 把下一个节点交给递归, 进入下一层递归
```

- 初始必须是 `(head, None)`；写 `(None, head)` 会直接退出。
- 递归每一层就是 while 的一次迭代。

------

## 类型注解 & 语法点

- `Optional[ListNode]` = `ListNode | None`，链表可能为空。
- `-> None`：无返回值函数的注解。
- Python `while cur.next:` 等价于 `while cur.next is not None:`。
- `3 // 2 == 1`（向下取整）；`-3 // 2 == -2`。

------

## 小抄：数组 vs 链表 & 单链 vs 双链

| 场景                 | 数组（动态数组） | 单链表    | 双链表                     |
| -------------------- | ---------------- | --------- | -------------------------- |
| 头插/头删            | O(n)             | O(1)      | O(1)                       |
| 尾插/尾删            | 摊还 O(1)/O(1)   | 尾删 O(n) | O(1)                       |
| 中间插删（已知前驱） | O(n)             | O(1)      | O(1)                       |
| 随机访问第 k 个      | O(1)             | O(n)      | O(n)（可从两端近的一侧走） |

------

✅ 记忆法：

- **链表改结构 = 改指针**。
- 永远问自己：「我要改谁的 next / prev？」
- 想清楚目标，就能自己算出循环步数，而不是死记。

------

