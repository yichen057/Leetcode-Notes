你这个感受很正常。`dict / set / Counter` 这类题的难点不是语法，而是：**看到题目时能不能识别“我需要快速查找/计数/去重/建立映射关系”。**

你可以按下面这套方式巩固。

------

# **1. 先把三者的用途分清楚**

## **`set`****：只关心“有没有见过”**

适合：

```text
去重
判断是否出现过
判断重复元素
快速 membership check
```

常见信号：

```text
contains duplicate
seen before
unique
intersection
visited
```

例子：

```python
def has_duplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False
```

这里 `seen` 只存 key，没有 value。

```text
seen = {1, 2, 3}
```

意思是：

```text
这些数字我见过
```

------

## **`dict`****：需要建立 key → value 的关系**

适合：

```text
一个东西对应另一个东西
数字 → 下标
字符 → 出现次数
前缀和 → 出现次数
节点 → 克隆节点
旧值 → 新值
```

常见信号：

```text
find complement
mapping
index
frequency
prefix sum
cache
lookup
```

例子：Two Sum

```python
def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        need = target - num

        if need in seen:
            return [seen[need], i]

        seen[num] = i
```

这里：

```text
key   = 数字
value = 这个数字的下标
```

所以：

```python
seen[num] = i
```

意思是：

```text
我见过 num，它的位置是 i
```

------

## **`Counter`****：专门用来计数**

适合：

```text
频率统计
字符出现次数
anagram
top k frequent
majority element
```

例子：

```python
from collections import Counter

def is_anagram(s, t):
    return Counter(s) == Counter(t)
```

`Counter("aabbc")` 得到：

```python
Counter({'a': 2, 'b': 2, 'c': 1})
```

意思是：

```text
a 出现 2 次
b 出现 2 次
c 出现 1 次
```

------

# **2. 看到题目时，用这张判断表**

| **题目关键词**               | **优先想到**        |
| ---------------------------- | ------------------- |
| 是否出现过 / 是否重复        | `set`               |
| 去重                         | `set`               |
| 找两个数凑 target            | `dict`              |
| 需要从一个值快速找到另一个值 | `dict`              |
| 出现次数 / frequency         | `Counter` 或 `dict` |
| anagram                      | `Counter`           |
| 子数组和等于 k               | prefix sum + `dict` |
| visited / 已访问             | `set`               |
| 图/树避免重复访问            | `set`               |
| 缓存计算结果                 | `dict`              |

你可以先记一句最核心的：

```text
只问有没有 → set
需要对应关系 → dict
需要统计次数 → Counter
```

------

# **3. 用 5 个经典模板巩固**

## **模板 1：****`set`** **判断重复**

```python
def has_duplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False
```

练习题：

```text
LC 217 Contains Duplicate
LC 219 Contains Duplicate II
LC 349 Intersection of Two Arrays
```

------

## **模板 2：****`dict`** **存 value → index**

```python
def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        need = target - num

        if need in seen:
            return [seen[need], i]

        seen[num] = i
```

练习题：

```text
LC 1 Two Sum
```

重点不是背代码，而是理解：

```text
我现在看到 num。
我需要找 target - num。
如果之前见过 need，答案就找到了。
```

------

## **模板 3：****`dict`** **/** **`Counter`** **计数**

不用 Counter 的写法：

```python
def count_chars(s):
    count = {}

    for ch in s:
        count[ch] = count.get(ch, 0) + 1

    return count
```

用 Counter：

```python
from collections import Counter

count = Counter(s)
```

练习题：

```text
LC 242 Valid Anagram
LC 383 Ransom Note
LC 387 First Unique Character in a String
LC 169 Majority Element
```

------

## **模板 4：****`dict`** **统计 prefix_sum 出现次数**

```python
def subarray_sum(nums, k):
    count = 0
    prefix_sum = 0
    seen = {0: 1}

    for num in nums:
        prefix_sum += num
        need = prefix_sum - k

        if need in seen:
            count += seen[need]

        seen[prefix_sum] = seen.get(prefix_sum, 0) + 1

    return count
```

练习题：

```text
LC 560 Subarray Sum Equals K
```

这个模板比较难，但非常重要。



你可以记：

```text
seen 不是存数字，而是存：
某个 prefix_sum 出现过几次
```

------

## **模板 5：****`set`** **做 visited**

