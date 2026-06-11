是的，**Prefix Sum（前缀和）其实既属于 Array，也经常和 HashMap 结合使用**。

很多人刷题时容易混淆，因为 Prefix Sum 本身只是一个工具，而不是最终解法。

我建议你把 Prefix Sum 单独当成一个专题学，因为面试里出现频率非常高。

------

# **Prefix Sum知识体系**

## **第一类：纯 Prefix Sum（Array）**

特点：

- 只求某个区间和
- 不需要 HashMap
- 一般是预处理数组

公式：

```
prefix[i] = nums[0] + nums[1] + ... + nums[i-1]

区间和:
sum(l,r) = prefix[r+1] - prefix[l]
```

例如：

### **LC 303 Range Sum Query**

```python
nums = [1,2,3,4]

prefix = [0,1,3,6,10]

sum(1,3)
= prefix[4]-prefix[1]
= 10-1
= 9
```

面试频率：

⭐⭐

------

## **第二类：Prefix Sum + HashMap**

这是最重要的一类。

特点：

- 问连续子数组
- 和 target 有关
- 求数量
- 求是否存在

关键词：

```
subarray
continuous
sum equals k
count
```

看到这些词就要想到：

Prefix Sum + HashMap

------

# **LC 560 Subarray Sum Equals K**

经典中的经典。

求：

```
连续子数组和 == k
有多少个
```

------

暴力：

```python
O(n²)
```

------

前缀和：

假设：

```python
currSum = 当前前缀和
```

如果：

```python
currSum - prevSum = k
```

那么：

```python
prevSum = currSum - k
```

只要之前出现过：

```python
currSum-k
```

就找到答案。



所以：

```python
hashmap[prefixSum]
```

记录出现次数。

------

模板：

```python
count = {0:1}

currSum = 0
ans = 0

for num in nums:
    currSum += num

    ans += count.get(currSum-k,0)

    count[currSum] = count.get(currSum,0)+1
```

------

# **第三类：Prefix Sum + HashMap 求最长**

关键词：

```
longest
maximum length
```

------

### **LC 325 Maximum Size Subarray Sum Equals K**

求：

```
sum = k

最长长度
```

------

区别：

560存频率

```python
count[prefix]
```

325存第一次出现的位置

```python
firstIndex[prefix]
```

因为：

```
距离越远
长度越长
```

------

模板：

```python
if prefix not in firstIndex:
    firstIndex[prefix] = i
```

只记录第一次出现。

------

# **第四类：Prefix Sum + Mod**

这个面试也很爱考。

关键词：

```
multiple of k
divisible by k
```

------

### **LC 523 Continuous Subarray Sum**

求：

```
是否存在子数组

sum % k == 0
```

------

核心：

如果

```python
prefix1 % k == prefix2 % k
```

那么

```python
(prefix2-prefix1)%k == 0
```

中间子数组一定能被k整除。

------

模板：

```python
modMap = {0:-1}

prefix = 0

for i,num in enumerate(nums):

    prefix += num

    mod = prefix % k

    if mod in modMap:
        ...
    else:
        modMap[mod] = i
```

------

# **第五类：Prefix Sum + Frequency**

关键词：

```
binary array
0和1
equal number
```

------

### **LC 525 Contiguous Array**

求：

```
0和1数量相同

最长长度
```

------

技巧：

把

```python
0 -> -1
1 -> 1
```

转换。



那么：

```
区间和 = 0
```

就代表：

```
0和1数量一样
```

变成 Prefix Sum 问题。

------

# **第六类：二维 Prefix Sum**

关键词：

```
matrix
submatrix
rectangle
```

------

### **LC 304 Range Sum Query 2D**

公式：

```text
    A
+-------+
|       |
|    D  |
|       |
+-------+
```

二维前缀和：

```python
sum =
prefix[r2][c2]
- prefix[r1-1][c2]
- prefix[r2][c1-1]
+ prefix[r1-1][c1-1]
```

------

# **面试最常考的 Prefix Sum 题单**

## **入门**

- LC 303 Range Sum Query - Immutable
- LC 1480 Running Sum of 1d Array

------

## **必会**

- LC 560 Subarray Sum Equals K
- LC 525 Contiguous Array
- LC 523 Continuous Subarray Sum

------

## **进阶**

- LC 325 Maximum Size Subarray Sum Equals K
- LC 930 Binary Subarrays With Sum
- LC 974 Subarray Sums Divisible by K

------

# **面试时如何识别 Prefix Sum**

看到下面任意一个关键词，就应该想到 Prefix Sum：

| **关键词**              | **想到什么**             |
| ----------------------- | ------------------------ |
| continuous subarray     | Prefix Sum               |
| sum = k                 | Prefix Sum + HashMap     |
| count subarray          | Prefix Sum + Frequency   |
| longest subarray        | Prefix Sum + First Index |
| divisible by k          | Prefix Sum + Mod         |
| equal number of 0 and 1 | Prefix Sum + 转换        |
| range sum query         | Prefix Sum Array         |
| submatrix sum           | 2D Prefix Sum            |

