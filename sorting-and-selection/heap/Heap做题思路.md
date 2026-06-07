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