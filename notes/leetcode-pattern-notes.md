下面是根据你最近问过的问题整理的 **Pattern Notes 初版**。你可以直接复制到一个 Markdown 文件里，比如：

```text
leetcode-pattern-notes.md
```

------

# **LeetCode Pattern Notes**

## **1. Hash Map / Set / Counter**

### **1.1 什么时候用 Hash Map / Set？**

一句话判断：

```text
Set：只关心“有没有见过”
Dict：需要“某个东西 -> 另一个东西”的映射
Counter：需要统计“每个元素出现几次”
```

| **题目关键词** | **常用数据结构**            |
| -------------- | --------------------------- |
| 是否重复       | `set`                       |
| 是否见过       | `set`                       |
| 去重           | `set`                       |
| 两数和         | `dict`                      |
| 频率 / 次数    | `Counter` / `dict`          |
| anagram        | `Counter` / frequency array |
| top k frequent | `Counter + heap/bucket`     |
| prefix sum     | `dict`                      |

------

## **1.2 Set**

### **用途**

`set` 适合记录：

```text
我之前是否见过这个元素？
```

模板：

```python
seen = set()

for x in nums:
    if x in seen:
        return True
    seen.add(x)
```

### **易错点**

`set` 只能存 hashable 的对象。

可以放：

```python
1
"abc"
(1, 2)
```

不能放：

```python
[1, 2]
{"a": 1}
{1, 2}
```

原因：

```text
list / dict / set 是 mutable，可变对象，不能 hash。
```

但是：

```python
set([1, 2, 3])
```

可以。



因为这不是把整个 list 放进 set，而是把 list 里的元素拆开加入 set。



等价于：

```python
s = set()
s.add(1)
s.add(2)
s.add(3)
```

------

## **1.3 Dict**

### **用途**

`dict` 适合建立映射：

```text
key -> value
```

常见例子：

```text
num -> index
char -> count
prefix_sum -> count
sorted_key -> list of strings
```

------

# **2. Two Sum Pattern**

## **2.1 核心模板**

```python
def twoSum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        need = target - num

        if need in seen:
            return [seen[need], i]

        seen[num] = i
```

## **2.2 Dict 里到底存什么？**

Two Sum 里的 dict 存的是：

```text
已经见过的真实数字 -> 它的 index
```

所以是：

```python
seen[num] = i
```

不是：

```python
seen[need] = i
```

### **为什么不是** **`seen[need] = i`****？**

因为 `need` 是“我希望找到的数字”，但它不一定真的出现在当前位置。

例如：

```python
nums = [2, 7, 11, 15]
target = 9
```

第一轮：

```python
num = 2
need = 7
```

如果写：

```python
seen[7] = 0
```

就等于说：

```text
数字 7 出现在 index 0
```

这是错的，因为 index 0 是 `2`。



正确是：

```python
seen[2] = 0
```

一句话记：

```text
check：查我需要的数以前有没有出现过
store：存我现在真实看到的数
```

------

# **3. Anagram Pattern**

## **3.1 什么是 Anagram？**

Anagram 是：

```text
两个字符串字符种类和出现次数一样，但顺序可以不同
```

例如：

```python
"listen"
"silent"
```

------

## **3.2 和 Palindrome 区别**

| **概念**   | **判断标准**                     |
| ---------- | -------------------------------- |
| palindrome | 正着读和反着读一样               |
| anagram    | 字符种类和次数一样，顺序可以不同 |

例子：

```python
"level"   # palindrome
"listen", "silent"   # anagram
```

------

## **3.3 方法一：Sorting**

```python
def isAnagram(s, t):
    return sorted(s) == sorted(t)
```

复杂度：

```text
Time: O(n log n)
Space: O(n)
```

适合 Unicode 字符，但如果有组合字符，比如 `é` 和 `e + accent`，可能需要 normalization。

------

## **3.4 方法二：Counter**

```python
from collections import Counter

def isAnagram(s, t):
    return Counter(s) == Counter(t)
```

`Counter(s)` 会统计字符出现次数。



例如：

```python
Counter("banana")
```

得到：

```python
Counter({'a': 3, 'n': 2, 'b': 1})
```

复杂度：

```text
Time: O(n)
Space: O(k)
```

`k` 是不同字符数量。

------

## **3.5 方法三：26 长度数组**