```python
def dfs(node, visited):
    if node in visited:
        return

    visited.add(node)

    for nei in graph[node]:
        dfs(nei, visited)
```

常见于：

```text
图遍历
检测环
避免重复访问
```

练习题后面再做，不急。

------

# **4. 你现在最该刷的一组题**

建议你按这个顺序刷，专门练 `set / dict / Counter`。

## **第一组：set 入门**

```text
LC 217 Contains Duplicate
LC 349 Intersection of Two Arrays
LC 202 Happy Number
```

目标：熟悉 `seen.add()` 和 `x in seen`。

------

## **第二组：dict 入门**

```text
LC 1 Two Sum
LC 205 Isomorphic Strings
LC 290 Word Pattern
```

目标：熟悉 `key -> value` 映射。

------

## **第三组：Counter / frequency**

```text
LC 242 Valid Anagram
LC 383 Ransom Note
LC 387 First Unique Character in a String
LC 451 Sort Characters By Frequency
```

目标：熟悉“出现次数”。

------

## **第四组：进阶 hash map**

```text
LC 560 Subarray Sum Equals K
LC 49 Group Anagrams
LC 347 Top K Frequent Elements
```

目标：知道 Hash Map 不只是查找，还能做分组、统计和前缀和。

------

# **5. 做题时固定问自己 4 个问题**

每次看到题目，先问：

```text
1. 我是否需要快速判断一个元素之前是否出现过？
   是 → set

2. 我是否需要从一个东西找到另一个东西？
   是 → dict

3. 我是否需要统计出现次数？
   是 → Counter / dict

4. 我是否在处理连续子数组求和？
   是 → prefix_sum + dict
```

例如：

## **Two Sum**

```text
我需要快速知道 target - num 是否出现过。
还需要知道它的 index。
所以用 dict：num -> index
```

## **Contains Duplicate**

```text
我只需要知道是否出现过。
不需要 index，不需要次数。
所以用 set。
```

## **Valid Anagram**

```text
我要比较字符出现次数。
所以用 Counter。
```

## **Subarray Sum Equals K**

```text
我要知道之前有没有某个 prefix_sum。
而且可能出现多次。
所以用 dict：prefix_sum -> count
```

------

# **6. 你可以做一个小练习表**

每做一道题，都写三行：

```text
这题为什么用 hash map / set？
key 是什么？
value 是什么？
```

比如 LC1：

```text
为什么用 hash map？
因为要快速查找 complement。

key 是什么？
num。

value 是什么？
index。
```

LC560：

```text
为什么用 hash map？
因为要快速查找之前出现过多少次 prefix_sum - k。

key 是什么？
prefix_sum。

value 是什么？
这个 prefix_sum 出现次数。
```

LC217：

```text
为什么用 set？
因为只需要知道数字之前是否出现过。

set 里存什么？
已经见过的数字。
```

这个练习非常有效，比单纯刷题更容易形成识别能力。

------

# **7. 你现在可以这样安排一周练习**

每天 30-45 分钟就够。

```text
Day 1: LC217, LC349
Day 2: LC1, LC242
Day 3: LC383, LC387
Day 4: LC205, LC290
Day 5: LC49
Day 6: LC560
Day 7: 复盘，把每题的 key/value/why 写出来
```

复盘比刷新题更重要。



你现在不是不会写代码，而是还没有形成：

```text
看到题目 → 识别模式 → 选择 set/dict/Counter
```

这个反射。

------

# **8. 最核心记忆口诀**

```text
Set：有没有。
Dict：谁对应谁。
Counter：有几个。
Prefix Sum + Dict：连续子数组和。
```

再具体一点：

```text
看到“是否重复” → set
看到“两数和” → dict 存 num -> index
看到“频率/次数” → Counter
看到“anagram” → Counter
看到“连续子数组和等于 k” → prefix_sum -> count
```

你后面刷题时，每题先不要急着写代码，先写：

```text
我准备用 set/dict/Counter。
它里面存的是：____。
为什么：____。
```

这个习惯练 10 道题，你会明显更熟。





Quick Sort（快速排序）是一种**分治算法**。

核心思想很简单：

选一个数作为 pivot，然后把数组分成两边：
 左边都比 pivot 小，右边都比 pivot 大。
 然后再分别对左边和右边继续做同样的事。

------

## **1. 举个例子**

数组：

```text
[5, 2, 9, 1, 7, 3]
```

