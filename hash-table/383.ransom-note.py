#
# @lc app=leetcode id=383 lang=python3
# @lcpr version=30305
#
# [383] Ransom Note
#
# https://leetcode.com/problems/ransom-note/description/
#
# algorithms
# Easy (65.41%)
# Likes:    5581
# Dislikes: 540
# Total Accepted:    1.8M
# Total Submissions: 2.8M
# Testcase Example:  '"a"\n"b"\n"aa"\n"ab"\n"aa"\n"aab"'
#
# Given two strings ransomNote and magazine, return true if ransomNote can be
# constructed by using the letters from magazine and false otherwise.
# 
# Each letter in magazine can only be used once in ransomNote.
# 
# 
# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
# 
# 
# Constraints:
# 
# 
# 1 <= ransomNote.length, magazine.length <= 10^5
# ransomNote and magazine consist of lowercase English letters.
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
# from common.node import *
# 解题的思路是利用一个哈希表或者说一个长度为 26 的数组，因为只有小写字母 a 到 z 共 26 个。
# 我们先统计 magazine 中每个字符出现的次数，然后再统计 ransom 中每个字符需要的次数。
# 最后比较 ransom 中每个字符的需求量是否都能被 magazine 中对应的字符数覆盖。
# 如果 magazine 中的某个字符不够用，那么返回 false；如果全部满足，则返回 true。
# @lc code=start
class Solution:
    # method 1: Array: # 因为只有 26 个字母，用数组比 HashMap 更快
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = [0] * 26
        magazine_count = [0] * 26
        for c in ransomNote:
            ransom_count[ord(c) - ord('a')] += 1
            # ord(c)：Python 的函数，用来获取字符 c 的 ASCII 码（整数）
        for c in magazine:
            magazine_count[ord(c) - ord('a')] += 1
        for i in range(26): # 让变量 i 依次取值 0, 1, 2, ..., 25。
            if ransom_count[i] > magazine_count[i]:
                return False
        return True
    # # 优化method 1: create only one list
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        record = [0] * 26
        for c in magazine:
            record[ord(c) - ord('a')] += 1
        for c in ransomNote:
            idx = ord(c) - ord('a')
            # 先减后查
            record[idx] = -1 # 1. 先从库存里扣掉
            if record[idx] <0: # 2. 扣完发现变成负数了（说明扣之前已经是 0）
                return False # 3. 失败
        return True

    # method 2: HashMap  
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # 1. Record the frequency of each character in magazine
        freq_dic = {}
        for char in magazine:
            # if char in freq_dic:
            #     freq_dic[char] += 1
            # else:
            #     freq_dic[char] = 1
            freq_dic[char] = freq_dic.get(char,0)+1 # dic.get(key, default) 的核心目的就是获取 key 对应的 value，但它比直接用 dic[key] 更安全
        # 2. Iterate thru ransomNote, offset the value in freq_dic
        for char in ransomNote:
            if char not in freq_dic or freq_dic[char] <= 0: # 先查后减 1. 先看库存够不够（如果是 0 就说明不够扣）
                return False # 2. 失败
            freq_dic[char] -= 1 # 3. 够扣才执行扣除

        return True



'''
1. counts[char] = counts.get(char, 0) + 1
这行代码其实涵盖了两种情况：

第一次遇到字符 'a'：

counts.get('a', 0) 发现字典里没 'a'，于是返回默认值 0。

代码变成 0 + 1。

结果：counts 变成 {'a': 1}。

第二次遇到字符 'a'：

counts.get('a', 0) 发现字典里已经有 'a' 了，当前值是 1，于是返回 1。

代码变成 1 + 1。

结果：counts 更新为 {'a': 2}。

💡 一个小细节
如果你写 dic.get(key) 而不写第二个参数（即 default），那么当 key 不存在时，它会默认返回 None。

所以总结一下：
它是获取 value 的一种“防御性”写法，专门用来对付那些“可能还没被创建”的键。

2. 边界是否等于0的校验, 这正体现了**“先减后查”**与**“先查后减”**这两种逻辑顺序的区别。

之所以这里用 `record[idx] < 0`，是因为在代码中，我们是**先执行了减法，后进行的检查**。

### 1. 逻辑顺序的拆解

让我们对比一下这两种写法：

#### 写法 A：先减后查（你现在的代码）
```python
record[idx] -= 1       # 1. 先从库存里扣掉
if record[idx] < 0:    # 2. 扣完发现变成负数了（说明扣之前已经是 0）
    return False       # 3. 失败
```

#### 写法 B：先查后减（之前的 HashMap 写法）
```python
if record[idx] <= 0:   # 1. 先看库存够不够（如果是 0 就说明不够扣）
    return False       # 2. 失败
record[idx] -= 1       # 3. 够扣才执行扣除
```

---

### 2. 举个例子：库存只有 1 个 'a'

假设 `magazine = "a"`, `ransomNote = "aa"`。

* **处理第 1 个 'a'：**
    1.  `record[idx]` 从 `1` 变成 `0`。
    2.  检查：`0 < 0` 为 **False**。
    3.  结果：通过，继续（此时库存刚好用完）。

* **处理第 2 个 'a'：**
    1.  `record[idx]` 从 `0` 变成 `-1`。
    2.  检查：`-1 < 0` 为 **True**。
    3.  结果：**返回 False**（正确拦截了越界行为）。

---

### 3. 为什么这种写法更受欢迎？

在数组解法中，大家习惯用 `record[idx] < 0`，主要有两个原因：

1.  **代码更简洁：** 你不需要写 `if char not in record`（因为数组索引总是存在的），直接无脑减，减完看一眼结果就行。
2.  **更符合直觉：** “欠债”（负数）代表不够。如果结果是 `0`，代表“刚好够，没欠钱”，所以不应该返回 False。

---

### 💡 总结

* 如果你**先减**，就判断是否 **`< 0`**（欠账了）。
* 如果你**先查**，就判断是否 **`<= 0`**（没余粮了）。

这两种逻辑在结果上是完全等价的，关键看你把 `if` 语句放在减法操作的前面还是后面。

如果你现在把代码改成下面这样，你觉得应该用 `< 0` 还是 `<= 0` 呢？
```python
for c in ransomNote:
    idx = ord(c) - ord('a')
    if record[idx] ??? 0:
        return False
    record[idx] -= 1
```
'''
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here

if __name__ == '__main__':
    solution = Solution()

    # Quick prints
    print(solution.canConstruct("a", "b"))    # False
    print(solution.canConstruct("aa", "ab"))  # False
    print(solution.canConstruct("aa", "aab")) # True

    # Or assertions
    assert solution.canConstruct("a", "b") is False
    assert solution.canConstruct("aa", "ab") is False
    assert solution.canConstruct("aa", "aab") is True



#
# @lcpr case=start
# "a"\n"b"\n
# @lcpr case=end

# @lcpr case=start
# "aa"\n"ab"\n
# @lcpr case=end

# @lcpr case=start
# "aa"\n"aab"\n
# @lcpr case=end

#

