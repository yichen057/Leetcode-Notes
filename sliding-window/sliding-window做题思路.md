# **Sliding Window 通用模板：从“识别题型”到“自己写出来”**

你现在已经接触了三道典型滑动窗口题：

| **题目**                                             | **窗口类型**           | **窗口合法条件**        |
| ---------------------------------------------------- | ---------------------- | ----------------------- |
| LC 3. Longest Substring Without Repeating Characters | 变长窗口，求最长       | 窗口内没有重复字符      |
| LC 424. Longest Repeating Character Replacement      | 变长窗口，求最长       | 需要替换的字符数 `<= k` |
| LC 567. Permutation in String                        | 固定长度窗口，判断存在 | 窗口频率和 `s1` 相同    |

你现在的问题不是某一题代码不会写，而是：

看到一道新题时，不知道什么时候该想到 sliding window，也不知道条件该写在哪里。

所以你不需要背很多具体题解，而是要建立一套固定分析流程。

------

# **一、Sliding Window 到底解决什么问题？**

Sliding window 主要处理：

在数组或字符串中，寻找一段**连续区间**，并且这个区间需要满足某种条件。

注意关键词：

```text
substring = 连续子串
subarray = 连续子数组
```

如果题目找的是：

```text
连续的一段
```

你就应该开始考虑 sliding window。



例如：

```text
最长无重复子串
最长可以替换后变成同字符的子串
长度固定的排列子串
和至少为 target 的最短连续子数组
```

它们都在研究：

```text
一段连续窗口 [left, right]
```

------

# **二、为什么不用暴力，而用 Sliding Window？**

例如 LC 3：

```python
s = "abcbd"
```

暴力思路会枚举：

```text
"a"
"ab"
"abc"
"abcb"
"abcbd"
"b"
"bc"
"bcb"
...
```

很多 substring 之间有大量重复部分。



Sliding window 的想法是：

```text
我不重新创建每一段 substring。
我只维护当前窗口中发生了什么：
右边加入一个字符；
如果窗口不满足条件，左边移出字符；
窗口合法后更新答案。
```

也就是：

```text
复用上一次窗口的信息，而不是重新计算。
```

------

# **三、什么时候应该想到 Sliding Window？**

做题时先问自己下面四个问题。

## **问题 1：题目研究的是连续区间吗？**

如果题目中出现：

```text
substring
subarray
contiguous
连续子串
连续子数组
```

优先考虑 sliding window。



例如：

```text
longest substring without repeating characters
minimum size subarray sum
find a permutation in a string
```

------

## **问题 2：窗口条件能不能随着左右边界移动而更新？**

例如：

| **题目**     | **窗口中需要维护的信息**         |
| ------------ | -------------------------------- |
| LC 3         | 当前窗口有哪些字符               |
| LC 424       | 每个字符出现次数，最高频字符次数 |
| LC 567       | 当前固定窗口中每个字符出现次数   |
| 最小和子数组 | 当前窗口的 sum                   |

如果右边加入一个元素、左边移出一个元素时，窗口状态可以快速更新，就非常适合 sliding window。

------

## **问题 3：窗口不合法时，移动左边界能不能修复？**

例如 LC 3：

```text
窗口中有重复字符
→ 从左边删字符
→ 可以恢复为没有重复字符
```

例如 LC 424：

```text
需要替换的字符太多
→ 从左边删字符
→ 需要替换的数量可能减少
```

这种“右边扩大，非法后左边缩小”的题，就是标准可变窗口。

------

## **问题 4：题目要求的是最长、最短、数量，还是是否存在？**

这会决定你什么时候更新答案。

| **目标**                 | **常见操作**                                |
| ------------------------ | ------------------------------------------- |
| 求最长合法窗口           | 窗口修复为合法后更新答案                    |
| 求最短满足条件窗口       | 窗口合法时更新答案，然后继续缩小            |
| 判断是否存在固定条件窗口 | 每个固定长度窗口检查一次                    |
| 统计合法窗口数量         | 通常在每轮计算以 `right` 结尾的合法窗口数量 |

------

# **四、你最应该掌握的统一模板**

对于你现在的学习阶段，不建议优先使用九章那种：

```text
固定左指针 i，右指针 j 尽量扩
```

虽然它也对，但边界更绕。



你优先记这一套：

```text
right 负责扩大窗口
窗口非法时，left 负责缩小窗口
窗口满足要求后，更新答案
```

代码骨架：

```python
left = 0
window_state = ...
answer = ...

for right in range(len(data)):
    # 1. Add data[right] into the window.
    ...

    # 2. Shrink the window while it is invalid.
    while window_is_invalid:
        # Remove data[left] from the window.
        ...
        left += 1

    # 3. The current window is valid.
    # Update the answer.
    ...

return answer
```

这是你以后遇到大多数 sliding window 题时，应该首先尝试套用的模板。

------

# **五、模板一：可变长度窗口，求最长合法区间**

## **适用题型**

题目通常包含：

```text
longest substring / subarray satisfying some condition
最长的满足某条件的连续子串 / 子数组
```

核心套路：

```text
right 负责不断扩大窗口
如果加入新元素后窗口非法，left 不断右移修复窗口
窗口合法后，记录当前长度
```

------

## **通用模板**

```python
def longest_valid_window(data) -> int:
    left = 0
    answer = 0
    window = ...

    for right in range(len(data)):
        # Add data[right] into the window.
        ...

        # Shrink until the window becomes valid again.
        while window_is_invalid:
            # Remove data[left] from the window.
            ...
            left += 1

        # The current window is valid.
        answer = max(answer, right - left + 1)

    return answer
```

------

# **六、LC 3 如何套用模板？**

## **题目**

```text
最长没有重复字符的 substring
```

## **第一步：窗口里维护什么？**

维护当前窗口中的字符：

```python
chars = set()
```

## **第二步：窗口什么时候非法？**

当新加入的字符已经在当前窗口中：

```python
s[right] in chars
```

## **第三步：非法时如何修复？**

不断从左边删除字符，直到重复字符消失：

```python
while s[right] in chars:
    chars.remove(s[left])
    left += 1
```

## **第四步：什么时候更新答案？**

窗口恢复合法后：

```python
answer = max(answer, right - left + 1)
```

------

## **最基础的模板版本**

```python
class Solution:
    # Variable-size Sliding Window + Set
    # TC: O(n), because each character enters and leaves the window at most once.
    # SC: O(n), because the set may store distinct characters in the window.
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        left = 0
        answer = 0

        for right in range(len(s)):
            # If s[right] already exists in the current window,
            # shrink the window from the left until it becomes valid.
            while s[right] in chars:
                chars.remove(s[left])
                left += 1

            # Add the new character after duplicates are removed.
            chars.add(s[right])

            # The current window s[left : right + 1] has no duplicates.
            answer = max(answer, right - left + 1)

        return answer
```

------

## **你的 dictionary 写法是什么？**

你之前写的是：

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_idx = {}
        left = 0
        answer = 0

        for right in range(len(s)):
            if s[right] in char_idx and char_idx[s[right]] >= left:
                left = char_idx[s[right]] + 1

            char_idx[s[right]] = right
            answer = max(answer, right - left + 1)

        return answer
```

这是同一个模板的**优化写法**：

```text
Set 版本：
发现重复后，left 一步一步向右移。

Dictionary 版本：
记录重复字符之前的位置，
left 直接跳到重复字符后面。
```

建议你的学习顺序是：

```text
先会 Set + while 通用模板
再记 Dictionary 直接跳跃优化
```

------

# **七、LC 424 如何套用模板？**

## **题目**

```text
最多替换 k 个字符，求替换后最长的重复字符子串长度
```

例如：

```python
s = "AABABBA"
k = 1
```

## **第一步：窗口里维护什么？**

维护当前窗口中每个字符的频率：

```python
count = {}
```

## **第二步：窗口什么时候非法？**

当前窗口中，保留出现最多的字符，其他字符都要替换。

```python
需要替换数 = 窗口长度 - 出现最多字符的次数
```

所以：

```python
invalid = (right - left + 1) - max(count.values()) > k
```

## **第三步：非法时如何修复？**

移除左侧字符：

```python
count[s[left]] -= 1
left += 1
```

## **第四步：什么时候更新答案？**

窗口合法之后：

```python
answer = max(answer, right - left + 1)
```

------

## **推荐你面试先写的版本**

```python
class Solution:
    # Variable-size Sliding Window + Frequency Map
    # TC: O(n), because max(count.values()) examines at most 26 letters.
    # SC: O(1), because s contains only 26 uppercase English letters.
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        answer = 0

        for right in range(len(s)):
            # Add the rightmost character into the current window.
            count[s[right]] = count.get(s[right], 0) + 1

            # If more than k replacements are needed,
            # shrink the window from the left.
            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1

            # The current window is valid.
            answer = max(answer, right - left + 1)

        return answer