假设选第一个数 `5` 作为 pivot。

把其他数字分成两组：

```text
小于 5 的: [2, 1, 3]
pivot: 5
大于 5 的: [9, 7]
```

所以变成：

```text
[2, 1, 3] + [5] + [9, 7]
```

然后继续排序左边 `[2, 1, 3]` 和右边 `[9, 7]`。

最后结果：

```text
[1, 2, 3, 5, 7, 9]
```

------

## **2. Quick Sort 的递归逻辑**

可以理解为：

```text
quickSort(array):
    选一个 pivot
    把数组分成 left 和 right
    quickSort(left)
    quickSort(right)
    合并 left + pivot + right
```

------

## **3. Python 简单版**

这个版本最容易理解，但不是原地排序：

```python
def quick_sort(nums):
    if len(nums) <= 1:
        return nums

    pivot = nums[0]

    left = []
    right = []

    for num in nums[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)

    return quick_sort(left) + [pivot] + quick_sort(right)
```

调用：

```python
nums = [5, 2, 9, 1, 7, 3]
print(quick_sort(nums))
```

输出：

```text
[1, 2, 3, 5, 7, 9]
```

------

## **4. 为什么它叫“快排”？**

因为平均情况下，它每次都能把数组比较均匀地分成两半。

时间复杂度：

```text
平均：O(n log n)
最坏：O(n^2)
```

最坏情况通常发生在 pivot 选得很差，比如数组已经有序，但你每次都选第一个数：

```text
[1, 2, 3, 4, 5]
```

选 `1` 当 pivot，左边为空，右边是 `[2, 3, 4, 5]`，这样就退化了。

------

## **5. 一句话记忆**

Quick Sort 就是：

找一个基准数 pivot，把小的放左边，大的放右边，然后递归排序左右两边。

------

你可以先把它和 Merge Sort 对比记：

```text
Merge Sort：先拆，再合并时排序
Quick Sort：先分区排序，再递归处理
```

我们从 **LeetCode 912. Sort an Array** 开始，因为它就是完整 Quick Sort。然后再做 **LeetCode 215. Kth Largest Element**，它是 Quick Sort 的变形：**Quick Select**。

------

# **Part 1：LeetCode 912. Sort an Array**

题目大意：

```text
给你一个数组 nums，把它升序排序后返回。
```

例如：

```python
nums = [5, 2, 3, 1]
```

返回：

```python
[1, 2, 3, 5]
```

------

## **1. Quick Sort 的核心思想**

Quick Sort 做三件事：

```text
1. 选一个 pivot，也就是基准值
2. 把小于 pivot 的数放左边，大于 pivot 的数放右边
3. 分别递归排序左边和右边
```

比如：

```text
[5, 2, 9, 1, 7, 3]
```

选 `5` 作为 pivot。

分区之后大概变成：

```text
[3, 2, 1]  5  [7, 9]
```

然后继续排序左边 `[3, 2, 1]` 和右边 `[7, 9]`。

------

## **2. 新手最容易理解的版本：非原地 Quick Sort**

这个版本会新建两个数组 `left` 和 `right`，非常适合理解。

```python
class Solution:
    def sortArray(self, nums):
        return self.quick_sort(nums)

    def quick_sort(self, nums):
        if len(nums) <= 1:
            return nums

        pivot = nums[0]

        left = []
        right = []

        for num in nums[1:]:
            if num < pivot:
                left.append(num)
            else:
                right.append(num)

        return self.quick_sort(left) + [pivot] + self.quick_sort(right)
```

------

## **3. 这段代码怎么运行？**

用这个数组：

```python
[5, 2, 9, 1, 7, 3]
```

第一次：

```text
pivot = 5

left = [2, 1, 3]
right = [9, 7]
```

于是变成：

```text
quick_sort([2, 1, 3]) + [5] + quick_sort([9, 7])
```

继续处理左边：

```text
[2, 1, 3]
pivot = 2

left = [1]
right = [3]
```

所以：

```text
quick_sort([1]) + [2] + quick_sort([3])
```

结果是：

```text
[1, 2, 3]
```

继续处理右边：

```text
[9, 7]
pivot = 9

left = [7]
right = []
```

结果是：

```text
[7, 9]
```

最后整体就是：

```text
[1, 2, 3] + [5] + [7, 9]
```

也就是：

