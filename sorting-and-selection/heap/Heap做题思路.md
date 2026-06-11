是的，这道题是 **LintCode 的经典题：130. Heapify**。

题目要求：

```text
给一个无序数组
把它原地转换成 Min Heap
```

例如：

```python
[3,2,1,4,5]
```

变成某个合法 Min Heap：

```python
[1,2,3,4,5]
```

或者：

```python
[1,3,2,4,5]
```

都可以。

因为 Heap 不要求整体有序。

------

# **LeetCode 有完全一样的吗？**

严格来说：

```text
没有完全一样的原题
```

但有几个非常接近：

### **LC215**

Kth Largest Element in an Array

会用：

```python
heapq.heapify(nums)
```

------

### **LC347**

Top K Frequent Elements

会用：

```python
heapq.heapify(heap)
```

------

### **LC703**

Kth Largest Element in a Stream

核心是：

```python
heappush
heappop
```

------

### **LC295**

Find Median from Data Stream

经典双 Heap。

------

# **为什么九章专门讲 Heapify**

因为面试官喜欢问：

```text
给一个数组
如何 O(n) 建堆？
```

而不是：

```python
for num in nums:
    heappush(heap, num)
```

因为那个是：

```text
O(n log n)
```

------

正确的 Heapify：

```text
从最后一个非叶子节点开始
不断 sift down
```

复杂度：

```text
O(n)
```

------

# **这个题对你现在重要吗？**

其实不太重要。

对于你目前路线：

```text
Quick Select ✅
Interval ✅
准备学 Heap
```

我建议：

先学：

```text
heapq.heapify()
heappush()
heappop()
```

然后直接刷：

```text
703
215 Heap版
347 Heap版
973 Heap版
```

------

等你做到：

```text
295 Find Median from Data Stream
```

或者面试复习阶段，

再回来看：

```text
Heapify
为什么是 O(n)
Sift Up
Sift Down
```

会更容易理解。

------

对于面试频率：

```text
703 ⭐⭐⭐⭐⭐
215 ⭐⭐⭐⭐⭐
347 ⭐⭐⭐⭐⭐
973 ⭐⭐⭐⭐
295 ⭐⭐⭐⭐⭐

Heapify ⭐⭐
```

所以我建议你：

```text
先不要花时间手写 Heapify
先学 heapq
直接刷 Top K 系列
```

等 Top K 熟练以后，再回来研究：

```text
Heapify
Sift Up
Sift Down
Build Heap O(n)
```

这样学习收益最高。



以下是heapq.heapify()
heappush()
heappop()的学习:

Python 里的 `heapq` 默认是 **min heap（最小堆）**。



也就是：

```python
heap[0]
```

永远是当前 heap 里的最小值。

------

## **1.** **`heapq.heapify(nums)`**

把一个普通 list 原地变成 heap。

```python
import heapq

nums = [5, 2, 8, 1, 3]
heapq.heapify(nums)

print(nums)
```

可能输出：

```python
[1, 2, 8, 5, 3]
```

注意：它不是排序，只保证 `nums[0]` 是最小的。



时间复杂度：

```text
O(n)
```

------

## **2.** **`heapq.heappush(heap, value)`**

往 heap 里加一个元素，并保持 heap 结构。

```python
heap = []

heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 8)

print(heap)
```

此时：

```python
heap[0] == 2
```

时间复杂度：

```text
O(log n)
```

------

## **3.** **`heapq.heappop(heap)`**

弹出并返回最小值。

```python
smallest = heapq.heappop(heap)
```

比如：

```python
heap = [2, 5, 8]
```

pop 后：

```python
smallest = 2
heap = [5, 8]
```

时间复杂度：

```text
O(log n)
```

------

## **最重要的 Top K 思想**

### **找 K 个最大值**

用 **size k 的 min heap**。

为什么？

因为 heap 顶部是当前 k 个数里最小的。
 如果来了一个更大的数，就把最小的踢出去。