```

------

## **这题和 LC 3 的共同模板**

| **部分**         | **LC 3**          | **LC 424**      |
| ---------------- | ----------------- | --------------- |
| `right` 加入什么 | 新字符加入 set    | 新字符频率 `+1` |
| 非法条件         | 当前字符重复      | 替换数 `> k`    |
| `left` 如何移出  | 从 set 删除左字符 | 左字符频率 `-1` |
| 什么时候更新答案 | 修复合法后        | 修复合法后      |

你会发现：

```text
两题真正不同的只有：
窗口中维护的数据结构，以及 invalid 条件。
```

代码骨架是一模一样的。

------

# **八、模板二：固定长度窗口，判断是否存在**

## **适用题型**

题目通常包含：

```text
permutation
anagram
长度固定为 k 的 substring
find whether a window exists
```

例如：

```text
LC 567. Permutation in String
LC 438. Find All Anagrams in a String
```

这类题的关键是：

目标窗口长度天然固定。

例如 `s1 = "ab"` 的任意排列长度都一定是 `2`。

------

## **通用模板**

```python
def fixed_size_window(data, target_length):
    left = 0
    window_state = ...

    for right in range(len(data)):
        # Add data[right].
        ...

        # Keep the window size no larger than target_length.
        if right - left + 1 > target_length:
            # Remove data[left].
            ...
            left += 1

        # Check only when the window reaches the required size.
        if right - left + 1 == target_length and window_is_valid:
            return True

    return False
```

这里一般用：

```python
if right - left + 1 > target_length:
```

而不是 `while`，因为每轮右边只加入一个字符，窗口最多只会超长 `1`。



当然写 `while` 也不会错：

```python
while right - left + 1 > target_length:
```

只是没有必要。

------

# **九、LC 567 如何套用固定窗口模板？**

## **题目**

```text
判断 s2 中是否存在 s1 的某个排列
```

例如：

```python
s1 = "ab"
s2 = "eidbaooo"
```

## **第一步：为什么窗口长度固定？**

因为 `"ab"` 的任何排列：

```text
"ab"
"ba"
```

长度都等于：

```python
len(s1) = 2
```

所以只检查 `s2` 中所有长度为 `2` 的窗口。

------

## **第二步：窗口中维护什么？**

维护：

```text
need：s1 的字符频率
window：当前 s2 窗口的字符频率
```

## **第三步：什么时候满足条件？**

```python
window == need
```

说明当前窗口和 `s1` 由相同数量的字符组成，也就是一个排列。

------

## **你选择的最终版本**

```python
class Solution:
    # Fixed-size Sliding Window + Frequency Arrays
    # TC: O(n), because s2 is scanned once and array comparison costs O(26).
    # SC: O(1), because both arrays always have size 26.
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        m = len(s1)
        need = [0] * 26
        window = [0] * 26

        # Build the target frequency array.
        for ch in s1:
            need[ord(ch) - ord('a')] += 1

        left = 0

        for right in range(len(s2)):
            # Add the new right character.
            window[ord(s2[right]) - ord('a')] += 1

            # Keep the window length equal to m.
            if right - left + 1 > m:
                window[ord(s2[left]) - ord('a')] -= 1
                left += 1

            # A fixed-size window with matching frequency
            # is a permutation of s1.
            if right - left + 1 == m and window == need:
                return True

        return False
```

------

# **十、模板三：可变长度窗口，求最短满足条件区间**

你目前还没有重点做这种题，但它和“求最长”非常容易混淆，所以先建立概念。

## **适用题型**

题目通常包含：

```text
minimum length
smallest window
最短连续子数组
最小覆盖子串
```

例如：

```text
LC 209. Minimum Size Subarray Sum
LC 76. Minimum Window Substring
```

------

## **和“求最长”的区别**

### **求最长合法窗口**

```text
窗口非法时缩小
窗口合法后更新最长答案
```

模板：

```python
for right in range(len(data)):
    add(data[right])

    while window_is_invalid:
        remove(data[left])
        left += 1

    answer = max(answer, right - left + 1)
```

------

### **求最短满足条件窗口**

```text
窗口合法时更新最短答案
然后继续缩小，看能不能更短
```

模板：

```python
for right in range(len(data)):
    add(data[right])

    while window_is_valid:
        answer = min(answer, right - left + 1)

        remove(data[left])
        left += 1
```

注意这里的 `while` 条件正好相反：

| **目标**           | `while` **条件**          |
| ------------------ | ------------------------- |
| 求最长合法窗口     | `while window is invalid` |
| 求最短满足条件窗口 | `while window is valid`   |

------

## **例子：LC 209 Minimum Size Subarray Sum**

题目：

```text
找到和至少为 target 的最短连续子数组长度
```

例如：

```python
target = 7
nums = [2, 3, 1, 2, 4, 3]
```

代码：

```python
class Solution:
    # Variable-size Sliding Window: minimum valid window
    # TC: O(n)
    # SC: O(1)
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        answer = float("inf")

        for right in range(len(nums)):
            current_sum += nums[right]

            # Once the window satisfies the requirement,
            # keep shrinking it to find a shorter valid window.
            while current_sum >= target:
                answer = min(answer, right - left + 1)

                current_sum -= nums[left]
                left += 1

        return 0 if answer == float("inf") else answer