```text
[1, 2, 3, 5, 7, 9]
```

------

## **4. 但是 LeetCode 912 不推荐这个版本**

因为这个版本虽然容易懂，但是它会创建很多新数组：

```python
left = []
right = []
```

空间开销比较大。

所以我们真正写 LeetCode 912，通常用 **原地 Quick Sort**。

------

# **Part 2：912 原地 Quick Sort 模板**

这个版本更适合面试和 LeetCode。

```python
class Solution:
    def sortArray(self, nums):
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums

    def quick_sort(self, nums, left, right):
        if left >= right:
            return

        pivot = nums[(left + right) // 2]

        i = left
        j = right

        while i <= j:
            while nums[i] < pivot:
                i += 1

            while nums[j] > pivot:
                j -= 1

            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        self.quick_sort(nums, left, j)
        self.quick_sort(nums, i, right)
```

------

## **5. 先解释函数参数**

```python
def quick_sort(self, nums, left, right):
```

意思是：

```text
只排序 nums[left] 到 nums[right] 这一段
```

比如：

```python
nums = [5, 2, 9, 1, 7, 3]
```

一开始是：

```python
left = 0
right = 5
```

表示排序整个数组。

之后递归时，可能变成：

```python
quick_sort(nums, 0, 2)
quick_sort(nums, 3, 5)
```

表示分别排序左半边和右半边。

------

## **6. base case：什么时候停止递归？**

```python
if left >= right:
    return
```

意思是：

```text
如果这一段只有 0 个或 1 个元素，就不用排序了。
```

比如：

```text
[3]
```

一个元素本身就是有序的。

------

## **7. pivot 是什么？**

```python
pivot = nums[(left + right) // 2]
```

我们选中间位置的数作为基准值。

比如：

```python
nums = [5, 2, 9, 1, 7, 3]
left = 0
right = 5
mid = (0 + 5) // 2 = 2
pivot = nums[2] = 9
```

所以这一次 `pivot = 9`。

注意：这里的 `pivot` 是一个**值**，不是固定的下标。

------

## **8. i 和 j 是什么？**

```python
i = left
j = right
```

你可以这样理解：

```text
i 从左往右走
j 从右往左走
```

它们的任务是：

```text
i 找左边“不应该待在左边”的数
j 找右边“不应该待在右边”的数
```

------

## **9. 这两段 while 是什么意思？**

```python
while nums[i] < pivot:
    i += 1
```

意思是：

```text
如果 nums[i] 比 pivot 小，说明它在左边是合理的。
所以 i 继续往右走。
```

------

```python
while nums[j] > pivot:
    j -= 1
```

意思是：

```text
如果 nums[j] 比 pivot 大，说明它在右边是合理的。
所以 j 继续往左走。
```

------

## **10. 什么时候交换？**

```python
if i <= j:
    nums[i], nums[j] = nums[j], nums[i]
    i += 1
    j -= 1
```

当两个指针都停下来时，说明：

```text
nums[i] 不小于 pivot，可能应该去右边
nums[j] 不大于 pivot，可能应该去左边
```

所以我们交换它们。

交换后：

```text
i 往右走一步
j 往左走一步
```

------

## **11. 用一个例子完整走一遍**

数组：

```text
[5, 2, 9, 1, 7, 3]
```

初始：

```text
left = 0
right = 5
pivot = nums[2] = 9

i = 0
j = 5
```

当前数组：

```text
[5, 2, 9, 1, 7, 3]
 i              j
```

### **第一次移动 i**

```python
while nums[i] < pivot:
    i += 1
```

因为：

```text
nums[0] = 5 < 9，所以 i 往右
nums[1] = 2 < 9，所以 i 往右
nums[2] = 9，不小于 9，停
```

现在：

```text
[5, 2, 9, 1, 7, 3]
       i        j
```

### **第一次移动 j**

```python
while nums[j] > pivot:
    j -= 1
```

因为：

```text
nums[5] = 3 > 9 ? 不是
```

所以 j 不动。

现在：

```text
i = 2
j = 5
```

因为 `i <= j`，交换：

```text
swap nums[2] 和 nums[5]
```

数组变成：

```text
[5, 2, 3, 1, 7, 9]
```

然后：

```text
i = 3
j = 4
```

现在：

```text
[5, 2, 3, 1, 7, 9]
          i  j
```

继续。

### **第二次移动 i**