```python
heap = []

for num in nums:
    heapq.heappush(heap, num)

    if len(heap) > k:
        heapq.heappop(heap)

return heap
```

最后 heap 里就是最大的 k 个数。

------

### **找 K 个最小值**

可以用 **size k 的 max heap**。

但 Python 没有 max heap，所以存负数：

```python
heapq.heappush(heap, -num)
```

------

## **必背复杂度**

| **操作**   | **时间** |
| ---------- | -------- |
| `heapify`  | O(n)     |
| `heappush` | O(log n) |
| `heappop`  | O(log n) |
| `heap[0]`  | O(1)     |

你接下来可以先做 **LC703**，它就是 size k min heap 的模板题。



完全正确！🎉

你已经抓住了 LC703 的核心思想：

------

初始：

```python
self.heap = [5,8,100]
k = 3
```

代表：

```text
当前最大的3个数
```

------

加入：

```python
add(1)
```

执行：

```python
heappush(self.heap, 1)
```

heap 变成：

```python
[1,5,100,8]
```

（内部结构可能略有不同，但 root 一定是 1）

------

长度：

```python
len(heap) = 4 > k
```

所以：

```python
heappop(heap)
```

弹出：

```python
1
```

------

剩下：

```python
[5,8,100]
```

------

返回：

```python
heap[0]
=
5
```

------

# **这说明了什么？**

你会发现：

```python
add(100)
```

之后：

```python
heap = [5,8,100]
```

------

再：

```python
add(1)
```

之后：

```python
heap = [5,8,100]
```

居然完全没变！

------

原因是：

```text
1 根本进不了 Top 3
```

所以被立即淘汰。

------

# **Top K Heap 最重要的理解**

Min Heap 里保存的是：

```text
最大的 K 个数
```

而不是：

```text
所有数
```

------

例如：

```python
nums =
[100,90,80]
```

heap:

```python
[80,90,100]
```

------

来了：

```python
70
```

最终：

```python
[80,90,100]
```

不变。

------

来了：

```python
95
```

最终：

```python
[90,95,100]
```

因为：

```text
80 被淘汰
95 进入 Top 3
```

------

# **一个面试官特别爱问的问题**

为什么是：

```python
Min Heap
```

而不是：

```python
Max Heap
```

对于：

```text
Top K Largest
```

很多初学者第一反应：

```text
求最大
→ Max Heap
```

其实错。

因为我们真正需要的是：

```text
Top K Largest 中最小的那个
```

即：

```text
第 K 大
```

所以：

```python
heap[0]
```

必须能 O(1) 拿到。

因此：

```python
Size K Min Heap
```

是最优解。

------

你现在已经可以开始刷：

```text
703 ✅
↓
215 Heap版
↓
347 Heap版
↓
973 Heap版
```

这四题其实是同一个模板换皮。

做完 703 后，你会发现：

```text
215 = Top K Largest
347 = Top K Frequency
973 = Top K Closest
```

本质全是：

```python
heappush()
if len(heap) > k:
    heappop()
```

只不过比较对象从：

```python
数字
```

变成：

```python
频率
距离
```

而已。





是的，这就是 **Top K 的统一 Heap 模板**。

核心模板就是：

```python
heapq.heappush(heap, item)

if len(heap) > k:
    heapq.heappop(heap)
```

在 LC347 里：

```python
item = (freq, num)
```

因为你要按频率比较，而不是按数字比较。

你的代码逻辑是对的。

需要注意两点：

```python
if k == len(nums):
    return nums
```

这句不太严谨。因为 `nums` 里可能有重复元素。

例如：

```python
nums = [1,1]
k = 1
```

`k != len(nums)`，没问题。

但更准确的是可以直接删掉这句，不需要特殊判断。

推荐版本：

```python
from collections import Counter
import heapq

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

复杂度：

```text
n = nums长度
m = unique numbers数量