```

这里：

```text
窗口合法条件：current_sum >= target
```

因为我们求的是最短，所以一旦合法，就要继续往小了缩。

------

# **十一、四类常见 Sliding Window 题型总结**

| **类型**     | **题目目标**                      | **窗口长度** | `while` **什么时候执行** | **代表题**     |
| ------------ | --------------------------------- | ------------ | ------------------------ | -------------- |
| 最长合法窗口 | 找最长满足条件 substring/subarray | 可变         | 窗口非法时缩小           | LC 3, LC 424   |
| 最短满足窗口 | 找最短满足条件 substring/subarray | 可变         | 窗口合法时继续缩小       | LC 209, LC 76  |
| 固定长度匹配 | 判断/查找固定长度窗口             | 固定         | 窗口超长时移出左侧       | LC 567, LC 438 |
| 统计合法窗口 | 统计满足条件的窗口个数            | 通常可变     | 依据题意修复窗口         | 以后再学       |

你现在先掌握前三类就够了。

------

# **十二、遇到新题时的固定分析流程**

以后看到一道疑似滑动窗口题，不要立刻想代码。按照下面六步写在草稿上。

------

## **Step 1：窗口是什么？**

先明确：

```text
窗口代表 s[left : right + 1] 中的什么？
```

例如：

| **题目** | **当前窗口代表**                            |
| -------- | ------------------------------------------- |
| LC 3     | 当前不包含重复字符的 substring              |
| LC 424   | 最多替换 `k` 次后可以变成同字符的 substring |
| LC 567   | 长度为 `len(s1)` 的候选排列 substring       |

------

## **Step 2：窗口是固定长度，还是可变长度？**

问自己：

```text
目标 substring 的长度是不是题目已经确定？
```

例如：

```text
Permutation of s1
```

长度一定是：

```python
len(s1)
```

所以 LC 567 是固定窗口。



而：

```text
Longest substring without repeating characters
```

不知道最长是多少，所以 LC 3 是可变窗口。

------

## **Step 3：窗口中要维护什么数据？**

常见维护内容：

| **条件**           | **维护的数据**            |
| ------------------ | ------------------------- |
| 是否有重复字符     | `set` 或 `dict`           |
| 字符出现次数       | `dict` 或长度 26 的 array |
| 数组总和           | `current_sum`             |
| 某字符出现次数最多 | `count` + `maxFreq`       |
| 与目标字符频率相同 | `need` + `window`         |

------

## **Step 4：窗口什么时候非法或满足条件？**

把条件翻译成 Python 表达式。

| **题目** | **条件**                                                  |
| -------- | --------------------------------------------------------- |
| LC 3     | `s[right] in chars` 表示加入后会重复                      |
| LC 424   | `(right - left + 1) - maxFreq > k` 表示非法               |
| LC 567   | `right - left + 1 == len(s1) and window == need` 表示找到 |
| LC 209   | `current_sum >= target` 表示满足条件                      |

------

## **Step 5：左指针什么时候移动？**

这是最关键的判断。

| **问题目标** | **左指针移动时机**     |
| ------------ | ---------------------- |
| 最长合法窗口 | 非法时移动，修复合法性 |
| 最短满足窗口 | 合法时移动，尝试缩短   |
| 固定长度窗口 | 超过目标长度时移动     |

口诀：

```text
求最长：坏了才缩。
求最短：好了还缩。
固定长：超长就缩。
```

------

## **Step 6：答案什么时候更新？**

| **问题目标**         | **更新答案的位置**           |
| -------------------- | ---------------------------- |
| 求最长合法窗口       | 窗口恢复合法后               |
| 求最短满足窗口       | `while` 合法循环内部，缩小前 |
| 判断固定窗口是否存在 | 窗口达到固定长度后           |
| 返回所有匹配起点     | 窗口匹配时加入结果           |

------

# **十三、把三道你学过的题放进同一张表**

| **分析项**      | **LC 3**               | **LC 424**             | **LC 567**              |
| --------------- | ---------------------- | ---------------------- | ----------------------- |
| 目标            | 最长无重复子串         | 最长可替换为同字符子串 | 是否存在排列子串        |
| 连续区间？      | 是                     | 是                     | 是                      |
| 窗口长度        | 可变                   | 可变                   | 固定为 `len(s1)`        |
| 维护什么        | `set` / 字符最近 index | 字符频率               | `need` 和 `window` 频率 |
| 非法 / 匹配条件 | 出现重复字符           | 替换数 `> k`           | `window == need`        |
| 左边什么时候移  | 重复时                 | 替换数过多时           | 窗口超长时              |
| 什么时候更新    | 修复合法后取最大长度   | 修复合法后取最大长度   | 达到固定长度后判断      |
| TC              | `O(n)`                 | `O(n)`                 | `O(n)`                  |
| SC              | `O(n)`                 | `O(1)`                 | `O(1)`                  |

------

# **十四、你可以保存的三个代码模板**

## **模板 A：求最长合法窗口**

```python
def longest_valid_window(data) -> int:
    left = 0
    answer = 0
    window = ...

    for right in range(len(data)):
        # Add data[right] into the window.
        ...

        # Shrink the window until it becomes valid.
        while window_is_invalid:
            # Remove data[left] from the window.
            ...
            left += 1

        # Current window is valid.
        answer = max(answer, right - left + 1)

    return answer
```

对应：

```text
LC 3
LC 424
```

------

## **模板 B：固定长度窗口，判断是否匹配**

```python
def contains_valid_fixed_window(data, target_length) -> bool:
    left = 0
    window = ...

    for right in range(len(data)):
        # Add data[right].
        ...

        # Keep the window at the required length.
        if right - left + 1 > target_length:
            # Remove data[left].
            ...
            left += 1

        # Check only when window length is correct.
        if right - left + 1 == target_length and window_is_valid:
            return True

    return False
```

对应：

```text
LC 567
LC 438
```

------

## **模板 C：求最短满足条件窗口**

```python
def minimum_valid_window(data) -> int:
    left = 0
    answer = float("inf")
    window = ...

    for right in range(len(data)):
        # Add data[right].
        ...

        # The window already satisfies the requirement.
        # Keep shrinking it to find a shorter valid window.
        while window_is_valid:
            answer = min(answer, right - left + 1)

            # Remove data[left].
            ...
            left += 1

    return answer
```

对应：

```text
LC 209
LC 76
```

------

# **十五、建议你的刷题顺序**

你现在已经学了 LC 3、LC 424、LC 567。不要立刻刷很多复杂题，按类别强化模板更有效。

## **第一阶段：巩固已学模板**

| **顺序** | **题目**                                             | **目标**                   |
| -------- | ---------------------------------------------------- | -------------------------- |
| 1        | LC 3. Longest Substring Without Repeating Characters | 掌握最长合法窗口：重复时缩 |
| 2        | LC 424. Longest Repeating Character Replacement      | 掌握复杂一点的非法条件     |
| 3        | LC 567. Permutation in String                        | 掌握固定长度窗口           |

要求：

```text
不看答案写出代码
能够说出窗口状态、非法条件、左指针移动条件
能够分析 TC 和 SC
```

------

## **第二阶段：给每类再补一道**

| **类型**     | **补充题目**                          | **为什么练**                           |
| ------------ | ------------------------------------- | -------------------------------------- |
| 固定窗口匹配 | LC 438. Find All Anagrams in a String | 和 LC 567 几乎同模板，只是返回所有起点 |
| 最短满足窗口 | LC 209. Minimum Size Subarray Sum     | 第一次理解“合法时继续缩小”             |
| 最长合法窗口 | LC 1004. Max Consecutive Ones III     | 和 LC 424 思维非常像，数组版本         |

------

## **第三阶段：再做综合难题**

| **题目**                             | **难点**                           |
| ------------------------------------ | ---------------------------------- |
| LC 76. Minimum Window Substring      | 最小覆盖窗口，频率和满足条件更复杂 |
| LC 904. Fruit Into Baskets           | 最长至多包含两种元素的窗口         |
| LC 713. Subarray Product Less Than K | 统计窗口数量                       |

------

# **十六、你以后自己分析题目时，可以填写这个表**

拿到新题后，先不要写代码，先填：

```text
题目名称：

1. 题目找的是 substring / subarray 吗？
   是 / 否

2. 窗口长度：
   固定 / 可变

3. 当前窗口表示什么？
   ____________________________________

4. 窗口中需要维护什么？
   set / dict / frequency array / sum / ...

5. 窗口什么时候 invalid 或满足条件？
   ____________________________________

6. left 在什么时候移动？
   invalid 时缩 / valid 时缩 / 超过固定长度时缩

7. answer 在哪里更新？
   ____________________________________

8. 复杂度：
   TC:
   SC:
```

------

## **用 LC 424 填一次**

```text
题目名称：LC 424 Longest Repeating Character Replacement

1. 连续区间吗？
   是，substring。

2. 窗口长度：
   可变，要求最长。

3. 当前窗口表示什么？
   一个候选 substring，最多替换 k 个字符后可能全部相同。

4. 维护什么？
   count：窗口中每个字符频率。

5. 窗口什么时候 invalid？
   窗口长度 - 最高频字符次数 > k。

6. left 在什么时候移动？
   invalid 时缩小窗口。

7. answer 在哪里更新？
   窗口恢复 valid 后更新最大长度。

8. 复杂度：
   TC: O(n)
   SC: O(1)，因为只有 26 个大写字母。
```

你能独立填出这张表，代码通常就已经接近写出来了。

------

# **十七、最重要的记忆口诀**

先判断是否是连续区间问题：

```text
substring / subarray → 考虑 sliding window
subsequence → 通常不是 sliding window
```

再判断窗口类型：

```text
目标长度已知 → 固定窗口
目标是最长/最短 → 可变窗口
```

再决定 `left` 什么时候移动：

```text
求最长：窗口坏了才缩。
求最短：窗口好了还缩。
固定长：窗口超长就缩。
```

最后写代码时永远先按这个顺序：

```python
for right in range(len(data)):
    # 1. 加入右边元素

    # 2. 根据题型移动 left

    # 3. 更新答案 / 判断是否找到
