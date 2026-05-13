#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (67.03%)
# Likes:    13559
# Dislikes: 456
# Total Accepted:    5.3M
# Total Submissions: 7.9M
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t, return true if t is an anagram of s, and false
# otherwise.
# 
# 
# Example 1:
# 
# 
# Input: s = "anagram", t = "nagaram"
# 
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "rat", t = "car"
# 
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.
# 
# 
# 
# Follow up: What if the inputs contain Unicode characters? How would you adapt
# your solution to such a case?
# 
#

# @lc code=start
class Solution:
     # 方法一: Frequency array method: 先统计 s 里每个字母出现次数再用 t 里的字母去抵消, 最后检查是否全部归零
    def isAnagram(self, s: str, t: str) -> bool:
        # 长度不等直接返回, 不用浪费计算
        if len(s) != len(t):
            return False
        
        # 用数组的哈希法做. 这个数组哈希法只适合题目限制为：只包含小写英文字母 a-z
        record = [0] * 26 # 创建长度为26的数组, 默认值为0. 题目里只有小写字母 'a'..'z'，它们的 ASCII 是 97~122。
        for i in s:
            record[ord(i)-ord("a")] += 1 # 用 ord(i) - ord("a")，就把 'a' 映射到 0，'z' 映射到 25，这样只需要一个 长度为 26 的数组。
            # index指的就是字母, value指的是字母出现的个数(初始值为0). 这是一种非常高效的哈希映射（Hash Mapping）简写方式
            # ord(i)：获取字符 i 的 ASCII 值。例如 ord('a') 是 97，ord('b') 是 98。ord(i) - ord('a')：这是一个偏移量（Offset）计算。
            # 如果是 'a'：97 - 97 = 0（对应 record[0]）如果是 'b'：98 - 97 = 1（对应 record[1]）如果是 'z'：122 - 97 = 25（对应 record[25]）所以，Index 0 到 25 完美映射到了字母 'a' 到 'z'。
            # ord() 在 Python 里就是把字符转换成 Unicode 编码（常见情况就是 ASCII 值）。
        for i in t:
            record[ord(i)-ord("a")] -= 1
            # 方法一, 提前判断
            if record[ord(i)-ord("a")] < 0:
            # 注意判断条件不能写!=0, 因为此处这个判断还没有把整个t都遍历完. 
            # s里同一个字母如果出现2次以上, 则count里元素对应是>=2的, 那t在减1时, 第一次-1得到的值未必等于0 ,有可能大于0, 那么对于>0的情况, 如果这里判断为不等于0, 就会提前误判
                return False
            
        #方法二: 循环后遍历这个新数组统一检查, 看有没有元素不为0, 则return false
        # for i in range(26):
        #     if record[i] != 0:
        #         return False
        return True
    
#     对比结论
# 最坏复杂度：方法一 = 方法二 = O(n)
# 最好情况：方法一更快（可以提前返回），方法二还是要扫完
# 常数开销：方法一不需要额外检查数组，方法二多一个 O(26) 的循环，但这可以认为是常数级无关紧要

# 方法二: sorting. TC: O(n log n); SC: O(1)
# Time complexity: O(nlogn).
# Assume that n is the length of s, sorting costs O(nlogn) and comparing two strings costs O(n). Sorting time dominates and the overall time complexity is O(nlogn).

# Space complexity: O(1).
# Space depends on the sorting implementation which, usually, costs O(1) auxiliary space if heapsort is used. Note that in Java, toCharArray() makes a copy of the string so it costs O(n) extra space, but we ignore this for complexity analysis
    # def isAnagram(self, s: str, t: str) -> bool:
    #     s = sorted(s) # nums.sort()仅限列表, 会修改原件, 返回值None; sorted(nums):可操作任何可迭代对象, 未修改原件, 返回值是新的列表. 总之: sort() 是“就地正法”，sorted() 是“另起炉灶”。
    #     t = sorted(t)
    #     return s == t # 判断字符串内容是否一样，用 == 就对了
        # ==：比较的是内容（Value）。就像两本书的内容是不是一模一样。
        # is：比较的是内存地址（Identity）。就像这两本书是不是物理上的同一本。

# 方法三: Counter更通用, 尤其是如果字符是大写字母, 中文, 空格, 符号, Unicode
# from collections import Counter
# class Solution:
#     def is_anagram(s, t):
#         s_count = Counter(s)
#         t_count = Counter(t)

#         return s_count == t_count
# Counter = 自动帮你统计“每个元素出现几次”的字典。等价于下面的代码:Counter就是帮你把自动做好frequemcy map, 所以时间和空间复杂度是O(n), 空间复杂度取决于字符种类。
# count = {}
# for ch in s:
#     count[ch] = count.get(ch, 0) + 1
'''
**Unicode 不是 ASCII，但它包含了 ASCII。**
你可以把 ASCII 想象成一个小信封，而 Unicode 是一个巨大的集装箱。
### 1. 核心区别：容量不同
* **ASCII** (American Standard Code for Information Interchange)：
* **诞生背景**：早期为美国设计的。
* **容量**：仅使用 7 位（bit）二进制，总共只能表示 **128 个字符**。
* **包含内容**：大小写英文字母、数字 0-9 以及一些基本标点符号（如 `!`, `@`, `#`）。
* **局限性**：它完全没法表示中文、日语、甚至是法语里的特殊重音符号。
* **Unicode** (万国码/统一码)：
* **诞生背景**：为了解决全球字符统一编码的问题。
* **容量**：理论上可以容纳 **超过 110 万个字符**（目前已定义了 14 万多个）。
* **包含内容**：几乎全世界所有的语言（中文、阿拉伯语、Emoji 表情 🐍、数学符号等）。
---
### 2. 它们的关系：向下兼容
为了让老程序也能跑，Unicode 在设计时做了一个非常聪明的决定：
**Unicode 的前 128 个字符与 ASCII 完全一模一样。**
* 例如：在 ASCII 中，字母 `A` 的编号是 **65**；在 Unicode 中，字母 `A` 的编号（码点）依然是 **65**。
* 这意味着：**所有的 ASCII 码都是合法的 Unicode 码，但 Unicode 码绝大多数都不是 ASCII 码。**
---
### 3. 一个容易混淆的概念：Unicode vs UTF-8
在写代码（比如你之前看的 [Valid Anagram](https://leetcode.com/problems/valid-anagram/description/)）时，你经常会听到这两个词。请记住这个比喻：
* **Unicode 是“字典”**：它规定了 `A` 对应 65，`哈` 对应 21704。它只负责给字符编号。
* **UTF-8 是“存储方案”**：它负责规定在电脑硬盘里，这个编号怎么存成二进制。
* 对于英文字符，UTF-8 只用 **1 个字节**（8 位），和 ASCII 几乎一样。
* 对于中文字符，UTF-8 通常用 **3 个字节**。
---
### 4. 为什么面试题（如 LeetCode）常问 Unicode？
回到你正在刷的算法题：
* **如果题目说只有小写字母**：你可以放心地开一个长度为 **26** 的数组 `record = [0] * 26`，因为 ASCII 范围很窄。
* **如果题目说包含 Unicode**：你不能再开固定长度的数组了（因为字符可能有几十万种），这时候必须使用 **HashMap / 字典** (`map = {}`) 来统计频率。
> **总结：** ASCII 是 Unicode 的一个**真子集**。你可以把 Unicode 看作是 ASCII 的全球超级加强版。
'''
# @lc code=end