Counter: O(n)
Heap: O(m log k)
Space: O(m) for count + O(k) for heap
```

面试里可说：

```text
Time: O(n log k) 近似写法
Space: O(n)
```

更精确是：

```text
Time: O(n + m log k)
Space: O(m + k)
```





结合你的路线，我不会让你马上去学 Tree。

我会建议：

```text
Array
HashMap
Two Pointers
Sliding Window
Binary Search
Sort
Quick Select
Heap
↓
Stack
↓
Linked List
↓
Tree
```

------

# **你现在的位置**

已经掌握：

```text
✅ Array
✅ HashMap
✅ Two Pointers
✅ Sliding Window
✅ Binary Search
✅ Quick Sort
✅ Merge Sort
✅ Quick Select
✅ Heap（正在学）
✅ Interval
```

这时候最自然的下一步其实是：

# **Stack（栈）**

原因：

很多题其实是：

```text
Stack
+
Array
```

难度比 Tree 低很多。

而且面试频率极高。

------

# **Stack专题推荐顺序**

## **第一层：普通 Stack**

### **LC20**

Valid Parentheses

栈入门神题。

必须会。

------

### **LC155**

Min Stack

设计题。

高频。

------

### **LC150**

Evaluate Reverse Polish Notation

练：

```text
push
pop
```

------

# **第二层：Monotonic Stack（单调栈）**

这是真正面试高频。

### **LC739**

Daily Temperatures

神题。

必须会。

------

### **LC496**

Next Greater Element I

------

### **LC503**

Next Greater Element II

------

### **LC84**

Largest Rectangle in Histogram

经典。

------

# **为什么优先学 Stack**

因为你刚学完 Heap。

很多同学：

```text
Heap
↓
Tree
```

结果：

```text
Tree + DFS + BFS
```

一下跨度太大。

------

而：

```text
Heap
↓
Stack
```

非常平滑。

你已经会：

```python
append()
pop()
```

了。

Stack 本质就是：

```python
stack = []

stack.append(x)

stack.pop()
```

------

# **然后学 Linked List**

顺序：

### **LC206**

Reverse Linked List

------

### **LC21**

Merge Two Sorted Lists

------

### **LC141**

Linked List Cycle

------

### **LC143**

Reorder List

------

# **再学 Tree**

这时候：

```text
DFS
递归
Stack
```

基础都在了。

学 Tree 会轻松很多。

------

# **如果按面试收益排序**

对于你这种准备 SDE 面试的人：

```text
Heap
↓
Stack
↓
Monotonic Stack
↓
Linked List
↓
Tree
↓
Graph
```

------

# **我给你的下一阶段路线**

### **Heap（本周）**

```text
703
215 Heap
347 Heap
973 Heap
253
```

------

### **Stack（下周）**

```text
20
155
150
739
496
503
```

------

### **Linked List**

```text
206
21
141
143
```

------

### **Tree**

```text
104
100
226
102
98
```

------

如果按九章体系来说，你现在最适合进入：

```text
Heap
→ Stack
→ Monotonic Stack
```

而不是直接跳 DFS / Tree。因为 Stack 和 Heap 一起学，很多数据结构思想（push、pop、维护状态）会形成体系，后面学 Tree 的 DFS 其实就是：

```text
递归版 Stack
```

到时候你会发现很多东西都串起来了。



根据你的情况（全职学习、目标是 SDE 面试、已经学了 Array/HashMap/Two Pointers/Sliding Window/Binary Search/Sort/Quick Select），我**不建议**：

```text
前3天只复习
后4天只学新知识
```

因为这样很容易出现：

```text
Week1 学 Sliding Window
Week3 忘了