```

------

## **你目前最需要形成的思维**

不要看到题目就问：

```text
这题答案代码是什么？
```

而要先问：

```text
窗口是什么？
窗口长度固定还是可变？
我要维护什么信息？
窗口什么时候不合法？
left 为什么移动？
answer 什么时候更新？
```

这六个问题能够回答出来，你就不是在背答案，而是在自己套用 sliding window 模板了。





可以把结论先定下来：

- **LC 643 Maximum Average Subarray I：推荐你保留方法一（先建立第一个窗口，再滑动）**。它更短、更自然，而且可以正确处理全负数数组。
- **LC 567 Permutation in String：推荐你保留一个** **`s2`** **滑动循环的统一模板版本**。你不需要再专门背 `matches` 或“先建立第一个窗口”的写法。
- 一个 `for` loop 并不比两个 `for` loop 的算法更高级。两者时间复杂度相同，只是代码组织方式不同。

------

# **一、先看 LC 643：你的第二种方法有一个 bug**

你的方法二：

```python
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if not nums or k <= 0 or k > len(nums):
            return 0
        
        l = 0
        window_sum = 0
        max_sum = 0

        for r in range(len(nums)):
            window_sum += nums[r]

            if r - l + 1 > k:
                window_sum -= nums[l]
                l += 1

            if r - l + 1 == k:
                max_sum = max(max_sum, window_sum)

        return round(max_sum / k, 5)
```

问题在这里：

```python
max_sum = 0
```

如果数组中的所有长度为 `k` 的窗口和都是负数，`max_sum` 就永远错误地停留在 `0`。



例如：

```python
nums = [-5, -4, -3]
k = 2
```

实际窗口和：

```text
[-5, -4] -> -9
[-4, -3] -> -7
```

正确最大和是：

```python
-7
```

正确最大平均值是：

```python
-3.5
```

但是你的方法二中：

```python
max_sum = 0
max(0, -9) = 0
max(0, -7) = 0
```

最后会错误返回：

```python
0.0
```

------

# **二、LC 643 两种写法对比**

## **方法一：先建立第一个完整窗口，再滑动**

```python
class Solution:
    # Fixed-size Sliding Window + Running Sum
    # TC: O(n)
    # SC: O(1)
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = 0

        # Build the first window of size k.
        for r in range(k):
            current_sum += nums[r]

        # The first valid window initializes the answer.
        max_sum = current_sum

        # Slide the window through the rest of the array.
        for r in range(k, len(nums)):
            current_sum += nums[r]       # Add the new right element.
            current_sum -= nums[r - k]   # Remove the old left element.
            max_sum = max(max_sum, current_sum)

        return max_sum / k
```

这版的优点是：

```text
第一个完整窗口直接初始化 max_sum，
所以无论元素是正数还是负数，都不会出错。
```

例如：

```python
nums = [-5, -4, -3]
k = 2
```

第一窗口：

```python
current_sum = -9
max_sum = -9
```

滑动后：

```python
current_sum = -7
max_sum = max(-9, -7) = -7
```

结果正确。

------

## **方法二：从空窗口开始，一个循环处理所有窗口**

方法二也可以写对，但要修改 `max_sum` 初始化：

```python
class Solution:
    # Fixed-size Sliding Window + Running Sum
    # TC: O(n)
    # SC: O(1)
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        window_sum = 0
        max_sum = float("-inf")

        for right in range(len(nums)):
            # Add the new right element.
            window_sum += nums[right]

            # Keep the window size no larger than k.
            if right - left + 1 > k:
                window_sum -= nums[left]
                left += 1

            # Record the sum only when the window size is exactly k.
            if right - left + 1 == k:
                max_sum = max(max_sum, window_sum)

        return max_sum / k
```

这版也正确。

------

# **三、LC 643 我推荐你用哪一种？**

对于 **LC 643**，我更推荐你的**方法一**：

```python
先计算第一个窗口和
max_sum = 第一个窗口和
后面每次加入右边、移出左边
```

原因是：

| **对比项**           | **方法一：先建立窗口** | **方法二：统一循环** |
| -------------------- | ---------------------- | -------------------- |
| 代码长度             | 更短                   | 稍长                 |
| 是否容易初始化答案   | **非常自然**           | 要注意不能设为 `0`   |
| 是否容易处理负数     | **天然正确**           | 容易踩坑             |
| 是否符合固定窗口思路 | 很符合                 | 也符合               |
| 面试推荐             | **更推荐**             | 也可以               |

所以这题你原来写的方法一其实很好，不需要为了“只有一个 `for` 循环”而改成方法二。

------

# **四、一个** **`for`** **loop 不代表更优**

这里需要建立一个很重要的认识：

算法好不好，不看代码里有几个 `for` loop，而看每个元素被处理了多少次。

你的方法一：

```python
for r in range(k):
    current_sum += nums[r]

for r in range(k, len(nums)):
    ...
```

虽然有两个 `for` loop，但它们不是嵌套循环。



处理次数是：

```text
第一个循环处理前 k 个元素
第二个循环处理剩下 n - k 个元素

总共：k + (n - k) = n
```

所以仍然是：

```text
O(n)
```

而不是：

```text
O(n²)
```

------

## **对比嵌套循环**

真正可能导致 `O(n²)` 的是：

```python
for i in range(n):
    for j in range(n):
        ...
```

因为第二个循环会对第一个循环的每一轮重新完整执行。



而你的方法一是：

```python
for 前一段:
    ...

for 后一段:
    ...
```

两个循环前后顺序执行，所以时间复杂度相加：

```text
O(k) + O(n - k) = O(n)
```

------

# **五、固定长度滑动窗口有两种合理写法**

你现在不需要觉得必须统一成一种代码。固定窗口本身就常见有两个组织方式。

------

## **写法 A：先建立第一个完整窗口，再向后滑动**

结构：

```python
# Build the first window.
for i in range(k):
    add(data[i])

process_first_window()

# Slide later windows.
for right in range(k, len(data)):
    add(data[right])
    remove(data[right - k])
    process_current_window()
```

适合：

```text
最大窗口和
最大平均值
每个窗口值都需要比较
第一窗口自然可以初始化答案
```

代表题：

```text
LC 643 Maximum Average Subarray I
LintCode 604 Window Sum
```

------

## **写法 B：从空窗口开始，统一用一个滑动循环**

结构：

```python
left = 0

for right in range(len(data)):
    add(data[right])

    if right - left + 1 > k:
        remove(data[left])
        left += 1

    if right - left + 1 == k:
        process_current_window()
```

适合：

```text
你希望所有窗口都在同一个位置判断
和你之前总结的 sliding window 模板保持一致
```

代表题：

```text
LC 567 Permutation in String
LC 438 Find All Anagrams in a String
```

两种写法都属于：

```text
Fixed-size Sliding Window
```

并不是两种不同算法。

------

# **六、LC 567 需要学两种写法吗？**

不需要专门背两种。

你现在为 LC 567 选择的版本已经足够好：

```python
class Solution:
    # Fixed-size Sliding Window + Frequency Arrays
    # TC: O(n)
    # SC: O(1)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        m = len(s1)
        need = [0] * 26
        window = [0] * 26

        # Build the frequency array for s1.
        for ch in s1:
            need[ord(ch) - ord('a')] += 1

        left = 0

        for right in range(len(s2)):
            # Add the new right character into the window.
            window[ord(s2[right]) - ord('a')] += 1

            # Keep the window size no larger than len(s1).
            if right - left + 1 > m:
                window[ord(s2[left]) - ord('a')] -= 1
                left += 1

            # A fixed-size window with the same frequency array
            # is a permutation of s1.
            if right - left + 1 == m and window == need:
                return True

        return False
```

这版具备全部面试需要的优点：

```text
逻辑直观
完全符合固定窗口模板
TC: O(n)
SC: O(1)
不需要 matches 的复杂更新
```

你只需要理解“先建立第一个窗口再滑动”版本，因为面试题解或课程里很可能会看到；但不需要为了这题额外背下来。

------

# **七、为什么 LC 643 更适合两段循环，而 LC 567 更适合统一循环？**

它们都可以互换写法，但从学习和面试表达角度，我建议这样区分。

## **LC 643：最大平均值**

题目最终要维护：

```python
max_sum
```

需要一个真实有效的窗口来初始化：

```python
max_sum = first_window_sum
```

所以先建立第一个窗口特别自然：

```python
for r in range(k):
    current_sum += nums[r]