适合题目限制为小写字母 `a-z`。

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter = [0] * 26

        for i in range(len(s)):
            counter[ord(s[i]) - ord('a')] += 1
            counter[ord(t[i]) - ord('a')] -= 1

        for count in counter:
            if count != 0:
                return False

        return True
```

也可以用 `zip`：

```python
for ch_s, ch_t in zip(s, t):
    counter[ord(ch_s) - ord('a')] += 1
    counter[ord(ch_t) - ord('a')] -= 1
```

复杂度：

```text
Time: O(n)
Space: O(1)
```

因为数组长度固定为 26。

------

# **4. Group Anagrams Pattern**

## **4.1 核心思想**

给每个字符串生成一个标准 key。

Anagram 的 key 一样，就放到同一个 group。

------

## **4.2 Sorting key**

```python
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            groups[key].append(s)

        return list(groups.values())
```

例如：

```python
"eat" -> "aet"
"tea" -> "aet"
"ate" -> "aet"
```

所以它们进入同一组。



复杂度：

```text
n = 字符串数量
k = 字符串平均长度

Time: O(n * k log k)
Space: O(n * k)
```

------

## **4.3 Frequency tuple key**

适合只有小写字母 `a-z`。

```python
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for ch in s:
                count[ord(ch) - ord("a")] += 1

            groups[tuple(count)].append(s)

        return list(groups.values())
```

为什么不能直接用 `count` 作为 key？

```text
dict 的 key 必须 hashable。
list 是 mutable，不可哈希。
tuple 是 immutable，可以作为 dict key。
```

所以要：

```python
tuple(count)
```

------

## **4.4** **`list(groups.values())`** **vs** **`[groups.values()]`**

正确：

```python
return list(groups.values())
```

意思是把 `dict_values` view 转成真正的 list。



错误：

```python
return [groups.values()]
```

这会把整个 `dict_values` 当成一个元素包进 list，结构多了一层。

------

# **5. Top K Frequent Elements - LC347**

## **5.1 Method 1: Frequency Map + Sorted**

```python
freq_dict = {}

for num in nums:
    freq_dict[num] = freq_dict.get(num, 0) + 1

sorted_items = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)

result = []
for i in range(k):
    result.append(sorted_items[i][0])

return result
```

复杂度：

```text
m = unique elements count

Time: O(n + m log m)，最坏 O(n log n)
Space: O(m + k)，最坏 O(n)
```

说明：

```python
sorted(freq_dict.items())
```

默认按 key 从小到大排序。

```python
sorted(freq_dict.items(), key=lambda x: x[1])
```

按 value 排序。

------

## **5.2 Method 2: Heap**

```python
from collections import Counter
import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []

        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))

            if len(heap) > k:
                heapq.heappop(heap)

        return [num for freq, num in heap]
```

### **为什么 heap 存** **`(freq, num)`****？**

因为 Python `heapq` 默认按 tuple 第一个元素排序。

```text
heap[0] 是当前 heap 里 frequency 最小的元素
```

我们维护 size k 的 min heap：

```text
如果 heap 超过 k，就 pop 最小 frequency 的元素
最后 heap 里剩下的就是 top k frequent
```

复杂度：

```text
Time: O(n + m log k)
Space: O(m + k)，最坏 O(n)
```

------

## **5.3 为什么返回** **`[num for freq, num in heap]`****？**

因为 heap 里是：

```python
[(freq, num), (freq, num)]
```

题目只需要数字 `num`。



所以：

```python
[num for freq, num in heap]
```

表示：

```text
遍历 heap
拆开每个 tuple
只取 num
组成一个新的 list
```

如果写：

```python
list(heap)
```

得到的是：

```python
[(freq, num), (freq, num)]
```

不是题目想要的答案。

------

## **5.4 Method 3: Bucket Sort**

```python
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            buckets[freq].append(num)

        result = []

        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)

                if len(result) == k:
                    return result