```text
nums[3] = 1 < 9，所以 i 往右
nums[4] = 7 < 9，所以 i 往右
nums[5] = 9，不小于 9，停
```

现在：

```text
i = 5
j = 4
```

此时：

```text
i > j
```

循环结束。

此时数组：

```text
[5, 2, 3, 1, 7, 9]
```

虽然还没完全排序，但已经完成了一次 partition：

```text
左边基本都 <= 9
右边基本都 >= 9
```

然后递归：

```python
self.quick_sort(nums, left, j)
self.quick_sort(nums, i, right)
```

也就是：

```python
quick_sort(nums, 0, 4)
quick_sort(nums, 5, 5)
```

右边 `[9]` 不用排，继续排左边：

```text
[5, 2, 3, 1, 7]
```

最终会得到完整有序数组。

------

# **Part 3：912 的完整推荐代码**

```python
class Solution:
    def sortArray(self, nums):
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums

    def quick_sort(self, nums, left, right):
        if left >= right:
            return

        pivot = nums[(left + right) // 2]

        i = left
        j = right

        while i <= j:
            while nums[i] < pivot:
                i += 1

            while nums[j] > pivot:
                j -= 1

            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        self.quick_sort(nums, left, j)
        self.quick_sort(nums, i, right)
```

------

# **Part 4：LeetCode 215. Kth Largest Element in an Array**

题目大意：

```text
给你一个数组 nums 和整数 k，返回第 k 大的元素。
```

例如：

```python
nums = [3, 2, 1, 5, 6, 4]
k = 2
```

排序后是：

```python
[1, 2, 3, 4, 5, 6]
```

第 1 大是 `6`。
 第 2 大是 `5`。

所以答案是：

```python
5
```

------

## **1. 最简单思路：先排序**

```python
class Solution:
    def findKthLargest(self, nums, k):
        nums.sort()
        return nums[len(nums) - k]
```

为什么是：

```python
len(nums) - k
```

因为升序排序后：

```text
nums = [1, 2, 3, 4, 5, 6]
index:  0  1  2  3  4  5
```

第 1 大是最后一个：

```text
index = len(nums) - 1
```

第 2 大：

```text
index = len(nums) - 2
```

第 k 大：

```text
index = len(nums) - k
```

所以：

```python
target = len(nums) - k
```

------

## **2. 但是 215 更经典的解法是 Quick Select**

Quick Select 和 Quick Sort 很像。

区别是：

```text
Quick Sort：左右两边都要继续排序
Quick Select：只去答案所在的一边
```

因为我们只是找第 k 大，不需要把整个数组排好。

------

## **3. 先把第 k 大转换成第 target 小**

例如：

```python
nums = [3, 2, 1, 5, 6, 4]
k = 2
```

如果升序排序：

```text
[1, 2, 3, 4, 5, 6]
```

第 2 大是 `5`。

它的下标是：

```python
target = len(nums) - k
target = 6 - 2 = 4
```

也就是排序后下标为 `4` 的元素。

```text
[1, 2, 3, 4, 5, 6]
             target
```

所以问题变成：

```text
找到排序后应该位于 index = 4 的元素。
```

------

# **Part 5：215 Quick Select 模板**

```python
class Solution:
    def findKthLargest(self, nums, k):
        target = len(nums) - k
        return self.quick_select(nums, 0, len(nums) - 1, target)

    def quick_select(self, nums, left, right, target):
        if left == right:
            return nums[left]

        pivot = nums[(left + right) // 2]

        i = left
        j = right

        while i <= j:
            while nums[i] < pivot:
                i += 1

            while nums[j] > pivot:
                j -= 1

            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        if target <= j:
            return self.quick_select(nums, left, j, target)
        elif target >= i:
            return self.quick_select(nums, i, right, target)
        else:
            return nums[target]
```

------

## **6. 这和 Quick Sort 哪里不一样？**

Quick Sort 最后是：

```python
self.quick_sort(nums, left, j)
self.quick_sort(nums, i, right)
```

意思是：

```text
左右都要排序
```

Quick Select 是：

```python
if target <= j:
    return self.quick_select(nums, left, j, target)
elif target >= i:
    return self.quick_select(nums, i, right, target)
else:
    return nums[target]
```

意思是：

```text
target 在左边，就只去左边
target 在右边，就只去右边
target 刚好在中间区域，就直接返回
```