max_sum = current_sum
```

------

## **LC 567：判断是否存在排列**

题目最终只需要：

```python
return True / False
```

不存在“答案初始化为多少”的问题。



所以统一写：

```python
for right in range(len(s2)):
    加入右边字符
    超长就移出左边字符
    长度等于 m 时判断是否匹配
```

逻辑非常统一。

------

# **八、你可以形成这样的个人固定窗口模板**

你不用强制所有题只用一种写法。建议把固定窗口分成两个小模板。

------

## **固定窗口模板 1：求最大值 / 最小值 / 所有窗口结果**

例如：

```text
窗口和
最大平均值
最大窗口值
```

使用“先建立第一个窗口”：

```python
# Build the first full window.
window_state = initial_state(data[:k])
answer = window_state

# Slide to later windows.
for right in range(k, len(data)):
    add(data[right])
    remove(data[right - k])
    update_answer()
```

LC 643 应该归入这里。

------

## **固定窗口模板 2：判断某种窗口是否存在 / 返回所有匹配位置**

例如：

```text
是否有 permutation
找到所有 anagrams 起点
```

使用统一循环：

```python
left = 0

for right in range(len(data)):
    add(data[right])

    if right - left + 1 > k:
        remove(data[left])
        left += 1

    if right - left + 1 == k and window_matches:
        record_or_return()
```

LC 567 应该归入这里。

------

# **九、你的代码复杂度检查**

## **LC 643 方法一**

```python
# TC: O(n)
# SC: O(1)
```

正确。



补充一点：你写的：

```python
return round(max_sum / k, 5)
```

可以通过多数情况，但 LeetCode 本题通常直接返回：

```python
return max_sum / k
```

即可。题目允许一定误差，不需要主动 `round()`。

------

## **LC 643 方法二**

你的复杂度分析正确：

```python
# TC: O(n)
# SC: O(1)
```

但必须把：

```python
max_sum = 0
```

改成：

```python
max_sum = float("-inf")
```

否则负数用例会出错。

------

## **LC 567 两段窗口循环版本**

```python
# TC: O(n)
# SC: O(1)
```

正确。



严格来说，若：

```python
m = len(s1)
n = len(s2)
```

则：

```text
建立 need 和第一窗口：O(m)
滑动 s2 后续窗口：O(n - m)
每次比较两个长度 26 的数组：O(26) = O(1)

总计：O(m + n)；由于 m <= n，所以也可以写 O(n)。
```

------

# **十、最后给你的学习建议**

你的目标不是让每题都只用一个 `for` loop，而是看到题时能识别：

```text
这是固定窗口题
窗口中我要维护什么
窗口移动时加入谁、移出谁
什么时候更新答案或返回结果
```

你现在可以这样保存：

| **题目**                             | **你保留的写法**                | **理由**                         |
| ------------------------------------ | ------------------------------- | -------------------------------- |
| LC 643 Maximum Average Subarray I    | **先建立第一个窗口，再滑动**    | 初始化最大和最自然，避免负数 bug |
| LC 567 Permutation in String         | **统一循环 + frequency arrays** | 模板清楚，判断窗口是否存在很自然 |
| LC 438 Find All Anagrams in a String | 延用 LC 567 统一循环            | 找到匹配时记录起点即可           |

你的 LC 643 方法一和 LC 567 单循环版本都值得保留。
 你不需要为了形式统一，把所有固定滑动窗口题都强行改成同一种写法。



对，你理解得很准确。



这类题本质都是：

```text
fixed-size sliding window + character frequency comparison
```

实现频率统计有两种常见方式：

```python
# 方式 1：dictionary frequency map
window = {}
need = {}
```

或者：

```python
# 方式 2：array frequency map
window = [0] * 26
need = [0] * 26
```

它们本质都是 **frequency map**，只是底层数据结构不同。

------

## **1. Dictionary 版本是不是更简单？**

对新手来说，**dictionary 更直观**。

因为你可以直接写：

```python
window[ch] = window.get(ch, 0) + 1
```

含义很清楚：

```text
当前窗口里，字符 ch 出现次数 +1
```

移出左边字符时：

```python
window[s[left]] -= 1

if window[s[left]] == 0:
    del window[s[left]]
```

含义也清楚：

```text
左边字符离开窗口，它的频率 -1
如果频率变成 0，就从 map 中删除
```

所以对于你现在学习模板，我建议：

**LC 438 / LC 567 先用 dictionary frequency map，更符合直觉。**

------

## **2. List** **`[0] \* 26`** **版本是什么？**

如果题目明确说：

```text
s and p consist of lowercase English letters
```

那么字符只可能是：

```text
'a' 到 'z'
```

一共 26 个。



所以可以用长度为 26 的 list 表示频率：

```python
freq = [0] * 26
```

其中：

```python
freq[0]  # 'a' 的次数
freq[1]  # 'b' 的次数
freq[2]  # 'c' 的次数
...
freq[25] # 'z' 的次数
```

字符转 index：

```python
idx = ord(ch) - ord('a')
```

例如：

```python
ord('a') - ord('a') == 0
ord('b') - ord('a') == 1
ord('z') - ord('a') == 25
```

所以加入字符：

```python
window[ord(s[right]) - ord('a')] += 1
```

移出字符：

```python
window[ord(s[left]) - ord('a')] -= 1
```

这个版本效率更稳定，但代码对新手来说没有 dictionary 那么直观。

------

## **3. 时间复杂度一样吗？**

在 LeetCode 438 / 567 这种只含小写字母的题里，**两者 Big-O 时间复杂度一样，都是** **`O(n)`**。

### **Dictionary 版本**

每轮做：

```python
window == need
```

由于最多只有 26 个小写字母，dictionary 最多 26 个 key。



所以比较成本是：

```text
O(26) = O(1)
```

总共遍历 `s` 一次：

```text
TC: O(n)
```

空间：

```text
SC: O(26) = O(1)
```

------

### **List 版本**

每轮比较：

```python
window == need
```

两个 list 长度固定为 26。



比较成本是：

```text
O(26) = O(1)
```

总共遍历 `s` 一次：

```text
TC: O(n)
```

空间：

```text
SC: O(26) = O(1)
```

所以复杂度一样：

```text
Dictionary version: TC O(n), SC O(1)
List version:       TC O(n), SC O(1)
```

------

## **4. 那哪个更推荐？**

对于你现在的阶段，我建议这样选：

| **情况**                                      | **推荐**                     |
| --------------------------------------------- | ---------------------------- |
| 新手理解、面试讲清楚                          | **dictionary frequency map** |
| 题目明确只有 `'a'` 到 `'z'`，想写更标准/更快  | `[0] * 26`                   |
| 字符集不固定，比如大小写、数字、符号、Unicode | **dictionary**               |
| 想避免 `ord()` 计算，看起来更直观             | **dictionary**               |

所以你的判断是对的：

```text
dictionary frequency map 更简单、更容易理解。
list [0] * 26 更偏向优化和固定字符集场景。
```

------

## **5. 但 dictionary 版本有一个注意点**

你用 dictionary 比较时，必须删除频率为 0 的 key：

```python
if window[s[left]] == 0:
    del window[s[left]]
```

否则：

```python
{"a": 1, "b": 1}
```

和：

```python
{"a": 1, "b": 1, "c": 0}
```

在 Python 里是不相等的。



而 list 版本不需要删除，因为所有字符位置一直都在：

```python
[0, 1, 0, 0, ...]
```

0 本来就是数组中的正常值。

------

## **6. 总结一句话**

你可以这样记：

```text
如果题目限定只有 26 个小写字母：
dictionary 和 [0] * 26 都是 O(n) 时间、O(1) 空间。

dictionary 更好理解；
[0] * 26 更标准、更快一点，但需要 ord() 转换。
```

所以你用 dictionary 完全可以，尤其是现在练习 sliding window 模板时，非常合适。    



你的代码现在是 **LC 209 的标准正确写法**：

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        window_sum = 0
        minLen = float('inf')

        for r in range(len(nums)):
            window_sum += nums[r]

            while window_sum >= target:
                minLen = min(minLen, r - l + 1)
                window_sum -= nums[l]
                l += 1

        return 0 if minLen == float('inf') else minLen
```

