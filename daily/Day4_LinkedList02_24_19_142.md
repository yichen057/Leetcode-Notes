# LeetCode 笔记：24 / 19 / 142（知识点 + 易错点 + 代码）

> 基于你前面所有提问与我们的讨论做的整理。重点突出指针关系、`dummy` 用法、快慢指针数学推导与常见坑。

---

“快慢指针”(fast & slow pointers) 的技巧在链表题里非常常见，它的本质是 **用两个速度不同的指针遍历链表**，来解决涉及「相对位置关系」的问题。

------

## 常见应用场景

### 1. **找中点**

- **题目例子**：LeetCode 876. Middle of the Linked List
- 思路：
  - 快指针一次走 2 步，慢指针一次走 1 步。
  - 当快指针到尾时，慢指针正好在中点。

👉 用在 **需要拆分链表** 或 **找中间节点** 的题目，比如链表归并排序。

------

### 2. **判断链表是否有环**

- **题目例子**：LeetCode 141. Linked List Cycle
- 思路：
  - 快指针一次走 2 步，慢指针一次走 1 步。
  - 如果有环，它们必定会相遇；如果无环，快指针会先到 `None`。

👉 用在 **检测环存在** 的问题。

------

### 3. **找环的入口**

- **题目例子**：LeetCode 142. Linked List Cycle II
- 思路：
  - 第一次相遇后，把一个指针放回头结点，另一个留在相遇点。
  - 两者改为一次走 1 步，再次相遇点就是环的入口。

👉 用在 **找环起点** 的问题。

------

### 4. **删除倒数第 N 个节点**

- **题目例子**：LeetCode 19. Remove Nth Node From End of List
- 思路：
  - 快指针先走 N 步，再让快慢指针一起走。
  - 当快指针到尾时，慢指针就在「倒数第 N 个节点的前一个」。

👉 用在 **和倒数位置有关** 的题目。

------

### 5. **判断回文链表**

- **题目例子**：LeetCode 234. Palindrome Linked List
- 思路：
  - 用快慢指针找到链表中点。
  - 翻转后半段，和前半段逐个比较。

👉 用在 **链表左右对称** 的题目。

------

### 6. **链表排序（归并排序）**

- **题目例子**：LeetCode 148. Sort List
- 思路：
  - 用快慢指针找到链表中点，把链表一分为二。
  - 分别排序再合并。

------

## 总结口诀

快慢指针常见用途可以记：

- **中点**（876, 148）
- **环存在**（141）
- **环入口**（142）
- **倒数第 N 个**（19）
- **回文判断**（234）

------

**142判断环形链表入口为什么一定要用快慢指针，不能直接两个同步指针去找环？**

------

## 先说答案

- **同步指针（一步一步一起走）** → 永远保持固定距离，不会相遇，所以不能判断有没有环。
- **快慢指针** → 因为速度差 ≠ 0，就像跑道上快的人追慢的人，一定能相遇（如果有环），从而既能判断“是否有环”，也能找到“环入口”。

------

## 为什么同步指针不行？

假设你有两个同步指针：

- `p1` 从头出发
- `p2` 也从头出发

它们每次都走一步：

- 如果链表有环，它们会同时进入环，但始终保持同步（重叠在一起），你没法区分“是正常走到一起”还是“因为有环才遇到”。
- 如果让它们一个从 `head` 出发，一个从 `head.next` 出发，它们之间的距离始终保持 1，不会缩短，也不会相遇。

👉 也就是说，**同步指针无法利用“相对速度差”去制造相遇**，自然也没法解决问题。

------

## 为什么快慢指针可以？

快慢指针的关键在于 **相对速度差**：

- 快指针一次走 2 步，慢指针一次走 1 步。
- 如果有环，快指针会一点点“追上”慢指针，最终在环中相遇。
- 这样我们就能知道“链表有环”。
- 然后再用数学关系（`a = c + (n-1)L`）找到环的入口。

------

## 总结

- **同步指针**：永远保持固定距离 → 无法相遇 → 没法判断是否有环。
- **快慢指针**：有速度差 → 必然相遇（如果有环） → 能判断有环，还能找到环入口。

------

要不要我帮你对比下 **「判断有环」的快慢指针解法** 和 **「用哈希表存 visited 节点」的解法**，优缺点一目了然？

## 24. Swap Nodes in Pairs（两两交换链表）