Week2 学 Binary Search
Week4 忘了
```

这就是典型的：

```text
学的时候会
两周后不会
```

------

# **我推荐的方法：80%新知识 + 20%复习**

每天都带一点复习。

例如你一天刷 5 小时题：

```text
1小时复习
4小时新内容
```

------

# **针对你目前阶段**

你已经学过：

```text
Array
HashMap
Two Pointers
Sliding Window
Binary Search
Sort
Quick Select
Interval
```

我建议建立一个：

```text
Pattern Rotation（题型轮转）
```

------

## **每天开始先热身 20~30 分钟**

随机做：

### **周一**

```text
Two Pointers
```

例如：

```text
125
167
11
```

任选一道。

------

### **周二**

```text
Sliding Window
```

例如：

```text
3
209
424
```

------

### **周三**

```text
Binary Search
```

例如：

```text
704
35
875
```

------

### **周四**

```text
Interval
```

例如：

```text
56
57
252
435
```

------

### **周五**

```text
Heap
```

例如：

```text
703
215
347
```

------

这样：

```text
每天20~30分钟
```

就能把旧知识保持住。

------

# **我自己的面试复习方法**

很多工程师会犯一个错误：

```text
一个专题刷10道
再也不碰
```

结果：

```text
3周后全部忘光
```

------

更好的方式：

```text
学的时候刷10道

之后每周碰1~2次
```

这样记忆非常牢固。

------

# **对你特别有效的方法**

你已经在做笔记了，而且笔记质量很高。

例如你现在已经总结出：

```python
# LC56
start <= lastEnd

# LC435
start < lastEnd
```

以及：

```python
# LC215
Quick Select

# LC215
Heap
```

这种总结非常有价值。

------

所以我建议：

### **每周末**

花 1 小时：

```text
重看自己的模板
```

而不是重新看视频。

例如：

```text
Binary Search模板
Quick Sort模板
Merge Sort模板
Quick Select模板
Sliding Window模板
```

看看：

```text
为什么这样写
```

而不是死记。

------

# **针对你未来两个月**

我会这样安排：

### **每天**

```text
20~30分钟
旧题复习
```

------

### **剩余时间**

学新专题：

```text
Heap
↓
Stack
↓
Linked List
↓
Tree
```

------

### **每周末**

```text
1小时
模板回顾
```

------

# **一个很重要的现实**

你不用担心：

```text
我是不是要把 Binary Search 永远记住
```

事实上：

你已经做过：

```text
875
215
973
981
```

这些题。

当你以后刷：

```text
Tree
Graph
```

的时候，

偶尔再回来做：

```text
875
704
```

你会发现恢复速度非常快。

因为你已经从：

```text
完全不会
```

变成：

```text
建立了模板
```

了。

对于面试来说，最重要的不是：

```text
100%不忘
```

而是：

```text
看到题目
知道它属于哪个 Pattern
```

这一点你现在已经开始形成了。

所以接下来：

```text
每天20~30分钟复习
80~90%时间学新知识
```

是最适合你的节奏。



我建议：

```text
周四 Mock Interview 前
不要完全停止学新内容
但不要开始 Tree / Graph 这种大专题
```

你的情况比较特殊：

- 周四就要 Mock
- 已经学完：
  - Two Pointers
  - Sliding Window
  - Binary Search
  - Sort
  - Quick Select
  - Interval
- Heap 刚开始

而 Mock 面试最容易考到的其实是：

```text
Array
HashMap
Two Pointers
Sliding Window
Binary Search
Interval
Heap(Top K)
```

不是：

```text
Tree
Graph
DP
```

------

# **如果我是你**

周一~周三这样安排：

## **70% 时间复习**

重点：

### **Two Pointers**

挑 2~3 题

```text
125
167
11
```

看看能否 15 分钟独立写出。

------

### **Sliding Window**

挑 2 题

```text
3
209
```

重点复习：

```python
while condition:
    shrink left