这题最关键的点就是：**当窗口已经满足** **`window_sum >= target`** **时，要用** **`while`** **不断移动左指针，尝试把窗口缩到最短。**

------

# **1. 什么时候用** **`while`** **移动左指针？**

你可以用这个规则判断：

如果移动一次左指针后，窗口可能仍然满足条件，并且你还想继续优化答案，就用 `while`。

LC 209 是求：

```text
和至少为 target 的最短连续子数组长度
```

所以当：

```python
window_sum >= target
```

说明当前窗口已经满足条件了。

但它不一定是最短的。你需要继续尝试：

```text
能不能去掉左边一个元素后，sum 仍然 >= target？
如果仍然 >= target，说明窗口还能更短。
那就继续去掉左边。
```

所以必须是：

```python
while window_sum >= target:
    minLen = min(minLen, r - l + 1)
    window_sum -= nums[l]
    l += 1
```

而不是：

```python
if window_sum >= target:
    ...
```

------

# **2. 为什么** **`if`** **会错？**

用一个例子看：

```python
target = 7
nums = [2, 3, 1, 2, 4, 3]
```

正确答案是：

```python
2
```

因为：

```text
[4, 3] 的和是 7，长度是 2
```

------

当 `r = 4` 时，窗口是：

```text
[2, 3, 1, 2, 4]
```

此时：

```python
window_sum = 12
l = 0
r = 4
```

因为：

```python
12 >= 7
```

窗口满足条件。

如果你只用 `if`，只会缩一次：

```text
移除 nums[0] = 2
窗口变成 [3, 1, 2, 4]
sum = 10
```

但是：

```python
10 >= 7
```

窗口还是满足条件，还可以继续缩。

继续缩：

```text
移除 3
窗口变成 [1, 2, 4]
sum = 7
```

仍然满足。

继续缩：

```text
移除 1
窗口变成 [2, 4]
sum = 6
```

这时才不满足。

所以在 `r = 4` 这一轮，左指针其实需要连续移动多次：

```text
l: 0 -> 1 -> 2 -> 3
```

如果只用 `if`，只能移动一次，就会漏掉更短的合法窗口。

------

# **3. 为什么这里是“窗口满足时缩”，不是“窗口不满足时缩”？**

你前面学过 LC 3 / LC 424：

```text
求最长合法窗口：窗口不合法时缩
```

但 LC 209 是：

```text
求最短满足窗口：窗口合法时缩
```

这两个方向相反。

## **求最长时**

比如 LC 3：

```text
窗口没有重复字符才是合法
如果重复了，才缩
合法后更新最长
```

模板：

```python
for r in range(len(s)):
    add s[r]

    while window is invalid:
        remove s[l]
        l += 1

    answer = max(answer, window_length)
```

------

## **求最短时**

比如 LC 209：

```text
窗口 sum >= target 就已经满足条件
但我们想让它更短
所以满足时还要继续缩
```

模板：

```python
for r in range(len(nums)):
    add nums[r]

    while window is valid:
        answer = min(answer, window_length)
        remove nums[l]
        l += 1
```

口诀：

```text
求最长：坏了才缩。
求最短：好了还缩。
固定长：超长就缩。
```

LC 209 属于：

```text
求最短：好了还缩。
```

------

# **4. 为什么右指针** **`r`** **不要走回头路？**

你一开始想：

左指针右移的时候，右指针是不是也可以回到左指针的位置，然后重新往右走？

这个思路相当于重新枚举每个起点：

```text
l = 0 时，让 r 从 0 往右找
l = 1 时，让 r 从 1 往右找
l = 2 时，让 r 从 2 往右找
...
```

这是暴力/半暴力思路，时间复杂度通常会变成：

```text
O(n^2)
```

例如：

```python
for l in range(len(nums)):
    window_sum = 0
    for r in range(l, len(nums)):
        window_sum += nums[r]
        if window_sum >= target:
            update answer
            break
```

这确实是一个可行解法，但不是最优。

------

# **5. Sliding window 的核心：****`r`** **不回头**

LC 209 的 `nums` 都是正整数，这是非常重要的条件。

因为都是正数，所以：

```text
右指针 r 向右移动，window_sum 只会增加；
左指针 l 向右移动，window_sum 只会减少。
```

这就保证了我们可以用双指针：

```text
r 只负责向右扩大窗口；
l 只负责向右缩小窗口；
两个指针都不回头。
```

所以总时间复杂度是：

```text
r 最多走 n 次
l 最多走 n 次
总共 O(n)
```

如果让 `r` 回到 `l`，就失去了这个优势。

------

# **6. 你说“我赋值 r = l 没用”是为什么？**

因为你写的是：

```python
for r in range(len(nums)):
```

在 Python 里，`for` 循环每一轮都会从 iterator 里取下一个值赋给 `r`。

也就是说，即使你在循环内部写：

```python
r = l
```

下一轮循环时，Python 还是会把 `r` 改成 `range` 里的下一个值。

例如：

```python
for r in range(5):
    print("before:", r)
    r = 100
    print("after:", r)
```

输出类似：

```text
before: 0
after: 100
before: 1
after: 100
before: 2
after: 100
...
```

你会发现，下一轮 `r` 还是会按 `range(5)` 继续走，不会因为你赋值成 `100` 就改变循环进度。

所以在 `for r in range(...)` 里，不应该通过修改 `r` 来控制右指针回退。

------

# **7. 有没有“右指针回到左指针”的其他解法？**

有，但不推荐，通常是暴力解法。

## **暴力解法：每个起点重新找终点**

```python
class Solution:
    # Brute force
    # TC: O(n^2)
    # SC: O(1)
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        minLen = float("inf")

        for l in range(n):
            current_sum = 0

            for r in range(l, n):
                current_sum += nums[r]

                if current_sum >= target:
                    minLen = min(minLen, r - l + 1)
                    break

        return 0 if minLen == float("inf") else minLen
```

这个就是你说的：

```text
每次左指针变了，右指针重新从左指针开始。
```

它能做，但不是最优。

------

## **更高级的另一种解法：prefix sum + binary search**

因为 `nums` 是正数，所以 prefix sum 是递增的，可以用二分找每个左端点对应的最短右端点。

时间复杂度：

```text
O(n log n)
```

但对于 LC 209，双指针 `O(n)` 更优，也更适合面试。

------

# **8. 为什么 LC 209 的双指针能成立？**

因为 `nums[i]` 都是 positive integers。

假设当前窗口：

```text
nums[l : r + 1]
```

如果：

```python
window_sum >= target
```

说明它满足条件。

这时我们想找更短窗口，只能尝试移动 `l`：

```text
去掉左边元素，窗口变短
```

如果去掉后仍然满足：

```python
window_sum >= target
```

那说明更短的窗口也可以，继续缩。

如果去掉后不满足：

```python
window_sum < target
```

那当前 `r` 下，不能再缩了。下一步只能让 `r` 继续向右加入新数字，让 sum 再变大。

这个过程非常自然：

```text
sum 不够 → r 向右扩
sum 够了 → l 向右缩
```

------

# **9. 用例子完整走一遍**

```python
target = 7
nums = [2, 3, 1, 2, 4, 3]
```

初始化：

```python
l = 0
window_sum = 0
minLen = inf
```

------

## **r = 0，加入 2**

```text
窗口 [2]
sum = 2
```

不满足：

```python
2 < 7
```

不缩。

------

## **r = 1，加入 3**

```text
窗口 [2, 3]
sum = 5
```

不满足。

------

## **r = 2，加入 1**

```text
窗口 [2, 3, 1]
sum = 6
```

不满足。

------

## **r = 3，加入 2**

```text
窗口 [2, 3, 1, 2]
sum = 8
```

满足：

```python
8 >= 7
```

进入 while。

更新答案：

```python
minLen = min(inf, 4) = 4
```

移除左边 `2`：

```text
窗口 [3, 1, 2]
sum = 6
l = 1
```

现在：

```python
6 < 7
```

停止缩。

------

## **r = 4，加入 4**

```text
窗口 [3, 1, 2, 4]
sum = 10
```

