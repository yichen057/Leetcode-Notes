# Mock Interview 全数据结构复习手册

> **适用**:5/7 Mock Interview 复习
> **范围**:Array、String、Hash、Two Pointer、Binary Search、Linked List、Stack、Queue、Binary Tree、Recursion、Graph
> **使用方法**:5/4-5/6 每天对应主题深读;5/6 晚通读;5/7 早上扫第十三、十四节

---

## 目录

### 已掌握章节(Mock 复习重点)

1. [Array(数组)](#一array数组)
2. [String(字符串)](#二string字符串)
3. [Hash Map / Hash Set / Counter](#三hash-map--hash-set--counter)
4. [`in` 操作复杂度大对比 ⭐](#四in-操作复杂度大对比-)
5. [Two Pointers(双指针)](#五two-pointers双指针)
6. [Binary Search(二分查找)](#六binary-search二分查找)
7. [Linked List(链表)](#七linked-list链表)
8. [Stack(栈)](#八stack栈)
9. [Queue(队列)](#九queue队列)
10. [Binary Tree(二叉树)](#十binary-tree二叉树)
11. [Recursion / Divide & Conquer](#十一recursion--divide--conquer递归--分治)
12. [Graph(图)](#十二graph图)
13. [Anagram 经典题专题](#十三anagram-经典题专题)

### 速查与复盘

14. [复杂度速查总表](#十四复杂度速查总表)
15. [Mock 当天的"5 必说"](#十五mock-当天的5-必说)
16. [必背的 6 个核心模板](#十六必背的-6-个核心模板)
17. [Mock Interview 实战复盘(2026-05-07)](#十七mock-interview-实战复盘2026-05-07)

### 进阶 Pattern(按面试重要性排序)

18. [Heap / Top K(优先队列)⭐⭐⭐](#ch18)
19. [Overlapping Intervals(区间问题)⭐⭐⭐](#ch19)
20. [Backtracking(回溯)⭐⭐](#ch20)
21. [Prefix Sum(前缀和)⭐⭐](#ch21)
22. [Matrix Traversal(矩阵遍历)⭐](#ch22)
23. [Dynamic Programming(动态规划)⭐ 小白入门版](#ch23)

### NeetCode Roadmap 补充章节

24. [Greedy(贪心算法)⭐⭐⭐](#ch24)
25. [Tries(字典树)⭐⭐](#ch25)
26. [Advanced Graphs(高级图算法)⭐⭐](#ch26)
27. [2-D DP(二维动态规划)⭐⭐](#ch27)
28. [Bit Manipulation(位运算)⭐](#ch28)
29. [Math(数学题)⭐](#ch29)

### 语法参考

30. [Python 语法速查(Mock 前 10 分钟回顾)](#ch30)

---

## 一、Array(数组)

### 1.1 基本概念

Python 的 `list` 是**动态数组**(可变长度),通过索引 O(1) 访问。

```python
arr = [1, 2, 3, 4, 5]
arr[0]      # 1,O(1) 访问
len(arr)    # 5,O(1)
```

### 1.2 复杂度速查

| 操作 | 复杂度 | 说明 |
|---|---|---|
| `arr[i]` 索引访问 | O(1) | 直接定位 |
| `arr.append(x)` | O(1) 均摊 | 末尾添加 |
| `arr.pop()` | O(1) | 末尾删除 |
| `arr.insert(i, x)` | **O(n)** | 中间/头部插入要移动元素 |
| `arr.pop(0)` | **O(n)** | 头部删除要移动元素 |
| `arr.remove(x)` | **O(n)** | 先线性查找再移动 |
| `arr.reverse()` | **O(n)** | 原地反转 |
| `x in arr` | **O(n)** | 线性扫描 |
| `len(arr)` | O(1) | 内置属性 |

### 1.3 增删改

```python
arr = [1, 2, 3]

# 添加
arr.append(4)            # [1, 2, 3, 4],末尾添加
arr.insert(1, 99)        # [1, 99, 2, 3, 4],在索引 1 处插入 99

# 删除
arr.pop()                # 删除并返回末尾元素
arr.pop(0)               # 删除并返回索引 0(慢,O(n))
arr.remove(99)           # 删除第一个值为 99 的元素(慢,O(n))
del arr[1]               # 删除索引 1 的元素

# 修改
arr[0] = 100             # 直接赋值
```

### 1.4 反转

```python
arr = [1, 2, 3]

# 方法 1:原地反转(改变原数组)
arr.reverse()                # arr 变成 [3, 2, 1]

# 方法 2:切片(返回新数组)
new_arr = arr[::-1]          # 不改变原数组

# 方法 3:reversed() 返回迭代器
list(reversed(arr))          # [3, 2, 1]
```

### 1.5 切片

切片**会创建新数组**(O(k))。

```python
arr = [1, 2, 3, 4, 5]
arr[2:5]      # [3, 4, 5],索引 2,3,4
arr[:3]       # [1, 2, 3],前 3 个
arr[-3:]      # [3, 4, 5],后 3 个
arr[::2]      # [1, 3, 5],每隔一个
arr[::-1]     # [5, 4, 3, 2, 1],逆序
```

### 1.6 `sorted()` 详解

#### 基础用法

```python
arr = [3, 1, 4, 1, 5, 9, 2, 6]

# 1) 默认升序
sorted(arr)                          # [1, 1, 2, 3, 4, 5, 6, 9]
arr.sort()                           # 原地排序,返回 None

# 2) 降序
sorted(arr, reverse=True)            # [9, 6, 5, 4, 3, 2, 1, 1]
sorted(arr, key=lambda x: -x)        # 等价写法,前提是元素是数字

# 3) 按规则排序
words = ["apple", "pi", "banana"]
sorted(words, key=len)               # ['pi', 'apple', 'banana']
```

#### `key=lambda x: -x` 详解

> 排序时**不直接看 `x` 本身,而是看 `-x`**。

```python
arr = [3, 1, 4]
sorted(arr, key=lambda x: -x)
# 内部计算:[-3, -1, -4]
# 升序排:[-4, -3, -1]
# 对应原值:[4, 3, 1]   ← 等于把 arr 从大到小排
```

**前提**:`arr` 内必须是数字(否则 `-x` 报错)。

#### `sorted()` 复杂度

| | 复杂度 | 说明 |
|---|---|---|
| **时间** | **O(n log n)** | Timsort 算法 |
| **空间** | **O(n)** | 创建新列表 |

**为什么是 O(n log n)?**

排序不是简单扫一遍,它要不断比较、调整元素顺序。
- 简单遍历是 O(n)(看一次)
- 排序需要多轮比较和移动,所以是 O(n log n)

例如 `sorted("dbca")`:
```
先比较 d 和 b
再比较 c 和 a
再不断调整位置
最后得到 ['a', 'b', 'c', 'd']
```

Python 的 `sorted()` 底层是 **Timsort**(merge sort + insertion sort 混合优化),平均/最坏都是 O(n log n)。在接近有序的数据上可能接近 O(n)。

Sorted(nums) 可操作任何可迭代对象, 未修改原Array, 返回值是new array

`arr.sort()` 原地排序会修改原array, , 仅限列表, 返回值是None, 空间复杂度depends on the impletation, 是 O(1)如果忽略排序栈。

---

## 二、String(字符串)

### 2.1 不可变性(immutable)

**Python string 不可变**!任何"修改"操作都创建新字符串。

```python
s = "abc"
s[0] = "x"               # ❌ TypeError

# 想修改字符,必须先转 list
s = "abc"
arr = list(s)            # ['a', 'b', 'c']
arr[1] = "x"             # ['a', 'x', 'c']
new_s = "".join(arr)     # 'axc'
```

**核心套路**:
1. 字符串 → list:`list(s)`(为了能修改)
2. 修改 list 内容
3. list → 字符串:`"".join(arr)`(拼回字符串)

⚠️ 如果只是**读字符串**(不修改),不需要转 list,直接用索引即可。

### 2.2 字符串拼接

```python
# ❌ 慢:每次 += 都创建新字符串,总 O(n²)
s = ""
for c in chars:
    s += c

# ✅ 快:join 一次性创建,O(n)
s = "".join(chars)
```

### 2.3 复杂度

| 操作 | 复杂度 |
|---|---|
| `s[i]` | O(1) |
| `len(s)` | O(1) |
| `s + s2` | O(n+m),创建新串 |
| `ch in s` | **O(n)** |
| `s.replace(...)` | O(n) |

### 2.4 内容判断三件套

```python
"abc".isalpha()              # True,纯字母
"abc123".isalpha()           # False(有数字)

"123".isdigit()              # True,纯数字
"abc".isdigit()              # False

"abc123".isalnum()           # True,字母或数字
"abc 123".isalnum()          # False(有空格)
```

| 方法 | 含义 |
|---|---|
| `isalpha()` | 只看是不是**纯字母** |
| `isdigit()` | 只看是不是**纯数字** |
| `isalnum()` | 只看是不是**字母或数字**(允许混合) |

### 2.5 大小写

```python
"Hello".lower()      # 'hello'
"Hello".upper()      # 'HELLO'
"hello world".title()  # 'Hello World'
"Hello".swapcase()   # 'hELLO'
```

### 2.6 替换 / 查找

```python
s = "hello world"

# replace(oldch, newch):替换所有出现
s.replace("o", "0")           # 'hell0 w0rld'
s.replace("o", "0", 1)        # 'hell0 world'(只替换第 1 个)

# find / index
s.find("o")                   # 4(找不到返回 -1)
s.index("o")                  # 4(找不到抛 ValueError)

# count
s.count("o")                  # 2

# 包含判断
"world" in s                  # True
```

### 2.7 分割 / 拼接

```python
"a,b,c".split(",")            # ['a', 'b', 'c'] split按空格(或指定的分隔符)分割
"hello world".split()         # ['hello', 'world'](默认按空白)

",".join(["a", "b", "c"])     # 'a,b,c'
"".join(["a", "b", "c"])      # 'abc'
```

`splitlines()` 会按照换行符把一个字符串分割成多个字符串，并放入 list 中。

## **基本例子**

```python
s = "apple\nbanana\norange"

result = s.splitlines()

print(result)
# ['apple', 'banana', 'orange']
```

原来的字符串可以理解为：

```text
apple
banana
orange
```

其中 `\n` 表示换行。执行：

```python
s.splitlines()
```

后，每一行变成 list 中的一个元素。

------

## **带空行的例子**

```python
s = "apple\n\norange"

result = s.splitlines()

print(result)
# ['apple', '', 'orange']
```

原字符串是：

```text
apple

orange
```

中间有一个空行，所以结果中有一个空字符串 `""`。

------

## **常见使用场景：处理多行输入**

比如题目给你一段文本：

```python
text = """Alice 90
Bob 85
Cindy 95"""

lines = text.splitlines()

print(lines)
# ['Alice 90', 'Bob 85', 'Cindy 95']
```

然后可以逐行处理：

```python
for line in lines:
    name, score = line.split()
    print(name, score)
```

输出：

```text
Alice 90
Bob 85
Cindy 95
```

这里：

```python
text.splitlines()
```

先把整段文字按行分开：

```python
['Alice 90', 'Bob 85', 'Cindy 95']
```

然后：

```python
line.split()
```

再把每一行按空格分开：

```python
'Alice 90'.split()
# ['Alice', '90']
```

------

## **`splitlines()`** **和** **`split("\n")`** **的一个区别**

普通情况下，它们看起来很像：

```python
s = "a\nb\nc"

print(s.splitlines())  # ['a', 'b', 'c']
print(s.split("\n"))   # ['a', 'b', 'c']
```

但是字符串最后有换行符时，结果不同：

```python
s = "a\nb\n"

print(s.splitlines())  # ['a', 'b']
print(s.split("\n"))   # ['a', 'b', '']
```

`splitlines()` 更适合表示“按行读取内容”，通常不会把最后一个单纯的换行解释成额外空行。

### 2.8 去除空白

```python
"  hello  ".strip()           # 'hello'(两端, 只删首尾的空格" ", 换行"\n", tab"\t")
"  hello  ".lstrip()          # 'hello  '(左端)
"  hello  ".rstrip()          # '  hello'(右端)
"xxhelloxx".strip("x")        # 'hello'(去掉指定字符)
s = s.replace(" ", "")				# 删除全部位的普通空格(ignore spaces)
s = "".join(s.split())				# 删全部位的所有空白字符(空格, 换行, tab)(ignore whitespaces)
```

### 2.9 字符 ↔ ASCII

```python
ord('a')                      # 97
chr(97)                       # 'a'
ord('A')                      # 65

# 计算字母在字母表的索引(0-25)
ord('c') - ord('a')           # 2
```

---

## 三、Hash Map / Hash Set / Counter

### 3.1 概念:Hash Map vs Dictionary

**在 Python 里,dictionary(`dict`)就是 hash map 的实现**。

```python
count = {}      # 这就是一个 dictionary,底层是 hash map
```

#### 名字上的区别

| 概念 | 含义 |
|---|---|
| **Hash map / Hash table** | **通用数据结构概念**,用 hash function 计算 key 的位置,快速找到 value |
| **Dictionary / dict** | **Python 里 hash map 的具体实现** |

各语言里的 hash map 实现:
```
Python:     dict
Java:       HashMap
C++:        unordered_map
JavaScript: Map / Object
```

类比:
```
动态数组(通用概念) ←→ list(Python 实现)
hash map(通用概念) ←→ dict(Python 实现)
```

**面试中遇到 "use a hash map",在 Python 里就是 "use a dict"**。

#### 为什么 dict 查询是 O(1)?

```python
count = {"a": 2, "b": 1}
count["a"]      # 怎么找到的?
```

Python 不是从头到尾扫,而是:
```
key "a" → hash("a") → 计算出一个位置 → 直接定位到 value 2
```

所以平均时间复杂度是 **O(1)**,这是所有 hash map 的核心优势。

#### Anagram 里 dict 的角色

```python
count = {}
for ch in s1:
    count[ch] = count.get(ch, 0) + 1

# 例如 s1 = "aabb",最后 count = {"a": 2, "b": 2}
```

这里:
- **key**:字符
- **value**:出现次数

这是 hash map 的典型用法 —— **key 是要分类/索引的对象,value 是这个对象的某种统计或状态**。

---

### 3.2 Dict 模板

```python
d = {}
d['key'] = value             # 添加/更新
value = d['key']             # 访问(key 不存在会 KeyError)
value = d.get('key', 0)      # 安全访问,默认 0
'key' in d                   # 检查 key 存在,O(1)
del d['key']                 # 删除
for k, v in d.items(): ...   # 遍历 key + value
for k in d: ...              # 只遍历 key
for v in d.values(): ...     # 只遍历 value
```

### 3.3 `count.get(ch, 0)` 详解

```python
count.get(key, default_value)
```

**含义**:从字典 count 取 key 对应的 value;**如果 key 不存在,返回默认值**。

```python
count = {}
count.get("a", 0)            # 0(不存在,返回默认)

count = {"a": 2}
count.get("a", 0)            # 2(存在,返回真实值)
count.get("b", 0)            # 0
```

**经典累加用法**:
```python
count[ch] = count.get(ch, 0) + 1
# 含义:count[当前字符] = (已出现次数 if 存在 else 0) + 1
```

例如统计 `"aabb"`:
```python
count = {}
for ch in "aabb":
    count[ch] = count.get(ch, 0) + 1
# {'a': 2, 'b': 2}
```

### 3.4 `defaultdict` 详解

`defaultdict` 是 dict 的升级版 —— **当访问的 key 不存在时,自动创建一个默认 value**,不会报 KeyError。

```python
from collections import defaultdict
```

`defaultdict()` 接受一个**类型/函数**作为参数,用来生成默认值。

#### 3.4.1 `defaultdict(int)` —— 用于计数

```python
from collections import defaultdict

d = defaultdict(int)
c = "a"
d[c] += 1
print(d)
# defaultdict(<class 'int'>, {'a': 1})
```

**为什么不报错?**

`d["a"]` 一开始不存在,但 `defaultdict(int)` 会自动给它默认值:
```python
int()    # 0
```

所以 `d["a"] += 1` 等价于 `d["a"] = 0 + 1`,最后 `d["a"] = 1`。

**计数经典用法**:
```python
from collections import defaultdict

s = "aabbc"
d = defaultdict(int)
for c in s:
    d[c] += 1

# defaultdict(<class 'int'>, {'a': 2, 'b': 2, 'c': 1})
```

| key | value |
|---|---|
| 'a' | 2 |
| 'b' | 2 |
| 'c' | 1 |

#### 3.4.2 `defaultdict(list)` —— 用于分组

```python
from collections import defaultdict

d = defaultdict(list)
d[5].append(10)
print(d)
# defaultdict(<class 'list'>, {5: [10]})
```

**为什么不报错?**

`d[5]` 一开始不存在,但 `defaultdict(list)` 会自动给它默认值:
```python
list()    # []
```

所以 `d[5]` 自动变成 `[]`,然后 `.append(10)` 把它变成 `[10]`。

**等价于普通 dict 的繁琐写法**:
```python
d = {}
if 5 not in d:
    d[5] = []
d[5].append(10)
```

**分组经典用法**:
```python
from collections import defaultdict

pairs = [
    ("fruit", "apple"),
    ("fruit", "banana"),
    ("color", "red")
]

d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)

# defaultdict(<class 'list'>, {
#     'fruit': ['apple', 'banana'],
#     'color': ['red']
# })
```

| key | value |
|---|---|
| 'fruit' | ['apple', 'banana'] |
| 'color' | ['red'] |

意思:**类别 → 这一类下面的所有东西**。

#### 3.4.3 一句话总结

```python
defaultdict(int)     # key 不存在时,默认 value 是 0  → 适合计数
defaultdict(list)    # key 不存在时,默认 value 是 [] → 适合分组
defaultdict(set)     # key 不存在时,默认 value 是 set() → 适合分组+去重
```

**记忆口诀**:
> defaultdict 的 **key** 是你访问的那个东西;
> defaultdict 的 **value** 是自动生成的默认值,然后再被你修改。

#### 3.4.4 `defaultdict` vs `dict.get()` 选哪个?

| 场景 | 推荐 |
|---|---|
| 简单计数(`d[c] += 1`) | `defaultdict(int)` 或 `Counter` |
| 分组到列表(`d[k].append(v)`) | `defaultdict(list)` |
| 一次性查询 + 默认值 | `d.get(key, default)` |
| 不想引入 import | `count.get(ch, 0) + 1` 写法 |

### 3.5 Set 模板

```python
s = set()
s.add(x)
s.remove(x)                  # 不存在会报错
s.discard(x)                 # 不存在不报错
x in s                       # O(1)
s1 & s2                      # 交集
s1 | s2                      # 并集
s1 - s2                      # 差集
```

### 3.6 Counter(神器)

#### 3.6.1 基础用法

```python
from collections import Counter

c = Counter("aabbbc")        # Counter({'b': 3, 'a': 2, 'c': 1})
c["a"]                       # 2
c["z"]                       # 0(不存在的 key 不报错,返回 0,跟 dict 不同)
```

⚠️ 注意 Counter 不是 string 的方法,是从 `collections` 导入的类。

#### 3.6.2 `most_common()` 详解

`Counter` 独有的方法,**按出现次数从高到低**返回元素。

```python
from collections import Counter

s = "aabbbc"
counter = Counter(s)
print(counter.most_common())
# [('b', 3), ('a', 2), ('c', 1)]

# 只取前 N 个
print(counter.most_common(1))
# [('b', 3)]

print(counter.most_common(2))
# [('b', 3), ('a', 2)]
```

**注意返回值是 list,每个元素是 tuple `(元素, 出现次数)`**。

**取出现最多的字符**:
```python
char, freq = counter.most_common(1)[0]
print(char)   # 'b'
print(freq)   # 3
```

拆解一下:
- `counter.most_common(1)` → `[('b', 3)]`(list)
- `[0]` → `('b', 3)`(tuple)
- `char, freq = ('b', 3)` → tuple 解包

#### 3.6.3 Counter 其他常用操作

```python
# Counter 之间的运算
c1 = Counter("aabb")
c2 = Counter("abc")
c1 + c2                      # Counter({'a': 3, 'b': 3, 'c': 1})
c1 - c2                      # Counter({'a': 1, 'b': 1})(只保留正数)
c1 & c2                      # 交集(取最小):Counter({'a': 1, 'b': 1})
c1 | c2                      # 并集(取最大):Counter({'a': 2, 'b': 2, 'c': 1})

# 总元素数
sum(c.values())              # 6
```

### 3.7 Hash Map / Counter / Set 高频套路展开

| 信号 | 用什么 | 存什么 |
|---|---|---|
| 两数和 = target | Hash Map | 数字 → 下标 |
| 出现频次 | Counter / `defaultdict(int)` | 元素 → 次数 |
| 分组(同类放一起) | `defaultdict(list)` | 类别 → 列表 |
| 去重 / 是否见过 | Set | 已见过的元素 |
| 连续子数组求和 = k | Hash Map(前缀和) | 前缀和 → 出现次数 |

下面每种套路展开讲。

---

#### 套路 1:两数和 = target → Hash Map(LC 1 Two Sum)

**题目**:给数组和 target,找两数相加等于 target,返回下标。

```python
nums = [2, 7, 11, 15]
target = 9
# 答案 [0, 1],因为 2 + 7 = 9
```

**代码**:
```python
def two_sum(nums, target):
    seen = {}                    # 已见过的数 → 它的下标
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i
```

**核心思路**:每看到一个 num,问"之前有没有见过 `target - num`?"

**走一遍**:
- num=2: need=7, 不在 seen, 存 `seen={2:0}`
- num=7: need=2, **在 seen** → 返回 `[seen[2], 1] = [0, 1]` ✓

---

#### 套路 2:出现频次 → Counter(LC 387 First Unique Character)

```python
from collections import Counter

s = "aabbbc"
counter = Counter(s)
# Counter({'b': 3, 'a': 2, 'c': 1})

# 找出现最多的
char, freq = counter.most_common(1)[0]
# char='b', freq=3
```

**手写版**(不用 Counter):
```python
def count_chars(s):
    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1
    return count
```

**核心思路**:统计每个元素出现几次。

---

#### 套路 3:去重 / 是否见过 → Set

**例 1:数组去重**
```python
nums = [1, 2, 2, 3, 3, 3]
unique = set(nums)              # {1, 2, 3}
```

**例 2:判断有没有重复元素(LC 217 Contains Duplicate)**
```python
def has_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

print(has_duplicate([1, 2, 3]))     # False
print(has_duplicate([1, 2, 2, 3]))  # True
```

**复杂度**:
- 时间:**O(n)**(set 的 in 是 O(1))
- 空间:**O(n)**(最坏情况所有元素都不重复)

#### ⚠️ set vs list 的复杂度对比(必懂!)

如果把 `seen` 改成 list:
```python
def has_duplicate(nums):
    seen = list()                # ❌ 用 list
    for num in nums:
        if num in seen:          # 这步从 O(1) 退化成 O(k)!
            return True
        seen.append(num)
    return False
```

**复杂度变化**:

| | set 版本 | list 版本 |
|---|---|---|
| 时间 | **O(n)** | **O(n²)** ☠️ |
| 空间 | O(n) | O(n) |

**为什么 list 是 O(n²)?**

`num in seen` 在 list 里要从头扫到尾:
```
第 1 个数:在长度 0 的 seen 里找
第 2 个数:在长度 1 的 seen 里找
...
第 n 个数:在长度 n-1 的 seen 里找
总成本:0 + 1 + 2 + ... + (n-1) = O(n²)
```

**一句话记**:**判断"是否见过",优先用 set,不要用 list**。

#### `enumerate()` 小知识

`enumerate()` 不只能用在 list,**任何可迭代对象都行**:

```python
# list
for i, num in enumerate([10, 20, 30]):  # 0 10 / 1 20 / 2 30

# string
for i, ch in enumerate("abc"):           # 0 a / 1 b / 2 c

# tuple
for i, item in enumerate(("apple", "banana")):  # 0 apple / 1 banana
```

**含义**:一边遍历元素,一边给你下标。

---

#### 套路 4:连续子数组求和 = k → 前缀和 + Hash Map(LC 560)

**这是 hash map 进阶题,面试高频,务必掌握**。

**题目**:给数组 `nums` 和整数 `k`,问有多少个**连续子数组**的和等于 k。

```python
nums = [1, 1, 1]
k = 2
# 答案 2
# nums[0:2] = [1, 1] 和=2
# nums[1:3] = [1, 1] 和=2
```

**代码**:
```python
def subarray_sum(nums, k):
    count = 0
    prefix_sum = 0
    seen = {0: 1}                # 前缀和 → 出现次数,初始有一个"和为 0"
    for num in nums:
        prefix_sum += num
        need = prefix_sum - k
        if need in seen:
            count += seen[need]  # 注意是 += seen[need],不是 += 1
        seen[prefix_sum] = seen.get(prefix_sum, 0) + 1
    return count
```

##### 4.1 为什么是 `prefix_sum - k`?

**核心数学**:
```
当前前缀和 - 之前某个前缀和 = 中间这段子数组的和
prefix_sum - previous_prefix_sum = k
→ previous_prefix_sum = prefix_sum - k
```

所以 `need = prefix_sum - k` 表示:**我需要之前出现过这个前缀和,出现过的话中间就有一段和为 k**。

##### 4.2 为什么 `seen = {0: 1}` 要预置?

为了处理"**从数组开头开始的子数组**"。

例如 `nums = [2, 3]`, `k = 5`:
- 处理完两个数后 `prefix_sum = 5`, `need = 0`
- 如果 `seen` 里没有 `{0: 1}`,就找不到 0,漏掉了 `nums[0:2]` 这个答案

##### 4.3 为什么是 `count += seen[need]` 而不是 `count += 1`?

**因为之前的某个前缀和可能出现过多次**。每出现一次,就对应一个不同起点的合法子数组。

**反例**:
```python
nums = [1, -1, 1, -1]
k = 0
```

走一遍:

| 轮次 | num | prefix_sum | need | seen[need] | count 变化 | 当前 seen |
|---|---|---|---|---|---|---|
| 初始 | - | 0 | - | - | 0 | `{0: 1}` |
| 1 | 1 | 1 | 1 | 不在 | 0 | `{0: 1, 1: 1}` |
| 2 | -1 | 0 | 0 | **1** | +1 → 1 | `{0: 2, 1: 1}` |
| 3 | 1 | 1 | 1 | **1** | +1 → 2 | `{0: 2, 1: 2}` |
| 4 | -1 | 0 | 0 | **2** | **+2** → 4 | `{0: 3, 1: 2}` |

最后 `count = 4`,对应 4 个和为 0 的子数组:
- `[1, -1]`(index 0:2)
- `[-1, 1]`(index 1:3)
- `[1, -1]`(index 2:4)
- `[1, -1, 1, -1]`(index 0:4)

**第 4 轮关键**:此时 `seen[0] = 2`,意思是"之前有 2 个位置的前缀和是 0",每个都能跟当前位置配对成一个合法子数组,所以 `count += 2`,**不是 +1**。

##### 4.4 一句话理解

```python
count += seen[need]
```
意思:
> "当前位置作为子数组的**结尾**时,有多少个**历史前缀和** == need,就新增多少个合法子数组(每个对应一个不同起点)。"

##### 4.5 为什么不能 `return seen[need]`?

三个原因:
1. **它只代表当前这一轮新增的数量**,不是累计总数
2. **`need` 可能不在 seen 里**,直接 `seen[need]` 会 KeyError
3. **`need` 是循环里的局部变量**,只在当前轮有意义

必须用 `count` 累加所有轮次的结果,最后返回 `count`。

##### 4.6 复杂度

- 时间:**O(n)**(扫一遍数组,字典操作 O(1))
- 空间:**O(n)**(seen 最多存 n+1 个不同的前缀和)

##### 4.7 切片小知识(顺便)

```python
nums = [1, 1, 1]
nums[1:3]                    # [1, 1]
```

**`nums[a:b]` 含义**:从下标 a 开始,**取到下标 b 之前**(不含 b)。

- `nums[1:3]` 拿的是 `[nums[1], nums[2]]`
- 即使 b 等于数组长度也不报错(切片允许超出末尾)

---

#### 总结一句话记

| 套路 | 关键 |
|---|---|
| Hash Map | 需要 **key → value** 的映射 |
| Counter | 需要**统计次数** |
| Set | 只需要判断**有没有**(不在乎几次) |
| Prefix Sum + Hash Map | **连续子数组求和** 类问题 |

---

### 3.8 Hash Table 底层原理(中英对照)⭐⭐

> **进阶内容**:之前讲的都是"怎么用",这里讲"为什么 O(1)"。面试官追问"hash table 底层怎么实现"时,这一节是你的标准答案。

#### 3.8.1 什么是 Hash Table?/ What is a Hash Table?

**中文**:Hash Table(哈希表)是一种用于**快速查找、插入、删除**的数据结构。核心思想:把 key 通过 **hash function** 转成数组下标。

```python
key = "apple"
hash("apple") = 12345
12345 % array_size = 5
# "apple" 存到数组下标 5
```

**English explanation**:
> "A hash table is a data structure for **fast lookup, insertion, and deletion**. The core idea is: `key → hash function → index in an array`. Average time complexity for all three operations is **O(1)**, but **worst case is O(n)** if many keys collide."

**复杂度速记**:

| 操作 | 平均 / Average | 最坏 / Worst |
|---|---|---|
| insert | O(1) | O(n) |
| search | O(1) | O(n) |
| delete | O(1) | O(n) |

#### 3.8.2 Hash Table vs Hash Map vs Hash Set

| 概念 | 存什么 | Python 对应 | 用途 |
|---|---|---|---|
| **Hash Table** | 底层思想 | (抽象概念) | 通用数据结构基础 |
| **Hash Map** | key-value pair | `dict` | 计数、映射、记录 index |
| **Hash Set** | 只存 key | `set` | 去重、判断存在 |

**English phrasing**:
> "A **hash table** is the underlying data structure idea. A **hash map** stores key-value pairs (like Python's `dict`), and a **hash set** stores only keys (like Python's `set`). Both are built on top of a hash table."

**判断用 set 还是 dict**:

```
只需要"它存在吗?"          → set
需要"它对应什么信息?"      → dict
需要"它出现了几次?"        → dict 或 Counter
```

##### 进阶:什么类型可以做 Hash Map 的 key?(Hashable / 可哈希性)

**关键概念:Primitive Type(基本类型)和 Hashable**

> **English**: "A **primitive type** is a basic built-in data type that stores a simple value directly — like `int`, `float`, `bool`, `char` (in Java/C++). In Python, although **everything is technically an object**, we still conceptually treat `int`, `float`, `bool`, and `str` as basic types."

**面试官常追问**:"What kind of objects can be used as dict keys?" → **必须是 hashable 的**。

##### Python 中能/不能做 key 的类型

```python
# ✅ 可以做 key(hashable / immutable)
mp = {}
mp[1] = "valid"            # int
mp["apple"] = "valid"      # str
mp[3.14] = "valid"         # float
mp[True] = "valid"         # bool
mp[(1, 2)] = "valid"       # tuple(且元素都 hashable)

# ❌ 不能做 key(unhashable / mutable)
mp[[1, 2]] = "invalid"     # list → TypeError: unhashable type: 'list'
mp[{1, 2}] = "invalid"     # set
mp[{"a": 1}] = "invalid"   # dict
```

##### 为什么 mutable 不能做 key?

假设 list 能做 key:
```python
key = [1, 2]
mp[key] = "hello"

# 然后修改 list 内容
key.append(3)              # 现在 key = [1, 2, 3]

# hash 值变了!hash table 找不到原来的位置了
```

> **English**: "If a mutable object were a key, **changing its contents would change its hash**. The hash table would lose track of where it stored the entry. Mutable objects break the **stability invariant** that hash tables rely on."

##### Hashable 的两个要求

```
1. 能产生稳定的 hash 值 / Produces a stable hash code
2. 在 hash table 里时不能被修改 / Must not change while stored
```

##### 面试英文话术

```
Q: "Can I use a list as a dict key in Python?"
A: "No. Lists are mutable, so their hash would change if you modify them. 
    Python only allows **hashable** types as dict keys — like int, str, 
    tuple of hashables. If you need a list-like key, convert it to a tuple."

Q: "What does 'hashable' mean?"
A: "A hashable object has two properties: it has a stable `__hash__` value 
    that doesn't change over its lifetime, and it implements `__eq__` so 
    we can check for equality after hashing. **Immutable types are usually 
    hashable**; mutable types like list, dict, set are not."
```

##### LeetCode 中的实战应用

```python
# 矩阵题里把坐标存进 set / Use coords as set element
visited = set()
visited.add((r, c))           # ✅ tuple of ints

# Two Sum 类:用 tuple 去重 pair / Tuple for pair deduplication
used_pairs = set()
used_pairs.add(tuple(sorted([a, b])))     # ✅

# 数独题:用 (row, col, box) 标记三种约束 / Three-tuple for constraints
seen = set()
seen.add((r, val, "row"))     # ✅
```

#### 3.8.3 Hash Function 是什么?

**中文**:Hash Function 是**把 key 转成数字**的函数。

```python
hash("apple") = 12345
index = hash(key) % array_size
```

**English explanation**:
> "A **hash function** converts a key into a number (hash code). We then take **modulo array size** to get an index. A good hash function should **distribute keys evenly** to minimize collisions."

**好的 hash function 的标准**:
- **均匀分布 / Uniform distribution**:避免数据堆积在同一位置
- **快速计算 / Fast to compute**:不能太复杂
- **确定性 / Deterministic**:相同 key 总产生相同 hash

#### 3.8.4 Hash Collision(哈希冲突)

**中文**:不同的 key 经过 hash function 得到**同一个下标**。

```python
hash("apple")  % 10 = 5
hash("banana") % 10 = 5
# 两个都想放 index 5 → 冲突!
```

**English**:
> "A **collision** happens when two different keys hash to the same index. Collisions are **unavoidable** because the number of possible keys is much larger than the array size."

冲突**不可避免**,因为 key 可以无限多,但数组位置有限。**所以 hash table 必须有处理冲突的策略**。

#### 3.8.5 处理冲突方式 1:Open Hashing(开放散列 / Separate Chaining)

⚠️ **名字陷阱**:Open Hashing 又叫 **Separate Chaining**(链地址法)。

**核心思想**:每个 bucket 存一个**链表/列表**,冲突的 key 都挂在这里。

```
index 0: []
index 1: []
index 2: apple -> banana -> orange     (三个都冲突在 index 2)
index 3: []
index 4: []
```

**查找步骤**:
1. 算出 hash(key) % size → 找到 bucket
2. 在 bucket 的链表里**线性扫描**

**English**:
> "In **separate chaining** (also called open hashing), each bucket holds a linked list of entries. When a collision occurs, the new entry is **appended to that bucket's list**. Lookups scan the list linearly."

**优缺点**:

| 优点 | 缺点 |
|---|---|
| 实现简单 | 链表过长会退化到 O(k) |
| 删除容易 | 需要额外的指针空间 |
| Load factor 可以 > 1 | 缓存不友好(链表分散) |

#### 3.8.6 处理冲突方式 2:Closed Hashing(封闭散列 / Open Addressing)

⚠️ **名字陷阱**:Closed Hashing 又叫 **Open Addressing**(开放寻址法)。

**核心思想**:所有元素都**存在数组内部**。冲突时,**在数组里找下一个空位**。

```
冲突前:                冲突后(linear probing):
index 5: apple         index 5: apple
index 6:               index 6: banana       (banana 本来要放 5,被占了往后)
```

**三种探测方法**:

| 方法 | 步长 | 优点 | 缺点 |
|---|---|---|---|
| **Linear Probing** | `i+1, i+2, i+3` | 简单、缓存友好 | 容易**聚集** |
| **Quadratic Probing** | `i+1², i+2², i+3²` | 减少聚集 | 可能找不到空位 |
| **Double Hashing** | `i+1*h2, i+2*h2` | 分布最均匀 | 实现复杂 |

**English**:
> "In **open addressing** (also called closed hashing), all elements live **inside the array itself**. On collision, we probe for the next empty slot. **Linear probing** moves one step at a time, **quadratic probing** uses squared offsets, and **double hashing** uses a secondary hash function as the step size."

#### 3.8.7 Open Hashing vs Closed Hashing 对比

| 对比 | Open Hashing | Closed Hashing |
|---|---|---|
| **别名** | Separate Chaining(链地址法) | Open Addressing(开放寻址法) |
| **冲突处理** | bucket 挂链表 | 数组里找下一个空位 |
| **元素位置** | 数组 + 链表 | **全部在数组内** |
| **删除** | 简单 | 复杂(需要 tombstone 标记) |
| **Load factor** | 可以 > 1 | 通常 < 0.7 |
| **典型实现** | Java HashMap(链表/红黑树) | **Python `dict` / `set`** |

> **小知识**:**Python 的 dict 和 set 用的是 open addressing**(closed hashing 思想),不是 separate chaining。这就是为什么 Python 的 dict 很快。

#### 3.8.8 Load Factor(负载因子)

**公式**:`load factor = 元素数量 / 数组长度`

```
元素数量 = 6, 数组长度 = 10
load factor = 0.6
```

**经验值**:
- Load factor **> 0.7**:冲突会显著增多,该 rehash 了
- Python `dict` 维持 load factor **≈ 0.66** 以下

**English**:
> "The **load factor** is the ratio of stored elements to array size. When it exceeds a threshold (usually around 0.7), performance degrades, so the hash table needs to **rehash** to a larger size."

#### 3.8.9 Rehashing(重哈希 / 扩容)

**中文**:当哈希表太满,创建**更大的数组**,把所有旧元素**重新计算 hash** 并放到新数组。

```python
# 旧数组长度 4:hash("apple") % 4 = 1
# 新数组长度 8:hash("apple") % 8 = 5
# "apple" 必须从 index 1 移到 index 5
```

**English**:
> "**Rehashing** means creating a larger array, then **recomputing the index for every existing key** and redistributing them. This is necessary because `index = hash(key) % array_size`, and **changing the array size changes the index**."

**时间复杂度**:
- **单次 rehash**:O(n)(要移动所有元素)
- **均摊插入复杂度 / Amortized insertion**:仍然是 **O(1)**

> **"Amortized" 解释**:大部分插入都很快(O(1)),只有偶尔一次插入会触发扩容(O(n))。**平均下来还是 O(1)**。

##### 中英对照面试话术

```
问: "What is the time complexity of inserting into a hash table?"

中文回答: 平均 O(1),最坏 O(n)。
         如果触发扩容(rehash),单次操作是 O(n),
         但均摊下来还是 O(1)。

英文回答: 
"On average, insertion is O(1). 
In the worst case, when many keys collide or when the table 
needs to be resized, a single insertion can take O(n). 
However, the **amortized** time complexity is still O(1), 
because rehashing only happens occasionally."
```

#### 3.8.9-deep:用 Poisson 分布解释"为什么平均 O(1)"⭐(进阶理论)

> **进阶内容**:如果面试官追问 "**Why is hash table O(1) on average?**",光说"hash function 均匀分布"是不够的。真正的数学解释是 **Poisson 分布**。

##### 核心问题

如果 hash function 把 keys **随机均匀**地分到 buckets,**每个 bucket 里大概会有多少个元素?**

##### 模型设定

```
n = 元素数量 / number of keys
m = bucket 数量 / number of buckets
α = n / m   = load factor(平均每个 bucket 的元素数)
```

##### Poisson 分布的结论

当 hash function 足够随机时,**某个 bucket 里有 k 个元素的概率**:

```
P(X = k) = e^(-α) * α^k / k!
```

> **English**: "If the hash function distributes keys uniformly and independently, the **number of keys in any given bucket** follows approximately a **Poisson distribution** with parameter α (the load factor)."

##### 具体例子:load factor = 1

假设 `n = 1000`,`m = 1000`,所以 `α = 1`(平均每个 bucket 1 个元素)。

| bucket 里的元素数 k | 概率 P(X=k) | 占比 |
|---|---|---|
| 0(空) | e^(-1) * 1 / 1 ≈ **0.368** | **36.8%** |
| 1 | e^(-1) * 1 / 1 ≈ **0.368** | **36.8%** |
| 2 | e^(-1) * 1 / 2 ≈ **0.184** | **18.4%** |
| 3 | e^(-1) * 1 / 6 ≈ **0.061** | **6.1%** |
| 4 | e^(-1) * 1 / 24 ≈ **0.015** | **1.5%** |

##### 关键洞察

**即使 α = 1**:
- **36.8% 的 bucket 是空的**(浪费一些空间)
- **36.8% 的 bucket 恰好 1 个元素**(完美)
- **少数 bucket 会有 2-3 个元素**(轻微冲突)
- **几乎没有 bucket 元素 ≥ 5**(严重冲突极少)

> **English**: "Even with load factor 1, only **~1.5% of buckets have 4 or more elements**, and almost none have 5+. **Most lookups still touch only 1-2 elements**, which is why average-case is O(1)."

##### 这就是 O(1) 的真正原因

每次查找的成本 ≈ `1 + α`(常数,如果 α 是常数)。

- **如果控制 α ≤ 0.75**:绝大多数 bucket 只有 0-1 个元素,查找 O(1)
- **如果 α 太大**(比如 5):平均每个 bucket 5 个元素,退化到 O(α)
- **所以要 rehashing**:把 α 降回小值

##### Rehashing 和 Poisson 分布的关系

```
扩容前:
  n = 1000, m = 500, α = 2
  P(X ≥ 4) ≈ 14%   ← 太多冲突!

扩容后:
  n = 1000, m = 2000, α = 0.5
  P(X ≥ 4) ≈ 0.2%  ← 冲突大幅下降
```

##### 直观理解:扔球进盒子

> 想象有 1000 个球和 1000 个盒子,每个球**随机**扔进一个盒子。
>
> 不会真的每个盒子刚好 1 个球。实际上:
> - 约 37% 的盒子是空的
> - 约 37% 的盒子恰好 1 个
> - 约 18% 的盒子 2 个
> - 约 6% 的盒子 3 个
> - 极少数盒子 4+ 个
>
> 这就是 Poisson 分布。

> **English (interview phrasing)**:
> "Even with random uniform hashing, **bucket sizes don't all equal the average** — they follow a Poisson distribution. But the distribution is **heavily concentrated around small values**, so most operations stay O(1)."

##### 一句话面试答案

```
问: "How can hash table operations be O(1) on average?"

英文答案:
"Because if the hash function distributes keys uniformly, 
bucket sizes follow a **Poisson distribution** with mean equal 
to the load factor α. As long as we keep α bounded by a constant 
(via rehashing), the expected number of comparisons per lookup 
is O(1 + α) = O(1)."
```

##### LeetCode 需要掌握到什么程度?

刷题中**不需要计算 Poisson 分布**。**记住结论就行**:

1. Hash function 均匀 → keys 在 buckets 间近似随机分布
2. 每个 bucket 元素数符合 Poisson(α)
3. **大部分 bucket 元素很少**(0-2 个),所以平均 O(1)
4. **Load factor 越大,大 bucket 越可能出现** → 性能退化
5. **Rehashing 把 α 拉低** → 性能恢复

#### 3.8.10 Hash Table 在面试中常见的追问

##### Q: "How does Python implement `dict`?"

**英文标准答案**:
> "Python's `dict` is implemented as a **hash table using open addressing** (closed hashing). It uses **probing** to handle collisions and **resizes when the load factor exceeds about 0.66**. As of Python 3.7+, `dict` also maintains **insertion order**."

##### Q: "What if all keys collide?"

**英文标准答案**:
> "If every key collides into the same bucket, lookups degenerate to **O(n)** — essentially a linear search. A good hash function and rehashing strategy minimize this risk. In adversarial scenarios, this is called a **hash flooding attack**, which is why production languages randomize their hash seeds."

##### Q: "Why is hash lookup O(1) and not O(log n)?"

**英文标准答案**:
> "Hash lookup is O(1) because we **directly compute the array index** from the key using the hash function — we don't need to compare or traverse anything. Tree-based lookups (like `TreeMap`) are O(log n) because they involve comparisons at each level."

#### 3.8.11 一句话记忆

```
Hash Table 是底层数据结构
Hash Map = key → value(Python dict)
Hash Set = 只存 key(Python set)
Hash Function = key → 数字下标
Collision 不可避免,需要处理:
  Open Hashing(Separate Chaining)— 链表挂在 bucket 后
  Closed Hashing(Open Addressing) — 数组内找空位 ⭐ Python 用这个
Load Factor > 0.7 → Rehashing 扩容
均摊插入 O(1),最坏 O(n)
```

---

## 四、`in` 操作复杂度大对比 ⭐

> **这是面试常考点,务必记牢!**

### 4.1 不同容器的 `in` 复杂度天差地别

| 表达式 | 复杂度 | 原因 |
|---|---|---|
| `ch in list` | **O(n)** | 线性扫描列表 |
| `ch in string` | **O(n)** | 线性扫描字符串 |
| `ch in dict` | **平均 O(1)** | 哈希表查 key |
| `ch in set` | **平均 O(1)** | 哈希表 |

### 4.2 字符串里的 `in`

```python
s2 = "abcdefg"
"a" in s2                    # 很快,开头就找到了
"g" in s2                    # 可能要扫到最后
"x" in s2                    # 找不到,扫完整个字符串
```

最坏情况 **O(n)**,n 是字符串长度。

### 4.3 字典里的 `in`

```python
count = {'a': 2, 'b': 1}
ch not in count              # 是在查字典的 key
```

字典查找平均 **O(1)**,因为哈希表底层不需要逐个扫 key。

### 4.4 关键易混淆点

很多人会想:`if ch not in count` 是不是也要遍历整个 count?

**不是!**

```python
ch in list      # O(n)  ← 列表要扫
ch in string    # O(n)  ← 字符串要扫
ch in dict      # O(1)  ← 字典哈希表,直接定位
ch in set       # O(1)  ← 集合哈希表,直接定位
```

### 4.5 实战影响:为什么 BFS/DFS 用 set 不用 list

```python
# ❌ 错误:用 list 当 visited
visited = [start]
while queue:
    node = queue.popleft()
    for neighbor in graph[node]:
        if neighbor not in visited:    # ← 每次 O(n)!
            visited.append(neighbor)
# 总复杂度从 O(V+E) 退化到 O(V·(V+E))

# ✅ 正确:用 set
visited = {start}
while queue:
    node = queue.popleft()
    for neighbor in graph[node]:
        if neighbor not in visited:    # ← O(1)
            visited.add(neighbor)
```

**面试加分话术**:
> "I'm using a set instead of a list for visited because set membership check is O(1) on average due to hashing, while list lookup is O(n). This keeps the overall BFS complexity at O(V+E)."

---

## 五、Two Pointers(双指针)

双指针是面试高频考点,**不是一个具体算法,而是一种思想**:用两个变量(指针)同时遍历数据,代替双重循环。共有 3 种核心模式,**判断用哪种是关键**。

### 5.1 模式判断速查

| 模式 | 信号关键词 | 典型题 |
|---|---|---|
| **对撞双指针** | 已排序数组、找一对、左右对称 | Two Sum II、Container With Most Water、回文判断 |
| **快慢指针** | 链表、环、中点、原地处理 | 链表找环、找中点、删除倒数第 N 个 |
| **滑动窗口** | 连续子数组/子串、最长/最短、满足某条件 | 无重复字符最长子串、最小覆盖子串 |

---

### 5.1-deep:Two Pointers 信号识别(看到什么会想起它?)⭐⭐⭐

> **核心痛点**:看到题目想不起来用 Two Pointers,因为它不是"看到数组就用",而是要识别**信号**。这一节专门讲信号识别。

#### 5.1-deep.1 一句话定义

> **当题目需要你在一个线性结构里,找两个位置 / 一个区间 / 两边一起移动,并且可以通过移动指针排除一批无用情况时,就考虑 Two Pointers。**

> **English**: "Two pointers is useful when you need to track **two positions** in a linear structure, and you can **eliminate** a range of useless candidates by moving one of the pointers."

#### 5.1-deep.2 四大触发信号

##### 信号 1:数组 / 字符串已经**有序** ⭐⭐⭐

**关键词**:
- `sorted array`
- `non-decreasing order`
- `increasing order`

**看到就想到**:对撞双指针(从两头夹逼)。

**经典题:LC 167 Two Sum II**(已排序数组找两数之和等于 target)

```python
l, r = 0, len(nums) - 1
while l < r:
    s = nums[l] + nums[r]
    if s == target:
        return [l + 1, r + 1]
    elif s < target:
        l += 1                   # 太小,左指针右移
    else:
        r -= 1                   # 太大,右指针左移
```

**为什么能这样**:**数组有序时,每次移动一个指针都能"安全排除"一批组合**:
- 若和太小,左指针所对应的所有更大组合都不需要了
- 若和太大,右指针所对应的所有更小组合都不需要了

> **English**: "Because the array is sorted, moving a pointer **safely eliminates a whole range of candidates** that can't possibly be the answer."

##### 信号 2:问"区间 / 子数组 / 子串" ⭐⭐⭐

**关键词**:
- `longest substring`
- `minimum subarray`
- `contiguous subarray`
- `window`
- `consecutive elements`

**看到就想到**:**滑动窗口**(同方向 Two Pointers)。

**经典题:LC 3 无重复字符最长子串**

```python
seen = set()
l = 0
res = 0
for r in range(len(s)):
    while s[r] in seen:
        seen.remove(s[l])
        l += 1
    seen.add(s[r])
    res = max(res, r - l + 1)
```

**特点**:
- `r` 负责**扩大**窗口(扩展边界)
- `l` 负责**修复**窗口(收缩到合法状态)
- `[l, r]` 是当前**有效区间**

> **English**: "In a sliding window, `r` expands the window, `l` shrinks it when constraints are violated."

##### 信号 3:**原地修改数组** ⭐⭐

**关键词**:
- `in-place`
- `remove duplicates`
- `remove elements`
- `move zeros`
- `partition array`

**看到就想到**:快慢指针(同向不同速)。

**经典题:LC 26 Remove Duplicates from Sorted Array**

```python
slow = 0
for fast in range(len(nums)):
    if nums[fast] != nums[slow]:
        slow += 1
        nums[slow] = nums[fast]
return slow + 1
```

**记忆**:**`fast` 找新元素,`slow` 放答案**。

> **English**: "`fast` scouts for valid elements, `slow` writes them to the result region."

##### 信号 4:**从两边往中间检查** ⭐⭐

**关键词**:
- `palindrome`(回文)
- `reverse string`
- `container with most water`
- `sorted squares`
- `compare from both ends`

**看到就想到**:对撞双指针。

**经典题:LC 125 Valid Palindrome**

```python
l, r = 0, len(s) - 1
while l < r:
    if s[l] != s[r]:
        return False
    l += 1
    r -= 1
return True
```

> **English**: "Comparing from both ends toward the middle is the most direct two-pointer pattern."

#### 5.1-deep.3 三连问决策框架

看到一道题,**问自己这三个问题**:

```
Q1: 是不是数组 / 字符串 / 链表?(线性结构)
    └─ 是 → 继续
    └─ 否 → 大概率不是 Two Pointers

Q2: 是不是在找"两个位置"、"一个区间"、或"左右比较"?
    └─ 是 → 继续
    └─ 否 → 可能不是 Two Pointers

Q3: 移动一个指针后,能不能"排除一批无用候选"?
    └─ 是 → ✅ 很可能用 Two Pointers
    └─ 否 → 可能需要其他算法(DP / Hash Map / etc.)
```

> **English (interview phrasing)**:
> "I'm considering two pointers here because: (1) the input is a linear structure, (2) we're looking for a pair / range / palindrome, and (3) moving a pointer eliminates a range of candidates safely."

#### 5.1-deep.4 信号 → Pattern 快速对照表

| 题目特征 | 推荐 Pattern | 经典题 |
|---|---|---|
| **sorted array** + target sum | 对撞双指针 | LC 167, LC 15 |
| **longest / shortest subarray** | 滑动窗口 | LC 3, LC 76, LC 209 |
| **remove / move / compress in-place** | 快慢指针 | LC 26, LC 27, LC 283 |
| **palindrome / reverse** | 对撞双指针 | LC 125, LC 344 |
| **linked list cycle / middle** | 快慢指针 | LC 141, LC 142, LC 876 |
| **container / area** | 对撞双指针 | LC 11 |

#### 5.1-deep.5 Two Pointers 跟暴力解的关系

许多 Two Pointers 题,**暴力解都是 O(n²) 的两层循环**:

```python
# 暴力 O(n²)
for i in range(n):
    for j in range(i + 1, n):
        check(i, j)
```

**Two Pointers 的本质优化**:
> **如果不需要枚举所有 (i, j),因为可以根据大小关系移动指针、排除一批,就能把 O(n²) 降到 O(n)。**

> **English**: "If we don't actually need to enumerate every pair, because we can use **ordering or constraint information** to prune the search space, two pointers reduces O(n²) to O(n)."

#### 5.1-deep.6 终极口诀(背下来)

```
有序找两数,左右夹逼。   Sorted + find pair → opposite-direction pointers.
原地改数组,快慢指针。   In-place modify → fast/slow pointers.
连续子数组,滑动窗口。   Contiguous subarray → sliding window.
回文或反转,两头相向。   Palindrome / reverse → opposite-direction.
```

**最重要**:不要背模板,记住**本质**:
> **Two pointers 是"用两个位置描述当前状态,并通过移动指针排除掉不可能的答案"。**
>
> **English**: "Two pointers describes the current state with two positions, and eliminates impossible answers by moving one of them."

---

### 5.2 模式 1:对撞双指针(从两头往中间)

#### 适用场景
1. **数组已经排序**
2. 要找**两个数 / 一对元素**
3. 要比较**左右两端**
4. 要在 O(n) 内完成,而不是 O(n²)

#### 模板

```python
left, right = 0, len(arr) - 1
while left < right:
    if condition_satisfied:
        return ...
    elif need_bigger:
        left += 1                # 需要更大的值,左指针右移
    else:
        right -= 1               # 需要更小的值,右指针左移
```

#### 例 1:Two Sum II(已排序数组)

```python
def two_sum_sorted(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left, right]
        elif total < target:
            left += 1            # 太小,左指针右移找更大的
        else:
            right -= 1           # 太大,右指针左移找更小的
    return []
```

**走一遍** `numbers = [2, 7, 11, 15]`, `target = 9`:

| 步骤 | left | right | total | 动作 |
|---|---|---|---|---|
| 1 | 0 (2) | 3 (15) | 17 | 太大,right-- |
| 2 | 0 (2) | 2 (11) | 13 | 太大,right-- |
| 3 | 0 (2) | 1 (7) | 9 | **找到!返回 [0, 1]** ✓ |

#### 例 2:判断回文字符串

```python
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
```

**回文 vs 异位词(常混淆)**:

| 概念 | 定义 | 例子 |
|---|---|---|
| **Palindrome 回文** | 正读 == 反读(顺序对称) | `"level"`, `"madam"`, `"racecar"` |
| **Anagram 异位词** | 字符种类和次数一样,顺序可以不同 | `"listen"` ↔ `"silent"` |

记忆:
- **palindrome 看左右顺序是否对称**
- **anagram 看字符种类和次数是否一样**

---

### 5.3 模式 2:快慢指针(同向不同速)

#### 适用场景
1. **链表**题(环、中点、第 N 个)
2. **原地去重 / 原地覆盖**

#### 核心思路

> 两个指针都往前走,但**走的速度不同**(或先后出发时间不同)。

#### 例 1:链表是否有环

直觉:操场上两个人跑步,快的迟早追上慢的。链表有环 → fast 一定追上 slow。

```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next            # 走 1 步
        fast = fast.next.next       # 走 2 步
        if slow == fast:
            return True
    return False
```

**为什么循环条件是 `fast and fast.next`?**

因为 `fast = fast.next.next` 一步要跨两个节点,必须保证:
- `fast` 不是 None(否则 `fast.next` 报错)
- `fast.next` 不是 None(否则 `fast.next.next` 报错)

#### 例 2:找链表中点

```python
def middle_node(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow                     # fast 走完时,slow 正好在中点
```

**原理**:fast 走 2 步、slow 走 1 步,fast 到终点时 slow 走完了一半 = 中点。

---

### 5.4 模式 3:滑动窗口(同向维护一个区间)

#### 适用场景

**关键词**:
- 连续子数组 / 连续子串
- 最长 / 最短
- 满足某种条件的区间
- "longest substring"、"shortest subarray"、"contiguous"

**典型题**:
- 无重复字符的最长子串(LC 3)
- 最小覆盖子串(LC 76)
- 长度最小的子数组(LC 209)
- 最多包含 K 个不同字符的最长子串

#### 通用模板

```python
left = 0
window = ...                        # 用 set/dict/Counter 维护窗口状态
for right in range(len(arr)):
    # 1. 把 arr[right] 加入窗口
    while 窗口不满足条件:
        # 2. 缩窗:移除 arr[left]
        left += 1
    # 3. 更新答案
```

#### 重点例题:无重复字符最长子串(LC 3)

```python
def length_of_longest_substring(s):
    left = 0
    seen = set()
    max_len = 0
    for right in range(len(s)):
        while s[right] in seen:     # 当前字符重复,缩窗
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len
```

#### 5.4.1 代码核心思想

**维护一个窗口** `s[left : right+1]`(包含 right):

- `seen` 存当前窗口里**有哪些字符**
- `right` 负责**扩张窗口**(每轮 +1)
- `left` 负责**收缩窗口**(发现重复时右移)
- 答案是窗口长度 `right - left + 1`

#### 5.4.2 为什么用 `while` 而不是 `if`?

```python
while s[right] in seen:
    seen.remove(s[left])
    left += 1
```

**因为可能要连续移除多个字符**,直到旧的重复字符被彻底移除。

#### 5.4.3 走一遍 `s = "abcabcbb"`

| right | s[right] | 操作 | seen | 窗口 | max_len |
|---|---|---|---|---|---|
| 0 | 'a' | 加入 | {'a'} | "a" | 1 |
| 1 | 'b' | 加入 | {'a','b'} | "ab" | 2 |
| 2 | 'c' | 加入 | {'a','b','c'} | "abc" | 3 |
| 3 | 'a' | 重复!移除 s[0]='a',left=1,加新'a' | {'b','c','a'} | "bca" | 3 |
| 4 | 'b' | 重复!移除 s[1]='b',left=2,加新'b' | {'c','a','b'} | "cab" | 3 |
| ... | | | | | |

#### 5.4.4 关键困惑解答:为什么先 remove `s[left]`?

新手最容易卡在这里:**重复的字符在窗口中间,为什么先 remove `s[left]` 而不是直接移除那个重复字符?**

**答案**:**滑动窗口只能从左边缩**,不能跳过中间。

##### 例子:`s = "abcdb"`

当 `right = 4`, `s[right] = 'b'`:
- 当前窗口 `"abcd"`,`seen = {'a','b','c','d'}`
- 重复的旧 'b' 在 index 1(**不是 left=0**)

直觉上你会想:"直接 remove 那个旧 'b' 不就行了?"

**但 set 只知道 'b' 存在,不知道它在哪个 index**。所以必须从 left 一个个往右缩,直到把旧 'b' 移出去:

| 轮 | s[right] in seen? | 动作 | seen | left |
|---|---|---|---|---|
| 1 | 'b' 在 → True | remove s[0]='a',left++ | {'b','c','d'} | 1 |
| 2 | 'b' 仍在 → True | remove s[1]='b',left++ | {'c','d'} | 2 |
| 3 | 'b' 不在 → False | while 退出 | {'c','d'} | 2 |

然后加入新 'b':`seen = {'c','d','b'}`,窗口变成 `"cdb"`,合法。

##### 为什么不能直接 `remove(s[right])`?

因为 `s[right]` 是**准备加入的新字符,还没真正加入**。`seen` 里的那个字符是**旧字符**,你删了 `seen` 里的字符,但旧字符的位置还在窗口里,窗口仍然不合法。

##### 一句话理解

> "**只要新字符已经在当前窗口里,就从窗口左边开始删,直到旧的重复字符被删掉为止。** 不是因为 `s[left]` 一定等于 `s[right]`,而是因为窗口只能通过移动 left 来缩小;移动 left 时,必须同步把 `s[left]` 从 seen 里删掉。"

#### 5.4.5 为什么 `right - left + 1` 是窗口长度?

窗口包含下标 `left, left+1, ..., right`,所以长度 = `right - left + 1`。

例如 `left=2`, `right=4`:下标 2, 3, 4 共 3 个,等于 `4 - 2 + 1 = 3`。

#### 5.4.6 滑动窗口角色分工

```
right  →  扩张窗口(每轮 for 自动 +1)
left   →  收缩窗口(while 内部 +1)
seen   →  记录当前窗口里的字符(用 set/dict/Counter)
```

**判断条件**:
- `s[right] in seen` → 新字符跟窗口某旧字符重复
- 不能马上加入,要先**从 left 开始删,直到窗口里没有这个字符**
- 然后再 `seen.add(s[right])`,保证窗口永远没有重复

---

### 5.4-bonus 滑动窗口经典题扩展

#### LC 209 Minimum Size Subarray Sum(可变窗口找最小)

##### 题目

找出和 ≥ target 的**最短连续子数组**长度。

```python
nums = [2, 3, 1, 2, 4, 3], target = 7
# [4, 3] 和=7,长度 2 ← 答案
```

##### 代码

```python
def minSubArrayLen(target, nums):
    left = 0
    curr_sum = 0
    min_len = float('inf')
    for right in range(len(nums)):
        curr_sum += nums[right]
        while curr_sum >= target:        # 满足条件,**尝试缩小窗口**
            min_len = min(min_len, right - left + 1)
            curr_sum -= nums[left]
            left += 1
    return min_len if min_len != float('inf') else 0
```

**核心模式**:**找最短** → 用 `while` 在满足条件时**缩小**窗口。

#### LC 76 Minimum Window Substring ⭐⭐⭐(滑动窗口"教科书题")

##### 题目

给字符串 `s` 和 `t`,在 `s` 中找**最短的子串**,包含 `t` 中**所有字符**(含重复次数)。

```python
s = "ADOBECODEBANC", t = "ABC"
# "BANC" 是包含 A、B、C 的最短子串,长度 4
```

> **这是最经典的"可变滑动窗口 + 字符计数"模板,几乎所有大厂都考过**。掌握后,LC 567、LC 438、LC 30 全都能套用。

##### 核心思路:两个 Counter + have/need 计数

- `need = Counter(t)` —— 还需要的字符
- 窗口里维护一个 Counter
- 用 `have` 和 `need_count` 计数,**避免每次重新比较两个 Counter**(那样 O(n×m))

##### 模板代码

```python
from collections import Counter

def minWindow(s, t):
    if not t or not s:
        return ""
    
    need = Counter(t)                   # 需要的字符:需要的次数
    have = {}                           # 窗口里已有的字符:出现次数
    need_count = len(need)              # 需要凑齐的"字符种类数"
    have_count = 0                      # 已凑齐的"字符种类数"
    
    left = 0
    result = [-1, -1]                   # [start, end]
    min_len = float('inf')
    
    for right in range(len(s)):
        c = s[right]
        have[c] = have.get(c, 0) + 1
        
        # 当前字符 c 是否凑够了需要的次数
        if c in need and have[c] == need[c]:
            have_count += 1
        
        # 窗口已满足条件 → 尝试缩小
        while have_count == need_count:
            # 更新答案
            if right - left + 1 < min_len:
                result = [left, right]
                min_len = right - left + 1
            # 左指针右移,从窗口移除 s[left]
            have[s[left]] -= 1
            if s[left] in need and have[s[left]] < need[s[left]]:
                have_count -= 1
            left += 1
    
    l, r = result
    return s[l:r+1] if min_len != float('inf') else ""
```

##### 走一遍 `s = "ADOBECODEBANC"`, `t = "ABC"`

需要:`A: 1, B: 1, C: 1`, `need_count = 3`

| right | s[right] | have | have_count | 是否触发缩窗 | 答案 |
|---|---|---|---|---|---|
| 0 | A | {A:1} | 1 | 否 | - |
| 1 | D | {A:1,D:1} | 1 | 否 | - |
| 2 | O | + O | 1 | 否 | - |
| 3 | B | + B | 2 | 否 | - |
| 4 | E | + E | 2 | 否 | - |
| 5 | C | + C | **3** | **是**!尝试缩 | 找到 [0,5]="ADOBEC" 长 6 |
| ... | ... 缩到 left=4 (移除 A 触发 have_count-1) | ... | 2 | 停止缩 | |
| 10 | A | ... 又凑齐 ... | 3 | 是 | 更新 |
| 12 | C | ... 缩到 left=9 ... | | | 最终 [9,12]="BANC" 长 4 ✓ |

##### 复杂度

- 时间:**O(n + m)**(每个字符最多被 right 和 left 各访问一次)
- 空间:O(m)(Counter 大小)

##### 为什么用 `have_count == need_count` 而不是直接比 Counter?

- 比两个 Counter:**O(字符种类数)**,每次都比 → 总 O(n × 种类数)
- 用计数器:**O(1)** 判断,只在某个字符**刚好达到所需次数**时 `have_count += 1`

##### 一句话记忆

```
LC 209(找最短和):curr_sum >= target 时 while 缩窗
LC 76(找最短覆盖):have/need 计数器,刚好凑齐时 while 缩窗
"找最长" → if 扩;"找最短" → while 缩
```

---

### 5.5 三种模式对比速查

| 维度 | 对撞双指针 | 快慢指针 | 滑动窗口 |
|---|---|---|---|
| 方向 | 相向(从两头往中间) | 同向不同速 | 同向,左右共同移动 |
| 数据 | 多用于已排序数组 | 多用于链表 | 多用于连续子串/子数组 |
| 关键判断 | `arr[left] + arr[right]` 跟 target 比 | `slow == fast`? | 窗口是否满足条件 |
| 典型题 | Two Sum II、Container With Most Water | 链表环、链表中点 | 无重复字符最长子串、最小覆盖 |
| 代码骨架 | `while left < right` | `while fast and fast.next` | `for right ... while not valid: left++` |

### 5.6 一句话记忆

- **有序数组找 pair** → 对撞双指针
- **链表环 / 中点** → 快慢指针
- **连续子串/子数组 + 最长最短** → 滑动窗口

---

### 5.7 Two Pointers 刷题路径(8 题建立肌肉记忆)⭐⭐⭐

> **重要**:不需要把所有双指针题刷完。**8 道核心题**就能建立感觉。**按这个顺序刷,效率最高**。

#### 5.7.1 推荐刷题顺序(一周完成)

| Day | 题号 | 题目 | 模式 | 难度 | 关键技能 |
|---|---|---|---|---|---|
| 1 | **LC 283** | Move Zeroes | 快慢指针 | Easy | `fast 找,slow 放` |
| 1 | **LC 27** | Remove Element | 快慢指针 | Easy | 跟 283 同模板 |
| 2 | **LC 26** | Remove Duplicates from Sorted Array | 快慢指针 | Easy | 有序数组去重 |
| 3 | **LC 344** | Reverse String | 对撞双指针 | Easy | 两指针交换 |
| 3 | **LC 125** | Valid Palindrome | 对撞双指针 | Easy | 两端往中间比 |
| 4 | **LC 167** | Two Sum II | 对撞双指针 | Medium | **有序 + target** 经典 |
| 5 | **LC 11** | Container With Most Water | 对撞双指针 | Medium | **贪心移动**(移短边) |
| 6-7 | **LC 15** | 3Sum | 对撞双指针 + 去重 | Medium | **进阶**:嵌套 + 跳重 |

**为什么这个顺序**:
- 前 3 题(283/27/26)**本质一样**,做完建立"in-place overwrite"肌肉记忆
- 4-5 题(344/125)建立"opposite direction"肌肉记忆
- 6-8 题加入"有序 + 比较"思维,**逐步进阶**

#### 5.7.2 第一组:快慢指针 / 原地覆盖

##### LC 283 Move Zeroes(必刷起点)

把所有 0 移到数组末尾,**不能改非零元素的相对顺序**。

```python
slow = 0
for fast in range(len(nums)):
    if nums[fast] != 0:
        nums[slow] = nums[fast]
        slow += 1
# 后面填 0
for i in range(slow, len(nums)):
    nums[i] = 0
```

**核心**:**`fast` 找非零,`slow` 放非零**。

##### LC 27 Remove Element(同模板变形)

删除数组中等于 `val` 的元素。

```python
slow = 0
for fast in range(len(nums)):
    if nums[fast] != val:
        nums[slow] = nums[fast]
        slow += 1
return slow
```

**核心顿悟**:不是真"删除",而是**覆盖**。

> **English**: "I'm not really deleting elements — I'm **overwriting** them by moving valid elements forward with `slow`."

##### LC 26 Remove Duplicates from Sorted Array(进阶版)

**已排序**数组去重。

```python
slow = 1
for fast in range(1, len(nums)):
    if nums[fast] != nums[fast - 1]:
        nums[slow] = nums[fast]
        slow += 1
return slow
```

**关键**:数组有序 → 重复元素**相邻**,只需比 `nums[fast]` 跟 `nums[fast - 1]`。

**做完这三题,你掌握了 in-place overwrite pattern**。

#### 5.7.3 第二组:对撞双指针 / 两边往中间

##### LC 344 Reverse String

```python
l, r = 0, len(s) - 1
while l < r:
    s[l], s[r] = s[r], s[l]    # Python 神技:一行交换
    l += 1
    r -= 1
```

##### LC 125 Valid Palindrome

```python
l, r = 0, len(s) - 1
while l < r:
    if s[l] != s[r]:
        return False
    l += 1
    r -= 1
return True
```

**做完这两题,你掌握了 opposite direction two pointers**。

#### 5.7.4 第三组:有序数组 + target

##### LC 167 Two Sum II(经典)

```python
l, r = 0, len(numbers) - 1
while l < r:
    total = numbers[l] + numbers[r]
    if total == target:
        return [l + 1, r + 1]    # 题目要求 1-indexed
    elif total < target:
        l += 1                   # 太小,左指针右移
    else:
        r -= 1                   # 太大,右指针左移
```

**这题让你彻底理解**:**为什么 sorted array 经常想到 two pointers** —— 排序让"移动指针"变成有方向的、能排除一批候选的操作。

##### LC 15 3Sum(进阶)

Two Sum II 的升级版。**核心思路**:
```
排序 → 固定一个 nums[i] → 剩下两数用 Two Pointers 找 target
```

```python
def threeSum(nums):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue                    # 跳过重复的 i
        l, r = i + 1, len(nums) - 1
        target = -nums[i]
        while l < r:
            total = nums[l] + nums[r]
            if total == target:
                result.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:    # 跳重
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
            elif total < target:
                l += 1
            else:
                r -= 1
    return result
```

**3Sum 三重去重**(这是最大难点):
1. **外层 `i`** 的去重:`if i > 0 and nums[i] == nums[i - 1]: continue`
2. **内层 `l`** 的去重:`while l < r and nums[l] == nums[l - 1]: l += 1`
3. **内层 `r`** 的去重:`while l < r and nums[r] == nums[r + 1]: r -= 1`

> **5/7 mock 你做过简化版**(target=0,只找 pair),3Sum 是**多了一层固定 nums[i] + 三重去重**。强烈建议作为下一步刷的题。

#### 5.7.5 第四组:贪心型对撞双指针

##### LC 11 Container With Most Water

给一组柱子高度,选两根装最多水,问最大面积。

```python
l, r = 0, len(height) - 1
res = 0
while l < r:
    area = min(height[l], height[r]) * (r - l)
    res = max(res, area)
    if height[l] < height[r]:
        l += 1                      # 移动较短的那边!
    else:
        r -= 1
return res
```

**最反直觉的点**:**为什么移动较短的边?**

> **English**: "The area is bounded by the **shorter** of the two heights times the width. If I move the **taller** pointer inward, the area can only get smaller (height stays bounded by the short one, width shrinks). Only by moving the **shorter** pointer might I find a taller one and increase the area."

**直觉理解**:面积 = `min(高1, 高2) * 宽`。宽度肯定会变小,**唯一可能"赚回来"的就是高度变高**,而**移动较短那边**才有这个机会。

#### 5.7.6 三大模板速查(背下来)

##### 模板 1:快慢指针(原地覆盖)

```python
slow = 0
for fast in range(len(nums)):
    if nums[fast] should_be_kept:
        nums[slow] = nums[fast]
        slow += 1
return slow                         # 或 slow + 1
```

**口诀**:`fast 找,slow 放`。
**适用**:Move Zeroes / Remove Element / Remove Duplicates。

##### 模板 2:对撞双指针(两边往中间)

```python
l, r = 0, len(nums) - 1
while l < r:
    # compare or swap
    l += 1
    r -= 1
```

**口诀**:`左边一个,右边一个,往中间靠`。
**适用**:Palindrome / Reverse String。

##### 模板 3:对撞双指针 + 比较(有序数组)

```python
l, r = 0, len(nums) - 1
while l < r:
    if condition_too_small:
        l += 1
    else:
        r -= 1
```

**口诀**:`有序数组找组合,优先想左右夹逼`。
**适用**:Two Sum II / 3Sum / Container With Most Water。

#### 5.7.7 学习路径建议(对你 Jun)

**最该先做的 3 题**:**LC 283 → LC 27 → LC 26**

因为这三题**本质相同**(都是快慢指针 + 原地覆盖),做完会有"原来我把同一个模板写了三遍"的顿悟感,是建立**双指针肌肉记忆**最快的方式。

之后:
- **Day 3-5**:Palindrome / Two Sum II / Container
- **Day 6-7**:3Sum(把 5/7 mock 的题彻底升级版做掉)

**做完这 8 题**:面试中**任何双指针题你都不会再"想不起来用它"**。

#### 5.7.8 一句话记忆

```
8 题打通双指针:283/27/26(快慢) + 344/125(对撞) + 167/11/15(有序+target)
最先做:283 → 27 → 26(三题同模板)
最难做:15 3Sum(三重去重)
最反直觉:11(为什么移动较短的边?)
```

---

## 六、Binary Search(二分查找)

### 6.1 适用条件

二分能用的两个核心场景:
1. **有序数组里找具体值或边界**(数据本身有序)
2. **答案空间单调**(check(x) 的结果是 False...False...True...True 这种单调形式)

### 6.2 核心思想:mid 还可能是答案吗?

**这是二分最核心的判断**,不是死记 `<` / `<=`,而是问:

> **mid 这个位置还有没有可能是答案?**

| 情况 | 边界更新 |
|---|---|
| mid **不可能**是答案 | `lo = mid + 1` 或 `hi = mid - 1`(排除 mid) |
| mid **可能**是答案 | `hi = mid` 或 `lo = mid`(保留 mid) |

后面所有模板都是这条原则的具体应用。

### 6.3 关于 `mid` 的两种写法

```python
mid = (lo + hi) // 2          # Python 推荐(简洁)
mid = lo + (hi - lo) // 2     # Java/C++ 推荐(防溢出)
```

#### 为什么 Java/C++ 推荐第二种?

**整数溢出问题**。Java 的 `int` 是 32-bit,范围约 ±21 亿。如果:
```java
int lo = 2_000_000_000;
int hi = 2_000_000_000;
int mid = (lo + hi) / 2;       // lo + hi = 40 亿,溢出!
```

所以 Java/C++ 推荐:
```java
int mid = lo + (hi - lo) / 2;  // 不会先算出 40 亿
```

#### Python 为什么没这个问题?

**Python 的 `int` 是任意精度整数**,大小只受内存限制。

```python
x = 10 ** 100                  # Python 也能处理
print(2_000_000_000 + 2_000_000_000)  # 4000000000,正常
```

所以 Python 刷题直接写 `mid = (lo + hi) // 2` 就行。

#### 注意 Java/C++ 是 `/ 2` 不是 `// 2`

```python
Python:    mid = lo + (hi - lo) // 2     # 整数除法 //
Java/C++:  mid = lo + (hi - lo) / 2;     # 整数 / 整数 默认就是整数除法
```

Python 里 `5 / 2 = 2.5`(浮点),`5 // 2 = 2`(整数);Java/C++ 里两个 int 相除自动取整,直接用 `/`。

---

### 6.4 模板 1:标准二分(找具体 target 是否存在)

```python
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1     # 左闭右闭 [lo, hi]
    while lo <= hi:              # 注意 <=
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid           # 找到立即返回
        elif arr[mid] < target:
            lo = mid + 1         # mid 不是答案,排除
        else:
            hi = mid - 1         # mid 不是答案,排除
    return -1                    # 没找到
```

#### 关键设计(必懂)

| 设计点 | 理由 |
|---|---|
| `hi = len(arr) - 1` | 搜索区间 `[lo, hi]` 左右都闭,hi 是有效下标 |
| `while lo <= hi` | 区间 `[lo, hi]` 当 `lo == hi` 时还有 1 个元素要查 |
| `lo = mid + 1` / `hi = mid - 1` | 已经检查过 mid 不等于 target,**mid 不可能是答案,直接排除** |

#### 走一遍 `arr = [1, 3, 5, 7, 9, 11]`, `target = 7`

| 步 | lo | hi | mid | arr[mid] | 比较 | 动作 |
|---|---|---|---|---|---|---|
| 1 | 0 | 5 | 2 | 5 | < 7 | lo = 3 |
| 2 | 3 | 5 | 4 | 9 | > 7 | hi = 3 |
| 3 | 3 | 3 | 3 | 7 | == 7 | **return 3** ✓ |

---

### 6.5 模板 2:lower_bound(找第一个 >= target)

适合**找左边界 / 插入位置 / 第一个满足条件的位置**。

```python
def lower_bound(arr, target):
    lo, hi = 0, len(arr)         # 左闭右开 [lo, hi)
    while lo < hi:               # 注意是 <
        mid = (lo + hi) // 2
        if arr[mid] < target:
            lo = mid + 1         # mid 太小,排除
        else:
            hi = mid             # mid 可能是答案,保留!
    return lo
```

#### 关键设计(为什么跟标准二分不一样?)

| 设计点 | 理由 |
|---|---|
| `hi = len(arr)` | **答案可能是 `len(arr)`**(target 比所有元素都大,要插到最末尾) |
| `while lo < hi` | 区间 `[lo, hi)` 当 `lo == hi` 时区间为空,搜索结束 |
| `hi = mid`(不是 `mid - 1`) | **`arr[mid] >= target` 时,mid 本身可能就是第一个 >= target 的位置,不能丢** |

#### 为什么 `hi = mid` 不能写 `hi = mid - 1`?

用反例直接看:

```python
arr = [1, 2, 3]
target = 2
# 正确答案 = 1(第一个 >= 2 的位置)
```

走一遍:
- 初始 `lo=0, hi=3`, `mid=1`, `arr[1]=2`
- `arr[mid] >= target`,**mid=1 正是答案!**
- 如果写 `hi = mid - 1 = 0`,**直接把答案丢了** ☠️
- 正确写法 `hi = mid = 1`,保留答案

最后 `lo=1, hi=1`,return 1 ✓

#### 为什么 `while lo < hi` 不能写 `<=`?

也用反例看:

```python
arr = [1, 3, 5]
target = 10                      # 没有元素 >= 10,答案应是 3 (= len(arr))
```

最后会到 `lo=3, hi=3`。
- 用 `while lo <= hi`,会继续:`mid = 3`, `arr[3]` **越界报错** ☠️
- 用 `while lo < hi`,正确退出循环,return 3 ✓

#### 走一遍 `arr = [1, 2, 2, 2, 3, 4]`, `target = 2`

| 步 | lo | hi | mid | arr[mid] | 比较 | 动作 |
|---|---|---|---|---|---|---|
| 1 | 0 | 6 | 3 | 2 | >= 2 | **保留 mid**,hi = 3 |
| 2 | 0 | 3 | 1 | 2 | >= 2 | 保留,hi = 1 |
| 3 | 0 | 1 | 0 | 1 | < 2 | lo = 1 |
| 结束 | 1 | 1 | - | - | - | **return 1** ✓ |

---

### 6.6 模板 3:upper_bound(找第一个 > target)

跟 lower_bound 几乎一样,**只把判断条件 `<` 改成 `<=`**。

```python
def upper_bound(arr, target):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] <= target:
            lo = mid + 1         # mid <= target,不是 > target,排除
        else:
            hi = mid             # mid > target,可能是答案,保留
    return lo
```

#### lower_bound vs upper_bound 对比

```python
# lower_bound:第一个 >= target
if arr[mid] < target:            # 排除小于 target 的
    lo = mid + 1
else:
    hi = mid

# upper_bound:第一个 > target
if arr[mid] <= target:           # 排除小于等于 target 的
    lo = mid + 1
else:
    hi = mid
```

**记忆口诀**:
- `>=` 的反面是 `<` → lower_bound 用 `<`
- `>` 的反面是 `<=` → upper_bound 用 `<=`

#### 应用:找最后一个 == target 的位置

```python
last_equal_pos = upper_bound(arr, target) - 1
```

例如 `arr = [1, 2, 2, 2, 3]`, `target = 2`:
- `upper_bound = 4`(arr[4]=3,第一个 > 2)
- 最后一个 == 2 的位置 = 4 - 1 = **3** ✓

---

### 6.7 经典题对比:LC 704 / LC 33 / LC 34

这三题都叫"二分查找",但**目标不同,模板选择也不同**。把它们放在一起对比,能彻底搞清楚什么时候用哪个模板。

| 题目 | 数组特点 | 目标 | 二分重点 | 用模板 |
|---|---|---|---|---|
| **LC 704** | 完全升序,无旋转 | 找任意 target | 标准二分 | 模板 1(`while lo <= hi`) |
| **LC 33** | 升序但被旋转过,无重复 | 找任意 target | 判断哪一半有序 | 模板 1(变形) |
| **LC 34** | 完全升序,**有重复** | 找 target 起止位置 | 找左右边界 | 模板 2 + 模板 3 |

记忆:
- **LC 704**:普通有序数组找一个值
- **LC 33**:旋转有序数组找一个值
- **LC 34**:有重复的有序数组找左右边界

---

#### 6.7.1 LC 704:Binary Search(标准二分)

最简单的一题,直接用模板 1。

**例子**:
```python
nums = [-1, 0, 3, 5, 9, 12]
target = 9
# 返回 4
```

**代码**:
```python
def search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

数组整体有序,直接二分判断 target 在 mid 哪边。

---

#### 6.7.2 LC 33:Search in Rotated Sorted Array(旋转数组)

**题目特征**:
- 数组**原本升序,但被旋转了**
- 没有重复元素
- 找 target 是否存在,存在返回 index

**例子**:
```python
nums = [4, 5, 6, 7, 0, 1, 2]
# 原数组 [0,1,2,4,5,6,7] 在 index 4 处旋转
target = 0
# 返回 4
```

**核心难点**:数组整体不有序,但**每次二分时,左半边或右半边至少有一边是有序的**。

##### 怎么判断哪半边有序?

比较 `nums[lo]` 和 `nums[mid]`:
- 如果 `nums[lo] <= nums[mid]` → **左半边 `[lo..mid]` 有序**
- 否则 → **右半边 `[mid..hi]` 有序**

**为什么?** 旋转点把数组分成两段升序。`nums[lo]` 和 `nums[mid]` 中间如果没跨过旋转点,左半边就是有序的;跨过了,右半边才是有序的。

##### 代码

```python
def search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        
        # 判断哪半边有序
        if nums[lo] <= nums[mid]:
            # 左半边 [lo..mid] 有序
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1                # target 在有序的左半边
            else:
                lo = mid + 1                # target 在右半边
        else:
            # 右半边 [mid..hi] 有序
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1                # target 在有序的右半边
            else:
                hi = mid - 1                # target 在左半边
    return -1
```

##### 关键判断的逻辑

只有在**有序的那半边**,才能用 `nums[lo] <= target <= nums[hi]` 这种区间判断,因为只有有序时这种判断才准确。无序的那半边不能直接判断,要丢给下一轮二分继续处理。

##### 走一遍 `nums = [4,5,6,7,0,1,2]`, `target = 0`

| 步 | lo | hi | mid | nums[mid] | 哪边有序 | target 在哪边 | 动作 |
|---|---|---|---|---|---|---|---|
| 1 | 0 | 6 | 3 | 7 | `nums[0]=4 <= 7`,**左有序** | 0 不在 [4, 7),在右 | lo = 4 |
| 2 | 4 | 6 | 5 | 1 | `nums[4]=0 <= 1`,**左有序** | 0 在 [0, 1),在左 | hi = 4 |
| 3 | 4 | 4 | 4 | 0 | == target | - | **return 4** ✓ |

---

#### 6.7.3 LC 34:Find First and Last Position(找边界)

**题目特征**:
- 数组升序排序
- **可能有重复元素**
- 返回 target **第一次出现和最后一次出现的位置**
- 不存在返回 `[-1, -1]`

**例子**:
```python
nums = [5, 7, 7, 8, 8, 10]
target = 8
# 返回 [3, 4]
```

##### 为什么要分两步?

因为数组里可能有**多个 target**:
```
index:  0  1  2  3  4   5
nums:   5  7  7  8  8  10
                ^  ^
                3  4
```

普通二分(模板 1)找到 `8` 后,可能停在 index 3,也可能停在 4,**不能保证找到边界**。所以必须用**边界二分**(lower_bound / upper_bound)。

##### 思路:找两个边界

```
left  = 第一个 >= target 的位置  →  用 lower_bound
right = 最后一个 == target 的位置 →  用 upper_bound - 1
```

##### 为什么右边界是 `upper_bound - 1`?

`upper_bound(target)` 找的是**第一个 > target 的位置**,而**最后一个 == target 一定在它前一位**。

```
index:  0  1  2  3  4   5
nums:   5  7  7  8  8  10
                ^  ^   ^
                |  |   upper_bound(8) = 5
                |  最后一个 8 = 5 - 1 = 4
                lower_bound(8) = 3
```

##### 完整代码

```python
def searchRange(nums, target):
    def lower_bound(target):
        """第一个 >= target 的位置"""
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo
    
    def upper_bound(target):
        """第一个 > target 的位置"""
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] <= target:
                lo = mid + 1
            else:
                hi = mid
        return lo
    
    left = lower_bound(target)
    # 检查 target 不存在的情况
    if left == len(nums) or nums[left] != target:
        return [-1, -1]
    right = upper_bound(target) - 1
    return [left, right]
```

##### 为什么要判断 target 不存在?

**情况 1**:target 比所有元素都小或在数组中间但不存在
```python
nums = [5, 7, 7, 8, 8, 10], target = 6
lower_bound(6) → 1   # nums[1]=7,第一个 >= 6 的位置
# 但 nums[1]=7 ≠ 6,说明 6 不存在
```
所以判断:`if nums[left] != target: return [-1, -1]`

**情况 2**:target 比所有元素都大
```python
nums = [5, 7, 7, 8, 8, 10], target = 11
lower_bound(11) → 6   # = len(nums),数组里所有元素都 < 11
```
所以判断:`if left == len(nums): return [-1, -1]`

##### 进阶技巧:`lower_bound(target + 1) - 1` 替代 upper_bound

可以只用 lower_bound 一个函数完成:

```python
def searchRange(nums, target):
    def lower_bound(t):
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < t:
                lo = mid + 1
            else:
                hi = mid
        return lo
    
    left = lower_bound(target)
    if left == len(nums) or nums[left] != target:
        return [-1, -1]
    right = lower_bound(target + 1) - 1   # 第一个 >= target+1 的位置 - 1
    return [left, right]
```

**原理**:整数数组里,`第一个 > target` == `第一个 >= target+1`。

---

#### 6.7.4 三题模板选择对比

```python
# LC 704 标准二分:while lo <= hi
lo, hi = 0, len(nums) - 1
while lo <= hi:
    ...
    lo = mid + 1
    hi = mid - 1

# LC 33 旋转数组:while lo <= hi(也是找具体值)
lo, hi = 0, len(nums) - 1
while lo <= hi:
    if nums[mid] == target: return mid
    if 左半边有序:
        ...
    else:
        ...

# LC 34 找边界:while lo < hi(模板 2 + 3)
lo, hi = 0, len(nums)
while lo < hi:
    ...
    lo = mid + 1
    hi = mid       # 注意:不 -1
```

##### 一句话区分

- **找具体 target(任意一个)** → `while lo <= hi`,模板 1
- **找边界(第一个/最后一个满足条件)** → `while lo < hi`,模板 2/3

---

### 6.8 用一个通用模板搞定所有边界二分

如果你觉得记 lower_bound / upper_bound 太多,**只背一个最通用模板**也行。

#### 通用模板:找第一个满足条件的位置

```python
def first_true(arr):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if check(mid):              # mid 满足条件
            hi = mid                # mid 可能是答案,保留
        else:
            lo = mid + 1            # mid 不满足,排除
    return lo
```

**心法**:
- `check(mid) == True` → mid 可能是答案 → `hi = mid`
- `check(mid) == False` → mid 不可能是答案 → `lo = mid + 1`

最后 `lo == hi`,return lo 就是第一个满足 check 的位置。

#### 用通用模板写 lower_bound / upper_bound

```python
# lower_bound:第一个 >= target,所以 check(mid) = nums[mid] >= target
def lower_bound(nums, target):
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] >= target:     # 满足条件
            hi = mid
        else:
            lo = mid + 1
    return lo

# upper_bound:第一个 > target,所以 check(mid) = nums[mid] > target
def upper_bound(nums, target):
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > target:      # 满足条件
            hi = mid
        else:
            lo = mid + 1
    return lo
```

#### 各种"找最后一个"用减一就行

| 你要找什么 | 转换成什么 | 怎么写 |
|---|---|---|
| 第一个 >= target | first nums[i] >= target | `lower_bound(target)` |
| 第一个 > target | first nums[i] > target | `upper_bound(target)` |
| 最后一个 < target | 第一个 >= target 减 1 | `lower_bound(target) - 1` |
| 最后一个 <= target | 第一个 > target 减 1 | `upper_bound(target) - 1` |
| 第一个 == target | lower_bound(target) 后检查是否等于 | `lower_bound(target)` |
| 最后一个 == target | upper_bound(target) 减 1 后检查 | `upper_bound(target) - 1` |

**核心思想一句话**:

> **找"第一个满足条件"** → `hi = mid`(保留 mid)
> **找"最后一个满足条件"** → 转成"第一个不满足条件 - 1"

新手阶段先吃透 lower_bound / upper_bound 这两个,LC 34、插入位置、左右边界都顺了。

---

### 6.9 模板 4:二分答案(本质是 lower_bound)

**适用关键词**:最小速度、最小容量、最小天数、最大最小值、最小最大值、"is it possible"、"can / cannot"、"是否能完成"。

#### 经典题:LC 875 Koko Eating Bananas

题意:
- piles 是几堆香蕉,Koko 每小时吃 k 根,一堆没吃完下小时继续吃这堆
- 求最小 k,使得在 h 小时内吃完

```python
piles = [3, 6, 7, 11], h = 8
# 答案 k = 4(刚好 1+2+2+3 = 8 小时)
```

#### 为什么能二分?

**速度越大,越容易吃完**(单调性):
```
k=1 不行 / k=2 不行 / k=3 不行 / k=4 可以 / k=5 可以 / ...
       ↑ 前面 False,后面 True,找第一个 True
```

这就是 lower_bound 的变形!

#### 代码

```python
def min_eating_speed(piles, h):
    def can_finish(k):
        hours = 0
        for pile in piles:
            hours += (pile + k - 1) // k    # 向上取整,等价 math.ceil(pile / k)
        return hours <= h
    
    lo, hi = 1, max(piles)
    while lo < hi:
        mid = (lo + hi) // 2
        if can_finish(mid):
            hi = mid              # mid 可行,但还想找更小的,保留 mid
        else:
            lo = mid + 1          # mid 不行,排除
    return lo
```

**结构跟 lower_bound 一模一样**,只是把 `arr[mid] < target` 换成了 `not can_finish(mid)`。

#### 二分答案通用模板

```python
lo, hi = min_possible, max_possible
while lo < hi:
    mid = (lo + hi) // 2
    if check(mid):
        hi = mid                  # mid 可行,缩右边界(找更小的可行答案)
    else:
        lo = mid + 1              # mid 不可行,缩左边界
return lo
```

**心法**:
- `check(mid) = True` → mid 是可行答案,但**想找最小可行**,所以继续往左找(`hi = mid`,保留 mid)
- `check(mid) = False` → mid 太小,答案必须更大(`lo = mid + 1`,排除 mid)

---

### 6.10 区间定义:左闭右闭 vs 左闭右开

二分的两种"区间风格",**两种都对,关键是配套使用**。

| 风格 | 区间 | 初始化 | while 条件 | mid 不是答案 | mid 可能是答案 |
|---|---|---|---|---|---|
| **左闭右闭** | `[lo, hi]` | `hi = len(arr) - 1` | `while lo <= hi` | `lo = mid + 1` 或 `hi = mid - 1` | (不常用)|
| **左闭右开** | `[lo, hi)` | `hi = len(arr)` | `while lo < hi` | `lo = mid + 1` | `hi = mid` |

#### 怎么选?

| 目标 | 推荐风格 | 原因 |
|---|---|---|
| 找具体 target 是否存在 | 左闭右闭 | 找到立即返回,自然 |
| 找第一个 >= / > target(边界) | 左闭右开 | 答案可能是 `len(arr)`,自然 |
| 找最后一个 < / <= target | **左闭右闭 + ans 变量** | 见下面 6.10 |
| 二分答案 | 左闭右开思路 | 本质是 lower_bound |

---

### 6.11 找"最后一个满足条件":用 ans 变量

#### 为什么需要 ans?

找**最后一个满足条件**的位置时,看到一个满足的不能立即返回(右边可能还有),要先记录,继续往右找。

```python
def last_less_equal(arr, target):
    """找最后一个 <= target 的位置"""
    lo, hi = 0, len(arr) - 1
    ans = -1                          # 没找到默认 -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] <= target:
            ans = mid                 # mid 满足,先记录
            lo = mid + 1              # 继续往右找更靠后的
        else:
            hi = mid - 1
    return ans
```

#### 走一遍 `arr = [1, 2, 2, 2, 3, 4]`, `target = 2`

期望答案:3(最后一个 <= 2 的位置)

| 步 | lo | hi | mid | arr[mid] | 动作 | ans |
|---|---|---|---|---|---|---|
| 1 | 0 | 5 | 2 | 2 | <= 2,记录,lo = 3 | **2** |
| 2 | 3 | 5 | 4 | 3 | > 2,hi = 3 | 2 |
| 3 | 3 | 3 | 3 | 2 | <= 2,记录,lo = 4 | **3** |
| 结束 | 4 | 3 | - | - | - | **return 3** ✓ |

#### 也可以用 upper_bound - 1

更简洁的写法:

```python
def last_less_equal(arr, target):
    idx = upper_bound(arr, target) - 1
    return idx if idx >= 0 else -1
```

---

### 6.12 第一个 vs 最后一个:核心区别

`return lo` vs `return hi` **不是关键**,因为循环结束时 `lo == hi`。**关键是边界更新逻辑**:

```python
# 找第一个满足条件的:看到满足,往左收缩
if check(mid):
    hi = mid                     # 保留 mid,继续找左边
else:
    lo = mid + 1

# 找最后一个满足条件的:看到满足,记录后往右收缩
if check(mid):
    ans = mid
    lo = mid + 1                 # 继续找右边
else:
    hi = mid - 1
```

---

### 6.13 二分模板 4 + 1 总览(背这些)

#### 模板 1:找具体 target

```python
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target: return mid
        elif arr[mid] < target: lo = mid + 1
        else: hi = mid - 1
    return -1
```

#### 模板 2:lower_bound(第一个 >= target)

```python
def lower_bound(arr, target):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < target: lo = mid + 1
        else: hi = mid
    return lo
```

#### 模板 3:upper_bound(第一个 > target)

```python
def upper_bound(arr, target):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] <= target: lo = mid + 1
        else: hi = mid
    return lo
```

#### 模板 4:二分答案(找最小可行值)

```python
lo, hi = min_possible, max_possible
while lo < hi:
    mid = (lo + hi) // 2
    if check(mid): hi = mid
    else: lo = mid + 1
return lo
```

#### 模板 5:找最后一个满足条件(ans 风格)

```python
lo, hi = 0, len(arr) - 1
ans = -1
while lo <= hi:
    mid = (lo + hi) // 2
    if check(mid):
        ans = mid
        lo = mid + 1
    else:
        hi = mid - 1
return ans
```

---

### 6.14 决策速查表

| 题目类型 | 模板 |
|---|---|
| 数组里找 target 是否存在 | 模板 1 |
| 找第一个 >= target / 找插入位置 | 模板 2(lower_bound) |
| 找第一个 > target | 模板 3(upper_bound) |
| 找最后一个 == target | `upper_bound(arr, target) - 1` |
| 找最后一个 <= target | 模板 5,或 `upper_bound - 1` |
| 找最后一个 < target | 模板 5,或 `lower_bound - 1` |
| 最小速度/容量/天数(二分答案) | 模板 4 |
| 旋转数组找 target(LC 33) | 模板 1 + 判断哪半边有序 |

### 6.15 一句话记忆

```
mid 不可能是答案 → +1 / -1 排除
mid 可能是答案 → 保留(hi = mid)
找第一个满足:看到满足往左收
找最后一个满足:用 ans 记录再往右
```

---

## 七、Linked List(链表)

### 7.1 基础结构

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

链表 `1 -> 2 -> 3 -> None` 意思是:
- 节点 1 的 `next` 指向节点 2
- 节点 2 的 `next` 指向节点 3
- 节点 3 的 `next` 指向 `None`(链表结尾)

#### `ListNode(0)` 里的 0 是什么?

是**节点的 value**,**不是 index**。看类定义:

```python
class ListNode:
    def __init__(self, val=0, next=None):
```

所以 `dummy = ListNode(0)` 等价于:
```python
dummy.val = 0
dummy.next = None
```

**这个 0 不重要**,你写 `ListNode(-1)`、`ListNode(999)` 都行,因为最后 return 的是 `dummy.next`,dummy 自己不出现在结果里。

---

### 7.2 反转链表(必须能闭眼写)

```python
def reverse(head):
    prev, cur = None, head
    while cur:
        nxt = cur.next        # 1. 暂存下一个节点
        cur.next = prev       # 2. 反转当前节点的指针
        prev = cur            # 3. prev 前进
        cur = nxt             # 4. cur 前进
    return prev               # 新头 = 原尾
```

#### 7.2.1 完整走一遍 `1 -> 2 -> 3 -> None`

##### 初始状态
```
prev = None
cur  = 1

prev          cur
 ↓             ↓
None          1 -> 2 -> 3 -> None
```
状态:
- 已反转部分:None
- 待处理部分:1 -> 2 -> 3 -> None

##### 第 1 轮

**Step 1**: `nxt = cur.next` → nxt = 2
```
prev        cur       nxt
 ↓          ↓         ↓
None        1   ->    2 -> 3 -> None
```

**Step 2**: `cur.next = prev` → 把 1 的箭头反过来指向 None
```
prev        cur       nxt
 ↓          ↓         ↓
None  <-    1         2 -> 3 -> None
```
现在 1 已经是反转好的开头。

**Step 3 + 4**: `prev = cur`, `cur = nxt` → prev 移到 1,cur 移到 2
```
prev          cur
 ↓            ↓
1 -> None    2 -> 3 -> None
```

第 1 轮结束:已反转 `1 -> None`,待处理 `2 -> 3 -> None`。

##### 第 2 轮

**Step 1**: `nxt = 3`

**Step 2**: `cur.next = prev` → 让 2 指向 1
```
cur
 ↓
2 -> 1 -> None
```

**Step 3 + 4**: prev → 2, cur → 3
```
prev               cur
 ↓                  ↓
2 -> 1 -> None     3 -> None
```

第 2 轮结束:已反转 `2 -> 1 -> None`,待处理 `3 -> None`。

##### 第 3 轮

**Step 1**: `nxt = None`

**Step 2**: `cur.next = prev` → 3 指向 2
```
cur
 ↓
3 -> 2 -> 1 -> None
```

**Step 3 + 4**: prev → 3, cur → None
```
prev                    cur
 ↓                       ↓
3 -> 2 -> 1 -> None     None
```

##### 循环结束
`while cur` 检查 cur=None,退出。**返回 prev = 3**。

最终结果:`3 -> 2 -> 1 -> None` ✓

#### 7.2.2 四行代码记忆口诀

```python
nxt = cur.next       # 先存下一个,否则丢链
cur.next = prev      # 反转箭头
prev = cur           # prev 往前走
cur = nxt            # cur 往前走
```

> **先存下一个,再改箭头,然后 prev 和 cur 一起往前走。**

---

### 7.3 Dummy Node 技巧

#### 7.3.1 什么时候用 Dummy Node?

**当题目可能改变头节点时**,适合用 dummy。典型场景:
- 删除链表中某个节点(可能就是头节点)
- 删除倒数第 N 个节点
- 合并链表
- 反转部分链表

#### 7.3.2 Dummy 的作用

考虑删除链表第一个值为 1 的节点:
```
1 -> 2 -> 3 -> None
```

如果不用 dummy,删除头节点就要单独处理:
```python
if head.val == target:
    return head.next
# else 普通删除...
```
有点麻烦。

**用 dummy 之后:**
```python
dummy = ListNode(0)
dummy.next = head
prev = dummy
```

```
dummy -> 1 -> 2 -> 3 -> None
  ^
 prev
```

现在即使要删头节点,也能统一写:
```python
prev.next = prev.next.next
```

#### 7.3.3 完整例子:删除值为 target 的第一个节点

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

##### 走一遍:删除 target=2,链表 `1 -> 2 -> 3 -> None`

**初始**:
```
prev
 ↓
dummy -> 1 -> 2 -> 3 -> None
```

**第 1 次循环**:`prev.next.val = 1 ≠ 2`,prev 前进
```
       prev
        ↓
dummy -> 1 -> 2 -> 3 -> None
```

**第 2 次循环**:`prev.next.val = 2 == 2`,删除
```python
prev.next = prev.next.next
# 让 1.next 从 2 改成 3
```
```
dummy -> 1 -> 3 -> None
```

**break,返回** `dummy.next` = `1 -> 3 -> None` ✓

##### 走一遍:删除 target=1(头节点)

**初始**:`prev = dummy`,`prev.next = 1`,`1 == 1` → 直接删除
```python
prev.next = prev.next.next     # dummy.next 从 1 改成 2
```
```
dummy -> 2 -> 3 -> None
```

返回 `dummy.next` = `2 -> 3 -> None` ✓

**这就是 dummy 的好处:删除头节点不需要特殊处理。**

#### 7.3.4 为什么必须返回 `dummy.next` 而不是 `head`?

**因为删除的节点可能就是原来的 head**。如果原 head 被删了,变量 `head` 仍然指向旧节点,**但真正的新头已经是 `dummy.next`**。

```
原始: head → 1 → 2 → 3 → None
加 dummy: dummy → 1 → 2 → 3 → None
              ↑
             head 还指向 1

删除 1 后:
dummy → 2 → 3 → None     # 新链表
head → 1 → ...           # head 还指向旧节点 1!(只是 1 不再属于新链表)
```

所以:
- `return head` ❌ → 返回了旧头 1
- `return dummy.next` ✅ → 返回真正的新头 2

如果删除的是中间节点,`return head` 和 `return dummy.next` 结果一样。**但为了统一所有情况,永远写 `return dummy.next`**。

> **head 是原来的头,不一定还是新头。dummy.next 永远指向当前真正的头。**

#### 7.3.5 为什么需要 `while prev.next`?

因为我们不知道 target 在哪里,可能在头、中间、尾,或不存在。所以要一路检查每个节点。

`while prev.next` 的意思是:**只要 prev 后面还有节点,就继续检查**。

---

### 7.4 快慢指针找中点

```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
# slow 在中点(偶数长度时偏右)
```

**核心思想**:slow 走 1 步,fast 走 2 步。fast 到终点时,slow 正好走完一半。

#### 7.4.1 奇数长度走一遍 `1 -> 2 -> 3 -> 4 -> 5 -> None`

**初始**:`slow = fast = 1`

| 轮 | 进入循环判断 | 执行后 slow | 执行后 fast |
|---|---|---|---|
| 1 | fast=1, fast.next=2 ✓ | 2 | 3 |
| 2 | fast=3, fast.next=4 ✓ | 3 | 5 |
| 3 | fast=5, fast.next=None ✗ | 不进入 | 不进入 |

**最后 slow = 3**(中点) ✓

#### 7.4.2 偶数长度走一遍 `1 -> 2 -> 3 -> 4 -> None`

**初始**:`slow = fast = 1`

| 轮 | 判断 | slow | fast |
|---|---|---|---|
| 1 | fast=1, fast.next=2 ✓ | 2 | 3 |
| 2 | fast=3, fast.next=4 ✓ | 3 | None |
| 3 | fast=None ✗ | 不进入 | 不进入 |

**最后 slow = 3(偏右中点)**

```
1 -> 2 -> 3 -> 4
     左中  右中
            ↑
           slow
```

#### 7.4.3 关于循环条件的常见疑问

**Q: 为什么是 `while fast and fast.next`,而不是 `while fast`?**

因为下面要执行 `fast = fast.next.next`,**必须保证**:
- `fast` 不是 None(否则 `fast.next` 报错)
- `fast.next` 不是 None(否则 `fast.next.next` 报错)

**Q: 循环条件不满足后,会不会回退到上一轮的状态?**

**不会**。while 条件只决定"下一轮要不要开始",**不会撤销已经执行过的代码**。

执行流程:
```
判断 → (如果通过) 进入循环 → 执行循环体 → 循环体完成 → 再判断
```

某一轮已经把 `slow` 和 `fast` 移动了,即使下一轮条件不满足,也是停在当前位置,不会回退。

> **while 条件只决定"下一轮要不要开始",不会撤销上一轮已经执行过的代码。**

---

### 7.5 快慢指针应用:LC 141 / LC 142 环检测

快慢指针的另一个经典用途是**检测链表是否有环 + 找环入口**,这两题用的是同一个核心思想:**Floyd Cycle Detection(弗洛伊德判圈算法)**。

#### 7.5.1 题目区别

| | 问题 | 返回 |
|---|---|---|
| **LC 141** | 链表有没有环? | True / False |
| **LC 142** | 如果有环,环入口是哪个节点? | 入口节点 / None |

LC 142 是 LC 141 的进阶版,需要多做一步找环入口。

#### 7.5.2 什么是"链表有环"?

**普通链表**(无环,会到 None):
```
1 -> 2 -> 3 -> 4 -> None
```

**有环链表**(某节点 next 指回前面):
```
1 -> 2 -> 3 -> 4 -> 5
          ↑         ↓
          └─────────┘
```
这里 5.next = 3,链表永远走不到 None,会一直绕圈。

#### 7.5.3 LC 141:判断有没有环

##### 核心思想

**操场跑步直觉**:slow 走 1 步、fast 走 2 步。如果有环,fast 迟早**套圈追上 slow**;如果没环,fast 会先到 None。

##### 代码

```python
def hasCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True            # 相遇,有环
    return False                   # fast 到 None,无环
```

##### 走一遍(有环例子)

链表:
```
1 -> 2 -> 3 -> 4 -> 5
          ↑         ↓
          └─────────┘   (5.next = 3,环入口是 3)
```

| 轮 | slow | fast | 相遇? |
|---|---|---|---|
| 初始 | 1 | 1 | - |
| 1 | 2 | 3 | 否 |
| 2 | 3 | 5 | 否 |
| 3 | 4 | 4 | **是!return True** ✓ |

##### 复杂度
- 时间:O(n)
- 空间:O(1)(只用两个指针)

#### 7.5.4 LC 142:找环入口

##### 核心思想(分两步)

**Step 1**:跟 LC 141 一样,先用快慢指针找到**相遇点**。
**Step 2**:从 head 和相遇点**同时**出发,各走 1 步,**再次相遇的位置就是环入口**。

##### 为什么 Step 2 能找到入口?(数学结论,先记)

> 快慢指针相遇后,**slow 从相遇点到环入口的距离 = head 到环入口的距离**。
> 所以一个从 head 走、一个从相遇点走,每次走 1 步,会同时到达环入口。

直觉理解:fast 比 slow 多走的距离 = 环长的整数倍,这正好让两段距离同步抵消。**新手记结论就行,不必死推**。

##### 代码(推荐版本)

```python
def detectCycle(head):
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:               # 相遇了,开始找入口
            p1 = head
            p2 = slow                  # 相遇点
            while p1 != p2:
                p1 = p1.next
                p2 = p2.next
            return p1                  # 再次相遇 = 环入口
    
    return None                        # 没相遇,无环
```

**模式**:
- while 里面相遇就立刻处理并 return
- while 正常结束(fast 到 None)→ 没环,return None

##### 走一遍

链表:
```
1 -> 2 -> 3 -> 4 -> 5 -> 6
          ↑              ↓
          └──────────────┘   (6.next = 3,环入口是 3)
```

**Step 1: 快慢指针找相遇点**

假设第一次在节点 5 相遇(实际相遇点取决于环长度,但不影响算法)。

**Step 2: 找环入口**

```
p1 从 head=1 出发, p2 从 slow=5 出发,各走 1 步:

第 0 步:p1=1, p2=5
第 1 步:p1=2, p2=6
第 2 步:p1=3, p2=3   ← 相遇!返回节点 3 ✓
```

环入口正是节点 3。

#### 7.5.5 LC 142 三种写法对比

##### 写法 A:while-else 紧凑版(进阶语法)

```python
def detectCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None
    
    p1, p2 = head, slow
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next
    return p1
```

`while...else` 的意思:**循环正常结束(没被 break)才执行 else**。这里如果没相遇就走 else 返回 None。语法稍冷门。

##### 写法 B:flag 标志版(最直观)

```python
def detectCycle(head):
    slow = fast = head
    has_cycle = False
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cycle = True
            break
    
    if not has_cycle:
        return None
    
    p1, p2 = head, slow
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next
    return p1
```

新手友好,逻辑清晰,但代码长。

##### 写法 C:嵌套 return 版(推荐背这个)

```python
def detectCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            p1, p2 = head, slow
            while p1 != p2:
                p1 = p1.next
                p2 = p2.next
            return p1
    return None
```

**优点**:不用学 while-else 语法,也不用 flag,直接在相遇时处理并 return。

**记忆**:
> while 里面相遇就处理并 return;while 正常结束说明没环,return None。

#### 7.5.6 复杂度

| | LC 141 | LC 142 |
|---|---|---|
| 时间 | O(n) | O(n) |
| 空间 | O(1) | O(1) |

两题都只用几个指针,空间常数。

#### 7.5.7 总结对比

| | 核心 | 第一步 | 第二步 |
|---|---|---|---|
| LC 141 | 快慢指针相遇 = 有环 | slow=1,fast=2,看是否相遇 | - |
| LC 142 | 找环入口 | 快慢指针找相遇点 | 从 head 和相遇点同时走,再次相遇 = 入口 |

**记忆口诀**:
- **141**:相遇就有环,没相遇就到 None
- **142**:先找相遇点,再让 head 和相遇点一起走,再次相遇就是入口

---

### 7.6 合并两个有序链表

#### 7.6.1 两种 "merge" 的区别

| | 单纯拼接 | 按大小合并(LC 21) |
|---|---|---|
| 输入 | l1: 1→3→5, l2: 2→4→6 | 同左 |
| 输出 | 1→3→5→2→4→6 | 1→2→3→4→5→6 |
| 是否保持有序 | ❌ 不保证 | ✅ 保持升序 |
| 操作 | 找 l1 尾,接上 l2 | 每次比较两头取小的 |

LC 21 是后者:**两个升序链表合并成一个升序链表**。

#### 7.6.2 完整代码

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
    tail.next = l1 or l2          # 接上剩余的
    return dummy.next
```

#### 7.6.3 关键变量的角色

- **dummy**:假头节点,方便最后 return 新链表头
- **tail**:始终指向**新链表的最后一个节点**,负责往后接节点
- **l1 / l2**:**当前两个原链表"还没合并的部分的头"**(不是整条链表)

#### 7.6.4 走一遍 l1=1→3→5, l2=2→4→6

**初始**:
```
dummy/tail
    ↓
   [0] -> None

l1: 1 -> 3 -> 5 -> None
l2: 2 -> 4 -> 6 -> None
```

**第 1 轮**:比较 `l1.val=1` 和 `l2.val=2`,1 更小
- `tail.next = l1` → dummy 接上 1
- `l1 = l1.next` → l1 移到 3
- `tail = tail.next` → tail 移到 1

```
dummy -> 1 -> ...
          ↑
         tail
l1: 3 -> 5 -> None
l2: 2 -> 4 -> 6 -> None
```

**第 2 轮**:比较 3 和 2,2 更小
- `tail.next = l2` → 1 接上 2
- `l2 = l2.next` → l2 移到 4
- `tail = tail.next` → tail 移到 2

```
dummy -> 1 -> 2 -> ...
               ↑
              tail
l1: 3 -> 5 -> None
l2: 4 -> 6 -> None
```

**继续第 3-5 轮**(类似),最终:

```
dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> ...
                              ↑
                             tail
l1 = None
l2: 6 -> None
```

**退出循环**,执行 `tail.next = l1 or l2`:
- l1 = None, l2 = 6→None → `l1 or l2` 取 l2
- tail.next = l2 → 接上 6

```
dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
```

返回 `dummy.next` = `1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None` ✓

#### 7.6.5 关键代码逐句解析

##### `l1 = l1.next` 是什么意思?

**不是删除节点,而是让变量 l1 往后移动**。

```
l1 在 1
↓
1 -> 3 -> 5 -> None

执行 l1 = l1.next:
     l1 在 3
      ↓
1 -> 3 -> 5 -> None
```

意思是"节点 1 已经被处理(接到结果里了),下次比较 3"。

##### `tail = tail.next` 是什么意思?

**让结果链表的尾指针往后移动**,因为刚才接了新节点,新链表尾巴变了。

如果不更新 tail,下一轮还会从旧位置接,会把链表接乱。

##### 为什么循环条件是 `while l1 and l2`?

因为里面要比较 `l1.val < l2.val`。如果其中一个是 None,访问 `.val` 会报错。所以必须保证两边都不空。

##### `tail.next = l1 or l2` 在干什么?

退出循环后,**至少一个链表已经空了,但另一个可能还有剩余**。因为两个原链表本来就是有序的,**剩余部分整段直接接上**就行。

`l1 or l2` 表达式:
- l1 不空 → 返回 l1
- l1 空,l2 不空 → 返回 l2
- 两个都空 → 返回 None(也合法,等价于 `tail.next = None`)

三种情况都正确处理。

#### 7.6.6 跟数组合并对比

数组版:
```python
i, j = 0, 0
while i < len(a) and j < len(b):
    if a[i] < b[j]:
        res.append(a[i]); i += 1
    else:
        res.append(b[j]); j += 1
```

链表版本质一样,只是:

| 数组 | 链表 |
|---|---|
| `i += 1` | `l1 = l1.next` |
| `res.append(x)` | `tail.next = x; tail = tail.next` |

---

### 7.7 Dummy + 双指针应用:LC 19 删除倒数第 N 个节点

LC 19 是 dummy 和双指针的结合应用,**面试高频题**。

#### 7.7.1 题意

```python
head = 1 -> 2 -> 3 -> 4 -> 5 -> None
n = 2
# 删除倒数第 2 个节点 = 4
# 输出:1 -> 2 -> 3 -> 5 -> None
```

#### 7.7.2 核心思路

要删除一个节点,**关键是找到它的前一个节点**(因为删除靠 `prev.next = prev.next.next`)。

问题转化为:**怎么找到倒数第 n 个节点的前一个节点?**

**答案:双指针保持 n 距离**
- fast 从 `head` 出发,先走 n 步
- slow 从 `dummy` 出发(关键!)
- 然后两个一起走
- **fast 走到 None 时,slow 正好停在"要删除节点的前一个节点"**

#### 7.7.3 推荐代码

```python
def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head
    fast = head
    slow = dummy
    
    # Step 1: fast 先走 n 步
    for _ in range(n):
        fast = fast.next
    
    # Step 2: fast 和 slow 一起走,直到 fast 到 None
    while fast:
        fast = fast.next
        slow = slow.next
    
    # Step 3: 删除 slow 后面的节点
    slow.next = slow.next.next
    
    return dummy.next
```

#### 7.7.4 完整走一遍 `1→2→3→4→5`, n=2

##### 初始状态

```
slow
 ↓
dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> None
          ↑
        fast
```

注意:**slow = dummy, fast = head**(这是关键设计)。

##### Step 1: fast 先走 n=2 步

第 1 步:fast 到 2
```
dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> None
               ↑
             fast
```

第 2 步:fast 到 3
```
slow                   fast
 ↓                      ↓
dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> None
                    
注:此时 fast 在 3,slow.next 在 1,中间隔 n=2 个位置
```

##### Step 2: fast 和 slow 一起走

| 同步轮 | slow | fast | 检查 fast |
|---|---|---|---|
| 第 1 步 | 1 | 4 | ✓ 继续 |
| 第 2 步 | 2 | 5 | ✓ 继续 |
| 第 3 步 | 3 | None | **退出循环** |

走完后:
```
                  slow
                   ↓
dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> None
                                    ↑
                                  fast=None
```

**slow 正好停在 3,而 slow.next = 4(倒数第 2 个)** ✓

##### Step 3: 删除节点

```python
slow.next = slow.next.next
# 让 3.next 从 4 改成 5
```

结果:`dummy -> 1 -> 2 -> 3 -> 5 -> None`

返回 `dummy.next` = `1 -> 2 -> 3 -> 5 -> None` ✓

#### 7.7.5 关键设计:为什么 `slow = dummy`,不是 `slow = head`?

这是新手最容易混淆的点。**slow 的起点决定它最后停在哪里**。

##### 如果 `slow = head` 会怎样?

```python
fast = head
slow = head            # ❌
```

走一遍 `1→2→3→4→5, n=2`:

| 阶段 | slow | fast |
|---|---|---|
| 初始 | 1 | 1 |
| fast 走 2 步 | 1 | 3 |
| 同步 1 | 2 | 4 |
| 同步 2 | 3 | 5 |
| 同步 3 | **4** | None |

**slow 停在 4**(要删除的节点本身),但删除需要它的**前一个**节点 3,**位置错了!**

##### 用 `slow = dummy` 修正

dummy 比 head 提前一步,相当于把 slow 的最终位置**提前一格**,刚好停在"要删除节点的前一个"。

| 阶段 | slow | fast |
|---|---|---|
| 初始 | dummy | 1 |
| fast 走 2 步 | dummy | 3 |
| 同步 1 | 1 | 4 |
| 同步 2 | 2 | 5 |
| 同步 3 | **3** | None |

**slow 停在 3**(待删 4 的前一个) ✓

##### 一句话记忆

> **fast 从 head 开始负责制造 n 的距离;slow 从 dummy 开始,是为了最后停在"待删除节点的前一个节点"。**

#### 7.7.6 dummy 的另一个作用:处理删除头节点

考虑边界情况:

```python
head = 1 -> 2 -> 3 -> None
n = 3
# 倒数第 3 个 = 1(头节点),删除后应是 2 -> 3
```

走一遍:
- `slow = dummy, fast = head=1`
- fast 走 3 步:1→2→3→None,fast 已经是 None
- while 循环不进入
- slow 还在 dummy
- `slow.next = slow.next.next` → `dummy.next` 从 1 改成 2

返回 `dummy.next` = `2 -> 3 -> None` ✓

**没有 dummy 就要单独处理头节点删除,有了 dummy 统一一套逻辑搞定**。

#### 7.7.7 复杂度

| | |
|---|---|
| 时间 | O(L)(L 是链表长度,每个指针最多走一遍) |
| 空间 | O(1)(只用几个指针) |

注意是**一遍遍历**,不需要先算长度再走第二遍。

#### 7.7.8 另一种写法:fast 和 slow 都从 dummy 出发

也可以这样写,fast 多走一步(n+1):

```python
def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head
    fast = slow = dummy            # 两个都从 dummy
    for _ in range(n + 1):         # fast 走 n+1 步
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next
```

效果一样,但 `n + 1` 让新手稍绕。**推荐 7.7.3 那个版本**(`slow = dummy, fast = head, 走 n 步`)。

#### 7.7.9 一句话记忆

```
1. dummy 处理删除头节点
2. fast 先走 n 步,制造 n 距离
3. fast 和 slow 一起走,fast 到 None 时 slow 在待删前一个
4. slow.next = slow.next.next
5. return dummy.next
```

**核心**:**fast 先跑 n 步,slow 停在待删节点前一个**。

---

### 7.8 链表三大安全规则(常见坑)

#### 坑 1:修改 next 之前先暂存

反转链表里最容易踩。

```python
nxt = cur.next      # ✅ 先存
cur.next = prev     # 再改
```

如果直接 `cur.next = prev`,就把 `cur` 后面的链表全弄丢了,找不到后面的节点。

#### 坑 2:画图理解,不要硬推

像 `prev.next = prev.next.next` 这种,**一定画图**:

```
dummy -> 1 -> 2 -> 3 -> None
  ^
 prev

执行 prev.next = prev.next.next:
- prev.next 原来 = 1
- prev.next.next = 2
- 让 prev.next 直接指向 2
- 1 被跳过

结果:
dummy -> 2 -> 3 -> None
```

#### 坑 3:访问 `.next.next` 前先 null 检查

`fast.next.next` 这种代码很危险,必须先确保 fast 和 fast.next 都不是 None。

```python
# ❌ 危险
while fast:
    fast = fast.next.next

# ✅ 安全
while fast and fast.next:
    fast = fast.next.next
```

---

### 7.9 链表四大模板速记

#### 反转
```python
prev, cur = None, head
while cur:
    nxt = cur.next
    cur.next = prev
    prev = cur
    cur = nxt
return prev
```

#### Dummy + 删除/插入
```python
dummy = ListNode(0)
dummy.next = head
prev = dummy
# ... 操作 ...
return dummy.next
```

#### 快慢指针
```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

#### 合并(dummy + tail)
```python
dummy = ListNode(0)
tail = dummy
while l1 and l2:
    if l1.val < l2.val:
        tail.next = l1; l1 = l1.next
    else:
        tail.next = l2; l2 = l2.next
    tail = tail.next
tail.next = l1 or l2
return dummy.next
```

### 7.10 一句话记忆

```
反转:   先存下一个,改箭头,prev/cur 一起前进
Dummy:  假头方便统一处理,return dummy.next
快慢:   fast 走 2 步,slow 走 1 步,中点偏右
合并:   dummy 放头,tail 放尾,小的接后面
```

---

## 八、Stack(栈)

### 8.1 基础概念

**LIFO(后进先出,Last In First Out)**。想象一摞盘子,你只能从顶上拿。

Python 用 `list` 实现:`append()` 入栈,`pop()` 出栈,**两个操作都是 O(1)**。

### 8.2 基础模板

```python
stack = []
stack.append(x)               # push,O(1)
top = stack.pop()             # pop,删除并返回栈顶,O(1)
peek = stack[-1]              # 看栈顶但不弹出
is_empty = not stack          # 空检查(等价于 len(stack) == 0)
```

##### 三个方法的区别

```python
stack = ['(', '[']

# append:把元素放到栈顶
stack.append('{')             # ['(', '[', '{']

# stack[-1]:看栈顶,但不删除
print(stack[-1])              # '{'(栈还是 ['(', '[', '{']

# pop:删除并返回栈顶
top = stack.pop()             # 返回 '{',栈变成 ['(', '[']
```

### 8.3 经典题 1:LC 20 Valid Parentheses(括号匹配)

#### 8.3.1 题目

给一个只含 `( ) [ ] { }` 的字符串,判断括号是否合法。

```python
"()"        # 合法
"()[]{}"    # 合法
"{[]}"      # 合法
"(]"        # 不合法(左右不匹配)
"([)]"      # 不合法(顺序错)
"("         # 不合法(没闭合)
"]"         # 不合法(没开头)
```

#### 8.3.2 核心思路

**用 stack 存"还没被匹配的左括号"**:
- 遇到**左括号** → push 进栈
- 遇到**右括号** → 检查栈顶是不是对应的左括号
  - 是 → pop(匹配成功)
  - 不是 / 栈是空的 → return False
- 最后**栈为空** → 全部匹配,return True

为什么用栈?因为括号要求**后开先闭**(嵌套结构),最近开的左括号必须最先被闭合,这正是栈的 LIFO 特性。

#### 8.3.3 代码

```python
def isValid(s):
    stack = []
    pair = {')': '(', ']': '[', '}': '{'}
    
    for ch in s:
        if ch in pair:
            # ch 是右括号
            if not stack or stack[-1] != pair[ch]:
                return False
            stack.pop()
        else:
            # ch 是左括号
            stack.append(ch)
    
    return len(stack) == 0
```

#### 8.3.4 走一遍 `s = "{[]}"`

| ch | 类型 | 动作 | stack |
|---|---|---|---|
| 初始 | - | - | `[]` |
| `{` | 左 | push | `['{']` |
| `[` | 左 | push | `['{', '[']` |
| `]` | 右 | 栈顶是 `[`,匹配,pop | `['{']` |
| `}` | 右 | 栈顶是 `{`,匹配,pop | `[]` |

最后 stack 为空 → **return True** ✓

#### 8.3.5 走一遍不合法例子 `s = "([)]"`

| ch | 类型 | 动作 | stack |
|---|---|---|---|
| `(` | 左 | push | `['(']` |
| `[` | 左 | push | `['(', '[']` |
| `)` | 右 | 期待匹配 `(`,但栈顶是 `[` | **return False** ✗ |

不合法的核心:`(` 还没闭合,就来了 `)`,顺序乱了。

#### 8.3.6 为什么最后要 `return len(stack) == 0`?

考虑 `"((("`:
- 全部 push,stack = `['(', '(', '(']`
- 没有右括号来匹配
- 如果直接 `return True` 就错了

所以**最后必须检查栈是否为空**(所有左括号都被匹配了)。

#### 8.3.7 复杂度

- 时间:O(n)
- 空间:O(n)(最坏情况栈存所有字符)

---

### 8.4 经典题 2:LC 739 Daily Temperatures(单调栈)

#### 8.4.1 题目

给一个温度数组,**每一天要等多少天才能等到更高温度**。如果之后没有更高的,填 0。

```python
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
# 答案:    [ 1,  1,  4,  2,  1,  1,  0,  0]
```

解释:
- 第 0 天 73 → 第 1 天就更高,等 **1** 天
- 第 1 天 74 → 第 2 天更高,等 **1** 天
- 第 2 天 75 → 要等到第 6 天 76,等 **4** 天
- 第 3 天 71 → 第 5 天 72 更高,等 **2** 天
- ...

#### 8.4.2 暴力解法(先理解,再优化)

最直观的写法:对每天往后扫,找第一个更高的。

```python
def dailyTemperatures(temperatures):
    n = len(temperatures)
    ans = [0] * n
    for i in range(n):
        for j in range(i + 1, n):           # 从 i+1 扫到末尾
            if temperatures[j] > temperatures[i]:
                ans[i] = j - i
                break                       # 找到了就停,不再继续
    return ans
```

##### 关于 `range(i + 1, n)`(`range` 用法补充)

`range(start, end)` 是**左闭右开**:
- 包含 `start`
- **不包含** `end`

所以 `range(i + 1, n)` 包含 `i+1, i+2, ..., n-1`,**不包含 n**。

例如:
```python
i = 2, n = 6
for j in range(i + 1, n):   # range(3, 6)
    print(j)
# 输出 3, 4, 5(不含 6)
```

##### 关于 `range(start, end, step)` 第三个参数

`range` 还有第三个参数 `step`(步长):

```python
range(0, 10, 2)     # 0, 2, 4, 6, 8(不含 10)
range(1, 10, 3)     # 1, 4, 7
range(10, 0, -2)    # 10, 8, 6, 4, 2(倒着走)
```

不写 step 默认是 1(每次 +1)。

##### 关于内层循环里的 `break`

`break` **只跳出离它最近的一层循环**(这里是内层 `for j`)。然后会回到外层 `for i` 继续下一个 `i`。

```python
for i in range(n):
    for j in range(i + 1, n):
        if temperatures[j] > temperatures[i]:
            ans[i] = j - i
            break                  # ← 只跳出 for j
    # ← break 跳到这里,继续 for i 的下一个 i
```

如果想跳出两层循环,需要 flag 或 return,直接 `break` 不够。

##### 暴力解法复杂度

- **时间**:O(n²)(最坏每个 i 都扫完后面所有元素)
- **空间**:O(n)(`ans` 数组),如果不算 `ans` 是 O(1)

n 大时(比如 n=10⁵)会超时。

#### 8.4.3 单调栈优化:O(n) 解法

##### 关键洞察

暴力解法重复做了很多无效检查。其实可以**让每个值只入栈一次、出栈一次**,总共 O(n)。

##### 思路

**stack 里存"还没找到更高温度的那些天的下标"**(注意是下标,不是温度本身)。

为什么存下标?因为答案要算 `当前天 - 之前天 = i - prev_index`,需要下标信息。

每天的处理逻辑:
1. 看当前温度 `temp` 比栈顶那一天的温度高吗?
2. 如果高 → 栈顶那天**找到答案了**,pop 出来,记录答案
3. 重复 2,直到栈顶温度 ≥ 当前温度(或栈空)
4. 把当前下标 push 进栈(它还没找到更高的)

##### 代码

```python
def dailyTemperatures(temperatures):
    n = len(temperatures)
    ans = [0] * n
    stack = []                              # 存下标
    
    for i, temp in enumerate(temperatures):
        while stack and temp > temperatures[stack[-1]]:
            prev_index = stack.pop()
            ans[prev_index] = i - prev_index
        stack.append(i)
    
    return ans
```

#### 8.4.4 完整走一遍 `temperatures = [73, 74, 75, 71, 69, 72, 76, 73]`

| i | temp | 操作 | stack(存下标) | 对应温度 | ans 变化 |
|---|---|---|---|---|---|
| 0 | 73 | 栈空,直接 push | `[0]` | 73 | - |
| 1 | 74 | 74 > 73,pop 0,ans[0] = 1 - 0 = 1;再 push | `[1]` | 74 | `[1, 0, 0, 0, 0, 0, 0, 0]` |
| 2 | 75 | 75 > 74,pop 1,ans[1] = 2 - 1 = 1;再 push | `[2]` | 75 | `[1, 1, 0, 0, 0, 0, 0, 0]` |
| 3 | 71 | 71 < 75,直接 push | `[2, 3]` | 75, 71 | - |
| 4 | 69 | 69 < 71,直接 push | `[2, 3, 4]` | 75, 71, 69 | - |
| 5 | 72 | **连续 pop**:72>69 pop 4(ans[4]=1),72>71 pop 3(ans[3]=2),72<75 停;push | `[2, 5]` | 75, 72 | `[1, 1, 0, 2, 1, 0, 0, 0]` |
| 6 | 76 | **连续 pop**:76>72 pop 5(ans[5]=1),76>75 pop 2(ans[2]=4);push | `[6]` | 76 | `[1, 1, 4, 2, 1, 1, 0, 0]` |
| 7 | 73 | 73 < 76,直接 push | `[6, 7]` | 76, 73 | - |

循环结束,stack 里剩下 `[6, 7]`,这两天后面没有更高温度,**ans 保持 0** ✓

最终:`[1, 1, 4, 2, 1, 1, 0, 0]`

#### 8.4.5 为什么叫"单调栈"?

**因为 stack 里对应的温度从栈底到栈顶是递减的**(单调递减)。

观察走表过程,某一刻栈是 `[2, 3, 4]`,温度对应 `75, 71, 69`,严格递减。

当来一个更高温度,它就**像扫地机一样**把比它低的全部清出去,直到遇到不低于它的为止。

#### 8.4.6 为什么是 `while` 不是 `if`?

因为**当前温度可能同时解决多个之前的天**。

比如栈里是 `[75, 71, 69]`,来了个 72:
- 72 > 69 → 解决第 4 天
- 72 > 71 → 解决第 3 天
- 72 < 75 → 不能解决第 2 天,停

所以要**一直 pop**,不能只 pop 一次。

#### 8.4.7 复杂度分析(为什么是 O(n) 不是 O(n²)?)

虽然有 while 嵌套在 for 里,但**每个下标最多入栈一次、出栈一次**:
- 入栈次数:n 次(每个下标只入一次)
- 出栈次数:最多 n 次

总操作次数 = 2n,**时间复杂度 O(n)**。

空间复杂度 O(n)(最坏栈装下所有下标,比如严格递减的输入)。

---

### 8.5 两题对比

| 题目 | stack 类型 | stack 里存什么 | 什么时候 pop |
|---|---|---|---|
| **LC 20 括号匹配** | 普通栈 | 还没被匹配的左括号 | 遇到能匹配的右括号 |
| **LC 739 单调栈** | 单调递减栈 | 还没找到更高温度的下标 | 当前温度 > 栈顶温度 |

**核心思想**:
- **LC 20**:括号配对,栈顶必须匹配
- **LC 739**:找下一个更大值,**当前值负责解决之前比它小的值**

### 8.6 用途总结

栈在面试里的三大用途:
1. **括号 / 表达式解析**(LC 20、LC 150 逆波兰式)
2. **单调栈**(找下一个更大/小元素:LC 739、LC 496、LC 84)
3. **DFS 迭代版**(替代递归调用栈)

### 8.7 一句话记忆

```
LC 20:左括号入栈,右括号匹配栈顶。
LC 739:单调递减栈,当前值比栈顶大就 pop,记录"等了几天"。
单调栈精髓:每个元素只入栈一次、出栈一次 → O(n)。
```

---

## 九、Queue(队列)

### 9.1 基础概念

**FIFO(先进先出)**。**用 `collections.deque`,不要用 list**(`list.pop(0)` 是 O(n))。

### 9.2 模板

```python
from collections import deque
q = deque()
q.append(x)                   # 入队
x = q.popleft()               # 出队,O(1)
peek = q[0]                   # 看队首

# deque 还能两头操作
q.appendleft(x)               # 左侧入
q.pop()                       # 右侧出
```

### 9.3 用途

- BFS 必备
- 滑动窗口最大值(单调队列,LC 239)

---

## 十、Binary Tree(二叉树)

### 10.1 基础结构

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

每个节点有 `val`、`left`、`right`。叶子节点的 `left = right = None`。

### 10.2 二叉树通用思考方式

每次看到二叉树题,先问自己 **3 个问题**:

1. **当前节点为空时,返回什么?**(base case)
2. **我要从左子树和右子树分别拿到什么?**(子问题)
3. **当前节点要如何合并左右子树的结果?**(合并)

举例:LC 104 最大深度
1. 空节点返回 0
2. 左右子树返回各自深度
3. 当前返回 `max(left, right) + 1`

举例:LC 543 直径
1. 空节点返回 0
2. 左右子树返回各自深度
3. 当前用 `left + right` 更新全局答案,返回 `max(left, right) + 1` 给父节点

> **二叉树递归 = 左子树答案 + 右子树答案 + 当前节点处理**

---

### 10.3 三种遍历(递归版)

```python
def preorder(node):           # 前序:根→左→右
    if not node: return
    print(node.val)           # 1. 处理当前
    preorder(node.left)       # 2. 处理左
    preorder(node.right)      # 3. 处理右

def inorder(node):            # 中序:左→根→右
    if not node: return
    inorder(node.left)
    print(node.val)
    inorder(node.right)

def postorder(node):          # 后序:左→右→根
    if not node: return
    postorder(node.left)
    postorder(node.right)
    print(node.val)
```

#### 三种遍历用途

| 遍历 | 顺序 | 适合的题 |
|---|---|---|
| **前序** | 根→左→右 | "先处理自己再处理孩子"(如 LC 226 翻转树) |
| **中序** | 左→根→右 | **BST 中序遍历得到升序序列**(LC 98、LC 230) |
| **后序** | 左→右→根 | "先知道孩子结果再处理自己"(如 LC 104 深度、LC 543 直径) |

#### LC 144 / 94 / 145 标准模板

```python
def preorderTraversal(root):
    res = []
    def dfs(node):
        if not node: return
        res.append(node.val)
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return res
# 中序:把 res.append 移到两个 dfs 中间
# 后序:把 res.append 移到两个 dfs 后面
```

---

### 10.4 层序遍历 BFS(LC 102)

#### 10.4.1 题目

二叉树:
```
      3
     / \
    9   20
       /  \
      15   7
```
输出:`[[3], [9, 20], [15, 7]]`(每层一个 list)

#### 10.4.2 代码

```python
from collections import deque

def levelOrder(root):
    if not root: return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        size = len(queue)              # 关键:固定当前层节点数
        for _ in range(size):
            node = queue.popleft()
            level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    return result
```

#### 10.4.3 queue 里存什么?

**存 TreeNode 节点对象**,**不是 `node.val`**。

因为我们不仅需要值 `node.val`,还要继续访问 `node.left` 和 `node.right`。

#### 10.4.4 走一遍

树:
```
      3
     / \
    9   20
       /  \
      15   7
```

**初始**:`queue = [3]`, `result = []`

**第 1 层**(进入 while 循环):
- `size = 1`(只有节点 3)
- 处理 3:加入 level,加入孩子 9 和 20
- queue 变成 `[9, 20]`,level = `[3]`
- `result = [[3]]`

**第 2 层**:
- `size = 2`
- 处理 9:level=[9],9 没孩子
- 处理 20:level=[9,20],加入孩子 15, 7
- queue 变成 `[15, 7]`
- `result = [[3], [9, 20]]`

**第 3 层**:
- `size = 2`
- 处理 15、7,都是叶子
- queue 变空
- `result = [[3], [9, 20], [15, 7]]` ✓

#### 10.4.5 为什么用 BFS 不用 DFS?

**层序要"从上到下、从左到右、一层一层"处理**。
- DFS 是沿一条路一路深入,不天然按层
- BFS 用队列,**先进先出 = 同层节点一起处理** = 层序

#### 10.4.6 为什么必须 `size = len(queue)`?

进入第 2 层时,queue 是 `[9, 20]`(2 个节点)。但处理它们时会往 queue 加 `15, 7`,**这俩属于下一层,不能算进当前层**。

`size = len(queue)` **冻结**当前层节点数,for 循环只跑这么多次。

#### 10.4.7 为什么用 `deque` 不用 list?

- `list.pop(0)` 是 **O(n)**(头部删除要移动所有元素)
- `deque.popleft()` 是 **O(1)**

BFS 必须用 `from collections import deque`,否则总复杂度从 O(n) 退化到 O(n²)。

---

### 10.5 经典题:递归处理当前节点 + 左右子树

#### 10.5.1 LC 104 Maximum Depth(模板入门)

```python
def maxDepth(root):
    if not root:
        return 0
    left = maxDepth(root.left)
    right = maxDepth(root.right)
    return max(left, right) + 1
```

##### 为什么 `left` 和 `right` 是左右子树的最大深度?

**因为 `maxDepth()` 函数本身就被定义为"返回以这个节点为根的最大深度"**。

```python
left = maxDepth(node.left)        # 左子树的最大深度
right = maxDepth(node.right)      # 右子树的最大深度
```

##### 走一遍

树:
```
      1
     /
    2
   / \
  4   5
```

- `maxDepth(4)` = `max(0, 0) + 1` = **1**
- `maxDepth(5)` = `max(0, 0) + 1` = **1**
- `maxDepth(2)` = `max(1, 1) + 1` = **2**
- `maxDepth(1)` = `max(2, 0) + 1` = **3**

#### 10.5.2 LC 226 Invert Binary Tree(翻转)

##### DFS 递归版(前序)

```python
class Solution:
    def invertTree(self, root):
        if not root:
            return None
        root.left, root.right = root.right, root.left      # 中:交换左右
        self.invertTree(root.left)                          # 左
        self.invertTree(root.right)                         # 右
        return root
```

这是 **DFS + 前序**(中→左→右)。

##### BFS 层序版

```python
from collections import deque

class Solution:
    def invertTree(self, root):
        if not root:
            return root
        queue = deque([root])
        while queue:
            cur = queue.popleft()
            cur.left, cur.right = cur.right, cur.left
            if cur.left: queue.append(cur.left)
            if cur.right: queue.append(cur.right)
        return root
```

##### BFS vs DFS 区别

| | 用什么数据结构 | 处理顺序 |
|---|---|---|
| **BFS** | queue | 一层一层 |
| **DFS(递归)** | 系统调用栈 | 沿一条路径深入 |
| **DFS(迭代)** | stack | 同 DFS |

> **用 queue 一层一层处理 = BFS;用 recursion 或 stack 往深处走 = DFS**

#### 10.5.3 LC 100 Same Tree(两棵树一起递归)

```python
def isSameTree(p, q):
    if not p and not q:           # 都空 → 相同
        return True
    if not p or not q:            # 一空一不空 → 不同
        return False
    if p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
```

**思路**:两棵树相同 = 当前节点值相同 AND 左子树相同 AND 右子树相同。

#### 10.5.4 LC 101 Symmetric Tree(镜像递归)

```python
def isSymmetric(root):
    if not root:
        return True
    def mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        # 关键:左树的左 vs 右树的右,左树的右 vs 右树的左
        return mirror(left.left, right.right) and mirror(left.right, right.left)
    return mirror(root.left, root.right)
```

**核心**:镜像对称 = **左树的左 == 右树的右**,**左树的右 == 右树的左**。

---

### 10.6 return + 全局变量 pattern(LC 543 详解)

这是二叉树进阶题最重要的 pattern,**LC 543、LC 124、LC 687 都用**。

#### 10.6.1 LC 543 题目

求二叉树**直径**(任意两节点之间最长路径的边数)。

例:
```
      1
     / \
    2   3
   / \
  4   5
```
最长路径:`4 → 2 → 1 → 3`(3 条边),答案 = **3**。

#### 10.6.2 关键洞察:深度 ≠ 直径

`depth(node)` 函数返回的是**深度**,但题目要的是**直径**。这两个量**不同**,所以需要:
- 内部递归 `depth(node)` 返回**深度**
- 外部 `ans` 变量记录**全局最大直径**

##### 为什么深度和直径不同?

经过当前节点的最长路径:
```
左子树最深节点 → 当前节点 → 右子树最深节点
```
长度 = `left + right`(经过当前节点的直径)

但**返回给父节点的不能是 `left + right`**,因为父节点往下走只能选**一条路**:
```
父 → 当前 → 左边一路    或    父 → 当前 → 右边一路
```
不能左右都走。所以返回给父节点的是 `max(left, right) + 1`(深度)。

#### 10.6.3 推荐写法(self.ans 版)

```python
class Solution:
    def diameterOfBinaryTree(self, root):
        self.ans = 0
        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            self.ans = max(self.ans, left + right)    # 更新全局直径
            return max(left, right) + 1                # 返回给上层是深度
        depth(root)
        return self.ans
```

#### 10.6.4 走一遍 `[1, 2, 3, 4, 5]` 树

```
      1
     / \
    2   3
   / \
  4   5
```

| 节点 | left | right | 经过此节点直径 (left+right) | self.ans 更新后 | 返回(深度) |
|---|---|---|---|---|---|
| 4 | 0 | 0 | 0 | 0 | 1 |
| 5 | 0 | 0 | 0 | 0 | 1 |
| 2 | 1 | 1 | 2 | **2** | 2 |
| 3 | 0 | 0 | 0 | 2 | 1 |
| 1 | 2 | 1 | 3 | **3** | 3 |

最终 `self.ans = 3` ✓

#### 10.6.5 self.ans vs nonlocal ans 写法对比

##### 写法 A:用 `self.ans`(LeetCode 推荐)

```python
class Solution:
    def diameterOfBinaryTree(self, root):
        self.ans = 0
        def depth(node):
            ...
            self.ans = max(self.ans, left + right)   # 不需要 nonlocal
```

##### 写法 B:用 `nonlocal ans`

```python
def diameterOfBinaryTree(root):
    ans = 0
    def depth(node):
        nonlocal ans                                  # 必须加 nonlocal
        ...
        ans = max(ans, left + right)
    depth(root)
    return ans
```

##### 为什么 `ans` 需要 `nonlocal`,但 `result.append()` 不需要?

**关键区别**:**重新赋值** vs **修改对象内容**。

```python
ans = max(ans, x)           # 重新赋值 → Python 默认认为 ans 是局部变量
                            # 必须 nonlocal 才能改外层

result.append(x)            # 修改 list 内容,result 还是原来那个对象
                            # 不需要 nonlocal
```

整数 `int` 不可变,只能重新赋值,所以必须 nonlocal。
list 可变,append 不是赋值,所以不用 nonlocal。

| 写法 | 是否需要 nonlocal/self | 原因 |
|---|---|---|
| `result.append(x)` | 不需要 | 修改 list 内容,不是重新赋值 |
| `ans = max(ans, x)` | 需要 `nonlocal ans` | 重新赋值 |
| `self.ans = max(self.ans, x)` | 不需要 nonlocal | 修改对象属性 |

**新手建议**:在 LeetCode class 里就用 **`self.ans`**,不用学 nonlocal。

---

### 10.7 BST(Binary Search Tree)

#### 10.7.1 BST 三大特性

1. **左子树所有值 < 根 < 右子树所有值**(严格)
2. **中序遍历得到升序序列**(BST 标志)
3. 查找/插入/删除平均 O(log n)(平衡时)

#### 10.7.2 LC 700 Search in BST

##### 推荐递归写法

```python
class Solution:
    def searchBST(self, root, val):
        if not root or root.val == val:
            return root
        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
```

**核心**:BST 搜索**只走一边**,所以直接 `return self.searchBST(...)`,不需要变量接收。

##### 常见错误写法

```python
# ❌ 错误
if val < root.val:
    left = self.searchBST(root.left, val)
if val > root.val:
    right = self.searchBST(root.right, val)
return left and right       # 报错:left 或 right 可能未定义
```

**两个问题**:
1. 进入第一个 if 后,`right` 没定义,最后 `return left and right` 会报错
2. **BST 只去一边**,不需要 `left and right`

##### 迭代写法(也很推荐)

```python
class Solution:
    def searchBST(self, root, val):
        while root:
            if val < root.val:
                root = root.left
            elif val > root.val:
                root = root.right
            else:
                return root
        return None
```

> **BST 搜索只走一边,所以递归时直接 return 左边或右边的搜索结果。**

#### 10.7.3 LC 98 Validate BST

##### 新手常犯错

只比较当前节点和它的左右孩子是**不够的**:
```python
# ❌ 不够
root.left.val < root.val < root.right.val
```

为什么?考虑:
```
      5
     / \
    3   7
       /
      4
```
`4 < 7` 满足局部 BST,但 `4` 在 `5` 的右子树,**必须 > 5**,实际 `4 < 5`,不合法。

##### 正确做法:给每个节点传范围

```python
def isValidBST(root):
    def dfs(node, low, high):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        # 左子树值都 < node.val
        # 右子树值都 > node.val
        return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
    return dfs(root, float("-inf"), float("inf"))
```

##### 两个 return 的含义

```python
return dfs(root, float("-inf"), float("inf"))     # 外层
```
意思:从根开始检查,初始范围是 (-∞, +∞)。

```python
return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)    # 内层
```
意思:**左子树合法 AND 右子树合法**,两个都满足才合法。

##### 为什么左子树范围是 `(low, node.val)`?

BST 规则:左子树所有值 < 当前节点。所以左子树的**上限**变成 `node.val`(原来的 high 也保留作为外层约束)。

##### 为什么右子树范围是 `(node.val, high)`?

右子树所有值 > 当前节点。所以右子树的**下限**变成 `node.val`。

##### 走一遍合法 BST `[5, 3, 7]`

```
      5
     / \
    3   7
```

- `dfs(5, -inf, inf)`:`-inf < 5 < inf` ✓
  - 左:`dfs(3, -inf, 5)`:`-inf < 3 < 5` ✓ → True
  - 右:`dfs(7, 5, inf)`:`5 < 7 < inf` ✓ → True
- 返回 `True and True` = **True** ✓

##### 走一遍不合法 `[5, 3, 7, null, null, 4]`

```
      5
     / \
    3   7
       /
      4
```

- `dfs(5, -inf, inf)`:`5` 合法
  - 右:`dfs(7, 5, inf)`:`7` 合法
    - 左:`dfs(4, 5, 7)`:**`5 < 4 < 7` 失败!** → return False
- 整体返回 **False** ✓

> **`dfs(node, low, high)` 的含义:检查以 node 为根的子树,所有节点值是否都在 (low, high) 之间。**

---

### 10.8 LeetCode 中的 self 和递归调用

#### 10.8.1 三种写法的区别

##### 写法 A:class 里的方法,递归用 `self.xxx`

```python
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        left = self.maxDepth(root.left)        # 用 self
        right = self.maxDepth(root.right)
        return max(left, right) + 1
```

`maxDepth` 是 `Solution` 类的方法,递归调用必须 `self.maxDepth(...)`。

##### 写法 B:普通函数,不用 self

```python
def maxDepth(root):
    if not root:
        return 0
    left = maxDepth(root.left)                 # 直接调用
    right = maxDepth(root.right)
    return max(left, right) + 1
```

不在 class 里,直接 `maxDepth(...)`。

##### 写法 C:class 里写 helper 内部函数(推荐)

```python
class Solution:
    def maxDepth(self, root):
        def dfs(node):                          # 内部函数
            if not node:
                return 0
            left = dfs(node.left)               # 不用 self
            right = dfs(node.right)
            return max(left, right) + 1
        return dfs(root)
```

`dfs` 是 `maxDepth` 内部的局部函数,**不是类方法**,所以**不用 self**。

#### 10.8.2 一句话记

```
class 里和题目函数同级缩进的函数 → 需要 self,递归用 self.xxx
class 里写的 helper 内部函数 → 不需要 self
完全独立的函数 → 不需要 self
```

#### 10.8.3 推荐对新手最友好的写法

**Helper 函数版**(写法 C),理由:
- 不用纠结 self
- 内部状态(如 `self.ans` 或 `nonlocal ans`)更清晰
- 适合 LC 543、LC 124 这类需要全局变量的题

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

---

### 10.9 推荐刷题顺序

#### 必做(覆盖核心 pattern,优先级 ⭐⭐⭐)

| 题号 | 题目 | 用什么 pattern |
|---|---|---|
| **LC 104** | Maximum Depth | 递归基本模板 |
| **LC 226** | Invert Binary Tree | DFS 前序 / BFS |
| **LC 102** | Level Order Traversal | BFS 层序 |
| **LC 543** | Diameter of Binary Tree | return + 全局变量 |
| **LC 100** | Same Tree | 双树递归 |
| **LC 101** | Symmetric Tree | 镜像递归 |

#### 推荐(进阶,⭐⭐)

| 题号 | 题目 | 用什么 |
|---|---|---|
| **LC 144 / 94 / 145** | 三种遍历 | 递归基本功 |
| **LC 700** | Search in BST | BST 单边搜索 |
| **LC 98** | Validate BST | 范围递归 |
| **LC 110** | Balanced Binary Tree | 递归剪枝 |

#### 进阶(⭐)

| 题号 | 题目 | 用什么 |
|---|---|---|
| **LC 124** | Binary Tree Max Path Sum | LC 543 进阶 |
| **LC 236** | Lowest Common Ancestor | LCA 经典 |
| **LC 230** | Kth Smallest in BST | 中序遍历应用 |

### 10.10 一句话记忆

```
二叉树递归 = 左子树答案 + 右子树答案 + 当前节点处理
深度 = max(left, right) + 1
直径 = left + right(更新全局),返回深度给父节点
BST 中序遍历 = 升序序列
BST 验证 = 给每个节点传 (low, high) 范围
BFS 用 queue 一层层,DFS 用递归/stack 走深路
```

---

## 十一、Recursion / Divide & Conquer(递归 / 分治)

### 11.1 递归三要素

1. **Base case**(递归终点)
2. **递归调用**(子问题)
3. **合并结果**

### 11.2 通用模板

```python
def recurse(input):
    # 1. base case
    if input is trivial:
        return base_result
    
    # 2. 分解 + 子问题
    sub_result1 = recurse(smaller_part_1)
    sub_result2 = recurse(smaller_part_2)
    
    # 3. 合并
    return combine(sub_result1, sub_result2)
```

### 11.3 分治法经典:Merge Sort

```python
def mergeSort(arr):
    if len(arr) <= 1: return arr        # base
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])         # 分
    right = mergeSort(arr[mid:])
    return merge(left, right)           # 治

def merge(a, b):
    res, i, j = [], 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            res.append(a[i]); i += 1
        else:
            res.append(b[j]); j += 1
    res.extend(a[i:])
    res.extend(b[j:])
    return res
```

### 11.4 易错点

- **忘记 base case** → 无限递归 / Stack Overflow
- **递归参数没在缩小** → 死循环
- **返回值用错**(`return` 在某个分支漏了)

---

## 十二、Graph(图)

### 12.1 表示方式

#### 邻接表(常用)

```python
from collections import defaultdict
graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)        # 无向图加两次,有向图只加一次
```

#### 邻接矩阵

```python
graph = [[0]*n for _ in range(n)]
graph[i][j] = 1               # i→j 有边
```

### 12.2 BFS 模板(求最短路径)

```python
from collections import deque

def bfs(graph, start, target):
    visited = {start}
    queue = deque([start])
    steps = 0
    while queue:
        steps += 1
        size = len(queue)
        for _ in range(size):
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in visited:
                    if neighbor == target:
                        return steps
                    visited.add(neighbor)
                    queue.append(neighbor)
    return -1
```

### 12.3 DFS 模板

#### 递归版

```python
def dfs(node, visited):
    if node in visited: return
    visited.add(node)
    # 处理 node
    for neighbor in graph[node]:
        dfs(neighbor, visited)
```

#### 迭代版(只比 BFS 改一个字)

```python
def dfs(start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()    # ← 跟 BFS 唯一区别:pop() 不是 popleft()
        if node in visited: continue
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)
```

### 12.4 网格 DFS(LC 200)

```python
def dfs(r, c):
    if (r < 0 or r >= rows or c < 0 or c >= cols 
        or (r, c) in visited or grid[r][c] == '0'):
        return
    visited.add((r, c))
    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:  # 四方向
        dfs(r + dr, c + dc)
```

### 12.5 复杂度对比

| | 邻接表 | 邻接矩阵 |
|---|---|---|
| 空间 | O(V+E) | O(V²) |
| BFS/DFS 时间 | O(V+E) | O(V²) |

### 12.6 关键决策

- **求最短路径** → BFS
- **求可达性 / 连通块** → DFS 或 BFS 都行
- **拓扑排序 / 环检测** → DFS 或 BFS

### 12.7 邻接矩阵下的 BFS/DFS 复杂度推导

**为什么是 O(V²)?**
- 外层循环最多 V 次(每个节点最多入队一次)
- 每次循环要扫整行 V 个格子找邻居
- 总:V × V = O(V²)

**邻接表下变成 O(V+E)**:
- 每个节点的邻居遍历 = 它的实际度数
- 所有节点的度数之和 = 2E(无向)或 E(有向)
- 总:O(V) 出队 + O(E) 遍历邻居 = O(V+E)

---

## 十三、Anagram 经典题专题

### 13.1 题目定义

**判断两个字符串是不是 anagram(字母异位词)**:
> 两个字符串用到的**字符种类**和**每个字符出现次数**都一样,只是顺序不同。

例子:
- `"listen"` 和 `"silent"` → ✅ 是 anagram
- `"aab"` 和 `"abb"` → ❌ 不是

### 13.2 方法 1:排序后比较

```python
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)
```

**原理**:如果是 anagram,排序后字符序列必然完全一样。

```python
sorted("listen")    # ['e', 'i', 'l', 'n', 's', 't']
sorted("silent")    # ['e', 'i', 'l', 'n', 's', 't']
# 相等 → True
```

**复杂度**:**O(n log n)** 时间(排序代价)

### 13.3 方法 2:Counter(推荐面试用)

```python
from collections import Counter

def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)
```

**原理**:`Counter` 统计每个字符出现次数,直接比较两个字典。

```python
Counter("aabb")     # Counter({'a': 2, 'b': 2})
Counter("abbb")     # Counter({'b': 3, 'a': 1})
```

**复杂度**:**O(n)** 时间(扫一遍即可)

### 13.4 方法 3:手写字典统计(理解底层)

```python
def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    
    count = {}
    
    # 用 s1 的字符次数加上去
    for ch in s1:
        count[ch] = count.get(ch, 0) + 1
    
    # 用 s2 的字符次数减回来
    for ch in s2:
        if ch not in count:
            return False        # s2 出现了 s1 没有的字符
        count[ch] -= 1
        if count[ch] < 0:
            return False        # s2 某字符出现次数比 s1 多
    
    return True
```

**复杂度推导**:
- `for ch in s1` 扫一遍 → O(n)
- `for ch in s2` 扫一遍 → O(n)
- **`ch in count` 是字典查找,平均 O(1)** ⭐
- 总:O(n) + O(n) = **O(n)**

### 13.5 为什么需要 `count[ch] < 0` 判断?

光判断 `if ch not in count` **不够**。考虑:

- `s1 = "aab"`, `s2 = "abb"`
- s2 里的 `'a'` 和 `'b'` 都在 count 里(都出现过)
- 但 s2 的 `'b'` 出现 2 次,s1 的 `'b'` 只有 1 次
- 减到第二个 `'b'` 时,`count['b']` 变成 -1
- 这才检测出"s2 b 多了"

**所以需要**:
1. 长度判断
2. `ch not in count` 判断(s2 有 s1 没有的字符)
3. `count[ch] < 0` 判断(s2 某字符出现次数比 s1 多)

### 13.6 边界情况

```python
# 默认区分大小写
Counter("Listen") == Counter("silent")    # False

# 想忽略大小写
s1, s2 = s1.lower(), s2.lower()

# 想忽略空格
s1 = s1.replace(" ", "")
s2 = s2.replace(" ", "")

# 完整鲁棒版
from collections import Counter
def is_anagram(s1, s2):
    s1 = s1.lower().replace(" ", "")
    s2 = s2.lower().replace(" ", "")
    return Counter(s1) == Counter(s2)
```

### 13.7 三种方法对比

| 方法 | 时间 | 空间 | 适用场景 |
|---|---|---|---|
| `sorted()` 比较 | O(n log n) | O(n) | 代码最短,刷题初期 |
| `Counter` 比较 | **O(n)** | O(k) | **面试推荐** |
| 手写字典 | **O(n)** | O(k) | 展示底层理解 |

### 13.8 面试标准答案

```python
from collections import Counter

def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)
```

**面试加分话术**:
> "This is case-sensitive by default. If we want it to be case-insensitive, we can convert both strings to lowercase first. Time complexity is O(n) since we just scan each string once. The dictionary equality check is also linear in the number of unique characters."

---

## 十四、复杂度速查总表

### 14.1 数据结构操作复杂度

| 数据结构 | 访问 | 查找(`in`) | 插入 | 删除 |
|---|---|---|---|---|
| Array (List) | O(1) | **O(n)** | O(n) | O(n) |
| String | O(1) | **O(n)** | 不可变 | 不可变 |
| Linked List | O(n) | O(n) | O(1)* | O(1)* |
| Hash Map (Dict) | - | **O(1)** | O(1) | O(1) |
| Hash Set | - | **O(1)** | O(1) | O(1) |
| Stack | O(n) | O(n) | O(1) | O(1) |
| Queue (deque) | O(n) | O(n) | O(1) | O(1) |
| Binary Tree | O(n) | O(n) | O(n) | O(n) |
| BST(平衡) | - | O(log n) | O(log n) | O(log n) |
| Heap | O(1) peek | O(n) | O(log n) | O(log n) |

*Linked List 在已知节点位置时是 O(1),搜索还是 O(n)

注意1: 因为 **大 O 会忽略常数系数**。

换底公式：log4(n) = log2(n) / log2(4) = log2(n) / 2

所以：

```text
O(log₄ n)
= O((1/2) log₂ n)
= O(log₂ n)
= O(log n)
```

关键点：
 `log₄ n` 和 `log₂ n` 只差一个常数倍 `1/2`。

举例：

```text
n = 16

log₂16 = 4
log₄16 = 2
```

虽然数值不一样，但增长趋势一样。
 所以在时间复杂度里：

```text
O(log₂ n) = O(log₄ n) = O(log₁₀ n) = O(ln n) = O(log n)
```

只要底数是大于 1 的常数，统一写成 **`O(log n)`**。

在算法复杂度里，**`O(log n)`** **不关心底数**。

因为只要底数是固定常数且大于 1：

```text
log₂ n, log₄ n, log₁₀ n, ln n
```

它们之间都只差一个**常数倍**，大 O 会忽略常数。

所以：

```text
O(log n)
```

通常可以理解为：

```text
任意固定底数的 log
```

在刷题里最常见的直觉是 **以 2 为底**，因为很多算法每次把问题规模减半，例如二分查找：

```text
n -> n/2 -> n/4 -> n/8 ...
```

所以面试/LeetCode 里你可以默认理解成：

```text
O(log₂ n)
```

但正式写复杂度时，直接写：

```text
O(log n)
```

注意2: O(n+m) = O(max(n + m))

因为n + m > max(n, m) > (n+m)/2, 而O(n+m) > O(max(n+m)) > O(1/2(n+m)), 因为O(n+m) = O(1/2(n+m)), 所以O(n+m) = O(max(n, m))

### 14.2 算法复杂度

| 算法 | 时间复杂度 | 空间复杂度 |
|---|---|---|
| 二分查找 | O(log n) | O(1) |
| `sorted()` / Merge Sort | O(n log n) | O(n) |
| Quick Sort | O(n log n) 平均 | O(log n) |
| BFS/DFS(邻接表) | O(V+E) | O(V) |
| BFS/DFS(邻接矩阵) | O(V²) | O(V) |
| 双指针 | O(n) | O(1) |

### 14.3 `in` 操作专题(必记)

| 表达式 | 复杂度 |
|---|---|
| `ch in list` | **O(n)** |
| `ch in string` | **O(n)** |
| `ch in dict` | **O(1) 平均** |
| `ch in set` | **O(1) 平均** |

---

## 十五、Mock 当天的"5 必说"

不管做哪道题,这五句话都要主动说:

1. **澄清题意**:"Let me make sure I understand — input is..., output is..., and edge cases include..."
2. **讲思路**:"My approach is to use [pattern]. The intuition is..."
3. **预估复杂度**:"Time complexity should be O(...), space O(...)."
4. **写代码时讲解**:"Here I'm using a hash map to track..."(不要沉默写代码)
5. **跑测试**:"Let me trace through with the example..."

---

## 十六、必背的 6 个核心模板

**5/7 早起这 6 段必须能闭眼写**:

### 模板 1:Binary Search

```python
lo, hi = 0, len(arr) - 1
while lo <= hi:
    mid = (lo + hi) // 2
    if arr[mid] == target: return mid
    elif arr[mid] < target: lo = mid + 1
    else: hi = mid - 1
return -1
```

### 模板 2:Reverse Linked List

```python
prev, cur = None, head
while cur:
    nxt = cur.next
    cur.next = prev
    prev = cur
    cur = nxt
return prev
```

### 模板 3:Valid Parentheses (Stack)

```python
stack = []
pairs = {')': '(', ']': '[', '}': '{'}
for c in s:
    if c in '([{':
        stack.append(c)
    else:
        if not stack or stack.pop() != pairs[c]:
            return False
return not stack
```

### 模板 4:二叉树层序遍历(BFS)

```python
from collections import deque
def levelOrder(root):
    if not root: return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        size = len(queue)
        for _ in range(size):
            node = queue.popleft()
            level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    return result
```

### 模板 5:Graph BFS 带层数(求最短路径)

```python
from collections import deque
def bfs(graph, start, target):
    visited = {start}
    queue = deque([start])
    steps = 0
    while queue:
        steps += 1
        size = len(queue)
        for _ in range(size):
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in visited:
                    if neighbor == target:
                        return steps
                    visited.add(neighbor)
                    queue.append(neighbor)
    return -1
```

### 模板 6:Graph DFS 递归 + 网格版

```python
# 通用 DFS
def dfs(node, visited):
    if node in visited: return
    visited.add(node)
    for neighbor in graph[node]:
        dfs(neighbor, visited)

# 网格 DFS(LC 200)
def dfs(r, c):
    if (r < 0 or r >= rows or c < 0 or c >= cols 
        or (r, c) in visited or grid[r][c] == '0'):
        return
    visited.add((r, c))
    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
        dfs(r + dr, c + dc)
```

---

## 十七、Mock Interview 实战复盘(2026-05-07)

> 这一节是真实 mock 的题目、解法、踩过的坑、和反馈整理。**这道题是 Two Sum 的变形 + Two Pointer 进阶**,涵盖了多个核心知识点,建议反复复习。

### 17.1 题目还原

**输入**:整数列表
**输出**:list of list,每个内部 list 是两个数,这两个数相加等于 0
**边界**:如果找不到任何 pair,返回 `[]`

例子:
```python
[-1, 0, 1, 2, -1, -4]    # 期望:[[-1, 1]] 或 [[1, -1]]
[]                        # []
[-1, -2, 4, 7]            # []
[-1, -1, -1, 1, 1, 1]     # 期望:取决于"unique pair"还是"index pair"
```

### 17.2 UMPIRE 模板(面试讲题流程)

mock 用的是 UMPIRE 框架,**面试时一定要按这个顺序说**:

| 步骤 | 内容 |
|---|---|
| **U**nderstand | 理解题意,确认输入输出和边界 |
| **M**atch | 这题让我想到什么 pattern?哪些数据结构适用? |
| **P**lan | 设计算法,可以画图或写伪代码 |
| **I**mplement | 写代码 |
| **R**eview | 走一遍例子,验证正确性 |
| **E**valuate | 时间空间复杂度分析 |

##### 题目对应的 UMPIRE 内容

```
Understand:
  inputs: integer list
  outputs: list of list, each inner list is a pair summing to 0
  edge case: 找不到 pair 返回 []

Match:
  - Brute force:nested for loop
  - Hash Set:利用 set O(1) 查找
  - Two Pointers:排序后双指针对撞

Evaluate:
  Brute force:    Time O(n²)  Space O(n)
  Hash Set:       Time O(n)   Space O(n)
  Two Pointers:   Time O(n log n)  Space O(n)
```

### 17.3 三种解法对比

#### 解法 1:暴力 Nested Loop

```python
def getPairs(nums):
    result = []
    for i, num1 in enumerate(nums):
        for num2 in nums[i + 1:]:        # 只看 i 后面,避免重复
            if num1 + num2 == 0:
                result.append([num1, num2])
    return result
```

**复杂度**:O(n²) 时间,O(k) 空间(k 是返回的 pair 数)

##### 关于 enumerate 的写法升级

```python
# ❌ 老式写法
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == 0:
            ...

# ✅ Pythonic 写法
for i, num1 in enumerate(nums):
    for num2 in nums[i + 1:]:
        if num1 + num2 == 0:
            ...
```

##### 如果还要保留 j 的下标

```python
for i, num1 in enumerate(nums):
    for j, num2 in enumerate(nums[i + 1:], start=i + 1):
        # j 是真实下标(不是切片的相对下标)
        ...
```

##### 不要用 `list` 作为变量名!

```python
def getPairs(list):       # ❌ list 是 Python 内置类型名
    ...

def getPairs(nums):       # ✅ 推荐
    ...
```

#### 解法 2:Hash Set(允许重复 pair 版)

```python
def getPairs(nums):
    result = []
    seen = set()
    for num in nums:
        if -num in seen:
            result.append([num, -num])
        seen.add(num)
    return result
```

**复杂度**:O(n) 时间(set 查找 O(1)),O(n) 空间

##### Hash Set 解法的"陷阱":seen 去重 ≠ result 去重

`seen` 只去重了"已经见过的数字",**不会自动帮 result 去重**。

##### 反例 `[-1, -1, -1, 1, 1, 1]`

| 当前 num | seen(只存数字,自动去重) | 操作 | result |
|---|---|---|---|
| -1 | {} → {-1} | 1 不在 seen | `[]` |
| -1 | {-1} → {-1} | 1 不在 seen | `[]` |
| -1 | {-1} → {-1} | 1 不在 seen | `[]` |
| 1 | {-1} → {-1, 1} | -1 在 seen,append | `[[1, -1]]` |
| 1 | {-1, 1} → {-1, 1} | -1 在 seen,**再次** append | `[[1, -1], [1, -1]]` |
| 1 | {-1, 1} | -1 在 seen,**再次** append | `[[1, -1], [1, -1], [1, -1]]` |

**关键观察**:`set` 只会对**自己内部元素**去重,**不会帮 result 去重**。

#### 解法 3:Hash Set(去重 pair 版)

```python
def getPairs(nums):
    result = []
    seen = set()
    used_pairs = set()                       # 专门记录已加入的 pair
    
    for num in nums:
        target = -num
        if target in seen:
            pair = tuple(sorted([num, target]))      # 排序后 tuple 化作 key
            if pair not in used_pairs:
                result.append([pair[0], pair[1]])
                used_pairs.add(pair)
        seen.add(num)
    
    return result
```

##### 为什么用 `tuple(sorted(...))`?

**两个原因**:

1. **list 不能放进 set**(list 可变,不可哈希):
```python
used_pairs.add([1, -1])    # ❌ TypeError: unhashable type: 'list'
used_pairs.add((1, -1))    # ✅ tuple 可以
```

2. **`[1, -1]` 和 `[-1, 1]` 应视为同一对**,所以先排序统一:
```python
tuple(sorted([1, -1]))     # (-1, 1)
tuple(sorted([-1, 1]))     # (-1, 1)   # 相同
```

#### 解法 4:Two Pointers(排序后对撞)

```python
def getPairs(nums):
    nums = sorted(nums)                       # 不修改原数组,创建新数组
    result = []
    left, right = 0, len(nums) - 1
    
    while left < right:
        total = nums[left] + nums[right]
        if total == 0:
            result.append([nums[left], nums[right]])
            left += 1
            right -= 1
        elif total < 0:
            left += 1                         # 太小,左指针右移
        else:
            right -= 1                        # 太大,右指针左移
    
    return result
```

**复杂度**:O(n log n) 时间(排序主导),O(n) 空间(`sorted()` 创建新数组)

##### 关键易错点:**找到 pair 后必须移动指针**

```python
# ❌ 错误写法(死循环)
if total == 0:
    result.append([nums[left], nums[right]])
    # 忘了移动 left/right,下一轮还是同一对!

# ✅ 正确
if total == 0:
    result.append([nums[left], nums[right]])
    left += 1
    right -= 1
```

##### Two Pointers 加去重(类似 LC 15 3Sum)

```python
def getPairs(nums):
    nums = sorted(nums)
    result = []
    left, right = 0, len(nums) - 1
    
    while left < right:
        total = nums[left] + nums[right]
        if total == 0:
            result.append([nums[left], nums[right]])
            left += 1
            right -= 1
            # 跳过重复(必须用 while,不是 if!)
            while left < right and nums[left] == nums[left - 1]:
                left += 1
            while left < right and nums[right] == nums[right + 1]:
                right -= 1
        elif total < 0:
            left += 1
        else:
            right -= 1
    
    return result
```

##### 为什么外层 while 不能替代内层 while?

**因为做的是两件事**:
- 外层 while:**指针越界检查**(`left < right`)
- 内层 while:**跳过相同值**(`nums[left] == nums[left - 1]`)

两件事缺一不可,所以**必须**嵌套两个 while。

### 17.4 `sort()` vs `sorted()` 选哪个?

| | `nums.sort()` | `nums = sorted(nums)` |
|---|---|---|
| 是否修改原数组 | **原地排序, 修改原数组** | 不修改原数组,返回新数组 |
| 时间 | O(n log n) | O(n log n) |
| 空间 | 原地排序(实际 Timsort 最坏 O(n)). <br />O(1) or O(n) depending on how strictly counting sort() internal space | **O(n)** |
| 返回值 | `None` | 新的有序 list |

**面试推荐**:**不要修改输入参数**(可能被面试官扣分),用 `sorted()` 更安全。

### 17.5 整体复杂度细节

#### Two Pointers 解法 (`sorted` 版)

| 部分 | 时间 | 空间 |
|---|---|---|
| `sorted(nums)` | O(n log n) | O(n)(新数组) |
| 双指针扫描 | O(n) | O(1) |
| `result` 输出 | - | O(n)(最坏 n/2 个 pair) |
| **总计** | **O(n log n)** | **O(n)** |

##### 面试可以这样说复杂度

> "Time complexity is O(n log n), dominated by the sort. The two-pointer scan is O(n). Space is O(n) — the sort creates a new array, plus the result list. If we used `nums.sort()` to sort in place, extra space drops to O(1) ignoring the output, but it would mutate the input."

### 17.6 `if not nums: return []` 这一行加不加?

**可加可不加**。即使输入是空 list,代码也能正常工作:

```python
nums = []
nums = sorted(nums)              # []
left, right = 0, -1              # right = len([]) - 1 = -1
while left < right:              # 0 < -1 是 False,跳过
    ...
return result                    # []
```

**加 early return 可读性更好**(防御式编程),但**不是必须的**。

### 17.7 不同解法返回结果不一致?

#### 现象

对 `[-1, 0, 1, 2, -1, -4]`:
- **Two Pointers** 返回:`[[-1, 1]]`
- **Hash Set(无去重版)** 返回:`[[1, -1], [-1, 1]]`

这不是 bug,是**两种解法对"pair"的定义不同**:
- Two Pointers 找完一对后两端都缩,**每个元素最多用一次**
- Hash Set 是顺序扫描,只要"之前见过 -num"就 append,**可能产生不同 index 但相同 value 的多对**

#### 面试时如何处理?

**先和面试官澄清需求**:
- "Should pairs be unique by value? Or are different index combinations allowed?"
- "Can the same element be reused?"

**这就是 UMPIRE 中 Understand 阶段最关键的环节**。

### 17.8 Nested Loop 的复杂度真相 ⭐

mock 反馈中重要的一课:**nested loop 不一定就是 O(n²)**。关键看**内层循环总共执行了多少次**。

#### 七种 nested loop 复杂度速查

| 代码形态 | 时间复杂度 | 例子 |
|---|---|---|
| `for i in range(n)` + `for j in range(n)` | O(n²) | 标准 |
| `for i` + `for j in range(i+1, n)` | **O(n²)** | 变短但本质不变(总次数 n(n-1)/2) |
| `for` + `while`,两指针只往前走 | **O(n)** | **滑动窗口、单调栈** |
| `for` + 二分查找 | O(n log n) | 排序后查 |
| `for` + `while j *= 2`(指数增长) | O(n log n) | 倍增 |
| `for i in range(n)` + `for j in range(10)`(常数) | O(n) | 常数会被省略 |
| `for i in range(n)` + `for j in range(m)`(不同长度) | O(n·m) | 两个数组 |

#### 重点:为什么滑动窗口/单调栈是 O(n)?

虽然有 for + while 看起来嵌套,但**每个元素最多被处理常数次**:

```python
left = 0
for right in range(n):                # right 走 n 次
    while s[right] in seen:
        seen.remove(s[left])
        left += 1                     # left 总共也只走 n 次
    seen.add(s[right])
```

**right 最多走 n 次,left 最多走 n 次**,总操作 ≤ 2n,所以是 **O(n)**,不是 O(n²)。

> **判断方法**:不要只看有几层 loop,要问"**所有循环加起来总共执行多少次?**"

### 17.9 这次 mock 学到的 5 个核心 takeaways

1. **UMPIRE 流程必须走全**:Understand → Match → Plan → Implement → Review → Evaluate。**Understand 阶段务必和面试官澄清边界**(unique pair?是否允许重用?)。

2. **不要用 `list`、`set`、`dict` 等 Python 内置类型作为变量名**。会覆盖内置功能,容易引发难调的 bug。

3. **Two Pointers 找到答案后必须移动指针**,否则死循环。这是面试官最常追问的细节。

4. **`set` 只对自己内部元素去重,不会帮你的 `result` 去重**。如果题目要求 unique pair,需要额外的 `used_pairs = set()`。

5. **Nested loop 不一定 O(n²)**。能用滑动窗口/单调栈时,不要简单套"两层 for = O(n²)"。**复杂度算的是总操作次数**。

### 17.10 总结模板:Two Sum / N Sum 类题目

遇到类似题目,**先在脑海里走这棵决策树**:

```
是否要返回 index?
├─ 是 → 用 Hash Map(存 num → index),O(n)
└─ 否,只要 value pair
    ├─ 数据已排序 / 可排序
    │   └─ Two Pointers,O(n log n)(或 O(n) 如果已排序)
    ├─ 不能改原数组,要 O(n) 时间
    │   └─ Hash Set + (可选) used_pairs 去重
    └─ 数据规模小
        └─ Brute Force 也 OK,O(n²)
```

---

### 17.11 Two Sum 全家桶 ⭐⭐⭐(5/7 + 5/9 二刷综合)

> **Two Sum 是面试常青树**。两次 mock 都考了这一题但角度不同 —— 5/7 考"找所有 pair"(去重核心),5/9 考"找一对 pair"(返回 index 核心)。**这两个变种基本覆盖了 Two Sum 的所有难点**,值得反复复习。

#### 17.11.1 Two Sum 的四种官方变种

| 变种 | 题目 | 输入特点 | 输出 | 推荐解法 |
|---|---|---|---|---|
| **LC 1 经典版** | Two Sum | 无序数组 | **原始 index** | Hash Map(O(n)) |
| **LC 167 升级版** | Two Sum II | **已排序**数组 | 1-indexed 位置 | Two Pointers(O(n)) |
| **LC 15 / 5/7 mock** | 3Sum 简化版 | 无序数组 | **所有 unique value pair** | 排序 + Two Pointers |
| **LC 653** | Two Sum IV in BST | BST | 是否存在 pair | 中序 + 双指针 / Hash |

#### 17.11.2 5/7 mock vs 5/9 mock 核心差异表

| | 5/7 `getPairs()` | 5/9 `twoSum()` |
|---|---|---|
| **目标** | 找**所有** value pair | 找**一对** index pair |
| **target** | 固定 0 | 任意 target |
| **去重** | 需要(unique value pair) | 不需要(题目保证唯一解) |
| **返回类型** | `List[List[int]]` | `List[int]`(2 个 index) |
| **关键陷阱** | `seen` 不去重 result | 排序后 index 丢了 |
| **最优解** | 排序 + Two Pointers + 跳重 | Hash Map(因为要 index) |

##### 一句话区分

```
要找所有不重复的 value pair  →  排序 + Two Pointers + 跳重
要找一对的 index            →  Hash Map(存 num → index)
```

#### 17.11.3 LC 1 Two Sum:四种 Hash Map 写法对比

##### 写法 A:`range(len(nums))` 写法(基础)

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []
        seen: Dict[int, int] = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if need in seen:
                return [seen[need], i]
            seen[nums[i]] = i
        return []
```

##### 写法 B:`enumerate` 写法(更 Pythonic)⭐ 推荐

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        seen = {}
        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], i]
            seen[num] = i
        return [-1, -1]
```

`enumerate` 同时拿 index 和 value,**面试推荐这个**。

##### 关键设计:为什么 `seen[num] = i` 放在 `if` 之后?

```python
for i, num in enumerate(nums):
    if target - num in seen:        # 1. 先检查
        return [...]
    seen[num] = i                    # 2. 后存
```

**先查,后存**。如果反过来:
```python
seen[num] = i                       # ❌ 先存
if target - num in seen:            # 这里可能查到自己!
    ...
```

考虑 `nums = [3, 3], target = 6`:正确写法找到 `[0, 1]`;错误写法第 0 步就 `seen[3] = 0`,然后查 `target - 3 = 3` 已经在 seen 里 → 返回 `[0, 0]`(同一个元素用了两次!)。

##### 写法 C:不存在时返回什么?

| 写法 | 返回值 | 适用场景 |
|---|---|---|
| `return []` | 空 list | 题目允许返回空 |
| `return [-1, -1]` | 占位 | 题目要求固定长度 |
| 不写 return | 默认 None | 调用方处理 None |

LC 1 的题目说 "exactly one solution exists",**理论上不会走到末尾**,但**面试时一定要写 return**(防御式编程)。

##### Two Sum Hash Map 复杂度

| | 时间 | 空间 |
|---|---|---|
| Hash Map | **O(n)** | O(n)(最坏存 n-1 个数) |

#### 17.11.4 排序 + Two Pointers 找 index:你 5/9 踩过的坑

##### ❌ 错误版本(你 5/9 第一次写的)

```python
class Solution:
    def twoSum(self, nums, target):
        if not nums:
            return []
        sorted(nums)                 # ❌ Bug 1:这一行没有效果
        left, right = 0, len(nums) - 1
        while left < right:
            total = nums[left] + nums[right]
            if total > target:
                right -= 1
            elif total < target:
                left += 1
            else:
                return [left, right]  # ❌ Bug 2:返回的是排序后的 index,不是原始 index
        return []
```

**两个致命 bug**:

###### Bug 1:`sorted(nums)` 没修改 nums

```python
sorted(nums)                # ❌ 创建新数组,但没赋值给 nums
nums.sort()                 # ✅ 原地修改
nums = sorted(nums)         # ✅ 把新数组赋值回去
```

`sorted()` 返回新 list,**调用结果必须接收**,否则相当于白排。
`.sort()` 是原地修改,直接生效。

###### Bug 2:即使排序成功,index 也丢了

题目要求**返回原始数组的 index**。排序后,原来的位置变了:

```python
nums = [3, 2, 4], target = 6
# 原始 index:0→3, 1→2, 2→4
# 排序后:[2, 3, 4],对应原 index [1, 0, 2]
# Two pointers 找到 2+4=6,在排序后的位置 [0, 2]
# 但题目要的是原始 index [1, 2]!
```

##### ✅ 正确版本:用 tuple 保留原始 index

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []
        # 排序时把原始 index 一起带上
        sorted_nums = sorted((num, i) for i, num in enumerate(nums))
        # sorted_nums = [(2, 1), (3, 0), (4, 2)]  对于 [3, 2, 4]
        
        left, right = 0, len(sorted_nums) - 1
        while left < right:
            current_sum = sorted_nums[left][0] + sorted_nums[right][0]
            if current_sum == target:
                return [sorted_nums[left][1], sorted_nums[right][1]]
            elif current_sum > target:
                right -= 1
            else:
                left += 1
        return []
```

##### 关键技巧:`sorted((num, i) for i, num in enumerate(nums))`

这一行干了三件事:
1. `enumerate(nums)` → 产生 `(0, 3), (1, 2), (2, 4)`
2. `(num, i) for i, num in ...` → 调换顺序成 `(3, 0), (2, 1), (4, 2)`
3. `sorted(...)` → 按 `num` 排序(tuple 比较默认按第一个元素)

**为什么 `(num, i)` 而不是 `(i, num)`?**
因为 sort 默认按 tuple 第一个元素排序。我们要按 num 排序,所以 num 必须放第一位。

##### 复杂度对比

| 方法 | 时间 | 空间 | 适用 |
|---|---|---|---|
| Hash Map | **O(n)** | O(n) | **首选**(简洁、高效) |
| Sort + Two Pointers + 保留 index | O(n log n) | O(n) | 没有其他选择时 |

**面试推荐**:LC 1 直接用 Hash Map,**Two Pointers 留给已排序的 LC 167 用**。

#### 17.11.5 5/7 mock 的"找所有 pair"四种解法对比

##### 解法对比表

| 解法 | 时间 | 空间 | 是否去重 | 是否返回 index |
|---|---|---|---|---|
| 暴力 nested loop | O(n²) | O(k) | 否 | 否 |
| Hash Set(无去重) | O(n) | O(n) | **否** | 否 |
| Hash Set + `used_pairs` | O(n) | O(n) | ✓ | 否 |
| Hash Dict + `used_pairs` | O(n) | O(n) | ✓ | 可保留(但用不到) |
| 排序 + Two Pointers + 跳重 | O(n log n) | O(n) | ✓ | 否 |

##### 5/7 你最终用的"Hash Dict 去重版"

```python
def getPairs(nums):
    result = []
    seen = {}                    # num → index(本题不需要 index,但模式通用)
    used_pairs = set()           # 已加入的 pair
    
    for i, num in enumerate(nums):
        if -num in seen:
            pair = tuple(sorted([num, -num]))    # 统一顺序 + 转 tuple
            if pair not in used_pairs:
                result.append([pair[0], pair[1]])
                used_pairs.add(pair)
        seen[num] = i
    
    return result
```

##### 关于 `seen[num] = i` 不要放进 else!

```python
# ❌ 错误
if -num in seen:
    ...
else:
    seen[num] = i           # 只在没匹配时才存

# ✅ 正确
if -num in seen:
    ...
seen[num] = i               # 不管匹配与否都存
```

**为什么**:`seen` 是"我所有见过的数字"的记录,**跟有没有匹配无关**。

考虑 `[1, 1, -1]`:
- i=0, num=1: `-1` 不在 seen,存 `seen[1]=0`
- i=1, num=1: `-1` 不在 seen,(错误版会跳过 seen[1]=1),正确版更新 `seen[1]=1`
- i=2, num=-1: `1` 在 seen,加入 pair

**错误版可能 miss 后续数字的有效配对**。

##### `tuple(sorted(...))` 双重技巧

```python
pair = tuple(sorted([num, -num]))
```

**两件事一次做完**:
1. **`sorted([num, -num])`** 让 `[1, -1]` 和 `[-1, 1]` 都变成 `[-1, 1]`,**视为同一组**
2. **`tuple(...)`** 把 list 变 tuple,因为 **list 不可哈希**(不能放 set)

```python
used_pairs.add([1, -1])     # ❌ TypeError: unhashable type: 'list'
used_pairs.add((1, -1))     # ✅ tuple 可以
```

#### 17.11.6 `seen` 用 set 还是 dict?

##### 5/7 时你的笔记踩到这个

```python
seen = set()                # 只记录"见过哪些数字"
seen = {}                   # 记录"数字 → index"
```

**判断标准**:**这题用不用得到 index?**

| 题型 | 推荐 |
|---|---|
| 只要判断"是否出现过" | `set` |
| 要返回 index | `dict` |
| 想统计出现次数 | `dict` 或 `Counter` |

5/7 mock 是判断和为 0 的 pair,不需要 index → 用 `set` 更合适。
5/9 mock 是 LC 1 要返回 index → 用 `dict` 必须。

#### 17.11.7 Two Sum 家族学习路径

按这个顺序刷,逐步增加难度:

```
LC 1 Two Sum                    ← 基础(Hash Map)
  ↓
LC 167 Two Sum II               ← 进阶(已排序 → Two Pointers)
  ↓
LC 653 Two Sum IV in BST        ← 进阶(BST + 双指针)
  ↓
5/7 mock getPairs               ← 进阶(找所有 pair + 去重)
  ↓
LC 15 3Sum                      ← 大魔王(三数和 + 多重去重)
  ↓
LC 18 4Sum                      ← 终极(套娃 + 剪枝)
```

#### 17.11.8 两次 mock 综合 takeaways(必看)

1. **判断要不要 index → 决定用 set 还是 dict**
2. **`sorted()` 不修改原数组**,要么 `.sort()` 要么 `nums = sorted(nums)`
3. **如果排序后还要原始 index,用 `(num, i)` tuple 配对**
4. **去重 pair**:`tuple(sorted([a, b]))` + `used_pairs` set
5. **Hash Map 写法**:**先查 `target - num`,后存 `seen[num] = i`**(顺序不能反!)
6. **`seen.add(num)` 不要放 else**(要无条件存,跟匹配无关)
7. **Two Pointers 找完 pair 一定要移动指针**,且**跳重要用 while 不是 if**
8. **不要用 `list` 做变量名**(覆盖 Python 内置类型)

#### 17.11.9 一句话记忆

```
要 index    → Hash Map(dict),先查后存
要所有 pair → 排序 + Two Pointers + 跳重(while 跳)
要去重 pair → tuple(sorted(...)) 配 used_pairs set
排序后丢 index → (num, i) tuple 配对
seen 是 set 还是 dict?看要不要 index
```

---

<a id="ch18"></a>

## 十八、Heap / Top K(优先队列)⭐⭐⭐

> **面试重要性:高频**。Microsoft、Google 常考。一旦题目出现 "top K"、"k largest"、"k smallest"、"k frequent",**优先想 Heap**。

### 18.1 什么是 Heap?

**Heap(堆)** 是一种特殊的二叉树,满足**堆序性质**:
- **Min-Heap(小顶堆)**:每个父节点 ≤ 它的孩子。**根节点是最小值**。
- **Max-Heap(大顶堆)**:每个父节点 ≥ 它的孩子。**根节点是最大值**。

```
Min-Heap:           Max-Heap:
     1                   9
    / \                 / \
   3   5               6   7
  / \                 / \
 4   8               2   1
```

#### Python 中的 Heap

Python 的 `heapq` 模块**只提供 Min-Heap**(没有 Max-Heap)。

```python
import heapq

heap = []
heapq.heappush(heap, 5)         # 加元素,O(log n)
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)
print(heap)                     # [1, 5, 3](注意不是完全有序!)

smallest = heapq.heappop(heap)  # 弹出并返回最小,O(log n)
print(smallest)                 # 1

peek = heap[0]                  # 看堆顶(最小),O(1)
```

⚠️ **`print(heap)` 看到的不是排序后的数组**,只是底层数组形式。但 `heap[0]` **保证是最小值**。

#### 关键操作复杂度

| 操作 | 复杂度 |
|---|---|
| `heappush(heap, x)` | O(log n) |
| `heappop(heap)` | O(log n) |
| `heap[0]` 看堆顶 | O(1) |
| `heapify(list)` 把 list 变成 heap | O(n) |

### 18.2 用 heapq 实现 Max-Heap(取负数技巧)

`heapq` 没有 max-heap,**取负数模拟**:

```python
import heapq

# 想要 max-heap 存 [3, 1, 5]
heap = []
for x in [3, 1, 5]:
    heapq.heappush(heap, -x)    # 存负数

# 取最大值
largest = -heapq.heappop(heap)  # 弹出 -5,取负 → 5
```

**核心:存的是 -x,取出来再 -x 还原**。

### 18.3 经典题 1:LC 215 Kth Largest Element in an Array

#### 18.3.1 题目

给一个未排序数组,找第 K 大的元素。

```python
nums = [3, 2, 1, 5, 6, 4]
k = 2
# 排序后是 [1,2,3,4,5,6],第 2 大 = 5
```

#### 18.3.2 解法 1:排序(O(n log n))

```python
def findKthLargest(nums, k):
    return sorted(nums)[-k]
# 或 sorted(nums, reverse=True)[k-1]
```

简单,但没用到题目本质。

#### 18.3.3 解法 2:Min-Heap 维护 K 个最大值(O(n log k),最优)

**核心思路**:维护一个**大小为 K 的 min-heap**,堆里始终是"目前见过的 K 个最大值"。最后堆顶就是第 K 大。

```python
import heapq

def findKthLargest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)        # 弹出最小的,保持 size = k
    return heap[0]                     # 堆顶就是第 K 大
```

##### 为什么用 min-heap 而不是 max-heap?

**反直觉但很重要**!

要找第 K 大,**用 min-heap 维护 K 个最大值**:
- heap 大小始终 ≤ K
- 堆顶是这 K 个值里**最小的**
- 当新数比堆顶大,堆顶被踢出,新数进来
- 最后堆顶 = 这 K 个最大值里最小的 = **第 K 大**

如果用 max-heap,你要把整个 n 个元素都存进去再 pop K 次,空间 O(n),不优雅。

##### 走一遍 `[3, 2, 1, 5, 6, 4]`, k=2

| num | push 后 heap | pop 后 heap | 当前堆顶 |
|---|---|---|---|
| 3 | [3] | [3](size=1) | 3 |
| 2 | [2, 3] | [2, 3](size=2) | 2 |
| 1 | [1, 3, 2] | [2, 3](size>2,pop 1) | 2 |
| 5 | [2, 3, 5] | [3, 5](pop 2) | 3 |
| 6 | [3, 5, 6] | [5, 6](pop 3) | 5 |
| 4 | [4, 6, 5] | [5, 6](pop 4) | 5 |

最后 `heap[0] = 5` ✓

#### 18.3.4 复杂度

| | 时间 | 空间 |
|---|---|---|
| 排序 | O(n log n) | O(1) 或 O(n) |
| Min-Heap(size K) | **O(n log k)** | **O(k)** |
| Quickselect | O(n) 平均 | O(1) |

**面试推荐**:Min-Heap 解法,代码短逻辑清晰,K 小的时候比排序快很多。

### 18.4 经典题 2:LC 347 Top K Frequent Elements

#### 18.4.1 题目

返回数组中**出现次数前 K 多**的元素。

```python
nums = [1,1,1,2,2,3]
k = 2
# 1 出现 3 次,2 出现 2 次 → 答案 [1, 2]
```

#### 18.4.2 解法:Counter + Min-Heap

```python
import heapq
from collections import Counter

def topKFrequent(nums, k):
    count = Counter(nums)              # {1: 3, 2: 2, 3: 1}
    heap = []
    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))    # 按 freq 排序
        if len(heap) > k:
            heapq.heappop(heap)              # 弹出 freq 最小的
    return [num for freq, num in heap]
```

##### 为什么 push `(freq, num)` 而不是 `(num, freq)`?

**Python 的 heap 比较 tuple 时按"第一个元素优先"**。我们想按频次排序,所以 freq 必须放第一位。

```python
heapq.heappush(heap, (3, 1))    # freq=3, num=1
heapq.heappush(heap, (2, 2))    # freq=2, num=2
# heap 按 freq 比较:2 < 3,所以堆顶是 (2, 2)
```

#### 18.4.3 还有一个更简单的解法:`Counter.most_common(k)`

```python
def topKFrequent(nums, k):
    return [num for num, freq in Counter(nums).most_common(k)]
```

`most_common(k)` 内部就是用 heap 实现的,代码最短。**面试可以先写这个,然后说"如果不让我用 most_common,我可以手写 heap"**,展示你既知道库也懂底层。

### 18.5 经典题 3:LC 23 Merge K Sorted Lists

#### 18.5.1 题目

合并 K 个升序链表。

```python
lists = [[1,4,5], [1,3,4], [2,6]]
# 输出 [1,1,2,3,4,4,5,6]
```

#### 18.5.2 解法:Min-Heap 一次取最小头

```python
import heapq

def mergeKLists(lists):
    heap = []
    # 先把每个链表的头节点放进 heap
    for i, head in enumerate(lists):
        if head:
            heapq.heappush(heap, (head.val, i, head))
            # i 是为了打破 val 相同时 ListNode 不能比较的尴尬
    
    dummy = ListNode(0)
    tail = dummy
    while heap:
        val, i, node = heapq.heappop(heap)
        tail.next = node
        tail = tail.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    return dummy.next
```

##### 为什么 tuple 是 `(val, i, head)` 三元组?

**Python heap 比较 tuple,如果第一个元素相同会比较第二个**。
- `val` 相同时,Python 会去比 `ListNode` 对象本身,但 ListNode 没定义 `<`,会报错
- 加一个 `i`(链表序号)作为打破平局的"次序键"

### 18.6 Heap 三大应用场景速查

| 场景 | 用法 | 题目 |
|---|---|---|
| **Top K Largest** | size K 的 **min-heap** | LC 215, 703 |
| **Top K Frequent** | Counter + size K 的 min-heap | LC 347, 692 |
| **Merge K Sorted** | size K 的 min-heap,每次取最小 | LC 23, 378 |
| **数据流找中位数** | 一个 min-heap + 一个 max-heap | LC 295 |
| **K Smallest 的变形** | size K 的 **max-heap** | LC 378 |

### 18.7 一句话记忆

```
Top K Largest  → size K 的 min-heap(反着用)
Top K Smallest → size K 的 max-heap(反着用)
Top K Frequent → Counter + heap,push (freq, val)
Merge K Sorted → heap 装每个序列的头,每次取最小再补
Python max-heap → 存 -x,取出再 -x
```

---

<a id="ch19"></a>

## 十九、Overlapping Intervals(区间问题)⭐⭐⭐

> **面试重要性:高频**。Meeting Rooms、日程冲突、合并区间是经典题型。**核心套路:先按起点排序**。

### 19.1 区间问题三大套路

| 套路 | 关键操作 | 经典题 |
|---|---|---|
| **合并** | 按 start 排序,与上一个区间比较是否重叠 | LC 56 Merge Intervals |
| **插入** | 找位置插入,处理重叠 | LC 57 Insert Interval |
| **占用统计** | min-heap 维护已占用资源 | LC 253 Meeting Rooms II |

**通用第一步:`intervals.sort(key=lambda x: x[0])`**(按起点升序)。

### 19.2 判断两个区间是否重叠

两个区间 `[a, b]` 和 `[c, d]`,**重叠的条件**:

```python
重叠 ⟺ a <= d and c <= b
不重叠 ⟺ b < c or d < a
```

更直观:

```
不重叠的两种情况:
区间1 在 区间2 左边:   [a, b]  [c, d]  → b < c
区间1 在 区间2 右边:   [c, d]  [a, b]  → a > d
其他情况都重叠
```

#### 排序后判断重叠的简化

如果已经按 start 排序,且 `intervals[i-1].start <= intervals[i].start`,则:
```python
# 前一个的 end >= 后一个的 start → 重叠
if intervals[i-1][1] >= intervals[i][0]:
    # 重叠了!
```

### 19.3 LC 56 Merge Intervals(合并区间)

#### 题目

```python
intervals = [[1,3], [2,6], [8,10], [15,18]]
# [1,3] 和 [2,6] 重叠 → 合并成 [1,6]
# 输出 [[1,6], [8,10], [15,18]]
```

#### 代码

```python
def merge(intervals):
    intervals.sort(key=lambda x: x[0])     # 按起点排序
    result = [intervals[0]]
    
    for current in intervals[1:]:
        last = result[-1]
        if current[0] <= last[1]:           # 当前 start <= 上一个 end → 重叠
            last[1] = max(last[1], current[1])    # 合并:取较大的 end
        else:
            result.append(current)
    return result
```

#### 走一遍

排序后:`[[1,3], [2,6], [8,10], [15,18]]`(本来就排好了)

| current | result 之前 | 是否重叠?(`current[0] <= last[1]`) | 操作 | result 之后 |
|---|---|---|---|---|
| 初始 | `[[1,3]]` | - | - | `[[1,3]]` |
| `[2,6]` | `[[1,3]]` | `2 <= 3` ✓ 重叠 | `last[1] = max(3, 6) = 6` | `[[1,6]]` |
| `[8,10]` | `[[1,6]]` | `8 <= 6` ✗ 不重叠 | append | `[[1,6], [8,10]]` |
| `[15,18]` | `[[1,6], [8,10]]` | `15 <= 10` ✗ | append | `[[1,6], [8,10], [15,18]]` |

#### 复杂度

- 时间:**O(n log n)**(排序主导)
- 空间:O(n)(result 数组)

### 19.4 LC 57 Insert Interval(插入区间)

#### 题目

给一个**已排序且不重叠**的区间数组 + 一个新区间,插入并保持排序、合并重叠。

```python
intervals = [[1,3], [6,9]]
newInterval = [2, 5]
# 输出 [[1,5], [6,9]]
```

#### 代码(三阶段)

```python
def insert(intervals, newInterval):
    result = []
    i, n = 0, len(intervals)
    
    # 阶段 1:把 newInterval 之前(完全在左,不重叠)的全加进 result
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1
    
    # 阶段 2:合并所有跟 newInterval 重叠的
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    result.append(newInterval)
    
    # 阶段 3:把 newInterval 之后(完全在右,不重叠)的全加进 result
    while i < n:
        result.append(intervals[i])
        i += 1
    
    return result
```

#### 复杂度

- 时间:**O(n)**(原数组已排序,不需要再排序)
- 空间:O(n)

### 19.5 LC 253 Meeting Rooms II(最少会议室数量)

#### 题目

给会议时间区间,问**最少需要多少个会议室**(同一时刻多少会议在开)。

```python
intervals = [[0,30], [5,10], [15,20]]
# 0-30 和 5-10 冲突,需要 2 个;15-20 跟 5-10 不冲突但跟 0-30 冲突
# 最少需要 2 个会议室
```

#### 解法:Min-Heap 维护已占用会议室的结束时间

**核心思路**:
- 按起点排序所有会议
- 用 min-heap 装"已开始但还没结束"的会议**的 end time**
- 每来新会议:看堆顶(最早结束的会议)是否已经结束。结束了 → pop(那个房间空出);没结束 → 必须开新房间
- push 当前会议的 end 进 heap
- 最后 heap 大小 = 同时占用过的最大房间数

```python
import heapq

def minMeetingRooms(intervals):
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[0])     # 按 start 排序
    heap = []                               # 存正在进行的会议的 end
    
    for start, end in intervals:
        if heap and heap[0] <= start:
            heapq.heappop(heap)             # 最早结束的会议已结束,房间释放
        heapq.heappush(heap, end)           # 当前会议占一个房间
    
    return len(heap)                        # 同时占用的最大房间数
```

#### 走一遍 `[[0,30], [5,10], [15,20]]`

| start, end | heap 之前 | 堆顶 ≤ start? | pop? | push end | heap 之后 |
|---|---|---|---|---|---|
| 0, 30 | [] | 堆空 | 否 | push 30 | [30] |
| 5, 10 | [30] | 30 ≤ 5? 否 | 否 | push 10 | [10, 30] |
| 15, 20 | [10, 30] | 10 ≤ 15? **是** | pop 10 | push 20 | [20, 30] |

最后 `len(heap) = 2` ✓

### 19.6 LC 452 Minimum Number of Arrows to Burst Balloons(贪心 + 区间)

#### 题目

x 轴上一排气球,每个用 `[start, end]` 表示。射一支垂直箭可以同时打爆**所有覆盖该 x 坐标**的气球。求**最少箭数**。

```python
points = [[10,16], [2,8], [1,6], [7,12]]
# 射 x=6 → 打爆 [1,6] 和 [2,8]
# 射 x=10 或 x=12 → 打爆 [10,16] 和 [7,12]
# 答案 2
```

#### 思路:按 **end** 排序,贪心射箭

跟 LC 435 几乎一样,**按 end 排序**:每次取**结束最早**的气球,在它的 end 处射一支箭,**所有 start ≤ 这个 end 的气球都被打爆**。

```python
def findMinArrowShots(points):
    if not points:
        return 0
    points.sort(key=lambda x: x[1])         # 按 end 排序
    arrows = 1
    arrow_pos = points[0][1]                # 第一支箭射在第一个气球的 end
    
    for start, end in points[1:]:
        if start > arrow_pos:               # 这箭打不到当前气球
            arrows += 1
            arrow_pos = end                 # 新箭射在这个气球的 end
    
    return arrows
```

#### 跟 LC 435 的关系

| | LC 435 | LC 452 |
|---|---|---|
| 问 | 删几个能不重叠 | 几支箭能打爆 |
| 排序 key | end | end |
| 思路 | 保留 end 早的,删后面重叠的 | 用一支箭打掉所有当前重叠的 |

**两题本质相同**:都是按 end 排序,贪心处理。

---

### 19.7 LC 228 Summary Ranges(连续区间合并)

#### 题目

给一个**已排序、无重复**的整数数组,**总结成连续范围**。

```python
nums = [0, 1, 2, 4, 5, 7]
# 输出 ["0->2", "4->5", "7"]
```

#### 思路:遍历找断点

```python
def summaryRanges(nums):
    if not nums:
        return []
    result = []
    start = nums[0]
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1] + 1:         # 不连续了
            if start == nums[i-1]:
                result.append(str(start))
            else:
                result.append(f"{start}->{nums[i-1]}")
            start = nums[i]
    # 处理最后一段
    if start == nums[-1]:
        result.append(str(start))
    else:
        result.append(f"{start}->{nums[-1]}")
    return result
```

#### 复杂度

- 时间:O(n)
- 空间:O(1)(不算输出)

#### 一句话记忆

> 维护 `start`,遇到断点(`nums[i] != nums[i-1] + 1`)就结算一段。

---

### 19.8 区间套路一句话记忆

```
合并区间(LC 56):    排序 + 看上一个的 end vs 当前的 start
插入区间(LC 57):    分三段(前/重叠/后)
会议室数量(LC 253): 排序 + min-heap 装 end,堆顶 ≤ start 就 pop
重叠判断公式:       a <= d AND c <= b
```

---

<a id="ch20"></a>

## 二十、Backtracking(回溯)⭐⭐

> **中频**,但是**不会就完全做不出来**。微软偶尔考。所有"找所有 / 列出所有 / 全排列 / 所有组合"的题用 backtracking。

### 20.1 什么是 Backtracking?

**回溯 = 递归 + 撤销**。像走迷宫:试一条路走到底,**走不通就退回来试另一条**。

**核心模板**:
```python
def backtrack(path, choices):
    if 满足结束条件:
        result.append(path[:])         # 注意复制!
        return
    for choice in choices:
        path.append(choice)            # 1. 做选择
        backtrack(path, new_choices)   # 2. 递归往下
        path.pop()                     # 3. 撤销选择(关键!)
```

**三步**:
1. **做选择**(添加到 path)
2. **递归**(进入下一层)
3. **撤销**(从 path 移除,回到选择前的状态)

### 20.2 经典题 1:LC 78 Subsets(所有子集)

#### 题目

```python
nums = [1, 2, 3]
# 输出所有子集:[[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]
# 共 2^n = 8 个
```

#### 代码

```python
def subsets(nums):
    result = []
    
    def backtrack(start, path):
        result.append(path[:])         # 每个 path 都是答案
        for i in range(start, len(nums)):
            path.append(nums[i])       # 选 nums[i]
            backtrack(i + 1, path)     # 往后递归(用 i+1 防重复)
            path.pop()                 # 撤销
    
    backtrack(0, [])
    return result
```

#### 走一遍 `[1, 2, 3]`(树形展开)

```
                       []
            ┌──────────┼──────────┐
           [1]        [2]        [3]
        ┌──┴──┐      [2,3]
       [1,2] [1,3]
        │
       [1,2,3]
```

`start` 参数避免重复:递归时只看 `i+1` 之后的元素。

#### 为什么 `path[:]`?

**Python 的 list 是引用类型**。如果直接 `result.append(path)`,后续 `path.pop()` 会**改变之前 append 进去的引用**!

```python
result.append(path)        # ❌ 后面 pop 会改变这个引用
result.append(path[:])     # ✅ 复制一份,独立保存
result.append(list(path))  # ✅ 等价
```

### 20.3 经典题 2:LC 46 Permutations(全排列)

#### 题目

```python
nums = [1, 2, 3]
# 输出 [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
# 共 n! = 6 个
```

#### 代码

```python
def permute(nums):
    result = []
    
    def backtrack(path):
        if len(path) == len(nums):
            result.append(path[:])
            return
        for num in nums:
            if num in path:            # 已选过,跳过
                continue
            path.append(num)
            backtrack(path)
            path.pop()
    
    backtrack([])
    return result
```

#### 跟 Subsets 的区别

| | Subsets | Permutations |
|---|---|---|
| 顺序重要吗 | 否(`[1,2]` == `[2,1]`) | **是**(`[1,2]` ≠ `[2,1]`) |
| 防重复方式 | `start` 参数(只看 i+1 之后) | `if num in path` 跳过已选 |
| 结束条件 | 无(每个 path 都是答案) | `len(path) == len(nums)` |
| 数量 | 2^n | n! |

### 20.4 经典题 3:LC 22 Generate Parentheses

#### 题目

生成所有 n 对**合法**括号组合。

```python
n = 3
# 输出 ["((()))", "(()())", "(())()", "()(())", "()()()"]
```

#### 思路:用 left 和 right 计数,只在合法时往下走

```python
def generateParenthesis(n):
    result = []
    
    def backtrack(path, left, right):
        if len(path) == 2 * n:
            result.append("".join(path))
            return
        if left < n:
            path.append("(")
            backtrack(path, left + 1, right)
            path.pop()
        if right < left:               # 关键:右括号数不能超过左括号
            path.append(")")
            backtrack(path, left, right + 1)
            path.pop()
    
    backtrack([], 0, 0)
    return result
```

**核心约束**:
- `left < n` 才能加 `(`(没用完)
- `right < left` 才能加 `)`(否则会出现 `()))` 这种不合法)

### 20.5 Backtracking 三个适用信号

题目里出现这些词,**优先想 backtracking**:

1. **"找所有 / 列出所有"**(All subsets, All permutations, All paths)
2. **"组合 / 排列"**(Combinations, Permutations, k 个)
3. **"穷举 / 枚举"**(N-Queens, Sudoku Solver)

### 20.6 Backtracking 模板速记

```python
def backtrack(path, choices):
    if 满足结束条件:
        result.append(path[:])     # 注意复制
        return
    for choice in choices:
        if 不合法:
            continue
        path.append(choice)         # 做选择
        backtrack(path, new_choices)
        path.pop()                  # 撤销选择
```

### 20.7 一句话记忆

```
Backtracking = 递归 + 撤销
三步:做选择 → 递归 → 撤销
result.append(path[:]) 必须复制
Subsets 用 start;Permutations 用 visited 或 in path
```

---

<a id="ch21"></a>

## 二十一、Prefix Sum(前缀和)⭐⭐

> **中频**。LC 560 之前在 §3.7 套路 4 讲过,这里独立成章便于复习。**核心:用 O(n) 预处理换 O(1) 区间查询**。

### 21.1 什么是前缀和?

**前缀和数组 `prefix[i]` = 原数组 `nums[0..i-1]` 的和**。

```python
nums    = [3, 1, 4, 1, 5, 9, 2, 6]
prefix  = [0, 3, 4, 8, 9, 14, 23, 25, 31]
#          ↑  ↑  ↑  ↑
#          空 [3] [3,1] [3,1,4]
```

**核心公式**:
```python
sum(nums[i..j]) = prefix[j+1] - prefix[i]
```

意思:**任意区间和 = 两个前缀和之差**,O(1)。

### 21.2 LC 303 Range Sum Query - Immutable(入门)

#### 题目

给数组,多次查询任意区间和。

```python
nums = [-2, 0, 3, -5, 2, -1]
sumRange(0, 2)   # nums[0..2] = -2+0+3 = 1
sumRange(2, 5)   # nums[2..5] = 3-5+2-1 = -1
```

#### 代码

```python
class NumArray:
    def __init__(self, nums):
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)
    
    def sumRange(self, i, j):
        return self.prefix[j + 1] - self.prefix[i]
```

#### 复杂度

- 预处理:O(n)
- 每次查询:**O(1)**(暴力是 O(n))

如果只查 1 次,前缀和不划算;**查询多次时优势巨大**。

### 21.3 LC 560 Subarray Sum Equals K(进阶)

(这题的完整推导在 §3.7 套路 4 已经讲过,这里只放速记版)

```python
def subarraySum(nums, k):
    count = 0
    prefix_sum = 0
    seen = {0: 1}                        # 前缀和 → 出现次数
    for num in nums:
        prefix_sum += num
        need = prefix_sum - k
        if need in seen:
            count += seen[need]
        seen[prefix_sum] = seen.get(prefix_sum, 0) + 1
    return count
```

**核心**:`prefix_sum - need = k` → `need = prefix_sum - k`。出现过 `need` 多少次,就有多少个子数组和为 k。

### 21.4 LC 1413 Minimum Value to Get Positive Step by Step Sum

#### 题目

给数组,初始值是某个数 `startValue`,从左往右累加。问 `startValue` 至少要多少,才能保证累加过程中**任何时刻 ≥ 1**?

```python
nums = [-3, 2, -3, 4, 2]
# startValue = 5 时:
# 5 + (-3) = 2  ≥ 1
# 2 + 2 = 4    ≥ 1
# 4 + (-3) = 1 ≥ 1
# ...
# startValue = 4 时第三步会 0,不行。所以最少 5。
```

#### 代码

```python
def minStartValue(nums):
    prefix_sum = 0
    min_prefix = 0
    for num in nums:
        prefix_sum += num
        min_prefix = min(min_prefix, prefix_sum)
    return 1 - min_prefix    # 让最低点也 ≥ 1
```

**思路**:找出累加过程中"最低谷",起始值至少要让这个最低点 ≥ 1。

### 21.5 前缀和适用场景

- **多次查询区间和**(immutable 数组 → 前缀和;mutable → 树状数组,这次面试不用学)
- **子数组和为 K**(配合 hash map)
- **累加过程的极值**(如 LC 1413)
- **二维前缀和**(LC 304 二维区间和,进阶)

### 21.6 一句话记忆

```
prefix[i] = nums[0..i-1] 的和
区间和 = prefix[j+1] - prefix[i]
预处理 O(n) + 查询 O(1)
配合 hash map → 子数组和为 K(LC 560)
```

---

<a id="ch22"></a>

## 二十二、Matrix Traversal(矩阵遍历)⭐

> **网格题专题**。LC 200 网格 DFS 在 §12.4 已经讲过,这里补充几个变形。

### 22.1 矩阵遍历四方向数组(必背)

```python
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]    # 上下左右
# 八方向加上对角线:
EIGHT_DIRECTIONS = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
```

### 22.2 网格 DFS 模板(LC 200 Number of Islands)

```python
def numIslands(grid):
    if not grid: return 0
    rows, cols = len(grid), len(grid[0])
    count = 0
    
    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return
        grid[r][c] = '0'                   # 标记访问(原地改,省 visited)
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            dfs(r + dr, c + dc)
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)
    return count
```

### 22.3 LC 733 Flood Fill(简单 DFS)

#### 题目

给一个图像(2D 数组),从 `(sr, sc)` 出发,把所有相连的同色像素改成新颜色。

```python
image = [[1,1,1],
         [1,1,0],
         [1,0,1]]
sr, sc = 1, 1
new_color = 2
# 输出 [[2,2,2], [2,2,0], [2,0,1]](注意右下的 1 不连通,不变)
```

#### 代码

```python
def floodFill(image, sr, sc, color):
    original = image[sr][sc]
    if original == color:                   # 防止无限递归(已经是目标色)
        return image
    
    def dfs(r, c):
        if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]):
            return
        if image[r][c] != original:
            return
        image[r][c] = color
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            dfs(r + dr, c + dc)
    
    dfs(sr, sc)
    return image
```

⚠️ **关键 bug**:如果新 color 跟原 color 相同,且不加 `if original == color: return`,会**无限递归**(改完色后还满足"等于原色")。

### 22.4 LC 54 Spiral Matrix(螺旋遍历)

#### 题目

按螺旋顺序输出矩阵元素。

```python
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
# 输出 [1,2,3,6,9,8,7,4,5]
```

#### 代码:四个边界缩进

```python
def spiralOrder(matrix):
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        # 上边:left → right
        for c in range(left, right + 1):
            result.append(matrix[top][c])
        top += 1
        
        # 右边:top → bottom
        for r in range(top, bottom + 1):
            result.append(matrix[r][right])
        right -= 1
        
        # 下边:right → left(注意检查行还在)
        if top <= bottom:
            for c in range(right, left - 1, -1):
                result.append(matrix[bottom][c])
            bottom -= 1
        
        # 左边:bottom → top
        if left <= right:
            for r in range(bottom, top - 1, -1):
                result.append(matrix[r][left])
            left += 1
    
    return result
```

**思路**:维护 4 个边界 `top, bottom, left, right`,每走完一边就缩进。

### 22.5 LC 48 Rotate Image ⭐⭐(Microsoft 经典)

#### 题目

将 n×n 矩阵**原地**顺时针旋转 90°(不能用额外矩阵)。

```python
matrix = [[1, 2, 3],          rotated = [[7, 4, 1],
          [4, 5, 6],     →               [8, 5, 2],
          [7, 8, 9]]                     [9, 6, 3]]
```

#### 思路:转置 + 水平翻转(两步法)

**核心洞察**:顺时针旋转 90° = **转置(沿主对角线翻转) + 每行水平翻转**

```python
def rotate(matrix):
    n = len(matrix)
    
    # Step 1: 转置(沿对角线翻转)
    for i in range(n):
        for j in range(i + 1, n):       # 注意 j 从 i+1 开始(只翻一半)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Step 2: 每行水平翻转
    for row in matrix:
        row.reverse()
```

#### 走一遍 `[[1,2,3],[4,5,6],[7,8,9]]`

**Step 1 转置后**:
```
[1, 4, 7]
[2, 5, 8]
[3, 6, 9]
```

**Step 2 每行 reverse 后**:
```
[7, 4, 1]
[8, 5, 2]
[9, 6, 3]   ✓
```

#### 为什么内层 `j` 从 `i + 1` 开始?

如果 `j` 从 0 开始,会**翻两次等于没翻**:
```python
swap(matrix[0][1], matrix[1][0])   # 翻一次
swap(matrix[1][0], matrix[0][1])   # 翻回来,白干!
```
所以只翻**对角线右上方**那一半三角形。

#### 复杂度

- 时间:O(n²)
- 空间:**O(1)**(原地操作)

#### 一句话记忆

> **转置 + 行翻转 = 顺时针 90°**
> **转置 + 列翻转 = 逆时针 90°**

---

### 22.6 LC 73 Set Matrix Zeroes(原地标记技巧)

#### 题目

如果矩阵某个元素是 0,把它所在的**整行整列**都变成 0(原地)。

```python
matrix = [[1, 1, 1],          [[1, 0, 1],
          [1, 0, 1],     →     [0, 0, 0],
          [1, 1, 1]]            [1, 0, 1]]
```

#### 朴素思路 vs 进阶思路

##### 朴素思路:O(m+n) 空间

用两个 set 记录"哪些行/列要清零":

```python
def setZeroes(matrix):
    rows, cols = set(), set()
    m, n = len(matrix), len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)
    for i in range(m):
        for j in range(n):
            if i in rows or j in cols:
                matrix[i][j] = 0
```

##### 进阶思路:O(1) 空间(用第一行/列当标记)

**面试官最常追问**:能不能不用额外空间?

技巧:**用矩阵自己的第一行和第一列当标记数组**。

```python
def setZeroes(matrix):
    m, n = len(matrix), len(matrix[0])
    first_row_zero = any(matrix[0][j] == 0 for j in range(n))
    first_col_zero = any(matrix[i][0] == 0 for i in range(m))
    
    # Step 1: 用第一行/列标记
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    
    # Step 2: 根据标记清零(除第一行第一列)
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    
    # Step 3: 单独处理第一行/列
    if first_row_zero:
        for j in range(n):
            matrix[0][j] = 0
    if first_col_zero:
        for i in range(m):
            matrix[i][0] = 0
```

#### 一句话记忆

> 矩阵的**第一行第一列**充当"哪些行哪些列要清零"的标记。

---

### 22.7 LC 36 Valid Sudoku(数独验证,常见 Hash Set 应用)

#### 题目

验证一个 9×9 数独**当前状态**是否合法(不要求能否解出)。规则:每行、每列、每个 3×3 宫格内 1-9 不能重复。

#### 解法:三组 Hash Set(行、列、宫格)

```python
def isValidSudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    
    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == '.':
                continue
            b = (r // 3) * 3 + c // 3           # 3×3 宫格编号 0-8
            if val in rows[r] or val in cols[c] or val in boxes[b]:
                return False
            rows[r].add(val)
            cols[c].add(val)
            boxes[b].add(val)
    return True
```

#### 关键公式:宫格编号

```python
box_index = (row // 3) * 3 + col // 3
```

- `row // 3` ∈ {0, 1, 2}:宫格所在大行
- `col // 3` ∈ {0, 1, 2}:宫格所在大列
- 二维转一维:`大行 × 3 + 大列`

---

### 22.8 矩阵题五大模式

| 题型 | 解法 | 经典题 |
|---|---|---|
| **连通块计数** | DFS / BFS,标记访问 | LC 200, 695 |
| **染色 / 填充** | DFS 从起点扩散 | LC 733, 130 |
| **路径 / 螺旋** | 维护方向或边界 | LC 54, 59 |
| **原地旋转/翻转** | 转置 + 翻转(组合操作) | LC 48 |
| **原地标记 / 验证** | 用矩阵自身或 Hash Set | LC 73, 36 |

### 22.9 一句话记忆

```
四方向数组 [(-1,0), (1,0), (0,-1), (0,1)] 必背
网格 DFS:边界检查 + visited 标记 + 四方向递归
连通块用 DFS,最短路径用 BFS
螺旋遍历:维护四个边界 top/bottom/left/right
```

---

<a id="ch23"></a>

## 二十三、Dynamic Programming(动态规划)⭐ 小白入门版

> **新内容**!Mock 不一定考,但**长期必学**。这一节用最浅显的方式讲清楚 DP 是什么、怎么写。

### 23.1 什么是 DP?用一个故事说明

#### 一个超简单的例子:爬楼梯

> 楼梯有 n 阶,每次只能爬 1 阶或 2 阶。问爬到第 n 阶有多少种走法?

`n = 1`:只有 1 种(爬 1 阶)
`n = 2`:2 种(1+1 或 2)
`n = 3`:3 种(1+1+1, 1+2, 2+1)
`n = 4`:5 种
`n = 5`:8 种
...

观察规律:**1, 2, 3, 5, 8, 13...** —— 是斐波那契!为什么?

#### 关键洞察:递推关系

> **爬到第 n 阶的方法数 = 爬到第 n-1 阶的方法数 + 爬到第 n-2 阶的方法数**

为什么?因为最后一步要么是从 n-1 跨 1 阶上来,要么是从 n-2 跨 2 阶上来。

```
ways(n) = ways(n-1) + ways(n-2)
```

**这就是 DP 的本质**:**把大问题拆成小问题,小问题的答案能"组装"出大问题的答案**。

### 23.2 DP 的两个核心

任何 DP 题都要回答这两个问题:

1. **状态(state)**:`dp[i]` 代表什么?(必须明确定义)
2. **转移(transition)**:`dp[i]` 怎么从更小的 `dp[?]` 得到?

**爬楼梯**的回答:
- 状态:`dp[i]` = 爬到第 i 阶的方法数
- 转移:`dp[i] = dp[i-1] + dp[i-2]`
- 初始:`dp[1] = 1`, `dp[2] = 2`

代码:
```python
def climbStairs(n):
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```

#### 空间优化:只用两个变量

注意每次只需要 `dp[i-1]` 和 `dp[i-2]`,**不用整个数组**:

```python
def climbStairs(n):
    if n <= 2:
        return n
    a, b = 1, 2                # a = dp[i-2], b = dp[i-1]
    for _ in range(3, n + 1):
        a, b = b, a + b        # 滚动更新
    return b
```

**空间从 O(n) 降到 O(1)**,这种技巧叫"**滚动数组**"。

### 23.3 DP 解题 4 步法(背下来!)

任何 DP 题用这 4 步思考:

1. **定义状态**:`dp[i]`(或 `dp[i][j]`)代表什么?
2. **写出转移方程**:`dp[i] = f(dp[i-1], dp[i-2], ...)`
3. **确定初始值**:`dp[0]`, `dp[1]` 等边界
4. **决定遍历顺序**:从前往后还是从后往前?

### 23.4 经典题 1:LC 70 Climbing Stairs(已讲)

见 23.2,**爬楼梯是 DP 入门第一题,务必能闭眼写**。

### 23.5 经典题 2:LC 198 House Robber(打家劫舍)

#### 题目

> 沿街有一排房子,每个房子里有钱。但**相邻两家不能同时偷**(会触发警报)。问最多能偷多少钱?

```python
nums = [2, 7, 9, 3, 1]
# 偷 2,9,1 = 12
# 偷 7,3 = 10
# 偷 2,9 = 11
# 最优:12
```

#### 4 步分析

1. **状态**:`dp[i]` = 考虑前 i 个房子能偷到的最大金额
2. **转移**:对第 i 个房子,**两种选择**:
   - **偷**:`dp[i-2] + nums[i]`(必须跳过 i-1)
   - **不偷**:`dp[i-1]`(继承前一个的最优)
   - 取较大值:`dp[i] = max(dp[i-1], dp[i-2] + nums[i])`
3. **初始值**:`dp[0] = nums[0]`, `dp[1] = max(nums[0], nums[1])`
4. **顺序**:从前往后

#### 代码

```python
def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    
    return dp[-1]
```

#### 走一遍 `[2, 7, 9, 3, 1]`

| i | nums[i] | dp[i-2] + nums[i] | dp[i-1] | dp[i] = max |
|---|---|---|---|---|
| 0 | 2 | - | - | **2** |
| 1 | 7 | - | - | max(2, 7) = **7** |
| 2 | 9 | 2 + 9 = 11 | 7 | **11** |
| 3 | 3 | 7 + 3 = 10 | 11 | **11** |
| 4 | 1 | 11 + 1 = 12 | 11 | **12** ✓ |

#### 空间优化版

```python
def rob(nums):
    prev, curr = 0, 0
    for num in nums:
        prev, curr = curr, max(curr, prev + num)
    return curr
```

### 23.6 经典题 3:LC 53 Maximum Subarray(最大子数组和)

#### 题目

> 找连续子数组,使它的和最大。

```python
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# 最大和子数组 [4,-1,2,1] = 6
```

#### 4 步分析

1. **状态**:`dp[i]` = **以 i 结尾**的最大子数组和(注意不是"前 i 个里的最大",而是必须以 i 结尾)
2. **转移**:对位置 i,两种选择:
   - **接到前面**:`dp[i-1] + nums[i]`
   - **重新开始**:`nums[i]`(单独以 i 起头)
   - 取较大:`dp[i] = max(dp[i-1] + nums[i], nums[i])`
3. **初始值**:`dp[0] = nums[0]`
4. **答案**:不是 `dp[-1]`,而是**整个 dp 数组的最大值**(因为最优可能在中间结束)

#### 代码

```python
def maxSubArray(nums):
    dp = [0] * len(nums)
    dp[0] = nums[0]
    max_sum = dp[0]
    
    for i in range(1, len(nums)):
        dp[i] = max(dp[i-1] + nums[i], nums[i])
        max_sum = max(max_sum, dp[i])
    
    return max_sum
```

#### 空间优化(就是 Kadane's algorithm)

```python
def maxSubArray(nums):
    curr_sum = max_sum = nums[0]
    for num in nums[1:]:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    return max_sum
```

### 23.7 经典题 4(进阶):LC 918 Maximum Sum Circular Subarray

#### 题目

跟 LC 53 一样,但数组是**环形**(末尾接回开头)。

```python
nums = [5, -3, 5]
# 普通最大子数组:[5] 或 [5,-3,5] → 7
# 环形:可以是 [5, 5](首尾相连)= 10  ← 答案
```

#### 关键思路:**两种情况取较大**

环形最大子数组**要么**:
1. **不跨越边界** → 就是普通 LC 53 答案
2. **跨越边界**(用了首尾) → **总和 - 中间最小子数组和**

```
情况 2 示意:
nums = [5, -3, 5]
跨越边界 [5, 5] 的和 = 总和 10 - 中间 [-3] 的和 = 7 ?
实际上 = 10 - (-3) = 13?? 错!
正确:跨边界选了 [5, 5](首尾各一个 5),没选中间 -3
总和 = 5 + (-3) + 5 = 7
最小子数组和 = -3
跨边界最大和 = 总和 - 最小子数组和 = 7 - (-3) = 10 ✓
```

#### 代码

```python
def maxSubarraySumCircular(nums):
    total = sum(nums)
    
    # 情况 1:普通 Kadane 找最大
    max_sum = curr_max = nums[0]
    # 情况 2:Kadane 反向找最小
    min_sum = curr_min = nums[0]
    
    for num in nums[1:]:
        curr_max = max(num, curr_max + num)
        max_sum = max(max_sum, curr_max)
        curr_min = min(num, curr_min + num)
        min_sum = min(min_sum, curr_min)
    
    # 特殊情况:全是负数,min_sum == total,total - min_sum = 0,但实际答案应是 max_sum
    if max_sum < 0:
        return max_sum
    return max(max_sum, total - min_sum)
```

#### 为什么"全是负数"要特殊处理?

如果 `nums = [-3, -2, -1]`:
- `total = -6`, `max_sum = -1`(最不糟糕的一个), `min_sum = -6`(全部)
- `total - min_sum = -6 - (-6) = 0`,**但 0 不在数组里**(子数组不能为空!)
- 正确答案是 `-1`

所以必须特判:**`max_sum < 0` 意味着全是负数,直接返回 max_sum**。

#### 一句话记忆

> 环形最大子数组 = `max(普通最大, 总和 - 最小子数组)`,但全负时返回 max_sum。

---

### 23.8 经典题 5:LC 300 Longest Increasing Subsequence

#### 题目

> 找最长**严格递增**子序列(可以不连续)。

```python
nums = [10, 9, 2, 5, 3, 7, 101, 18]
# 最长递增子序列:[2, 3, 7, 18] 或 [2, 3, 7, 101],长度 4
```

#### 4 步分析

1. **状态**:`dp[i]` = 以 i 结尾的最长递增子序列长度
2. **转移**:对每个 i,看前面所有 j (j < i):
   - 如果 `nums[j] < nums[i]`,可以接在 j 后面:`dp[i] = max(dp[i], dp[j] + 1)`
3. **初始值**:`dp[i] = 1`(每个元素自己就是长度 1)
4. **答案**:`max(dp)`

#### 代码

```python
def lengthOfLIS(nums):
    n = len(nums)
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)
```

#### 复杂度

- 时间:**O(n²)**(双层循环)
- 空间:O(n)

(进阶:用二分能优化到 O(n log n),但面试 O(n²) 已经过关)

### 23.8 DP 入门必做题(由易到难)

| 题号 | 题目 | 状态定义 | 难度 |
|---|---|---|---|
| **LC 70** | Climbing Stairs | `dp[i]` 爬到 i 阶方法数 | ⭐ |
| **LC 198** | House Robber | `dp[i]` 前 i 家最大金额 | ⭐ |
| **LC 53** | Maximum Subarray | `dp[i]` 以 i 结尾的最大和 | ⭐ |
| **LC 121** | Best Time to Buy/Sell Stock | 维护历史最低价 | ⭐ |
| **LC 300** | LIS | `dp[i]` 以 i 结尾的最长递增 | ⭐⭐ |
| **LC 322** | Coin Change | `dp[i]` 凑出 i 的最少硬币数 | ⭐⭐ |
| **LC 1143** | Longest Common Subsequence | `dp[i][j]` 两个串的 LCS | ⭐⭐ |
| **LC 72** | Edit Distance | `dp[i][j]` s 变 t 的最少操作 | ⭐⭐⭐ |

### 23.9 DP 题判断信号

题目里出现这些词,**优先想 DP**:

1. **"最大 / 最小"**(Max / Min subarray, sum, length)
2. **"多少种方法"**(How many ways)
3. **"是否能"**(Can you reach, Can you make)
4. **"最长 / 最短"**(Longest / Shortest)

### 23.10 DP vs Backtracking 对比

| | DP | Backtracking |
|---|---|---|
| 用途 | 求**最优值或方案数** | 列出**所有方案** |
| 关键 | 状态 + 转移 | 选择 + 撤销 |
| 复杂度 | 通常多项式 | 通常指数 |
| 例题 | LC 70, 198, 300 | LC 78, 46, 22 |

### 23.11 一句话记忆

```
DP 4 步:状态 → 转移 → 初始 → 顺序
LC 70:dp[i] = dp[i-1] + dp[i-2]
LC 198:dp[i] = max(dp[i-1], dp[i-2] + nums[i])
LC 53:dp[i] = max(dp[i-1] + nums[i], nums[i])
LC 300:dp[i] = max(dp[j] + 1 for j < i if nums[j] < nums[i])
能用滚动数组的就用,空间 O(n) → O(1)
```

### 23.12 学 DP 的建议

DP 不是一两天能"会"的,需要刷至少 20 题才能形成直觉。建议:

1. **先把 23.8 的前 4 题(LC 70, 198, 53, 121)反复做 3 遍**,直到能闭眼写
2. **每做一题,显式写出 4 步**(状态/转移/初始/顺序),不要直接抄代码
3. **DP 一定要画"状态转移图"或"表格"**,不要纯靠脑子推
4. 行有余力再挑战 LC 300, 322, 1143
5. 最难的字符串 DP(LC 72)留到后面,**mock 不会考**

---

<a id="ch24"></a>

## 二十四、Greedy(贪心算法)⭐⭐⭐

> **高频**!Greedy 跟 Intervals 是亲兄弟,跟 DP 是表亲。**核心:每一步都做"局部最优"选择,期望得到全局最优**。

### 24.1 什么是 Greedy?

**Greedy = 每一步都做当前看起来最好的选择**,**不回头不悔棋**。

#### Greedy vs DP 的核心区别

| | DP | Greedy |
|---|---|---|
| 思路 | 试所有可能,记录最优 | 每步做局部最优选择 |
| 复杂度 | 通常 O(n²) 或 O(n×m) | 通常 O(n log n) |
| 可行性 | 总能解出最优 | **必须证明局部最优 → 全局最优** |
| 难点 | 状态定义 | **找出正确的贪心策略** |

**注意**:不是所有问题都能用 greedy。**用错了 greedy 会得到错误答案**(局部最优 ≠ 全局最优)。

#### 一个反例:看为什么 greedy 不一定行

> 给硬币面值 `[1, 3, 4]`,凑出 `6`,问最少需要几枚?

**Greedy 思路**:每次拿最大的不超过剩余值的硬币
- 先拿 4,剩 2
- 再拿 1,剩 1
- 再拿 1,剩 0
- 总共 **3 枚** ❌

**实际最优**:`3 + 3 = 6`,只需 **2 枚** ✓

所以**这题 Greedy 错了,必须用 DP**(LC 322 Coin Change)。

### 24.2 Greedy 适用判断:能不能贪?

只有当问题满足**贪心选择性质**时才能用:

> **贪心选择性质**:每一步的局部最优,**不会破坏后续步骤的最优解**。

**判断套路**(凭经验):
- 题目允许排序后处理 → 大概率 greedy
- 题目是"最少 / 最多 / 最大 / 最小" + 某种线性扫描就能解 → 试 greedy
- 不确定时:**先用 greedy 试,找反例**;找不到反例就用,找到了换 DP

### 24.3 经典题 1:LC 55 Jump Game

#### 题目

数组每个元素表示**从该位置最多能跳几步**,问能否从起点跳到终点。

```python
nums = [2, 3, 1, 1, 4]    # True(0→1→4 或 0→2→3→4)
nums = [3, 2, 1, 0, 4]    # False(到 index 3 就走不动了)
```

#### Greedy 思路

**维护当前能到达的最远位置 `farthest`**。遍历每个位置 i,如果 i 在 farthest 范围内,更新 farthest。如果 farthest 到达终点就成功。

```python
def canJump(nums):
    farthest = 0
    for i in range(len(nums)):
        if i > farthest:               # 当前位置不可达
            return False
        farthest = max(farthest, i + nums[i])
        if farthest >= len(nums) - 1:  # 已经能到终点
            return True
    return True
```

#### 走一遍 `[2, 3, 1, 1, 4]`

| i | nums[i] | i + nums[i] | farthest 更新后 |
|---|---|---|---|
| 0 | 2 | 2 | 2 |
| 1 | 3 | 4 | **4(已 >= len-1=4)** → return True |

**复杂度**:O(n) 时间,O(1) 空间。

#### 为什么这个 greedy 是对的?

**关键证明思路**:如果在某个位置 i 能到达,且当前 farthest >= i,那么所有 0..i 之间的位置都可达。**只要 farthest 一直能 >= 当前位置,就不会卡住**。

### 24.4 经典题 2:LC 122 Best Time to Buy and Sell Stock II

#### 题目

可以**多次买卖**股票,但同一时刻只能持有一只。求最大利润。

```python
prices = [7, 1, 5, 3, 6, 4]
# 最优:1 买 5 卖(赚 4)+ 3 买 6 卖(赚 3)= 7
```

#### Greedy 思路

**只要明天比今天涨,就今天买明天卖**。把所有上涨段累加。

```python
def maxProfit(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    return profit
```

#### 直觉

任何涨幅都是利润的一部分,既然能多次交易,就**把每段上涨都吃掉**。

### 24.5 经典题 3:LC 435 Non-overlapping Intervals(贪心 + 区间)

#### 题目

给一组区间,**最少删除多少个**,能让剩下的都不重叠?

```python
intervals = [[1,2], [2,3], [3,4], [1,3]]
# 删 [1,3] 后剩 [[1,2],[2,3],[3,4]] 不重叠
# 答案 1
```

#### Greedy 思路:**按结束时间排序**,贪心保留结束最早的

**关键**:不是按 start 排序,**是按 end 排序**!

```python
def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda x: x[1])     # 按 end 排序!
    count = 0
    end = float('-inf')
    for start, e in intervals:
        if start >= end:
            end = e                        # 不重叠,保留
        else:
            count += 1                     # 重叠,删除当前
    return count
```

#### 为什么按 end 排序?

**直觉**:每次保留**结束最早**的区间,给后面的区间留出最大空间。

如果按 start 排序,你可能保留一个超长的区间,挤占了 后续多个短区间的空间。

### 24.6 Greedy + Intervals 的常见组合

很多区间题既可以用 Intervals 套路,也可以用 Greedy 套路。**核心区别就是排序的 key**:

| 题 | 排序 key | 思路 |
|---|---|---|
| LC 56 Merge Intervals | **start** | 合并重叠 |
| LC 253 Meeting Rooms II | **start** + heap of end | 算最大同时占用 |
| LC 435 Non-overlapping | **end** | 保留结束最早的 |
| LC 452 Min Arrows to Burst Balloons | **end** | 类似 LC 435 |

### 24.7 Greedy 题型识别

题目里出现这些信号,**先试试 greedy**:

1. **"最少 / 最多次数"** + 线性扫描可解
2. **可以排序后逐个处理**
3. **不需要回溯过去的决定**(每一步定下来就不改)
4. **跟区间相关**(很多 interval 题用 greedy)

### 24.8 一句话记忆

```
Greedy = 每步取局部最优,不回头
LC 55:维护 farthest,看是否一直 >= i
LC 122:吃掉每段上涨
LC 435:按 end 排序,保留结束早的
不确定能不能贪 → 试,找反例
```

---

<a id="ch25"></a>

## 二十五、Tries(字典树)⭐⭐

> **中频**。专门处理**字符串前缀**问题。Microsoft 考过 LC 208。

### 25.1 什么是 Trie?

**Trie(发音 "try")** 是一种**树状结构**,每条边代表一个字符,从根到任意节点的路径形成一个字符串前缀。

#### 例子

把 `["cat", "car", "card", "dog"]` 放进 Trie:

```
        root
       /    \
      c      d
      |      |
      a      o
     / \     |
    t   r    g
        |
        d
```

- "cat":root → c → a → t
- "car":root → c → a → r
- "card":root → c → a → r → d
- "dog":root → d → o → g

**节点上需要标记 "是不是某个单词的结尾"**(因为 "car" 和 "card" 共享前缀,要区分)。

### 25.2 Trie 的优势

| 操作 | Hash Set | Trie |
|---|---|---|
| 查询单词是否存在 | O(L) (L=单词长度) | O(L) |
| **查询前缀是否存在** | O(N×L)(扫所有单词) | **O(L)** |
| **遍历某前缀的所有单词** | O(N×L) | **O(出现次数)** |

**Trie 的杀手级用法:前缀查询**。Hash 做不到。

### 25.3 LC 208 Implement Trie(必背模板)

#### 题目

实现 Trie,支持 `insert`、`search`、`startsWith`。

```python
trie = Trie()
trie.insert("apple")
trie.search("apple")      # True
trie.search("app")        # False(没插入过)
trie.startsWith("app")    # True(有 apple 这个前缀)
trie.insert("app")
trie.search("app")        # True
```

#### 标准实现

```python
class TrieNode:
    def __init__(self):
        self.children = {}             # 字符 → TrieNode
        self.is_end = False            # 是不是某个单词的结尾

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True             # 标记单词结尾
    
    def search(self, word):
        node = self._find(word)
        return node is not None and node.is_end
    
    def startsWith(self, prefix):
        return self._find(prefix) is not None
    
    def _find(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node
```

#### 走一遍

```python
trie.insert("app")
# root → a → p → p (is_end=True)

trie.insert("apple")
# root → a → p → p (is_end=True) → l → e (is_end=True)

trie.search("app")
# 走到 root→a→p→p,is_end = True → return True

trie.search("ap")
# 走到 root→a→p,is_end = False → return False

trie.startsWith("ap")
# 走到 root→a→p,不为 None → return True
```

#### 复杂度

| 操作 | 时间 |
|---|---|
| insert(word) | O(L) |
| search(word) | O(L) |
| startsWith(prefix) | O(L) |

L 是单词长度,**跟单词总数 N 无关**。

### 25.4 LC 211 Design Add and Search Words(支持通配符)

#### 题目

`search("b.d")` 中的 `.` 可以匹配任意字符。

```python
addWord("bad")
addWord("dad")
addWord("mad")
search("pad")     # False
search("bad")     # True
search(".ad")     # True(匹配 bad、dad、mad)
search("b..")     # True(匹配 bad)
```

#### 思路:DFS 处理通配符

```python
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True
    
    def search(self, word):
        return self._dfs(self.root, word, 0)
    
    def _dfs(self, node, word, i):
        if i == len(word):
            return node.is_end
        ch = word[i]
        if ch == ".":
            for child in node.children.values():
                if self._dfs(child, word, i + 1):
                    return True
            return False
        else:
            if ch not in node.children:
                return False
            return self._dfs(node.children[ch], word, i + 1)
```

**核心**:遇到 `.` 时,**对所有 children 递归搜索**,任一成功即可。

### 25.5 LC 212 Word Search II ⭐(Trie + Backtracking 组合)

#### 题目

给一个 2D 字符网格和单词列表,找出所有在网格中能用**相邻字符串接**而成的单词(每个格子在一次搜索中只能用一次)。

```python
board = [['o','a','a','n'],
         ['e','t','a','e'],
         ['i','h','k','r'],
         ['i','f','l','v']]
words = ["oath","pea","eat","rain"]
# 输出 ["oath", "eat"]
```

#### 朴素思路 vs Trie 优化

##### 朴素 O(words × cells × 4^L):对每个单词跑一遍 DFS,会**超时**

##### Trie 优化:把所有单词放进 Trie,网格只扫**一遍**,**O(cells × 4^L)**

#### 完整代码(经典模板)

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None              # 在单词结尾节点存完整单词,方便收集

def findWords(board, words):
    # Step 1: 建 Trie
    root = TrieNode()
    for word in words:
        node = root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.word = word
    
    rows, cols = len(board), len(board[0])
    result = []
    
    # Step 2: DFS + 回溯 + Trie 剪枝
    def dfs(r, c, node):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        ch = board[r][c]
        if ch == '#' or ch not in node.children:
            return                    # 已访问 或 Trie 里没这条路 → 剪枝
        
        next_node = node.children[ch]
        if next_node.word:
            result.append(next_node.word)
            next_node.word = None     # 防止重复收集同一个单词
        
        # 标记 + 四方向 + 撤销
        board[r][c] = '#'
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            dfs(r + dr, c + dc, next_node)
        board[r][c] = ch              # 回溯还原
    
    for r in range(rows):
        for c in range(cols):
            dfs(r, c, root)
    
    return result
```

#### 三个关键技巧

##### 1. `node.word = word`(在叶节点存完整单词)

不需要在 DFS 中手动拼字符串,**直接读叶节点存好的 word**,代码更简洁。

##### 2. `next_node.word = None`(防重复收集)

如果有两条路径都拼出同一个单词,只收集一次。

##### 3. `board[r][c] = '#'` 标记访问 + 回溯还原

**回溯标准动作**:
- 进入前改成 `'#'`(防止本路径循环用)
- 退出时还原(其他路径还能用)

#### 复杂度

- 时间:O(rows × cols × 4^L)(L 是最长单词长度)
- 空间:O(总字符数)用于 Trie

#### 为什么 Trie 是关键?

**Trie 让"对所有单词同时搜索"成为可能**。每走一步只需检查 `ch in node.children` (O(1)),不在则**立即剪枝**,大量节省搜索。

---

### 25.6 Trie 适用场景

| 场景 | 例子 |
|---|---|
| **前缀搜索 / 自动补全** | 搜索引擎、IDE 提示 |
| **单词字典 / 拼写检查** | LC 208, 211, 212 |
| **公共前缀问题** | LC 14 Longest Common Prefix |

### 25.7 一句话记忆

```
Trie = 字符串前缀的树
每个节点存 children dict + is_end 标记
insert/search/startsWith 都是 O(L)
通配符 . → 对所有 children DFS
Word Search II → Trie + 回溯 + 网格 DFS
```

---

<a id="ch26"></a>

## 二十六、Advanced Graphs(高级图算法)⭐⭐

> **中频**。这一节补两个之前 §12 没讲透的:**Union Find** 和 **Dijkstra**。

### 26.1 Union Find(并查集)

**用途**:快速判断"两个节点是否属于同一组",或"图中有几个连通分量"。

#### 26.1.1 Union Find 三大操作

| 操作 | 含义 | 复杂度 |
|---|---|---|
| `find(x)` | 找 x 所在组的代表(根) | 几乎 O(1) |
| `union(x, y)` | 把 x 和 y 合并到同一组 | 几乎 O(1) |
| `connected(x, y)` | x 和 y 是否在同一组 | 几乎 O(1) |

(严格来说是 O(α(n)),反阿克曼函数,实际值 ≤ 4)

#### 26.1.2 标准模板(必背)

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))    # 初始每个节点自己是根
        self.rank = [1] * n             # 树的深度
        self.count = n                  # 连通分量数
    
    def find(self, x):
        # 路径压缩:递归找根,顺手把沿途节点直接挂到根
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False                 # 已经同组
        # 按秩合并:小树挂到大树下
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        self.rank[root_x] += self.rank[root_y]
        self.count -= 1
        return True
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)
```

#### 26.1.3 LC 547 Number of Provinces

#### 题目

给一个邻接矩阵 `isConnected`,问图中有多少个连通分量?

```python
isConnected = [[1,1,0],
               [1,1,0],
               [0,0,1]]
# 答案 2(节点 0,1 一组;节点 2 一组)
```

#### 解法

```python
def findCircleNum(isConnected):
    n = len(isConnected)
    uf = UnionFind(n)
    for i in range(n):
        for j in range(i+1, n):
            if isConnected[i][j] == 1:
                uf.union(i, j)
    return uf.count
```

#### 26.1.4 LC 684 Redundant Connection(检测环)

#### 题目

n 个节点的树多加了一条边变成图,找出这条**多余的边**。

```python
edges = [[1,2], [1,3], [2,3]]
# [2,3] 是多余的(造成 1-2-3 闭环)
```

#### 解法:union 时如果两节点已在同组,这条边就是多余的

```python
def findRedundantConnection(edges):
    uf = UnionFind(len(edges) + 1)
    for u, v in edges:
        if not uf.union(u, v):
            return [u, v]               # union 失败 = 已经连通 = 多余边
```

#### 26.1.5 Union Find 适用场景

- 判断图是否连通
- 计算连通分量数
- 检测图中是否有环(无向图)
- LC 547, 684, 200(网格变形), 261

### 26.2 Dijkstra(单源最短路径)

**用途**:**带权图**中,从一个起点找到到所有其他点的最短距离。

(无权图最短路径用 BFS;有权图用 Dijkstra)

#### 26.2.1 核心思想

**每次从未访问的节点中,选出"距离 source 最近的",更新它邻居的距离。重复直到访问完。**

用 **min-heap** 维护"待访问节点的距离",每次取最近的。

#### 26.2.2 模板

```python
import heapq

def dijkstra(graph, start, n):
    """
    graph: dict, graph[u] = [(v, weight), ...]
    返回 dist[i] = source 到 i 的最短距离
    """
    dist = [float('inf')] * n
    dist[start] = 0
    heap = [(0, start)]                 # (距离, 节点)
    
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue                    # 已经有更短的,跳过
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    
    return dist
```

#### 26.2.3 LC 743 Network Delay Time(经典 Dijkstra)

#### 题目

n 个节点,times 表示边和权重,从节点 k 发信号,所有节点收到的最长用时?

```python
times = [[2,1,1], [2,3,1], [3,4,1]]
n = 4, k = 2
# 从 2 出发:1 距离 1,3 距离 1,4 距离 2
# 答案 2(4 节点最远)
```

#### 解法

```python
import heapq
from collections import defaultdict

def networkDelayTime(times, n, k):
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))
    
    dist = {i: float('inf') for i in range(1, n + 1)}
    dist[k] = 0
    heap = [(0, k)]
    
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                heapq.heappush(heap, (dist[v], v))
    
    max_dist = max(dist.values())
    return max_dist if max_dist < float('inf') else -1
```

#### 26.2.4 复杂度

- 时间:**O((V + E) log V)**(用 min-heap)
- 空间:O(V + E)

#### 26.2.5 适用场景

- **带权图最短路径**(权重必须非负)
- **网络延迟、地图导航**
- LC 743, 787, 1631

### 26.3 Union Find vs Dijkstra 用途对比

| | Union Find | Dijkstra |
|---|---|---|
| 解决什么 | "是否同组""几个连通块" | 带权图最短距离 |
| 数据结构 | parent 数组 | min-heap |
| 时间 | 接近 O(n) | O((V+E) log V) |
| 经典题 | LC 547, 684 | LC 743 |

### 26.4 一句话记忆

```
Union Find:管"分组",find/union/connected,需要路径压缩
Dijkstra: 管"带权最短路",min-heap 取最近,只对非负权重有效
无权图最短路 → BFS;有权图最短路 → Dijkstra
```

---

<a id="ch27"></a>

## 二十七、2-D DP(二维动态规划)⭐⭐

> **进阶**!1-D DP(§23)是入门,2-D DP 才是真正的"大问题"。状态需要**二维表格**。

### 27.1 1-D vs 2-D DP 区别

| | 1-D DP | 2-D DP |
|---|---|---|
| 状态 | `dp[i]` | `dp[i][j]` |
| 例子 | 爬楼梯、打家劫舍 | 编辑距离、最长公共子序列 |
| 空间 | O(n) | O(n×m) |
| 难度 | ⭐ | ⭐⭐⭐ |

### 27.2 经典题 1:LC 1143 Longest Common Subsequence(必学)

#### 题目

给两个字符串,找它们最长**公共子序列**的长度(子序列可以不连续)。

```python
text1 = "abcde"
text2 = "ace"
# 公共子序列:"ace",长度 3
```

#### 4 步分析

1. **状态**:`dp[i][j]` = `text1` 前 i 个字符 和 `text2` 前 j 个字符 的 LCS 长度
2. **转移**:看 `text1[i-1]` 和 `text2[j-1]`(注意下标错位):
   - 如果**相同**:`dp[i][j] = dp[i-1][j-1] + 1`(在小问题基础上 +1)
   - 如果**不同**:`dp[i][j] = max(dp[i-1][j], dp[i][j-1])`(取较大的子问题)
3. **初始值**:`dp[0][?] = 0`,`dp[?][0] = 0`(空串和任何串的 LCS 都是 0)
4. **答案**:`dp[n][m]`

#### 代码

```python
def longestCommonSubsequence(text1, text2):
    n, m = len(text1), len(text2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[n][m]
```

#### 走一遍 `text1="abc"`, `text2="ac"`

|       |   | "" | a | c |
|-------|---|---|---|---|
| **""** | 0 | 0 | 0 | 0 |
| **a**  | 0 | **1** | 1 | 1 |
| **b**  | 0 | 1 | 1 | 1 |
| **c**  | 0 | 1 | 1 | **2** |

`dp[3][2] = 2` ✓("ac" 是公共子序列)

### 27.3 经典题 2:LC 62 Unique Paths

#### 题目

m×n 网格,从左上角走到右下角,**只能向右或向下**,有多少条不同的路径?

```python
m = 3, n = 7
# 答案 28
```

#### 4 步分析

1. **状态**:`dp[i][j]` = 到达 `(i, j)` 的路径数
2. **转移**:`dp[i][j] = dp[i-1][j] + dp[i][j-1]`(从上来或从左来)
3. **初始值**:第一行第一列都是 1(只有一种走法)
4. **答案**:`dp[m-1][n-1]`

#### 代码

```python
def uniquePaths(m, n):
    dp = [[1] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]
```

### 27.4 经典题 3:LC 72 Edit Distance(经典面试题)

#### 题目

给两个字符串 `word1`, `word2`,把 `word1` 变成 `word2` 最少需要几次操作?
- 操作:插入一个字符 / 删除一个字符 / 替换一个字符

```python
word1 = "horse", word2 = "ros"
# horse → rorse(替换 h→r) → rose(删除 r) → ros(删除 e)
# 答案 3
```

#### 4 步分析

1. **状态**:`dp[i][j]` = `word1[0..i-1]` 变 `word2[0..j-1]` 的最少操作数
2. **转移**:看 `word1[i-1]` 和 `word2[j-1]`:
   - **相同**:`dp[i][j] = dp[i-1][j-1]`(不需要操作)
   - **不同**:取三种操作的最小值:
     - 替换:`dp[i-1][j-1] + 1`
     - 删除:`dp[i-1][j] + 1`(从 word1 删一个字符)
     - 插入:`dp[i][j-1] + 1`(往 word1 插一个字符)
3. **初始值**:`dp[0][j] = j`(空串变成长 j 串需要 j 次插入),`dp[i][0] = i`
4. **答案**:`dp[n][m]`

#### 代码

```python
def minDistance(word1, word2):
    n, m = len(word1), len(word2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = i              # 删除 i 个字符
    for j in range(m + 1):
        dp[0][j] = j              # 插入 j 个字符
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(
                    dp[i-1][j-1],     # 替换
                    dp[i-1][j],       # 删除
                    dp[i][j-1]        # 插入
                ) + 1
    
    return dp[n][m]
```

### 27.5 2-D DP 适用场景

- **两个序列 / 字符串的对比**(LCS, Edit Distance)
- **网格路径**(LC 62, 64)
- **背包问题**(LC 416 Partition Equal Subset Sum)

### 27.6 一句话记忆

```
2-D DP:dp[i][j] 通常处理两个序列的关系
LCS:相同 +1,不同取 max
Edit Distance:相同不变,不同取替换/删除/插入的 min + 1
Unique Paths:dp[i][j] = dp[i-1][j] + dp[i][j-1]
```

---

<a id="ch28"></a>

## 二十八、Bit Manipulation(位运算)⭐

> **低频但有套路**。掌握几个常见操作就够,不用深入。

### 28.1 必懂的 6 个位运算

| 运算 | 符号 | 含义 | 例子 |
|---|---|---|---|
| AND | `&` | 都是 1 才是 1 | `5 & 3 = 1`(101 & 011) |
| OR | `\|` | 有一个 1 就是 1 | `5 \| 3 = 7` |
| XOR | `^` | 相同为 0,不同为 1 | `5 ^ 3 = 6` |
| NOT | `~` | 取反 | `~5 = -6` |
| 左移 | `<<` | 乘 2 | `5 << 1 = 10` |
| 右移 | `>>` | 除 2 | `5 >> 1 = 2` |

### 28.2 XOR 的三大神奇性质(必记)

```python
x ^ x = 0           # 自己异或自己 = 0
x ^ 0 = x           # 异或 0 不变
x ^ y ^ x = y       # 满足交换律,可以"抵消"
```

**应用**:**找单独出现的数**(其他都出现两次)。

### 28.3 经典题 1:LC 136 Single Number

#### 题目

数组里**每个数出现两次,只有一个出现一次**。找出那个。

```python
nums = [4, 1, 2, 1, 2]
# 答案 4
```

#### XOR 解法(神奇!)

```python
def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result
```

**原理**:所有出现 2 次的数 XOR 起来都是 0,只有出现 1 次的会留下。

#### 走一遍 `[4, 1, 2, 1, 2]`

```
0 ^ 4 = 4
4 ^ 1 = 5
5 ^ 2 = 7
7 ^ 1 = 6
6 ^ 2 = 4    ✓
```

**复杂度**:O(n) 时间,**O(1) 空间**(用 hash set 是 O(n) 空间)。

### 28.4 经典题 2:LC 191 Number of 1 Bits

#### 题目

数 32 位整数中 1 的个数。

```python
n = 11    # 二进制 1011,有 3 个 1
```

#### 解法 1:逐位检查

```python
def hammingWeight(n):
    count = 0
    while n:
        count += n & 1        # 最后一位是不是 1
        n >>= 1               # 右移一位
    return count
```

#### 解法 2:n & (n-1) 技巧(更快)

```python
def hammingWeight(n):
    count = 0
    while n:
        n &= (n - 1)          # 抹掉最右边的 1
        count += 1
    return count
```

**`n & (n-1)` 会消掉 n 最右边的 1**:
```
n     = 1100
n - 1 = 1011
n & (n-1) = 1000   ← 最右的 1 没了
```

### 28.5 经典题 3:LC 268 Missing Number

#### 题目

数组包含 `[0, n]` 中的 n 个数(缺一个),找出缺的。

```python
nums = [3, 0, 1]
# 范围 [0, 3] 应该有 4 个数,缺 2
```

#### XOR 解法

把所有数 XOR 一遍 + 把 `[0, n]` XOR 一遍。**重复的会抵消,只剩缺的那个**。

```python
def missingNumber(nums):
    result = len(nums)        # 把 n 也 XOR 进去
    for i, num in enumerate(nums):
        result ^= i ^ num
    return result
```

### 28.6 经典题 4:LC 67 Add Binary(二进制加法)

#### 题目

给两个二进制字符串,返回它们的和(也用二进制字符串表示)。

```python
a = "1010", b = "1011"
# 1010 + 1011 = 10101
```

#### 思路:模拟竖式加法

```python
def addBinary(a, b):
    result = []
    carry = 0
    i, j = len(a) - 1, len(b) - 1
    
    while i >= 0 or j >= 0 or carry:
        total = carry
        if i >= 0:
            total += int(a[i])
            i -= 1
        if j >= 0:
            total += int(b[j])
            j -= 1
        result.append(str(total % 2))   # 当前位
        carry = total // 2              # 进位
    
    return "".join(reversed(result))
```

#### 关键点

- **从右往左**(低位到高位)
- 用 `carry` 处理进位
- `while i >= 0 or j >= 0 or carry`(注意 `or carry`):防止漏掉最高位进位(如 `"1" + "1" = "10"`)

---

### 28.7 经典题 5:LC 190 Reverse Bits(翻转 32 位)

#### 题目

把 32 位整数的二进制位**前后翻转**。

```python
n = 00000010100101000001111010011100  (43261596)
# 翻转后:00111001011110000010100101000000 (964176192)
```

#### 思路:逐位取出,左移拼接

```python
def reverseBits(n):
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)    # 把 n 的最低位拼到 result 的最低位
        n >>= 1
    return result
```

#### 走一遍 `n = 0b101`(只看 3 位简化)

| 轮 | n & 1 | result(左移并 OR) |
|---|---|---|
| 1 | 1 | `0 → 1`(001) |
| 2 | 0 | `1 → 10`(010) |
| 3 | 1 | `10 → 101`(101) |

最终 result = `101`(其实就是 5 翻转后还是 5,因为对称)。

---

### 28.8 经典题 6:LC 137 Single Number II(进阶 XOR)

#### 题目

数组里**每个数出现 3 次,只有一个出现 1 次**。找出来。

```python
nums = [2, 2, 3, 2]
# 答案 3
```

#### 朴素思路:用 Counter

```python
from collections import Counter
def singleNumber(nums):
    return [k for k, v in Counter(nums).items() if v == 1][0]
```

简单但 O(n) 空间。**面试官追问**:能 O(1) 空间吗?

#### 进阶:位运算技巧(O(1) 空间)

**逐位统计 1 的个数 mod 3**:每一位上,如果出现 3 次的数都是 0 或都是 1,**那一位的 1 总数 % 3 = 出现 1 次的数那一位的值**。

```python
def singleNumber(nums):
    result = 0
    for i in range(32):
        count = sum((num >> i) & 1 for num in nums)
        if count % 3 != 0:
            result |= (1 << i)
    # 处理负数(Python 整数没有固定位数)
    if result >= 2 ** 31:
        result -= 2 ** 32
    return result
```

**进阶面试可以提一句**:这种思路叫"**位独立分析**",每位互不影响,所以可以分别处理。

---

### 28.9 实用位运算技巧速查

| 目的 | 写法 |
|---|---|
| 检查第 i 位是不是 1 | `(n >> i) & 1` |
| 把第 i 位设为 1 | `n \| (1 << i)` |
| 把第 i 位设为 0 | `n & ~(1 << i)` |
| 翻转第 i 位 | `n ^ (1 << i)` |
| 抹掉最右的 1 | `n & (n-1)` |
| 取最右的 1 | `n & (-n)` |
| 判断是不是 2 的幂 | `n > 0 and n & (n-1) == 0` |

### 28.10 位运算面试出现频率

实话:**面试中位运算很少见**(可能 1-2 题),但**XOR 找单数**、**判断 2 的幂**、**Add Binary** 是经典必备。

### 28.11 一句话记忆

```
XOR 三性质:x^x=0, x^0=x, 可抵消
LC 136 找单数 → 全部 XOR
LC 191 数 1 → n & (n-1) 抹最右的 1
LC 67 加法:从右往左,记 carry,while 条件加 or carry
LC 190 翻转 32 位:(result << 1) | (n & 1),走 32 次
LC 137 单数 II:每位 % 3 独立分析
n & (n-1) == 0 → 是 2 的幂
```

---

<a id="ch29"></a>

## 二十九、Math(数学题)⭐

> **低频但有套路**。Math 题通常**不靠数据结构**,靠**数学小技巧**。掌握这几道经典题就够覆盖大部分面试场景。

### 29.1 Math 题三大特点

1. **不用复杂数据结构**(很多是 O(1) 空间)
2. **要会"找规律"**(常涉及模运算、位运算、数论)
3. **边界情况多**(溢出、负数、零)

### 29.2 LC 9 Palindrome Number(回文数)

#### 题目

判断一个整数是不是回文数(正读反读一样)。

```python
121     # True
-121    # False(负号在前)
10      # False(01 不是)
```

#### 思路:反转一半即可

朴素思路是反转整个数比较,但**只反转后一半,跟前一半比**就够了。

```python
def isPalindrome(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False                # 负数和 10/100/... 都不是
    
    reverted = 0
    while x > reverted:
        reverted = reverted * 10 + x % 10
        x //= 10
    
    # 偶数位:x == reverted;奇数位:x == reverted // 10(去掉中间位)
    return x == reverted or x == reverted // 10
```

#### 走一遍 `x = 1221`

| 轮 | x | reverted |
|---|---|---|
| 初始 | 1221 | 0 |
| 1 | 122 | 1 |
| 2 | 12 | 12 |
| 退出 | x ≤ reverted | |

`x == reverted` → True ✓

#### 走一遍奇数位 `x = 12321`

| 轮 | x | reverted |
|---|---|---|
| 初始 | 12321 | 0 |
| 1 | 1232 | 1 |
| 2 | 123 | 12 |
| 3 | 12 | 123 |

`x == reverted // 10` → `12 == 12` ✓(去掉中间的 3)

#### 复杂度

- 时间:**O(log n)**(每轮 x 除以 10)
- 空间:O(1)

---

### 29.3 LC 66 Plus One(数组形式加 1)

#### 题目

数组每个元素是一个数字位,**整体表示一个非负整数,给它加 1**。

```python
digits = [1, 2, 3]      # 表示 123
# 加 1 → [1, 2, 4]
digits = [9, 9]         # 99
# 加 1 → [1, 0, 0]
```

#### 思路:从后往前进位

```python
def plusOne(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits           # 没进位,直接返回
        digits[i] = 0               # 进位:当前位变 0,继续向前
    return [1] + digits             # 走完循环还没返回,说明全部进位(如 999 → 1000)
```

#### 关键边界:`999 → 1000`

如果最高位也进位了,**需要在前面加一个 1**。例:
- `[9, 9]` → 末尾改 0:`[9, 0]` → 再向前改 0:`[0, 0]` → 加 1:`[1, 0, 0]` ✓

---

### 29.4 LC 50 Pow(x, n)(快速幂)⭐⭐

#### 题目

实现 `pow(x, n)`,不能用内置的 `**`。

```python
pow(2, 10)    # 1024
pow(2, -2)    # 0.25
pow(2.1, 3)   # 9.261
```

#### 朴素 O(n) 解法

```python
def myPow(x, n):
    result = 1
    for _ in range(abs(n)):
        result *= x
    return result if n >= 0 else 1 / result
```

**问题**:n 可以达到 `2^31`,O(n) 会超时。

#### 快速幂(Fast Exponentiation)⭐ O(log n)

**核心思想**:`x^10 = x^5 * x^5`,而 `x^5 = x^2 * x^2 * x`。每次把指数减半,**O(log n)**。

##### 递归版

```python
def myPow(x, n):
    if n < 0:
        x, n = 1/x, -n
    
    def helper(x, n):
        if n == 0:
            return 1
        half = helper(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x
    
    return helper(x, n)
```

##### 迭代版(更省栈空间)

```python
def myPow(x, n):
    if n < 0:
        x, n = 1/x, -n
    result = 1
    while n > 0:
        if n & 1:                   # n 是奇数
            result *= x
        x *= x                      # x 翻倍
        n >>= 1                     # n 减半
    return result
```

#### 走一遍 `pow(2, 10)`

二进制 `10 = 1010`,从低位到高位看每一位:

| n | n & 1 | x | result |
|---|---|---|---|
| 10 (1010) | 0 | 2 → 4 | 1 |
| 5 (101) | 1 | 4 → 16 | 1 × 4 = 4 |
| 2 (10) | 0 | 16 → 256 | 4 |
| 1 (1) | 1 | 256 → 65536 | 4 × 256 = **1024** ✓ |

#### 复杂度

- 时间:**O(log n)**(每次 n 减半)
- 空间:O(1)(迭代版)

---

### 29.5 LC 69 Sqrt(x)(整数平方根)

#### 题目

返回 `sqrt(x)` 的整数部分(向下取整)。

```python
sqrt(4)     # 2
sqrt(8)     # 2(因为 2.828...,取整 2)
```

#### 朴素 O(sqrt(n)) 线性查找

```python
def mySqrt(x):
    i = 0
    while i * i <= x:
        i += 1
    return i - 1
```

#### 二分查找 O(log n)(推荐)

```python
def mySqrt(x):
    if x < 2:
        return x
    left, right = 1, x // 2          # sqrt 不超过 x/2(x ≥ 2 时)
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1
    return right                     # 退出后 right 是最后一个 mid² ≤ x 的值
```

**为什么返回 `right`?**:循环退出时 `left > right`,而 `right` 始终满足 `right² ≤ x`,**right 就是答案**。

---

### 29.6 LC 172 Factorial Trailing Zeroes(阶乘末尾零)

#### 题目

返回 `n!` 末尾有多少个 0。

```python
n = 5    # 5! = 120,有 1 个 0
n = 10   # 10! = 3628800,有 2 个 0
```

#### 数学洞察:末尾零 = 因子 10 的个数 = 因子 5 的个数

每个末尾零都是 **2 × 5 = 10** 产生的。在 1 到 n 的乘积中,**2 的因子总比 5 多**(每隔 2 个数就有一个 2,每隔 5 个数才有一个 5)。

所以**问题简化为:n! 含多少个因子 5**。

#### 公式

```
零的个数 = n/5 + n/25 + n/125 + ...
```

- `n/5`:1~n 中 5 的倍数有多少个(每个贡献至少一个 5)
- `n/25`:25 的倍数额外贡献一个 5(25 = 5×5)
- `n/125`:125 = 5×5×5,再贡献一个

#### 代码

```python
def trailingZeroes(n):
    count = 0
    while n > 0:
        n //= 5
        count += n
    return count
```

#### 走一遍 `n = 25`

| 轮 | n | count |
|---|---|---|
| 1 | 25 // 5 = 5 | 5 |
| 2 | 5 // 5 = 1 | 5 + 1 = 6 |
| 3 | 1 // 5 = 0 | 6 |

`25! = 15511210043330985984000000`,末尾 6 个 0 ✓

#### 复杂度

- 时间:**O(log₅ n)**(非常快)
- 空间:O(1)

---

### 29.7 Math 题套路总结

| 题型 | 套路 | 经典题 |
|---|---|---|
| **回文 / 反转** | 一半比一半,/= 10 | LC 9 |
| **数组进位** | 从后往前 + carry | LC 66 |
| **幂运算** | **快速幂**(指数二分) | LC 50 |
| **平方根** | 二分查找 | LC 69 |
| **阶乘 / 因子** | **数学公式**,不要硬算 | LC 172 |

### 29.8 Math 题的"潜规则"

1. **看到大数,想"溢出"**(虽然 Python 不溢出,但 Java/C++ 会问)
2. **看到指数大,想"快速幂"**(LC 50, LC 372)
3. **看到 sqrt / 范围搜索,想"二分"**(LC 69, LC 367)
4. **看到因子统计,想"数学公式"**(LC 172, LC 204 质数筛)
5. **看到负数 / 0,想"边界 case"**(必加 if 处理)

### 29.9 一句话记忆

```
LC 9   回文数 → 反转一半比另一半
LC 66  加 1 → 从后往前 carry,全 9 要加首位
LC 50  Pow → 快速幂,n & 1 判奇,x *= x 减半
LC 69  sqrt → 二分,return right
LC 172 阶乘 0 → 数因子 5,while n: n //= 5; count += n
```

### 29.10 Math 面试现实

**实话**:除非投量化金融或 ICPC 出身的公司(Jane Street、Two Sigma 等),**面试中 Math 题占比 < 5%**。一般公司最多考 LC 9 / 50 / 69 这三道经典。

**你的备战策略**:把 §29.2-29.6 这五道经典题看一遍 + 能写出来,**就足够覆盖 90% 场景**。

---

<a id="ch30"></a>

## 三十、Python 语法速查(Mock 前 10 分钟回顾)

> 改编自 NeetCode 的 **"Python for Coding Interviews - Everything you need to Know"**(YouTube,17 个主题),结合你 mock 真实踩过的坑。**这一节是"速查表"**,不是教学。详细解释看对应主章节。

### 30.1 Variables(变量 / Variables)

```python
n = 0                          # int
n, m, z = 0.125, "abc", False  # 多重赋值 / Multiple assignment
n, m = m, n                    # 交换 / Swap two variables
```

**中英对照讲解**:
- "Python is **dynamically typed**, meaning we don't declare variable types."
- "We can do **multiple assignment** in one line, like `n, m, z = 0.125, "abc", False`."
- "Python supports **tuple unpacking**, so we can swap two variables in one line without a temp variable."
- "Use `type()` to check the type of a variable at runtime."

```python
print(type(7))      # <class 'int'>
print(type(7 / 2))  # <class 'float'>  注意!除法变 float / Division returns float
```

**易错 / Common pitfalls**:
- `7 / 2 = 3.5`(**float division** — 浮点除法), 整除用 `7 // 2 = 3`(**integer / floor division**)
- **不要用内置类型名做变量**: `list`, `dict`, `set`, `str`, `sum`, `min`, `max`, `id`, `type`, `input`
  - "I never shadow built-in names like `list` or `sum` because it can cause subtle bugs."

---

### 30.2 If / Else(条件 / Conditionals)

```python
# 标准 / Standard
if n < 0:
    print("neg")
elif n == 0:
    print("zero")
else:
    print("pos")

# Python 风格:链式比较 / Chained comparison
if 0 < n < 10:                 # ✅ 真的可以这样写!
    print("single digit")

# 三元表达式 / Ternary expression
result = "neg" if n < 0 else "pos"
```

**中英对照讲解**:
- "Python supports **chained comparisons** like `0 < n < 10`, which is equivalent to `0 < n and n < 10`."
- "We can use a **ternary expression** for inline conditional assignment: `value_if_true if condition else value_if_false`."
- "**Logical operators** in Python are spelled out: `and`, `or`, `not` — not `&&`, `||`, `!`."

**易错 / Common pitfalls**:
- `&` `|` 是**位运算符 / bitwise operators**,不是逻辑运算符。
  - "I'd use `and` for boolean logic, not `&`, which is bitwise AND."

---

### 30.3 Loops(循环 / Loops)

```python
# range:左闭右开 / half-open interval
for i in range(5):             # 0,1,2,3,4
for i in range(2, 6):          # 2,3,4,5
for i in range(5, 1, -1):      # 5,4,3,2(倒着 / step backward)
for i in range(0, 10, 2):      # 0,2,4,6,8(每次跳 2 / step of 2)

# enumerate:同时拿 index 和 value
for i, num in enumerate(nums):
    print(i, num)

# zip:同时遍历两个 list / iterate two lists in parallel
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
for n1, n2 in zip(nums1, nums2):
    print(n1, n2)              # 1 4, 2 5, 3 6
# 如果长度不同,zip 取较短的 / zip stops at the shortest iterable

# while
i = 0
while i < 5:
    i += 1                     # Python 没有 i++!/ No ++ operator in Python
```

**中英对照讲解**:
- "`range(start, stop, step)` is **half-open** — it includes start but excludes stop."
- "I use `enumerate` to get **both the index and the value** at the same time. It's more Pythonic than using `range(len(nums))`."
- "`zip` lets me **iterate over multiple iterables in parallel**. It automatically stops at the shortest one."
- "Python doesn't have `i++` — I increment with `i += 1`."

---

### 30.4 Math(数学 / Math Operations)

```python
# 除法的两种 / Two types of division
7 / 2 = 3.5                    # 浮点除 / float division
7 // 2 = 3                     # 整除(向下取整) / integer (floor) division

# 负数整除是"向下取整",不是"截断"!
# Floor division rounds toward negative infinity, not toward zero!
-3 // 2 = -2                   # 不是 -1!
int(-3 / 2) = -1               # 要"向 0 截断" / truncate toward zero

# 幂运算 / Exponentiation
2 ** 10                        # 1024
import math
math.pow(2, 10)                # 1024.0 (returns float)
math.sqrt(16)                  # 4.0

# 取模 / Modulo
10 % 3 = 1
# 负数取模:Python 结果总是和除数同号
# Python's modulo always has the same sign as the divisor
-10 % 3 = 2                    # 不是 -1!

# 极值 / Infinity
float('inf')                   # positive infinity
float('-inf')                  # negative infinity
```

**中英对照讲解**:
- "Python has two division operators: `/` for **true division** (always returns float), and `//` for **floor division**."
- "Be careful — **floor division** rounds **toward negative infinity**, not toward zero. So `-3 // 2` is `-2`, not `-1`."
- "Use `**` for exponentiation, like `2 ** 10`."
- "For initialization, I often use `float('inf')` as a sentinel value — for example, `min_val = float('inf')`."
- "**Python integers have arbitrary precision**, so I don't have to worry about overflow like in Java or C++."

---

### 30.5 Arrays / Lists(列表)

```python
arr = [1, 2, 3]
arr.append(4)                  # 末尾加 / append to end, O(1)
arr.pop()                      # 末尾删并返回 / pop from end, O(1)
arr.insert(0, 99)              # 头部插入 / insert at head, O(n) ❌ 避免
arr.pop(0)                     # 头部删除 / pop from head, O(n) ❌ 用 deque

# 索引(负数从右数) / Negative indexing
arr[-1]                        # 最后一个 / last element
arr[-2]                        # 倒数第二 / second to last

# 切片 [start:end:step] / Slicing
arr[1:3]                       # 不含 end / excludes end index
arr[:2]                        # 前两个 / first two
arr[2:]                        # 从第 2 个到末尾 / from index 2 to end
arr[::-1]                      # 反转!⭐ / reversed copy
arr[::2]                       # 每隔一个取一个 / every other element

# 初始化 / Initialization
arr = [0] * 5                  # [0, 0, 0, 0, 0]

# 解包 / Unpacking
a, b, c = [1, 2, 3]            # 多重赋值 / multiple assignment
first, *rest = [1, 2, 3, 4]    # first=1, rest=[2,3,4] / starred unpacking
```

**中英对照讲解**:
- "Python `list` is implemented as a **dynamic array**, so `append` and `pop` from the end are amortized O(1)."
- "But `insert(0, x)` or `pop(0)` are **O(n)** because they shift all other elements. For O(1) operations on both ends, I'd use `collections.deque`."
- "**Negative indexing**: `arr[-1]` gives the last element."
- "**Slicing** uses `[start:end:step]`. `arr[::-1]` is a Pythonic way to **reverse** a list."
- "I can use **starred unpacking**, like `first, *rest = [1, 2, 3, 4]`, to capture the rest of the list."

---

### 30.6 Sorting(排序)

```python
arr = [3, 1, 4, 1, 5]
arr.sort()                     # 原地排序 / sorts in-place, returns None
arr.sort(reverse=True)         # 降序 / descending order

new_arr = sorted(arr)          # 返回新 list / returns a new sorted list
new_arr = sorted(arr, reverse=True)

# 自定义 key / Custom sort key
words = ["bb", "a", "ccc"]
words.sort(key=lambda w: len(w))             # 按长度 / sort by length
words.sort(key=lambda w: (len(w), w))        # 先长度再字母 / multi-key sort

# Tuple 排序(默认按第一个元素) / Tuples sort by first element by default
pairs = [(1, "b"), (2, "a"), (1, "a")]
pairs.sort()                   # [(1, 'a'), (1, 'b'), (2, 'a')]
```

**中英对照讲解**:
- "There are two ways to sort: `.sort()` **sorts in-place** and returns `None`, while `sorted()` **returns a new sorted list** without modifying the original."
- "I prefer `sorted()` when I don't want to **mutate the input** — it's a good practice to avoid side effects."
- "I can pass a `key` function for **custom sort order**. For example, `key=lambda w: len(w)` sorts strings by length."
- "For **multi-criteria sorting**, I return a tuple from the key function, like `key=lambda w: (len(w), w)` — Python compares tuples lexicographically."
- "Python's sort is **Timsort**, which is O(n log n) worst case and **stable** — it preserves the relative order of equal elements."

---

### 30.7 List Comprehension(列表推导式)⭐ Pythonic 必学

**核心句式 / Core syntax**: `[expression for item in iterable if condition]`

```python
# 平方 / Squares
squares = [n * n for n in range(5)]            # [0, 1, 4, 9, 16]

# 带条件 / With filter condition
evens = [n for n in range(10) if n % 2 == 0]   # [0, 2, 4, 6, 8]

# 嵌套(创建 2D 数组) / Nested (create 2D array)
matrix = [[0] * 3 for _ in range(3)]           # 3×3 全 0 矩阵 ⭐

# dict comprehension
square_map = {i: i*i for i in range(5)}        # {0:0, 1:1, 2:4, 3:9, 4:16}

# set comprehension
unique = {n for n in [1, 2, 2, 3]}             # {1, 2, 3}
```

**中英对照讲解**:
- "**List comprehension** is a Pythonic way to build a list in one line. The syntax is `[expression for item in iterable if condition]`."
- "It's usually **faster and more readable** than a for loop with `append`."
- "Python also supports **dict comprehension** and **set comprehension** with similar syntax."
- "For creating a 2D array, I use `[[0] * n for _ in range(m)]` — **never** `[[0] * n] * m`, because that would create m references to the same inner list."

**最大的坑 / Biggest pitfall**:2D 数组初始化
```python
# ❌ 危险!三行共用同一个 list,改一个会改三个
grid = [[0] * 3] * 3
grid[0][0] = 1
# 结果:[[1, 0, 0], [1, 0, 0], [1, 0, 0]]  ← 三行都变了!

# ✅ 正确
grid = [[0] * 3 for _ in range(3)]
```

> **English explanation**: "If I write `[[0] * 3] * 3`, all three inner lists are **the same reference**, so modifying one row modifies all of them. Using a list comprehension creates **independent inner lists**."

---

### 30.8 2D Arrays(二维数组)

```python
# 初始化 / Initialization
grid = [[0] * cols for _ in range(rows)]

# 访问 / Access
grid[r][c]
len(grid)                      # 行数 / number of rows
len(grid[0])                   # 列数 / number of columns

# 遍历 / Iteration
for r in range(len(grid)):
    for c in range(len(grid[0])):
        print(grid[r][c])

# 四方向遍历(矩阵题必备) / Four-direction traversal
DIRECTIONS = [(-1,0), (1,0), (0,-1), (0,1)]    # 上下左右 / up, down, left, right
for dr, dc in DIRECTIONS:
    nr, nc = r + dr, c + dc
    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
        # 在边界内,处理 / in bounds, process
        ...
```

**中英对照讲解**:
- "I represent a 2D grid as a **list of lists**. `grid[r][c]` accesses the cell at row r, column c."
- "For matrix problems, I always define a **directions array** like `[(-1,0), (1,0), (0,-1), (0,1)]` to iterate over the four neighbors."
- "I check **bounds** with `0 <= nr < rows and 0 <= nc < cols` before accessing a neighbor."

---

### 30.9 Strings(字符串)

```python
s = "abc"
s[0]                           # 'a',可以索引 / indexable
s[1:]                          # 'bc',可以切片 / sliceable
# 但 strings 不可变 / But strings are IMMUTABLE!
s[0] = 'z'                     # ❌ TypeError

# 转 list 才能修改 / Convert to list to modify
chars = list(s)                # ['a', 'b', 'c']
chars[0] = 'z'
s = "".join(chars)             # 'zbc'

# 长度 / 反转 / Length and reverse
len(s)
s[::-1]                        # 反转 ⭐

# 转大小写 / Case conversion
s.upper()                      # "ABC"
s.lower()                      # "abc"

# 判断字符类型 / Character type checks
ch.isalpha()                   # 是字母 / is letter
ch.isdigit()                   # 是数字 / is digit
ch.isalnum()                   # 字母或数字 / alphanumeric
ch.isspace()                   # 是空白 / whitespace

# 字符 ↔ ASCII
ord('a')                       # 97
chr(97)                        # 'a'
ord('a') - ord('a')            # 0(算字母位置常用)

# 拼接 / Concatenation
"".join(["a", "b", "c"])       # "abc" ⭐ 比 += 高效 / much faster than +=
"-".join(["a", "b", "c"])      # "a-b-c"

# 分割 / Split and strip
"a,b,c".split(",")             # ['a', 'b', 'c']
"  hi  ".strip()               # "hi"(去两端空白)

# 整数 ↔ 字符串
str(42)                        # "42"
int("42")                      # 42

# 格式化(推荐 f-string) / Formatted strings
name = "Jun"
f"Hello, {name}!"              # "Hello, Jun!"
f"{n:05d}"                     # "00042"(补零 / zero-padded)
f"{x:.2f}"                     # 保留 2 位小数 / two decimal places
```

**中英对照讲解**:
- "**Strings in Python are immutable**, so I can't modify them in place. To modify, I convert to a list of characters, change it, then **join** it back."
- "Building a string with repeated `+=` is **O(n²)** because each concatenation creates a new string. I always use `''.join(list)` instead — that's **O(n)**."
- "`ord(ch)` gives the **ASCII / Unicode code point**, and `chr(n)` does the reverse. I often use `ord(ch) - ord('a')` to **map a letter to an index 0-25**."
- "For string formatting, I prefer **f-strings** like `f'Hello, {name}!'` — they're concise and fast."

---

### 30.10 Queues(队列)

```python
from collections import deque

q = deque()
q.append(1)                    # 尾部加 / append to right, O(1)
q.append(2)
q.appendleft(0)                # 头部加 / append to left, O(1) ⭐
q.popleft()                    # 头部删 / pop from left, O(1) ⭐
q.pop()                        # 尾部删 / pop from right, O(1)
q[0]                           # 看头部 / peek front, O(1)
len(q)

# 初始化时传 iterable
q = deque([1, 2, 3])
```

**中英对照讲解**:
- "For a queue, I use `collections.deque`, which is a **double-ended queue** with **O(1) append and pop on both ends**."
- "I **don't use a regular list as a queue**, because `list.pop(0)` is O(n) — it shifts every other element. This would turn a BFS into O(n²)."
- "`appendleft` and `popleft` are the two operations that make deque better than list."

---

### 30.11 Hash Sets(集合)

```python
s = set()
s.add(1)
s.add(2)
s.remove(1)                    # 不存在会 KeyError / raises KeyError if missing
s.discard(1)                   # 不存在不报错 ⭐ 更安全 / safer alternative
1 in s                         # O(1) 查找 ⭐ / O(1) membership check

# 创建 / Initialization
s = {1, 2, 3}
s = set([1, 2, 2, 3])          # 从 list 去重 / dedup from list: {1, 2, 3}

# 集合运算 / Set operations
a, b = {1, 2, 3}, {2, 3, 4}
a & b                          # 交集 / intersection {2, 3}
a | b                          # 并集 / union {1, 2, 3, 4}
a - b                          # 差集 / difference {1}
a ^ b                          # 对称差 / symmetric difference {1, 4}
```

**中英对照讲解**:
- "A `set` provides **O(1) membership testing** and **O(1) insertion**. It's perfect for **deduplication** or **checking if we've seen an element before**."
- "Python sets support **set operations** like union (`|`), intersection (`&`), difference (`-`), and symmetric difference (`^`)."
- "**Tip**: an empty set is `set()`, **not** `{}` — `{}` creates an empty **dict**."

**注意:空集合的写法 / Empty set syntax**
```python
s = {}                         # ❌ 这是空 dict!/ This is an empty dict!
s = set()                      # ✅ 空 set / This is an empty set
```

---

### 30.12 Hash Maps(字典 / Dictionaries)⭐ 面试最常用

```python
d = {}
d["key"] = 1
d["key"]                       # 1
"key" in d                     # 检查 key 存在 / check key exists, O(1)
del d["key"]                   # 删除 / delete

# 安全访问(防 KeyError) / Safe access (avoid KeyError)
d.get("nokey")                 # None
d.get("nokey", 0)              # 默认值 0 / default value 0 ⭐ 常用

# 计数模式(超常用!) / Counting pattern
counts = {}
for ch in s:
    counts[ch] = counts.get(ch, 0) + 1

# 更优雅:Counter / Cleaner: use Counter
from collections import Counter
counts = Counter(s)            # 直接得到 {字符: 次数} / directly gives a frequency map
counts.most_common(2)          # 出现次数 top 2 / top 2 most frequent

# defaultdict:省去判断 key 是否存在 / defaultdict: skip "key exists" check
from collections import defaultdict
adj = defaultdict(list)
adj[1].append(2)               # 不报 KeyError,自动创建空 list / auto-creates empty list
adj[1].append(3)               # adj = {1: [2, 3]}

# 遍历 / Iteration
for k in d:                    # 遍历 keys / iterate over keys
for v in d.values():           # 遍历 values
for k, v in d.items():         # 遍历 key-value ⭐ 最常用
```

**中英对照讲解**:
- "Python's `dict` is implemented as a **hash table**, giving **O(1) average-case** lookup, insertion, and deletion."
- "I use `dict.get(key, default)` for **safe access** — it returns the default value instead of raising `KeyError`."
- "For frequency counting, I use **`collections.Counter`**, which is a `dict` subclass specifically designed for counting hashable objects."
- "**`collections.defaultdict(list)`** auto-initializes missing keys to an empty list — super handy for building **adjacency lists** in graph problems."
- "To iterate over both keys and values, I use **`.items()`**: `for k, v in d.items():`."

---

### 30.13 Tuples(元组)

```python
t = (1, 2, 3)
t[0]                           # 1,可以索引 / indexable
# 但不可变!/ But immutable!
t[0] = 99                      # ❌ TypeError

# 单元素 tuple 注意写法 / Single-element tuple syntax
t = (1)                        # ❌ 这是 int 1 / This is just int 1
t = (1,)                       # ✅ 加逗号才是 tuple / The trailing comma makes it a tuple

# 解包 / Unpacking
a, b, c = (1, 2, 3)
```

**中英对照讲解**:
- "**Tuples are immutable** — once created, they can't be changed."
- "Because tuples are immutable, they are **hashable**, which means they can be used as **dict keys or set elements**. Lists can't, because they're mutable."

**Tuple 的杀手级用法 / Killer use case**:
```python
# ❌
visited = set()
visited.add([1, 2])            # TypeError: unhashable type: 'list'

# ✅
visited.add((1, 2))            # 矩阵题里标记访问过的位置

# Two Sum 去重技巧(5/7 mock)/ Two Sum dedup trick
used_pairs = set()
used_pairs.add(tuple(sorted([a, b])))   # 把 pair 转 tuple 才能进 set
```

> **English**: "I can convert a list to a tuple with `tuple(sorted([a, b]))` to make it **hashable**, then store it in a set for **O(1) duplicate detection**."

---

### 30.14 Heaps(堆 / 优先队列)

```python
import heapq

# Python heapq 只有 min-heap!/ Python only has min-heap
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 5)
heap[0]                        # 1(最小)/ smallest, O(1) peek
heapq.heappop(heap)            # 1(弹出最小)/ pop smallest, O(log n)

# 把 list 直接变 heap / Heapify in-place
arr = [3, 1, 5, 2, 4]
heapq.heapify(arr)             # O(n) ⭐ faster than n pushes (O(n log n))

# Max-Heap?Python 没有,取负数模拟 / Simulate max-heap with negation
max_heap = []
for x in [3, 1, 5]:
    heapq.heappush(max_heap, -x)
largest = -heapq.heappop(max_heap)   # 5

# 取最小 N / 最大 N / Top N elements
heapq.nsmallest(3, [5, 1, 4, 2, 3])  # [1, 2, 3]
heapq.nlargest(3, [5, 1, 4, 2, 3])   # [5, 4, 3]

# tuple 进 heap:按第一个元素排序 / Tuples in heap sort by first element
heapq.heappush(heap, (priority, value))
```

**中英对照讲解**:
- "`heapq` is Python's built-in **min-heap** — also called a **priority queue**. The smallest element is always at the root."
- "`heappush` and `heappop` are **O(log n)**, while `heap[0]` to peek the top is **O(1)**."
- "**Python only has a min-heap**, no max-heap. To simulate a max-heap, I **negate the values** when pushing and negate again when popping."
- "`heapify` converts an existing list into a heap **in-place in O(n)** — which is faster than pushing n times (O(n log n))."
- "When pushing **tuples** like `(priority, value)`, the heap orders by the **first element** by default. This is handy for tasks like Top K Frequent."

---

### 30.15 Functions(函数)

```python
def greet(name, msg="Hello"):              # 默认参数 / Default argument
    return f"{msg}, {name}!"

greet("Jun")                               # "Hello, Jun!"
greet("Jun", "Hi")                         # "Hi, Jun!"
greet(name="Jun", msg="Hi")                # 关键字参数 / Keyword arguments

# 多返回值(其实是返回 tuple) / Multiple return values (actually a tuple)
def min_max(arr):
    return min(arr), max(arr)

low, high = min_max([3, 1, 4])             # 解包 / Tuple unpacking

# *args 和 **kwargs / Variable arguments
def fn(*args, **kwargs):
    print(args)                            # tuple of positional args
    print(kwargs)                          # dict of keyword args

fn(1, 2, 3, name="Jun")
# args = (1, 2, 3)
# kwargs = {'name': 'Jun'}
```

**中英对照讲解**:
- "Python supports **default arguments**, so I can write `def greet(name, msg='Hello')` and call `greet('Jun')` without providing `msg`."
- "I can pass arguments **positionally** or by **keyword**, like `greet(name='Jun', msg='Hi')`."
- "Functions can **return multiple values** — really, this returns a tuple that I unpack with `low, high = min_max(arr)`."
- "**`*args`** collects extra positional arguments into a tuple, and **`**kwargs`** collects extra keyword arguments into a dict."

**默认参数的坑 / Default argument pitfall**:
```python
# ❌ 危险!list 被所有调用共享 / Mutable default is shared across calls!
def add(item, arr=[]):
    arr.append(item)
    return arr

# ✅ 用 None 当哨兵 / Use None as sentinel
def add(item, arr=None):
    if arr is None:
        arr = []
    arr.append(item)
    return arr
```

> **English**: "I never use a **mutable default argument** like `arr=[]`, because the default list is created **once** and shared across all calls. Instead, I use `None` as a sentinel and initialize inside the function."

---

### 30.16 Nested Functions(嵌套函数)⭐ 面试必学

二叉树、回溯题里到处都是 / Common in tree, backtracking, and DFS problems

```python
def outer():
    x = 0
    def inner():
        # 读外层变量:OK / Reading outer variable: OK
        print(x)
    inner()

# 修改外层变量需要 nonlocal!/ Modifying outer variable requires `nonlocal`
def outer():
    count = 0
    def inner():
        nonlocal count          # 必须声明 / Required declaration
        count += 1
    inner()
    print(count)                # 1

# 但是 list/dict 的 append/add 不需要 nonlocal!
# But mutating a list/dict (append, etc.) does NOT need nonlocal
def outer():
    result = []
    def inner():
        result.append(1)        # ✅ 不需要 nonlocal(没有重新赋值)
    inner()
```

**中英对照讲解**:
- "A **nested function** is a function defined inside another function. It can **read** variables from the enclosing scope automatically."
- "To **modify** a variable in the enclosing scope, I use the **`nonlocal`** keyword."
- "**Key distinction**: `nonlocal` is required for **reassignment** (like `count += 1`), but **not** for **mutating** an existing object (like `result.append(...)`)."
  - "Mutating a list doesn't rebind the variable, so Python still resolves `result` to the outer scope."
- "Nested helper functions are very common in **DFS/recursion** problems, where I need to **share state** like a running maximum or a visited set."

##### 类方法 vs 嵌套函数 / Class method vs nested function

```python
class Solution:
    def diameter(self, root):
        # 嵌套 helper(不需要 self) / Nested helper (no self)
        def dfs(node):
            ...
        return dfs(root)
    
    def maxDepth(self, root):
        # 类方法递归(需要 self.) / Recursive class method (needs self.)
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
```

> **English**: "Inside a class, methods need `self` as the first parameter, and recursive calls go through `self.methodName(...)`. But a **nested helper function** defined inside a method is just a regular function — no `self` needed."

---

### 30.17 Classes(类)

```python
class MyClass:
    # 构造函数 / Constructor
    def __init__(self, val):
        self.val = val          # 实例变量 / Instance variable
    
    # 方法 / Instance method
    def get(self):
        return self.val
    
    # 字符串表示(打印对象时调用) / String representation
    def __repr__(self):
        return f"MyClass({self.val})"

obj = MyClass(42)
obj.get()                       # 42
print(obj)                      # MyClass(42)
```

**中英对照讲解**:
- "**`__init__`** is the **constructor**, called when you instantiate the class. It initializes instance variables."
- "**`self`** is the conventional name for the **instance reference** — equivalent to `this` in Java or C++."
- "Methods that look like `__xxx__` are called **dunder methods** (double underscore). They define how objects behave with built-in operations."
- "For example, **`__repr__`** controls how `print(obj)` displays the object."

**LeetCode 里的标准结构 / Standard LeetCode classes**
```python
class Solution:
    def twoSum(self, nums, target):
        # 题目方法 / Solution method
        ...

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

##### 比较自定义对象(heap / sort 中常用) / Custom comparison

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # 让对象能用 < 比较(heap 和 sort 需要)
    # Define __lt__ so this class can be sorted or pushed onto a heap
    def __lt__(self, other):
        return self.x < other.x
```

> **English**: "By implementing **`__lt__`** (the 'less than' dunder method), I can make my custom class **sortable** or **pushable onto a heap**. Python's `sorted()` and `heapq` use `<` under the hood."

---

### 30.17-deep:Class 深入(self、实例化、调用规则完整指南)⭐⭐

> **属于 OOP(面向对象编程)语法基础,不是 OOD 题型**。OOD 是"设计 LRU Cache / 停车场系统"那种类设计题,这里讲的是 LeetCode 写 Solution 的语法基础。

#### 1️⃣ OOP 三种函数 / Three Function Types

##### A. 普通函数 / Regular Function

```python
def add(a, b):
    return a + b

print(add(1, 2))                        # 直接调用 / Call directly
```

- **不需要 `self`**,不属于任何 class
- "**It's not bound to any class or object**, just a regular standalone function."

##### B. Instance Method / 实例方法(LeetCode 最常见)

```python
class Solution:
    def twoSum(self, nums, target):
        return []

sol = Solution()                         # 实例化 / Instantiate
print(sol.twoSum([2, 7, 11, 15], 9))     # 用对象调用 / Call via instance
```

- **定义时第一个参数必须是 `self`** / `self` is required as the first parameter
- **调用时不传 self,Python 自动传** / Python passes `self` automatically when you call `obj.method()`
- "An **instance method** belongs to a specific object. The first parameter `self` is the **instance reference**, similar to `this` in Java or C++."

##### C. Static Method / 静态方法

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(1, 2))               # 用 class 名直接调用 / Call via class name
```

- **不需要 `self`**,加 `@staticmethod` 装饰器
- "A **static method** is a function that lives inside a class but **doesn't access any instance state**. It's just for organization."
- 常用于工具函数:`@staticmethod def isValid(...)` 

#### 2️⃣ 实例化是什么 / What is Instantiation?

```python
class Solution:        # 模板 / template (the blueprint)
    def hello(self):
        print("hello")

sol = Solution()       # 实例化 / instantiation (create an object)
sol.hello()            # 用对象调用方法 / call method on the instance
```

**英文说法**:
- "`Solution` is the **class**, which is like a **blueprint**."
- "`sol = Solution()` is **instantiation** — we **create an instance** (object) of the class."
- "Then `sol.hello()` **calls a method on that instance**."

##### LeetCode 为什么不用自己写 `sol = Solution()`?

```python
# LeetCode 后台帮你做了
sol = Solution()
answer = sol.twoSum(nums, target)
```

> **English**: "LeetCode's grader **instantiates your `Solution` class automatically** and calls the method on it. That's why I don't write `sol = Solution()` when I submit code."

**本地测试时**需要自己写:
```python
if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))
```

#### 3️⃣ self 的本质 / What is self?

```python
class Solution:
    def say_hi(self):
        print("hi")

sol = Solution()
sol.say_hi()                     # 看似 0 参数,实际上 Python 自动传了 sol
```

**Python 实际做的事**:
```python
sol.say_hi()
# 等价于 / Equivalent to:
Solution.say_hi(sol)             # 把 sol 当 self 传进去
```

> **English**: "When I call `sol.say_hi()`, Python **automatically passes `sol` as the `self` argument**. So `sol.say_hi()` is really equivalent to `Solution.say_hi(sol)` under the hood."

**记忆 / Memorize**:
```
定义时:写 self / Write self when defining
调用时:不要传 self / Don't pass self when calling
```

#### 4️⃣ class 内递归调用:self.method() vs helper()

##### 写法 A:类方法递归(需要 `self.`)

```python
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        left = self.maxDepth(root.left)      # ⭐ 必须 self.
        right = self.maxDepth(root.right)
        return max(left, right) + 1
```

##### 写法 B:内部 helper(不需要 `self.`)

```python
class Solution:
    def maxDepth(self, root):
        def dfs(node):                       # 嵌套函数 / nested function
            if not node:
                return 0
            left = dfs(node.left)            # ⭐ 直接调用,不用 self.
            right = dfs(node.right)
            return max(left, right) + 1
        return dfs(root)
```

**为什么差别**:
- "**`maxDepth` is a class method**, so to call it recursively, I have to go through `self.maxDepth(...)`."
- "**`dfs` is a nested function** defined inside `maxDepth`. It's not a class method, so I call it directly as `dfs(...)`."

详见 §10.8 LeetCode 中的 self 和递归调用。

#### 5️⃣ 5 种常见错误 / 5 Common Pitfalls

##### ❌ 错误 1:定义 instance method 忘了 self

```python
class Solution:
    def add(a, b):            # ❌ 漏了 self
        return a + b
```

> "I forgot to add `self` as the first parameter. When Python calls `sol.add(1, 2)`, it implicitly passes `sol` as the first argument, so `a = sol`, `b = 1`, and `2` is an extra argument — argument count mismatch."

##### ❌ 错误 2:调用 instance method 时手动传 self

```python
sol.add(sol, 1, 2)            # ❌ 多传了 self
sol.add(1, 2)                 # ✅
```

##### ❌ 错误 3:class 里递归忘了 self.

```python
class Solution:
    def maxDepth(self, root):
        return maxDepth(root.left)        # ❌ NameError
        return self.maxDepth(root.left)   # ✅
```

##### ❌ 错误 4:内部 helper 加了 self

```python
class Solution:
    def maxDepth(self, root):
        def dfs(node):
            return self.dfs(node.left)    # ❌ self 没有 dfs 属性
            return dfs(node.left)         # ✅
        return dfs(root)
```

##### ❌ 错误 5:把 `Solution.method()` 当 instance method 调用

```python
class Solution:
    def hello(self):
        print("hi")

Solution.hello()              # ❌ 没传 self
Solution.hello(Solution())    # 能跑但奇怪
Solution().hello()            # ✅ 标准写法
```

#### 6️⃣ 调用规则速查表 / Quick Reference Table

| 场景 / Scenario | 定义 / Definition | 调用 / Call |
|---|---|---|
| 普通函数 / Regular function | `def f(x):` | `f(x)` |
| Instance method | `class A: def f(self, x):` | `obj = A(); obj.f(x)` |
| class 内调用另一个 method | `def helper(self, x):` | `self.helper(x)` |
| 内部嵌套 helper | `def outer(...): def helper(x):` | `helper(x)`(无 `self.`) |
| Static method | `@staticmethod def f(x):` | `A.f(x)` |

#### 7️⃣ LeetCode 实战模板 / LeetCode Practical Templates

##### 模板 A:直接递归 method(推荐简单题用)

```python
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1

# 本地测试 / Local testing
if __name__ == "__main__":
    sol = Solution()
    # print(sol.maxDepth(root))
```

##### 模板 B:内部 helper(推荐需要全局变量的题用,如 LC 543)

```python
class Solution:
    def diameterOfBinaryTree(self, root):
        self.ans = 0                       # 实例变量,helper 内部能改
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.ans = max(self.ans, left + right)
            return max(left, right) + 1
        dfs(root)
        return self.ans
```

#### 8️⃣ 面试英文标准话术 / Interview English

##### 解释自己的代码结构时

```
"I'm defining my solution as a class with a single instance method, 
following LeetCode's convention."

"I'm using `self.ans` here so my nested helper function can update 
the running answer across all recursive calls."

"This is a static method because it doesn't need access to instance state — 
it's just a utility function."
```

##### 被问 self 是什么时

```
"`self` is the conventional name for the **instance reference** — 
it's the object on which the method is called. 
It's equivalent to `this` in Java or C++. 
Python passes it implicitly when you call `obj.method()`."
```

##### 被问为什么用 helper vs class method 时

```
"I prefer a nested helper here because the recursion only makes sense 
within this method's context, and I want to share state via closure 
without polluting the class namespace."
```

#### 9️⃣ 终极口诀 / The Ultimate Mantra

```
class 里的方法定义要写 self / Define class methods with self
对象调用方法时用 obj.method(...),不用手动传 self / Don't pass self when calling
class 内部调用同级方法时用 self.method(...) / Use self. for sibling methods
函数里面定义的 helper,直接 helper(...) / Direct call for nested helpers
staticmethod 不用 self,通常用 ClassName.method(...) 调用
```

---

### 30.18 Mock 当天的 Python 自查清单

**进入 mock 之前 10 分钟,过一遍**:

1. ☐ 不用 `list`, `dict`, `set`, `sum` 做变量名
2. ☐ 整除是 `//`,负数除法行为特殊
3. ☐ `sorted()` 返回新 list,`.sort()` 原地
4. ☐ 2D 数组用 `[[0]*n for _ in range(m)]`,不用 `[[0]*n]*m`
5. ☐ String 不可变,要改先 `list(s)`
6. ☐ BFS / 队列用 `from collections import deque`,不用 list
7. ☐ 计数器用 `Counter` 或 `defaultdict(int)`
8. ☐ Hash 查询 / Hash Set 添加是 **O(1)**
9. ☐ Python 只有 min-heap,要 max-heap 存负数
10. ☐ 嵌套函数改外层 int 要 `nonlocal`,append list 不要
11. ☐ Tuple 可哈希,list 不可
12. ☐ 类方法递归用 `self.xxx`,内部 helper 不用 self

---

### 30.19 一句话记忆

```
变量:不要用内置类型名;7/2=3.5,7//2=3
循环:enumerate 拿 index+value;zip 同时遍历两 list
排序:sorted 返回新数组,.sort() 原地
列表推导:[expr for x in xs if cond]
2D 初始化:[[0]*n for _ in range(m)] 不用 *
字符串:不可变,要改先 list(s);join 拼接最高效
队列:用 deque,popleft 是 O(1)
Counter:计数神器;defaultdict:自动初始化
heap:只有 min,max 用 -x;heap[0] 看顶 O(1)
nonlocal:改外层 int 要,append list 不要
```

---

### 30.20 中英对照 Python 面试话术 ⭐⭐⭐(必看)

> **面试是英文场,但用中文思考没问题,关键是关键术语用对英文**。下面这些是面试官 90% 会用的英文,以及你应该怎么用英文回应。

#### 30.20.1 数据结构英文术语

| 中文 | 英文 | 面试场景例句 |
|---|---|---|
| 数组 | **array** / **list**(Python 里 list 更准确) | "I'll use a list to store the result." |
| 字符串 | **string** | "Strings in Python are immutable." |
| 哈希表 / 字典 | **hash map** / **dictionary** / **dict** | "I'll use a hash map for O(1) lookup." |
| 哈希集合 | **hash set** / **set** | "A set gives us O(1) membership checking." |
| 链表 | **linked list** | "I'll use a dummy node to handle edge cases." |
| 栈 | **stack** | "Stack follows LIFO — last in, first out." |
| 队列 | **queue** | "Queue follows FIFO — first in, first out." |
| 双端队列 | **deque** / **double-ended queue** | "I'll use a deque for O(1) operations on both ends." |
| 堆 / 优先队列 | **heap** / **priority queue** | "Python's `heapq` is a min-heap by default." |
| 二叉树 | **binary tree** | "I'll do a DFS on the tree." |
| 二叉搜索树 | **binary search tree (BST)** | "In-order traversal of a BST gives a sorted sequence." |
| 图 | **graph** | "I'll model this as a graph with adjacency list." |
| 元组 | **tuple** | "Tuples are immutable, so they can be used as dict keys." |

#### 30.20.2 关键操作 / 概念英文

| 中文 | 英文 | 面试场景例句 |
|---|---|---|
| 时间复杂度 | **time complexity** | "The time complexity is O(n log n)." |
| 空间复杂度 | **space complexity** | "Space complexity is O(n) excluding the output." |
| 原地修改 | **in-place** / **modify in-place** | "I can do this in-place with O(1) extra space." |
| 边界情况 | **edge case** / **corner case** | "Let me think about edge cases first." |
| 遍历 | **traverse** / **iterate through** | "I'll iterate through the array once." |
| 递归 | **recursion** / **recursive** | "I'll use a recursive approach." |
| 迭代 | **iteration** / **iterative** | "Can I do it iteratively instead?" |
| 暴力解法 | **brute force** | "The brute force solution is O(n²)." |
| 优化 | **optimize** | "Let me optimize this to O(n)." |
| 不变 / 不可变 | **immutable** | "Strings are immutable in Python." |
| 可变 | **mutable** | "Lists are mutable, but tuples aren't." |
| 引用 | **reference** | "Lists are passed by reference." |
| 复制 | **copy** | "I need to make a deep copy here." |
| 升序 / 降序 | **ascending** / **descending** | "Sort in ascending order." |
| 子数组 | **subarray** | "Find the longest subarray with sum equals k." |
| 子序列 | **subsequence** | "Subsequence doesn't have to be contiguous." |
| 子串 | **substring** | "A substring is a contiguous part of a string." |
| 连续的 | **contiguous** | "A subarray is a contiguous slice of the array." |
| 前缀 / 后缀 | **prefix** / **suffix** | "I'll build a prefix sum array." |
| 重叠 | **overlap** / **overlapping** | "These two intervals overlap." |
| 重复 | **duplicate** | "I need to skip duplicates." |
| 唯一 | **unique** | "Return all unique pairs." |
| 排序 | **sort** / **sorted** | "I'll sort the array first." |
| 翻转 / 反转 | **reverse** | "Reverse the linked list in-place." |
| 合并 | **merge** | "Merge two sorted lists." |
| 拆分 | **split** | "Split the string by comma." |

#### 30.20.3 算法 Pattern 英文

| 中文 | 英文 | 例句 |
|---|---|---|
| 双指针 | **two pointers** | "I'll use the two-pointer technique." |
| 快慢指针 | **fast and slow pointers** / **tortoise and hare** | "Floyd's tortoise and hare detects cycles." |
| 滑动窗口 | **sliding window** | "This is a sliding window problem." |
| 二分查找 | **binary search** | "I'll binary search the sorted array." |
| 深度优先 | **depth-first search (DFS)** | "I'll DFS through the tree." |
| 广度优先 | **breadth-first search (BFS)** | "BFS gives us the shortest path in an unweighted graph." |
| 回溯 | **backtracking** | "I'll use backtracking to enumerate all possibilities." |
| 动态规划 | **dynamic programming (DP)** | "I'll define the state as dp[i] = ..." |
| 贪心 | **greedy** | "We can solve this greedily." |
| 分治 | **divide and conquer** | "Merge sort is a divide-and-conquer algorithm." |
| 拓扑排序 | **topological sort** | "I'll do a topological sort to detect course prerequisites." |
| 并查集 | **union-find** / **disjoint set** | "Use union-find to count connected components." |
| 单调栈 | **monotonic stack** | "I'll maintain a monotonic decreasing stack." |
| 前缀和 | **prefix sum** | "Precompute the prefix sum for O(1) range queries." |
| Top K | **top K elements** | "I'll use a heap to find the top K." |

#### 30.20.4 UMPIRE 阶段英文话术

##### Understand(理解题意)

```
英文: "Let me make sure I understand the problem correctly..."
       "So the input is X and the output is Y, right?"
       "What are the constraints on the input size?"
       "Can the input be empty?"
       "Can there be negative numbers?"
       "Can there be duplicates?"
       "Should I return the index or the value?"
       "Is the array sorted?"

中文意思: 我想确认下题目理解是否正确...输入是X输出是Y对吗?
         输入规模限制是?能空吗?能有负数吗?能有重复吗?
         返回 index 还是 value?数组是否有序?
```

##### Match(匹配模式)

```
英文: "This problem reminds me of [LC X]."
       "This looks like a sliding window problem."
       "I think we can use a hash map to achieve O(n)."
       "Let me think about which data structure fits best here."

中文意思: 这题让我想到 LC X / 看起来像滑动窗口 / 用 hashmap 应该能 O(n) / 让我想想用什么数据结构最合适。
```

##### Plan(设计算法)

```
英文: "Here's my approach: I'll iterate through the array, and for each element, 
       I'll check if its complement exists in the hash map."
       "Let me walk through the algorithm step by step before coding."
       "I'll first solve the brute force, then optimize."

中文意思: 我的思路是这样的... / 写代码前先把算法走一遍 / 我先写暴力解法,再优化。
```

##### Implement(编码)

```
英文: "Let me start coding."
       "I'll use a dummy node here to simplify edge cases."
       "I'm going to name this variable `seen` because it tracks elements we've encountered."
       "Let me handle the edge case where the input is empty first."

中文意思: 开始写代码 / 用 dummy 节点简化边界 / 这个变量叫 seen,记录看过的元素 / 先处理输入为空的情况。
```

##### Review(走一遍验证)

```
英文: "Let me walk through this with an example."
       "Let's trace through with input [1, 2, 3]."
       "At step 1, i is 0 and num is 1, so..."
       "I see, this returns [0, 1], which matches the expected output."

中文意思: 我用一个例子走一遍 / 用 [1,2,3] 跟踪一下 / 第一步,i=0,num=1,所以... / 这返回 [0,1],跟预期一致。
```

##### Evaluate(复杂度分析)

```
英文: "The time complexity is O(n) because we iterate through the array once."
       "Space complexity is O(n) for the hash map in the worst case."
       "If we don't count the output, the extra space is O(1)."
       "Sorting dominates, so the overall time is O(n log n)."

中文意思: 时间 O(n),只遍历一次 / 空间最坏 O(n) 用了 hashmap / 不算输出额外是 O(1) / 排序主导,总时间 O(n log n)。
```

#### 30.20.5 跟面试官沟通的英文(超实用!)

##### 卡住 / 思考时

```
"Let me think about this for a moment."             (让我想一下)
"Can I take a moment to think about the approach?"  (能稍微思考下吗?)
"I want to explore a different approach."           (我想换个思路)
"Actually, scratch that — let me think differently." (算了,换个角度想)
```

##### 提问澄清

```
"Could you clarify what happens when ___?"           (___ 时该怎么办?)
"Should I optimize for time or space?"              (优化时间还是空间?)
"Is it okay to modify the input in-place?"          (可以原地改输入吗?)
"Do you want me to handle invalid input?"           (要处理非法输入吗?)
```

##### 提示提问

```
"I have one approach in mind. Would you like me to go through it first 
 before optimizing?"                                 (我有个思路,要先讲一遍再优化吗?)

"I'm not sure if there's a more optimal solution. 
 Would you like me to proceed with this?"           (不确定有没有更优解,要继续吗?)

"Could you give me a hint?"                          (能给点提示吗?)— 最后手段,不要太早问
```

##### 发现 Bug 时

```
"Wait, I think there's an issue here. Let me reconsider."   (这里有问题,重新想想)
"Hmm, this edge case isn't handled. Let me fix it."         (这边界没处理)
"I see, I had an off-by-one error here."                    (这里差一错误)
"Let me trace through to make sure this is correct."        (我跟踪一下确认)
```

##### 沟通复杂度

```
"This gives us an O(n) solution, which is optimal."                
(这个 O(n) 解法,已经最优)

"The bottleneck is the sorting step at O(n log n)."                
(瓶颈是排序的 O(n log n))

"I think we can't do better than O(n log n) because we need to sort."   
(因为要排序,做不到比 O(n log n) 更好)
```

#### 30.20.6 经典 Python idiom 的英文解释

面试官常问"为什么这样写",**用英文回答的标准 phrasing**:

##### 关于 `enumerate`

```
中文:用 enumerate 同时拿 index 和 value
英文:"I'm using `enumerate` to get both the index and value in one go,
      which is more Pythonic than using `range(len(nums))`."
```

##### 关于 `sorted` vs `.sort()`

```
中文:sorted 返回新数组,sort 原地修改
英文:"`sorted()` returns a new sorted list without modifying the original,
      while `.sort()` sorts in-place and returns None."

面试中文翻译: 面试官问 "Why did you use sorted instead of sort?"
你可以说: "Because I don't want to mutate the input. It's a good practice 
         to avoid side effects on the function's arguments."
```

##### 关于 Hash Map 找 pair(LC 1 Two Sum)

```
英文:"I'll use a hash map where the key is the number and the value is its index.
      For each element, I check if the complement (target minus current number) 
      already exists in the map. If yes, I return the indices. 
      Otherwise, I add the current number to the map."

中文对应:用 hashmap,key 是数字,value 是 index。对每个元素,
        检查 target - 当前数字是否已在 map 里,在就返回两个 index,
        否则把当前数字存进去。
```

##### 关于 Min-Heap 找 Top K Largest

```
英文:"This might seem counterintuitive, but to find the K largest elements,
      I'll use a **min-heap** of size K. The min-heap's root is the smallest 
      of the K largest, so when a new larger element comes in, I pop the root.
      At the end, the root is the Kth largest."

中文对应:这看起来反直觉,但找前 K 大用 min-heap,堆顶是这 K 个里最小的,
        新来的更大就把堆顶踢出去,最后堆顶就是第 K 大。
```

##### 关于 Sliding Window

```
英文:"I'll maintain a window with two pointers, `left` and `right`. 
      I expand the window by moving `right`, and shrink it by moving `left` 
      when the window violates the constraint."

中文对应:用 left/right 两个指针维护一个窗口。right 扩展窗口,
        如果窗口违反条件就 left 收缩。
```

##### 关于 DFS / Backtracking

```
英文:"I'll do a depth-first search with backtracking. 
      For each node, I make a choice, recurse, and then undo the choice 
      so I can try other options."

中文对应:DFS + 回溯。每个节点做选择、递归、撤销选择,这样能尝试其他可能。
```

##### 关于 Dummy Node(链表)

```
英文:"I'll use a dummy node before the head to simplify edge cases — 
      this way, I don't need to special-case operations on the head node."

中文对应:在 head 前加 dummy 节点简化边界,不用特殊处理头节点。
```

##### 关于 Two Pointers(已排序数组)

```
英文:"Since the array is sorted, I can use two pointers from both ends 
      and converge them toward the middle based on the sum comparison."

中文对应:数组已排序,用对撞双指针,根据和的比较决定向中间移动。
```

#### 30.20.7 终面常见的"软技能"英文

##### 解释思路时显得 confident 但不傲慢

```
✅ "I believe this approach is optimal because..."           (我认为这个解法最优,因为)
✅ "I'd lean toward the hash map approach because..."        (我倾向于 hashmap,因为)
✅ "There might be edge cases I haven't considered, but..."  (可能还有边界没考虑到,但)

❌ "This is obviously the best solution."                    (太傲慢)
❌ "I have no idea."                                         (太消极)
```

##### 承认不会但不卡死

```
✅ "I'm not familiar with [topic], but based on [other knowledge], 
    I'd reason that..."                                       (我不熟悉这个,但根据...)
✅ "I haven't seen this exact problem, but it reminds me of...
    Let me try to apply that pattern here."                   (没见过这题,但让我想到...)

❌ 直接说 "I don't know."(没有补救)
```

##### 收尾(被问 "Any questions?")

```
✅ "Could you tell me more about the team's tech stack?"
✅ "What does a typical day look like for someone in this role?"
✅ "What are the biggest challenges the team is facing right now?"
```

#### 30.20.8 5 句话救命 phrasing(Mock 前背下来)

```
1. "Let me make sure I understand the problem correctly."
   (确认题意时最稳的开场白)

2. "Let me walk through with an example."
   (写完代码后第一句话,演示能让面试官给你"机会分")

3. "The time complexity is O(__) because __, 
    and the space complexity is O(__) because __."
   (面试官最爱听这种带 "because" 的复杂度分析)

4. "Could you clarify __?"
   (任何时候不确定都可以问,显得严谨不是软弱)

5. "I think we can optimize this further. 
    Would you like me to try, or shall we move on?"
   (写完一个解法后,主动展现优化意识)
```

#### 30.20.9 一句话记忆

```
术语:array/string/hash map/heap/deque 这些最常用
概念:in-place/edge case/time complexity 必须脱口而出
沟通:Let me clarify/Let me walk through/Let me think
显得专业:每讲复杂度都带 "because"
显得严谨:边界 case 主动提,不要等面试官问
```

---

## 用法建议

1. **现在不要全部细读**,先扫目录知道有哪些主题
2. **每天对应你计划里的主题**,做题前看一下当天的章节模板
3. **5/6 晚上**通读一遍,标出还不会的地方,5/7 早上重点看
4. **5/7 早上**只看第十四(复杂度)、十五(必说话术)、十六(6 个模板)

---

**祝 5/7 mock 顺利!保持平常心,讲清楚思路比写完代码更重要 💪**