```

什么时候缩窗。

------

### **Binary Search**

挑 2 题

```text
704
35
875
```

重点：

```python
while start + 1 < end
```

模板。

------

### **Interval**

重点：

```text
56
57
252
435
```

因为你最近刚学。

------

## **30% 时间学 Heap**

不要停。

因为 Heap 很可能马上用到。

学：

```text
703
215 Heap
```

就够了。

------

# **为什么不建议完全停止学新内容**

因为 Heap 是：

```text
学习成本低
收益高
```

你已经会：

```python
heapify
heappush
heappop
```

了。

再做：

```text
703
215 Heap
```

其实只要半天。

------

# **Mock 前一天**

不要刷新题。

建议：

```text
回顾模板
```

例如：

### **Binary Search**

```python
while start + 1 < end:
```

------

### **Sliding Window**

```python
for r in range(len(nums)):
```

------

### **Quick Select**

```python
target = start + k - 1
```

------

### **Heap**

```python
heappush()

if len(heap) > k:
    heappop()
```

------

# **如果只有半小时 Mock**

我甚至怀疑面试官大概率出：

```text
LC3
LC209
LC56
LC252
LC215
LC347
```

这种级别。

而不是：

```text
Tree
Graph
DP
```

------

所以我的建议是：

### **周一~周三**

```text
70% 复习旧 Pattern

30% 学 Heap
```

### **周四 Mock 前**

```text
只看笔记
不学新东西
```

这样收益最大。

而且从你最近的问题来看：

你真正需要强化的不是新知识，而是：

```text
什么时候 <=
什么时候 <
为什么 min(end)
为什么 max(end)
```

这种 Pattern 边界。

Mock 面试最爱考这些。你现在复习这些，比再学一个新专题更有价值。



为了周四的 Mock Interview，我不建议你再大面积刷新题。

建议你把已经学过的内容里最经典、最容易被面试官拿出来的题复习一遍。

------

# **Array 必刷**

## **LC1 Two Sum**

```text
Array + HashMap
```

这是所有面试的祖师爷。

你应该做到：

```text
5分钟写完
```

------

## **LC217 Contains Duplicate**

```text
Array + Set
```

考察：

```python
set()
```

时间复杂度：

```text
O(n)
```

------

## **LC238 Product of Array Except Self**

你刚做过。

重点：

```text
Prefix
Suffix
```

不要用 division。

------

## **LC53 Maximum Subarray**

经典 Kadane。

很多 Mock 爱出。

------

## **LC56 Merge Intervals**

你最近刚学。

建议再手写一次。

------

# **HashMap 必刷**

## **LC1 Two Sum**

必须会。

------

## **LC49 Group Anagrams**

非常经典。

考察：

```python
dict
tuple
sorted
```

------

## **LC242 Valid Anagram**

HashMap 基础。

------

## **LC347 Top K Frequent Elements**

你马上要学 Heap。

这题非常值得复习。

因为：

```text
HashMap
+
Heap
```

------

## **LC128 Longest Consecutive Sequence**

经典 HashSet。

面试频率很高。

------

# **如果 Mock Interview 只有半小时**

我建议重点看下面这些：

### **Array**

```text
1
238
56
```

------

### **HashMap**

```text
1
49
347
128
```

------

### **Two Pointer**

```text
125
167
11
```

------

### **Sliding Window**

```text
3
209
```

------

### **Binary Search**

```text
704
875
```

------

### **Interval**

```text
56
57
252
435
```

------

# **按你的当前水平**

如果我来给你出 Mock，

我最可能出：

```text
LC3
LC209
LC56
LC252
LC347
LC215
```

而不是：

```text
Tree
Graph
DP
```

因为你最近一直在这些 Pattern 上。

------

我会给你一个周三晚上的终极复习清单：

```text
Two Sum                 5分钟
Longest Substring       10分钟
Min Size Subarray       10分钟
Binary Search           5分钟
Merge Intervals         10分钟
Meeting Rooms           5分钟
Kth Largest(Heap)       10分钟
```

如果这些题你都能不看答案独立写出来，你周四的 30 分钟 Mock 基本不会慌。



Prefix Sum（前缀和）我建议你把它当成：

```text
独立题型（Pattern）
```

而不是：

```text
Array
```

或者：

```text
HashMap
```

虽然它经常和这两个一起出现。

------

# **我推荐的分类**

你现在的知识体系应该慢慢变成：

```text
Array
│
├── Traversal
├── Simulation
├── Sorting
└── Prefix Sum