------

## **7. 为什么可以只去一边？**

因为 partition 之后，数组会被大概分成三段：

```text
[left ... j]       [j+1 ... i-1]       [i ... right]
小于等于 pivot        pivot 附近区域        大于等于 pivot
```

所以如果目标下标 `target` 在左边：

```text
target <= j
```

那答案一定在左边，不需要管右边。

如果目标下标在右边：

```text
target >= i
```

那答案一定在右边，不需要管左边。

如果：

```text
j < target < i
```

说明 target 落在中间区域，当前 `nums[target]` 就是答案。

------

# **Part 6：用 215 的例子走一遍**

```python
nums = [3, 2, 1, 5, 6, 4]
k = 2
```

目标：

```python
target = len(nums) - k = 6 - 2 = 4
```

我们要找排序后 index 4 的元素。

排序后的结果应该是：

```text
[1, 2, 3, 4, 5, 6]
             index 4
```

答案是 `5`。

------

第一次 Quick Select：

```text
nums = [3, 2, 1, 5, 6, 4]
left = 0
right = 5
pivot = nums[2] = 1
```

partition 后，`1` 会被移动到偏左的位置。数组可能变成：

```text
[1, 2, 3, 5, 6, 4]
```

这时候 `target = 4` 明显在右半边，所以只递归右边。

继续处理右边：

```text
[2, 3, 5, 6, 4]
```

下一次选 pivot，继续 partition。

慢慢缩小范围，直到找到下标 `4` 应该对应的值，也就是 `5`。

------

# **Part 7：你现在应该先记住这两个模板**

## **912：Quick Sort**

```python
class Solution:
    def sortArray(self, nums):
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums

    def quick_sort(self, nums, left, right):
        if left >= right:
            return

        pivot = nums[(left + right) // 2]
        i = left
        j = right

        while i <= j:
            while nums[i] < pivot:
                i += 1

            while nums[j] > pivot:
                j -= 1

            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        self.quick_sort(nums, left, j)
        self.quick_sort(nums, i, right)
```

------

## **215：Quick Select**

```python
class Solution:
    def findKthLargest(self, nums, k):
        target = len(nums) - k
        return self.quick_select(nums, 0, len(nums) - 1, target)

    def quick_select(self, nums, left, right, target):
        if left == right:
            return nums[left]

        pivot = nums[(left + right) // 2]
        i = left
        j = right

        while i <= j:
            while nums[i] < pivot:
                i += 1

            while nums[j] > pivot:
                j -= 1

            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        if target <= j:
            return self.quick_select(nums, left, j, target)
        elif target >= i:
            return self.quick_select(nums, i, right, target)
        else:
            return nums[target]
```

------

# **Part 8：新手最容易混淆的点**

## **混淆点 1：pivot 不一定最终停在正确位置**

在这个双指针模板里：

```python
pivot = nums[(left + right) // 2]
```

pivot 是一个值，不是说这个位置最后一定就是 pivot。

所以不要理解成：

```text
pivot 最后一定在中间
```

更准确地说：

```text
partition 之后，左边大体 <= pivot，右边大体 >= pivot
```

------

## **混淆点 2：为什么交换后 i 和 j 都要移动？**

```python
nums[i], nums[j] = nums[j], nums[i]
i += 1
j -= 1
```

因为交换后，这两个位置已经处理过了。

如果不移动，可能会卡住，尤其是遇到重复元素时。

例如：

```text
[2, 2, 2, 2]
```

如果交换后不移动，程序可能一直停在同一对位置。

------

## **混淆点 3：为什么递归是 left 到 j，i 到 right？**

partition 结束时：

```text
left ... j     i ... right
```

`j` 是左边最后一个还没完全排序的位置。
 `i` 是右边第一个还没完全排序的位置。

所以：

```python
quick_sort(nums, left, j)
quick_sort(nums, i, right)
```

------

# **Part 9：你可以这样练习**

先别急着刷很多题。你可以按这个顺序练：

```text
第一步：手写 912 的 quick_sort 模板 3 遍
第二步：用 [5, 2, 9, 1, 7, 3] 手动走一遍 i/j 移动
第三步：把 quick_sort 改成 quick_select
第四步：做 215
```

最核心的一句话：

```text
912 是把整个数组排好，所以左右都递归。
215 只是找一个位置的数，所以只递归 target 所在的一边。
```