满足，进入 while。

第一次：

```text
长度 4，minLen = 4
移除 3
窗口 [1, 2, 4]
sum = 7
l = 2
```

仍然满足。

第二次：

```text
长度 3，minLen = 3
移除 1
窗口 [2, 4]
sum = 6
l = 3
```

不满足，停止。

------

## **r = 5，加入 3**

```text
窗口 [2, 4, 3]
sum = 9
```

满足，进入 while。

第一次：

```text
长度 3，minLen = 3
移除 2
窗口 [4, 3]
sum = 7
l = 4
```

仍然满足。

第二次：

```text
长度 2，minLen = 2
移除 4
窗口 [3]
sum = 3
l = 5
```

不满足，停止。

最终：

```python
minLen = 2
```

------

# **10. 什么时候** **`if`** **就够，什么时候必须** **`while`****？**

## **固定长度窗口：通常** **`if`** **就够**

比如 LC 567 / 438：

```python
if r - l + 1 > k:
    remove left
    l += 1
```

为什么 `if` 够？

因为每轮右边只加入一个元素，窗口最多只会超长 1。

所以移出一个左边元素就一定恢复到长度 `k`。

------

## **可变窗口求最长：通常用** **`while invalid`**

比如 LC 3 / 424：

```python
while window is invalid:
    remove left
    l += 1
```

为什么用 `while`？

因为移动一次左指针后，窗口可能仍然 invalid。

------

## **可变窗口求最短：通常用** **`while valid`**

比如 LC 209：

```python
while window_sum >= target:
    update answer
    remove left
    l += 1
```

为什么用 `while`？

因为移动一次左指针后，窗口可能仍然 valid，还能继续变短。

------

# **11. 你的 LC 209 可以加这样的注释**

```python
class Solution:
    # Variable-size Sliding Window: minimum valid window
    # TC: O(n), because both left and right pointers only move forward.
    # SC: O(1)
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        window_sum = 0
        minLen = float('inf')

        for right in range(len(nums)):
            # Expand the window by adding nums[right].
            window_sum += nums[right]

            # If the current window satisfies the condition,
            # keep shrinking it from the left to find the shortest valid window.
            while window_sum >= target:
                minLen = min(minLen, right - left + 1)

                # Remove nums[left] from the window.
                window_sum -= nums[left]
                left += 1

        return 0 if minLen == float('inf') else minLen
```

------

# **12. 最后总结**

你一开始的思路里，有一部分是对的：

```text
左指针右移后，要重新考虑新的窗口。
```

但不需要让右指针回到左指针。

Sliding window 的优化点正是：

```text
右指针不回头；
左指针也不回头；
通过维护 window_sum 来复用之前计算过的信息。
```

LC 209 的核心口诀是：

```text
sum 不够，right 继续扩。
sum 够了，left 一直缩，直到不够为止。
每次缩之前都更新最短长度。
```

所以这里必须用：

```python
while window_sum >= target:
```

而不是：

```python
if window_sum >= target:
```

因为你要求的是**最短**，满足条件后要尽可能多地缩小左边界。



可以把三者关系这样理解：



**同向双指针是大类。Sliding Window 是同向双指针的一种常见应用。固定长度窗口和变长窗口，是 Sliding Window 的两种常见子类型。**



关系图：

```text
Two Pointers
├── 相向双指针：left 从左，right 从右，往中间走
│   └── 例：LC 125, LC 167, LC 15
│
└── 同向双指针：left/right 都从左往右走
    ├── Sliding Window 滑动窗口
    │   ├── 固定长度窗口
    │   │   └── 例：LC 567, LC 438, LC 643
    │   └── 变长窗口
    │       ├── 求最长：LC 3, LC 424, LC 1004
    │       └── 求最短：LC 209, LC 76
    │
    └── 非典型窗口型同向双指针
        └── 例：去重、链表交点、快慢指针等
```

------

# **1. 同向双指针是什么？**

同向双指针就是两个指针都往同一个方向移动，通常都是从左到右。

常见形式：

```python
left = 0

for right in range(len(nums)):
    ...
```

或者：

```python
i = 0
j = 0

while i < n:
    while j < n and condition:
        j += 1
    i += 1
```

它的核心特点是：

```text
left 不回头
right 不回头
每个指针最多走 n 步
所以通常是 O(n)
```

------

# **2. Sliding Window 是什么？**

Sliding Window 是同向双指针里最常见的一类。

它强调的是：

用 `left` 和 `right` 维护一个连续区间。

窗口通常是：

```python
nums[left : right + 1]
s[left : right + 1]
```

比如：

```text
s = "abcba"
     l   r
窗口 = s[l:r+1]
```

只要题目研究的是：

```text
substring / subarray / 连续子串 / 连续子数组
```

你就应该优先考虑 sliding window。

------

# **3. 固定长度 Sliding Window**

## **特点**

窗口长度固定，比如：

```text
长度必须是 k
长度必须是 len(s1)
```

这种题不需要思考“窗口什么时候非法”，因为窗口非法通常只是：

```text
窗口太长了
```

所以只要窗口超过固定长度，就移出左边元素。

------

## **适用题型**

看到这些关键词：

```text
length k
size k
permutation of s1
anagram of p
每个长度为 k 的子数组 / 子串
```

就考虑固定长度窗口。

------

## **模板**

```python
left = 0
window_state = ...
answer = ...

for right in range(len(data)):
    # 1. 加入右边元素
    add(data[right])

    # 2. 如果窗口超过固定长度，移出左边元素
    if right - left + 1 > k:
        remove(data[left])
        left += 1

    # 3. 当窗口长度正好为 k 时，判断/更新答案
    if right - left + 1 == k:
        update_answer_or_check()
```

------

## **代表题**

### **LC 567. Permutation in String**

固定窗口长度：

```python
k = len(s1)
```

窗口状态：

```python
need = s1 的频率
window = 当前窗口频率
```

判断：

```python
window == need
```

------

### **LC 438. Find All Anagrams in a String**

和 LC 567 几乎一样。

区别：

```text
LC 567：找到一个就 return True
LC 438：找到一个就 res.append(left)，继续找
```

------

### **LC 643. Maximum Average Subarray I**

固定窗口长度：

```python
k
```

窗口状态：

```python
window_sum
```

答案：

```python
max_sum
```

------

## **固定窗口口诀**

```text
右边加一个；
超长就左边删一个；
长度刚好时检查答案。
```

------

# **4. 变长 Sliding Window**

变长窗口的长度不是固定的，而是根据条件动态变化。

通常有两类：

```text
求最长合法窗口
求最短满足窗口
```

这两类最容易混淆。

------

# **5. 变长窗口：求最长合法窗口**

## **特点**

题目问：

```text
longest substring/subarray ...
最长满足某条件的连续区间
```

这类题的策略是：

```text
right 不断扩大窗口
如果窗口坏了，就移动 left 修复
修好后更新最长答案
```

------

## **模板**

```python
left = 0
answer = 0
window_state = ...

for right in range(len(data)):
    # 1. 加入右边元素
    add(data[right])

    # 2. 如果窗口不合法，左边一直缩，直到合法
    while window_is_invalid:
        remove(data[left])
        left += 1

    # 3. 此时窗口合法，更新最长长度
    answer = max(answer, right - left + 1)

return answer
```

------

## **代表题 1：LC 3**

题目：

```text
最长无重复字符子串
```

窗口状态：

```python
chars = set()
```

非法条件：

```python
s[right] in chars
```

代码骨架：

```python
while s[right] in chars:
    chars.remove(s[left])
    left += 1

chars.add(s[right])
answer = max(answer, right - left + 1)
```

------

## **代表题 2：LC 424**

题目：

```text
最多替换 k 次，得到最长重复字符子串
```

窗口状态：

```python
count = {}
maxf = 当前/历史最高频字符次数
```

非法条件：

```python
窗口长度 - 最高频字符次数 > k
```

代码骨架：

```python
while (right - left + 1) - maxf > k:
    count[s[left]] -= 1
    left += 1

answer = max(answer, right - left + 1)
```

------

## **求最长口诀**

```text
求最长：坏了才缩。
修好以后，更新最大长度。
```

------