按照你现在的刷题进度（Array → HashMap → Two Pointers → Sliding Window → Heap），我建议：



**先刷 560 → 525 → 523 这三题。**



这三题基本覆盖了面试里 80% 的 Prefix Sum 思维，学完之后再去做 325、930、974 会轻松很多。



先给你一个结论：

**你的理解速度其实是正常的。**

LC303、304、560、525、523、325 这些题已经属于面试里比较系统的一块知识了，不是看一遍就能形成模板的。

我看你最近的学习过程，其实已经从：

```text
Array
HashMap
Two Pointers
Sliding Window
```

进入到了：

```text
Prefix Sum
```

这是一个明显更抽象的层次。

------

# **矩阵算什么题型？**

严格来说：

```text
Matrix
```

不是独立算法。

属于：

```text
Array
```

的二维版本。

例如：

```python
nums = [1,2,3,4]
```

是一维 Array。

------

```python
matrix = [
 [1,2],
 [3,4]
]
```

是二维 Array。

------

所以 LeetCode 通常分类：

```text
Array
String
Hash Table
Two Pointers
Sliding Window
Stack
Queue
Heap
Binary Search
Linked List
Tree
Graph
DP
```

矩阵通常被归到：

```text
Array
```

下面。

------

# **为什么矩阵让人难受？**

因为你同时要处理：

```text
row
col
```

两套坐标。

------

一维：

```python
nums[i]
```

只需要想：

```text
i
```

------

二维：

```python
matrix[r][c]
```

需要想：

```text
r
c
```

------

Prefix Sum 又引入：

```python
sumMat[r][c]
```

于是变成：

```text
matrix坐标

vs

prefix坐标
```

新手特别容易晕。

------

# **Prefix Sum 算难吗？**

如果面试题难度分：

```text
Array基础       ⭐

HashMap基础     ⭐⭐

Sliding Window ⭐⭐

Prefix Sum     ⭐⭐⭐

Heap           ⭐⭐⭐

Binary Search  ⭐⭐⭐

Tree           ⭐⭐⭐⭐

Graph          ⭐⭐⭐⭐

DP             ⭐⭐⭐⭐⭐
```

我会把 Prefix Sum 放在：

```text
⭐⭐⭐
```

属于：

```text
中等偏抽象
```

------

因为它有一个特点：

不是在原数组上操作。

而是在构造一个：

```text
辅助信息
```

------

例如：

LC303

```python
nums
```

变成：

```python
prefix
```

------

LC304

```python
matrix
```

变成：

```python
sumMat
```

------

LC560

```python
nums
```

变成：

```python
prefixSum + HashMap
```

------

这和：

```python
left += 1
right += 1
```

那种直观操作完全不一样。

------

# **Prefix Sum 其实只有两个模板**

这是最重要的。

你现在学了好多题。

实际上只有：

------

## **模板1**

### **Range Query**

代表：

```text
LC303
LC304
```

------

核心思想：

```text
提前预处理

查询O(1)
```

------

一维：

```python
prefix[right+1] - prefix[left]
```

------

二维：

```python
BR - Above - Left + TopLeft
```

------

------

## **模板2**

### **Prefix Sum + HashMap**

代表：

```text
560
525
523
325
974
```

------

统一套路：

```python
prefixSum += num

need = ...

if need in hashmap:
    ...

更新hashmap
```

------

只是：

### **560**

```python
need = prefixSum - k

hashmap存frequency
```

------

### **325**

```python
need = prefixSum - k

hashmap存firstIndex
```

------

### **525**

```python
k = 0

need = prefixSum
```

------

### **523**

```python
need = prefixSum % k

hashmap存firstIndex
```

------

### **974**

```python
need = prefixSum % k

hashmap存frequency
```

------

# **你现在最大的误区**

你一直在试图记：

```text
560怎么做

525怎么做

523怎么做

325怎么做
```

------

实际上应该记：

### **第一类**

```text
Range Query
```

代表：

```text
303
304
```

------

### **第二类**

```text
Prefix Sum + HashMap
```

代表：

```text
560
325
525
523
974
```

------

你会突然发现：

```text
560
325
525
```

几乎是同一个题。

区别只是：

```python
HashMap存什么
```

和：

```python
need怎么定义
```

------

# **以你目前的水平**

我建议：

不要继续学新的 Prefix Sum 题。

先把下面五道题吃透：

```text
LC303
LC560
LC325
LC525
LC523
```

尤其是：

```text
303 → 基础Prefix Sum

560 → count模板

325 → longest模板

525 → 325特例

523 → mod模板
```

如果这五题能不看答案自己写出来，

那么 Prefix Sum 这一章你基本就过关了。

而且从你最近的问题看，其实你已经理解了：

```text
查 need

存 curSum

count存frequency

longest存firstIndex
```

这些最核心的东西。

现在缺的不是新知识，而是通过几道经典题把这套模板固化下来。