HashMap
│
├── Counting
├── Lookup
└── Prefix Sum + HashMap

Two Pointers

Sliding Window

Binary Search

Heap

Stack

Interval
```

所以：

```text
Prefix Sum
```

值得单独作为一个专题。

------

# **为什么 Prefix Sum 是独立题型**

核心思想：

定义：

```python
prefix[i]
=
nums[0] + nums[1] + ... + nums[i]
```

这样：

```python
sum(i~j)
=
prefix[j] - prefix[i-1]
```

把：

```text
区间和
```

从：

```text
O(n)
```

变成：

```text
O(1)
```

------

# **第一类：纯 Prefix Sum**

## **LC303**

Range Sum Query

神级入门题。

------

例如：

```python
nums = [1,2,3,4]

prefix = [1,3,6,10]
```

求：

```python
[1,3]
```

区间和：

```python
10 - 1
=
9
```

------

# **第二类：Prefix Sum + HashMap**

这是面试最爱考的。

## **LC560**

Subarray Sum Equals K

经典中的经典。

------

例如：

```python
nums = [1,1,1]
k = 2
```

------

如果暴力：

```text
O(n²)
```

------

Prefix Sum + HashMap：

```python
prefix = 0

map = {0:1}
```

一路统计。

------

复杂度：

```text
O(n)
```

------

# **第三类：二维 Prefix Sum**

## **LC304**

Range Sum Query 2D

------

矩阵：

```python
1 2 3
4 5 6
7 8 9
```

------

提前计算：

```python
prefix[row][col]
```

------

查询：

```python
矩形区域和
```

变：

```text
O(1)
```

------

# **第四类：Prefix Sum + Frequency**

例如：

## **LC525**

Contiguous Array

------

## **LC974**

Subarray Sums Divisible by K

------

这些题都属于：

```text
Prefix Sum + HashMap
```

------

# **你现阶段应该学到什么程度？**

我建议：

### **必须掌握**

#### **LC303**

纯 Prefix Sum

------

#### **LC560**

Prefix Sum + HashMap

------

这两题做完，

基本就理解：

```text
Prefix Sum
```

整个套路。

------

# **面试里的识别信号**

看到题目出现：

```text
Subarray
```

或者：

```text
Continuous
```

或者：

```text
Range Sum
```

就要想：

```text
Prefix Sum?
```

------

# **和 Sliding Window 区别**

很多同学会混。

------

### **Sliding Window**

适合：

```text
全正数
```

例如：

```python
[1,2,3,4]
```

------

LC209

```text
Minimum Size Subarray Sum
```

------

### **Prefix Sum + HashMap**

适合：

```text
有正有负
```

例如：

```python
[1,-1,2,-2]
```

------

LC560

```text
Subarray Sum Equals K
```

------

# **我给你的路线**

等你 Mock Interview 结束后：

```text
Heap
↓
Stack
↓
Prefix Sum
↓
Linked List
↓
Tree
```

其实比直接冲 Tree 更合理。

因为 Prefix Sum 的学习成本很低：

```text
1~2天
```

但是面试收益很高。

------

对于你现在的 LeetCode Pattern 体系，我会把 Prefix Sum 放在：

```text
Array
HashMap
Two Pointers
Sliding Window
Binary Search
Sort
Quick Select
Heap
Interval
Prefix Sum
Stack
Linked List
Tree
```

里面作为一个**独立专题**，而不是归类到 Array 或 HashMap。因为它有自己非常固定的思维模式和模板。