```

### **核心思想**

```text
frequency 最大不会超过 len(nums)
所以可以用 frequency 当 index
buckets[freq] 存所有出现 freq 次的数字
```

例如：

```python
nums = [1,1,1,2,2,3]
```

frequency map:

```python
1 -> 3
2 -> 2
3 -> 1
```

bucket:

```python
buckets[1] = [3]
buckets[2] = [2]
buckets[3] = [1]
```

从高频往低频扫，取够 k 个。



复杂度：

```text
Time: O(n)
Space: O(n)
```

------

## **5.5 Bucket range 易错点**

这两个都可以：

```python
for freq in range(len(buckets) - 1, 0, -1):
```

会遍历到 `1`，不包含 `0`。

```python
for freq in range(len(buckets) - 1, -1, -1):
```

会遍历到 `0`。



在 frequency bucket 里，`buckets[0]` 没意义，因为出现过的元素频率至少是 1。



所以推荐：

```python
for freq in range(len(buckets) - 1, 0, -1):
```

------

## **5.6 面试讲解顺序**

建议顺序：

```text
1. 先讲 Counter + sorting，最直观
2. 再优化为 min heap，避免完整排序
3. 最后讲 bucket sort，满足 follow-up better than O(n log n)
```

------

# **6. Bucket Sort Pattern**

## **6.1 什么时候想到 Bucket Sort？**

看到这些关键词：

```text
frequency
count
top k frequent
范围有限
better than O(n log n)
```

------

## **6.2 通用模板**

```python
from collections import Counter

count = Counter(items)

buckets = [[] for _ in range(len(items) + 1)]

for item, freq in count.items():
    buckets[freq].append(item)

result = []

for freq in range(len(buckets) - 1, 0, -1):
    for item in buckets[freq]:
        result.append(item)

        if len(result) == k:
            return result
```

------

## **6.3 易错点：二维 list 初始化**

不要写：

```python
buckets = [[]] * (len(nums) + 1)
```

因为这会创建多个指向同一个 list 的引用。



正确：

```python
buckets = [[] for _ in range(len(nums) + 1)]
```

------

# **7. Heap Pattern**

## **7.1 Heap 和 Deque 区别**

| **数据结构** | **关注点**          | **常见题**                         |
| ------------ | ------------------- | ---------------------------------- |
| deque        | 先进先出 / 两端操作 | BFS, queue, sliding window         |
| heap         | 按优先级取最小/最大 | Top K, kth largest, priority queue |

------

## **7.2 Python heap 是 min heap**

```python
import heapq

heap = []

heapq.heappush(heap, x)
smallest = heapq.heappop(heap)
smallest_now = heap[0]
```

`heap[0]` 永远是当前最小值。

------

## **7.3 找第 K 大**

```python
import heapq

def findKthLargest(nums, k):
    heap = []

    for num in nums:
        heapq.heappush(heap, num)

        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]
```

思路：

```text
维护 size k 的 min heap
heap 里保留最大的 k 个数
heap[0] 是这 k 个数里最小的
也就是第 k 大
```

例如：

```python
nums = [3, 2, 1, 5, 6, 4]
k = 2
```

最后 heap 保留：

```python
[5, 6]
```

`heap[0] = 5`，就是第 2 大。

------

# **8. Linked List Pattern**

## **8.1 Dummy Node**

适合：

```text
删除节点
合并链表
头节点可能变化
```

模板：

```python
dummy = ListNode(0)
dummy.next = head
prev = dummy

# operations...

return dummy.next
```

为什么返回 `dummy.next`？

```text
head 是原来的头，不一定还是新头。
dummy.next 永远指向当前真正的头。
```

------

## **8.2 删除节点**

```python
def delete_node(head, target):
    dummy = ListNode(0)
    dummy.next = head

    prev = dummy

    while prev.next:
        if prev.next.val == target:
            prev.next = prev.next.next
            break
        prev = prev.next

    return dummy.next
```

关键：

```python
prev.next = prev.next.next
```

表示跳过要删除的节点。

------

## **8.3 LC19 Remove Nth Node From End**

```python
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head

        fast = head
        slow = dummy

        for _ in range(n):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next
```

为什么：

```python
fast = head
slow = dummy
```

因为删除节点需要找到待删除节点的前一个节点。

`fast` 先走 n 步，制造 n 的距离。

当 `fast` 到 `None` 时，`slow.next` 就是倒数第 n 个节点。

------

## **8.4 Reverse Linked List**

```python
def reverse(head):
    prev, cur = None, head

    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt

    return prev
```

四步记忆：

```text
1. nxt = cur.next       保存下一个
2. cur.next = prev      反转箭头
3. prev = cur           prev 前进
4. cur = nxt            cur 前进
```

易错点：

```text
改 next 前，先保存 next，否则后面的链表会丢。
```

------

## **8.5 Merge Two Sorted Lists**

```python
def merge(l1, l2):
    dummy = ListNode(0)
    tail = dummy

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next

        tail = tail.next

    tail.next = l1 or l2

    return dummy.next