### 思路模板（迭代 + dummy）
- 建立 `dummy`，`cur = dummy`。
- 循环条件：`while cur.next and cur.next.next:`（必须同时保证两节点存在）。
- 命名三节点：`first = cur.next`，`second = first.next`，`third = second.next`。
- 三步换指针：
  1) `first.next = third`  
  2) `second.next = first`  
  3) `cur.next = second`
- `cur` 前进到本对的新尾：`cur = first`。

### 易错点
- ❌ 写成：
  ```python
  cur.next = cur.next.next
  cur.next = first  # 把 second 丢了
  ```
  ✅ 应该先连 `first.next`，再 `second.next = first`，最后 `cur.next = second`。
- `cur` 的移动：交换后应当 `cur = first`（这对的新尾），而不是盲目 `cur = cur.next.next`。
- 循环条件用 `while cur.next and cur.next.next:`，利用短路，安全又简洁。
- `dummy = ListNode(0)` 中的 `0` 是 **值**，非 index。`dummy` 必须实际创建，不是 `None`。

### 代码（推荐迭代）
```python
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next
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
            cur.next.next = temp # 改变指针方向, 2指向1
            temp.next = temp1 # 1指向3
            # 此时要移动指针cur, 从dummyhead的位置往后移动2位, 移动到能找到下一对要处理的节点, 也就是移动到它的前一个节点(即此时1的位置)
            cur= cur.next.next
        return dummyhead.next # 返回链表的入口
```

---

## 19. Remove Nth Node From End of List（删除倒数第 N 个节点）

### 思路模板（双指针同速 + 间隔 N）
- `dummy -> head`，`fast = slow = dummy`。
- `fast` 先走 `n` 步。
- 然后 `fast/slow` 同步前进直到 `fast.next` 为空，此时 `slow` 停在 **待删节点的前一个**。
- `slow.next = slow.next.next`。

### 易错点
- `fast` 先行 `n` 步不可少；若少走会错位。
- 删除的是 `slow.next`，不是 `slow` 自己。
- 注意 `n` 可能等于链表长度，必须用 `dummy` 才能安全删除头节点。
- Python 中空判断：`while cur.next:` 或 `is not None`；**没有** `null`。

### 代码（推荐）
```python
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

class Solution:
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
```

---

## 142. Linked List Cycle II（环形链表 II）

### 思路模板（两阶段）
**阶段 1：判环（快慢指针）**
- `fast = slow = head`
- `while fast and fast.next:`  
  `fast = fast.next.next`，`slow = slow.next`  
- 若相遇（`fast == slow`），进入阶段 2；否则无环。

**阶段 2：找入口（同步指针）**
- 数学关系：设 `a=头到入口`，`b=入口到相遇`，`L` 为环长。  
  有 `a = (n·L) - b`，等价于 **从 head 走 a 步 == 从相遇点走 L-b 步（即 c 步）**。  
- 实现：`p1 = head`，`p2 = meet`，二者同步走，一步一步，相遇处即入口。

> 注意：第二阶段已不再是快慢指针，而是 **两个同步指针**。

### 易错点
- Python 里返回无环用 `return None`，不是 `null`。
- 判环循环条件必须写 `while fast and fast.next:`，否则可能 `NoneType.next` 报错。
- 第二阶段不是“相向指针”从两端夹，而是“同向同步”从 `head` 与 `meet` 出发。
- 时间复杂度是 **O(n)** 而不是 O(n²)：相遇追赶最多环长 L 步，L ≤ n。

### 代码（快慢 + 同步）
```python
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

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
```

### 备选解（哈希表法，易理解，O(n) 空间）
```python
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
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
```

---

## 通用指针小抄（本次问答高频点）
- **dummy 节点**：`dummy = ListNode(0, head)`，`0` 是值；`dummy` 不是 `None`。  
- **引用**：指变量或 `.next` 持有的“指向关系”（地址/指针），不是“前一个节点”。  
- **空判断**：Python 用 `None`；简写 `while cur.next:`；需要访问两级时用 `while cur.next and cur.next.next:`。  
- **保存谁？**：在交换/删除等操作中，**会失去引用的节点** 必须事先保存（如 24 题里的 `first`）。  
- **复杂度**：24/19/142 都是 **O(n) 时间、O(1) 额外空间**（哈希法除外）。  