# **6. 变长窗口：求最短满足窗口**

## **特点**

题目问：

```text
minimum length
shortest subarray/substring
最短满足某条件的连续区间
```

这类题和“求最长”刚好反过来。



策略是：

```text
right 不断扩大窗口
一旦窗口满足条件，就立刻更新答案
然后继续移动 left，看能不能更短
```

------

## **模板**

```python
left = 0
answer = float("inf")
window_state = ...

for right in range(len(data)):
    # 1. 加入右边元素
    add(data[right])

    # 2. 只要窗口满足条件，就更新答案，并继续缩小
    while window_is_valid:
        answer = min(answer, right - left + 1)

        remove(data[left])
        left += 1

return answer
```

------

## **代表题：LC 209**

题目：

```text
和至少为 target 的最短连续子数组
```

窗口状态：

```python
window_sum
```

满足条件：

```python
window_sum >= target
```

代码骨架：

```python
for right in range(len(nums)):
    window_sum += nums[right]

    while window_sum >= target:
        answer = min(answer, right - left + 1)
        window_sum -= nums[left]
        left += 1
```

------

## **求最短口诀**

```text
求最短：好了还缩。
每次缩之前，先更新最短答案。
```

------

# **7. 三者关系总结表**

| **概念**                    | **是什么**                     | **窗口长度** | **left 何时移动** | **代表题**             |
| --------------------------- | ------------------------------ | ------------ | ----------------- | ---------------------- |
| 同向双指针                  | 两个指针都往右走的大类         | 不一定有窗口 | 视题而定          | 去重、快慢指针、窗口题 |
| 固定长度 sliding window     | 同向双指针维护固定大小连续区间 | 固定         | 超过固定长度时    | LC 567, 438, 643       |
| 变长 sliding window：求最长 | 同向双指针维护可变连续区间     | 可变         | 窗口非法时        | LC 3, 424, 1004        |
| 变长 sliding window：求最短 | 同向双指针维护可变连续区间     | 可变         | 窗口满足条件时    | LC 209, 76             |

------

# **8. 你做题时该怎么判断是哪一种？**

拿到题后按这个顺序问。

------

## **Step 1：是不是连续区间？**

如果题目是：

```text
substring
subarray
contiguous
连续子串
连续子数组
```

优先考虑 sliding window。



如果题目是：

```text
subsequence
子序列
```

通常不是 sliding window，更多是 DP / 双指针匹配。

------

## **Step 2：窗口长度是否固定？**

如果题目说：

```text
长度为 k
permutation of s1
anagram of p
```

就是固定窗口。



因为：

```text
permutation/anagram 的长度固定等于原字符串长度
```

用模板：

```python
if right - left + 1 > k:
    remove left
    left += 1

if right - left + 1 == k:
    check/update
```

------

## **Step 3：如果长度不固定，是求最长还是最短？**

### **求最长**

关键词：

```text
longest
maximum length
最长
```

通常：

```python
while window_is_invalid:
    shrink left

answer = max(answer, window_length)
```

### **求最短**

关键词：

```text
minimum length
smallest
shortest
最短
```

通常：

```python
while window_is_valid:
    answer = min(answer, window_length)
    shrink left
```

------

# **9. 一个非常实用的判断口诀**

```text
固定长：超长就缩。
求最长：坏了才缩。
求最短：好了还缩。
```

对应代码：

## **固定长**

```python
if window_len > k:
    shrink_left()

if window_len == k:
    check()
```

## **求最长**

```python
while invalid:
    shrink_left()

answer = max(answer, window_len)
```

## **求最短**

```python
while valid:
    answer = min(answer, window_len)
    shrink_left()
```

------

# **10. 为什么有时用** **`if`****，有时用** **`while`****？**

这是你之前最容易踩坑的地方。

## **固定长度窗口通常用** **`if`**

因为每轮 `right` 只加一个元素，所以窗口最多只会超长 1。

```python
if right - left + 1 > k:
    remove left
    left += 1
```

移动一次就够。

例如 LC 438 / 567 / 643。

------

## **变长窗口通常用** **`while`**

因为移动一次 `left` 后，窗口可能仍然不满足你想要的状态。

### **LC 3**

重复字符可能还没被移掉，所以要：

```python
while s[right] in chars:
```

### **LC 424**

替换次数可能还是大于 `k`，所以要：

```python
while window_len - maxf > k:
```

### **LC 209**

窗口可能仍然满足 `sum >= target`，还能继续缩短，所以要：

```python
while window_sum >= target:
```

------

# **11. 三套最终模板**

## **模板 A：固定长度窗口**

```python
def fixed_window(data, k):
    left = 0
    window_state = ...
    answer = ...

    for right in range(len(data)):
        # Add right element.
        ...

        # Keep window size at most k.
        if right - left + 1 > k:
            # Remove left element.
            ...
            left += 1

        # Check/update only when window size is exactly k.
        if right - left + 1 == k:
            ...

    return answer
```

适合：

```text
LC 567
LC 438
LC 643
LintCode Window Sum
```

------

## **模板 B：变长窗口，求最长**

```python
def longest_window(data):
    left = 0
    answer = 0
    window_state = ...

    for right in range(len(data)):
        # Add right element.
        ...

        # Fix the window if it becomes invalid.
        while window_is_invalid:
            # Remove left element.
            ...
            left += 1

        # Now the window is valid.
        answer = max(answer, right - left + 1)

    return answer
```

适合：

```text
LC 3
LC 424
LC 1004
LC 904
```

------

## **模板 C：变长窗口，求最短**

```python
def shortest_window(data):
    left = 0
    answer = float("inf")
    window_state = ...

    for right in range(len(data)):
        # Add right element.
        ...

        # Once the window satisfies the condition,
        # keep shrinking to find the shortest one.
        while window_is_valid:
            answer = min(answer, right - left + 1)

            # Remove left element.
            ...
            left += 1

    return 0 if answer == float("inf") else answer
```

适合：

```text
LC 209
LC 76
```

------

# **12. 你目前学过的题应该这样归类**

| **题目** | **分类**       | **你应该记住的核心**                   |
| -------- | -------------- | -------------------------------------- |
| LC 3     | 变长窗口求最长 | 重复时缩                               |
| LC 424   | 变长窗口求最长 | 替换数超过 k 时缩                      |
| LC 567   | 固定长度窗口   | 长度为 `len(s1)`，频率匹配             |
| LC 438   | 固定长度窗口   | 长度为 `len(p)`，频率匹配，记录 `left` |
| LC 643   | 固定长度窗口   | 维护 `window_sum`                      |
| LC 209   | 变长窗口求最短 | `sum >= target` 时一直缩               |

------

# **13. 面试中怎么解释“为什么 right 不回头”**

你可以这样说：

I use two pointers moving in the same direction. The right pointer expands the window, and the left pointer shrinks it when needed. Since both pointers only move forward and never move backward, each element is added and removed at most once, so the time complexity is O(n).

中文就是：

```text
right 只负责扩张窗口；
left 只负责缩小窗口；
两个指针都不回头；
每个元素最多进窗口一次、出窗口一次；
所以是 O(n)。
```

------

# **14. 最后给你一个做题检查表**

以后遇到新题，先填这个：

```text
1. 题目是不是在找连续区间？
   substring / subarray / contiguous?

2. 窗口长度固定吗？
   - 是：固定窗口
   - 否：继续看是求最长还是最短

3. 目标是最长还是最短？
   - 最长：坏了才缩
   - 最短：好了还缩

4. 窗口里维护什么？
   - set?
   - dict/frequency map?
   - [0] * 26?
   - sum?
   - count + maxFreq?

5. 窗口什么时候 invalid / valid？
   写成一个 Python 条件。

6. left 什么时候移动？
   - 超长
   - invalid
   - valid

7. answer 在哪里更新？
   - 固定长：长度正好时
   - 最长：修复合法后
   - 最短：满足条件时，缩小前
```

------

你现在真正需要记住的不是每题代码，而是这三句话：

```text
固定长：超长就缩。
求最长：坏了才缩。
求最短：好了还缩。
```

再加上：

```text
right 只往右加元素；
left 只往右删元素；
right 不需要，也不应该回头。
```