```

理解：

```text
dummy：假头，方便返回结果
tail：新链表的尾巴
l1/l2：两个待处理链表的当前位置
```

谁被接到结果里，谁就往后移动：

```python
l1 = l1.next
```

tail 也要往后移动：

```python
tail = tail.next
```

------

# **9. Binary Search Pattern**

## **9.1 标准二分：找 exact target**

```python
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1
```

适合：

```text
找 target 是否存在
找到任意一个位置
```

------

## **9.2 找第一个** **`>= target`**

```python
def lower_bound(arr, target):
    lo, hi = 0, len(arr)

    while lo < hi:
        mid = (lo + hi) // 2

        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid

    return lo
```

这里：

```text
搜索区间是 [lo, hi)
lo == hi 时结束
```

------

## **9.3 找第一个** **`> target`**

```python
def upper_bound(arr, target):
    lo, hi = 0, len(arr)

    while lo < hi:
        mid = (lo + hi) // 2

        if arr[mid] <= target:
            lo = mid + 1
        else:
            hi = mid

    return lo
```

------

## **9.4 LC34**

```python
left = lower_bound(nums, target)

if left == len(nums) or nums[left] != target:
    return [-1, -1]

right = upper_bound(nums, target) - 1

return [left, right]
```

记忆：

```text
left = 第一个 >= target
right = 第一个 > target 的位置 - 1
```

------

# **10. Stack Pattern**

## **10.1 LC20 Valid Parentheses**

```python
def isValid(s):
    stack = []
    pair = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for ch in s:
        if ch in pair:
            if not stack or stack[-1] != pair[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)

    return len(stack) == 0
```

核心：

```text
左括号入栈
右括号检查栈顶是否匹配
最后 stack 为空才合法
```

------

## **10.2 LC739 Daily Temperatures**

```python
def dailyTemperatures(temperatures):
    n = len(temperatures)
    ans = [0] * n
    stack = []

    for i, temp in enumerate(temperatures):
        while stack and temp > temperatures[stack[-1]]:
            prev_index = stack.pop()
            ans[prev_index] = i - prev_index

        stack.append(i)

    return ans
```

stack 存的是：

```text
还没找到更高温度的下标
```

为什么存 index？

```text
因为答案要算 i - prev_index
```

为什么是 while？

```text
当前温度可能同时解决多个之前的天
```

------

# **11. Binary Tree Pattern**

## **11.1 DFS / 递归**

前序：

```python
def preorder(node):
    if not node:
        return
    print(node.val)
    preorder(node.left)
    preorder(node.right)
```

中序：

```python
def inorder(node):
    if not node:
        return
    inorder(node.left)
    print(node.val)
    inorder(node.right)
```

后序：

```python
def postorder(node):
    if not node:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.val)
```

------

## **11.2 BFS / 层序遍历**

```python
from collections import deque

def levelOrder(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level = []
        size = len(queue)

        for _ in range(size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result
```

queue 存的是：

```text
接下来要处理的 TreeNode 节点
```

不是 `node.val`，因为还要访问：

```python
node.left
node.right
```

------

## **11.3 LC104 Maximum Depth**

```python
def maxDepth(root):
    if not root:
        return 0

    left = maxDepth(root.left)
    right = maxDepth(root.right)

    return max(left, right) + 1
```

递归三问：

```text
1. 空节点返回什么？
2. 左右子树返回什么？
3. 当前节点怎么合并？
```

------

## **11.4 LC543 Diameter of Binary Tree**

```python
class Solution:
    def diameterOfBinaryTree(self, root):
        self.ans = 0

        def depth(node):
            if not node:
                return 0

            left = depth(node.left)
            right = depth(node.right)

            self.ans = max(self.ans, left + right)

            return max(left, right) + 1

        depth(root)
        return self.ans
```

关键区分：

```text
depth 返回给上层的是“最大深度”
self.ans 更新的是“全局最大直径”
```

为什么：

```python
self.ans = max(self.ans, left + right)
```

因为经过当前节点的最长路径是：

```text
左子树最大深度 + 右子树最大深度
```

为什么 return 不是 `left + right`？

```text
往父节点返回时，只能选择左边或右边一条路继续往上。
所以返回 max(left, right) + 1。
```

------

## **11.5 LC98 Validate BST**

```python
def isValidBST(root):
    def dfs(node, low, high):
        if not node:
            return True

        if not (low < node.val < high):
            return False

        return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

    return dfs(root, float("-inf"), float("inf"))
```

`dfs(node, low, high)` 表示：

```text
检查以 node 为根的树，所有节点值是否都在 (low, high) 范围内
```

外层：

```python
return dfs(root, -inf, inf)
```

表示从整棵树开始检查。



内层：

```python
return dfs(left) and dfs(right)
```

表示左右子树都必须合法。

------

# **12. Python Syntax Notes**

## **12.1** **`for`** **vs** **`while`**

```text
for：知道要遍历什么 / 循环多少次
while：只知道停止条件
```

数组常用 for：

```python
for num in nums:
    ...
```

链表常用 while：

```python
while cur:
    cur = cur.next
```

双指针常用 while：

```python
while left < right:
    ...
```

------

## **12.2 从后往前遍历**

```python
for i in range(len(nums) - 1, -1, -1):
    print(i, nums[i])
```

只拿 value：

```python
for num in reversed(nums):
    print(num)
```

while：

```python
i = len(nums) - 1

while i >= 0:
    print(i, nums[i])
    i -= 1
```

------

## **12.3 Slicing 复杂度**

```python
arr[l:r]
s[l:r]
```

时间和空间都是：

```text
O(k)
```

`k` 是 slice 长度。



反转：

```python
s[::-1]
```

复杂度：

```text
Time: O(n)
Space: O(n)
```

------

## **12.4 Unpacking**

```python
a, b = [1, 2]
```

表示把右边拆开赋值。



常见：

```python
for i, num in enumerate(nums):
    ...
```

`enumerate(nums)` 每轮产生：

```python
(i, num)
```

然后自动 unpack。

------

## **12.5** **`self.ans`** **vs** **`nonlocal ans`**

如果内部函数要修改外层数字变量：

```python
ans = 0

def helper():
    nonlocal ans
    ans += 1
```

如果用 class 属性：

```python
self.ans = 0

def helper():
    self.ans += 1
```

不需要 `nonlocal`。



list 的 `.append()` 不需要 `nonlocal`：

```python
result = []

def dfs(node):
    result.append(node.val)
```

因为这是修改 list 内容，不是重新赋值。

------

# **13. 你目前最需要强化的点**

根据你问的问题，你现在最该重点练这几类：

## **13.1 Hash Map / Set / Counter**

练习：

```text
LC1 Two Sum
LC217 Contains Duplicate
LC242 Valid Anagram
LC49 Group Anagrams
LC347 Top K Frequent Elements
LC560 Subarray Sum Equals K
```

每题写三行：

```text
为什么用 hash map / set？
key 是什么？
value 是什么？
```

------

## **13.2 Binary Search 边界**

重点背：

```text
lower_bound = 第一个 >= target
upper_bound = 第一个 > target
right boundary = upper_bound - 1
```

练习：

```text
LC704
LC34
LC35
LC278
LC875
```

------

## **13.3 Linked List 指针移动**

重点练：

```text
dummy
fast/slow
reverse
merge
```

练习：

```text
LC206 Reverse Linked List
LC21 Merge Two Sorted Lists
LC19 Remove Nth Node From End
LC141 Linked List Cycle
LC142 Linked List Cycle II
```

------

## **13.4 Tree 递归**

重点练：

```text
base case
left result
right result
merge current node
```

练习：

```text
LC102
LC104
LC226
LC100
LC101
LC543
LC98
LC700
```

------

# **14. 最推荐你的笔记结构**

每道题用这个格式：

```markdown
# LC347 Top K Frequent Elements

## Pattern
Counter + Bucket Sort

## Why this pattern
Need top k frequent elements. Frequency range is 1..n, so use bucket.

## Key idea
buckets[freq] stores numbers appearing freq times.

## Code
...

## Complexity
Time: O(n)
Space: O(n)

## My mistakes
- Do not use [[]] * n.
- buckets[0] is unused.
- return [num for freq, num in heap], not list(heap).
```

你以后复习时，重点看：

```text
Pattern
Key idea
Mistakes
```

而不是重新看长篇解释。