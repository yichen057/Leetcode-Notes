#
# @lc app=leetcode id=151 lang=python3
# @lcpr version=30305
#
# [151] Reverse Words in a String
#
# https://leetcode.com/problems/reverse-words-in-a-string/description/
#
# algorithms
# Medium (54.95%)
# Likes:    10236
# Dislikes: 5520
# Total Accepted:    2.8M
# Total Submissions: 5.1M
# Testcase Example:  '"the sky is blue"\n"  hello world  "\n"a good   example"'
#
# Given an input string s, reverse the order of the words.
# 
# A word is defined as a sequence of non-space characters. The words in s will
# be separated by at least one space.
# 
# Return a string of the words in reverse order concatenated by a single
# space.
# 
# Note that s may contain leading or trailing spaces or multiple spaces between
# two words. The returned string should only have a single space separating the
# words. Do not include any extra spaces.
# 
# 
# Example 1:
# 
# Input: s = "the sky is blue"
# Output: "blue is sky the"
# 
# 
# Example 2:
# 
# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing
# spaces.
# 
# 
# Example 3:
# 
# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single
# space in the reversed string.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^4
# s contains English letters (upper-case and lower-case), digits, and spaces '
# '.
# There is at least one word in s.
# 
# 
# 
# Follow-up: If the string data type is mutable in your language, can you solve
# it in-place with O(1) extra space?
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    # 方法一: 时间复杂度 O(n)：整体反转 O(n)，再用快慢双指针扫描并反转每个单词，总体仍是线性。空间复杂度 O(n)：把字符串转成列表 s = list(s)，还有 result 存结果，都是线性额外空间。
    def reverseWords(self, s: str) -> str:
        s = list(s)
        # Step 1: 对已知string做整体翻转
        s.reverse() # list的反转, 此时： "the sky" -> "yks eht"
# list 有 .reverse() 方法，会就地反转。
# str 没有 .reverse() 方法，所以字符串不能直接调用。如果是字符串，要么用切片 s[::-1]，要么先转成 list 再 reverse()

        # Step 2: 使用快慢指针, 对单词间加空格 
        result = [] # 这里的result是list列表
        fast = 0

        while fast < len(s): # 外层 while fast < len(s) 只保证“开始这一轮”时 fast 没越界
            # 当fast指针指向的非空元素, 确认当前位置不是空格, 只判断了当前一个字符
            if s[fast] != " ":
                if result: # 如果result列表不为空，说明不是第一个单词，需要先加一个空格
                    result.append(" ")

                # 此时result列表为空, 说明是第一个单词, 直接记录单词到result
                start = fast # 记录单词开始的位置
# 内层 while的二次判断, 是用来“走完整个单词”，fast不断递增一直推进到单词末尾（空格或结尾）。所以不是重复判断：外层判断进入单词，内层负责吃完整个单词。
# 内层 while 会不断递增 fast，中途可能到达末尾，所以内层也必须检查 fast < len(s) 才安全访问 s[fast]
                while fast<len(s) and s[fast] != " ": # 内层 while 已经把 fast 向右移动，直到遇到空格或字符串末尾为止。
                    fast += 1

                # step 3: 切片取出字符串里的每个单词, 并在单词内部进行翻转, 变成正常顺序的单词
                #str 和 list 都支持切片语法 s[start:fast]，返回同类型的新对象：对 str 切片得到的是新的 str; 对 list 切片得到的是新的 list
                # 这一步很关键：
                # 因为s整体反转了，单词内部也是反的('yks')。
                # 我们切片取出这个单词，再反转一次变回('sky')，然后加入result
# 在进入这行之前，内层 while 已经把 fast 向右移动，直到遇到空格或字符串末尾为止。也就是说此时 fast 指向的是“单词后面的第一个位置”（空格或末尾），而切片 s[start:fast] 是左闭右开，正好取到完整单词。
                word = s[start:fast] # word是一个字符列表, 左闭右开区间
                word.reverse() # 单词内部反转
                result.extend(word) # 使用 extend 批量加入字符  
                # extend(word) 会把里面的每个字符逐个加入 result。
                # append(word) 会把整个列表当成一个元素塞进去，变成嵌套列表，最后 ''.join(result) 会报错。
                # 示例：
                # result = ['a']; word = ['b','c']
                # extend → ['a','b','c']
                # append → ['a',['b','c']] 
            # 当fast指针指向的空格, fast+1跳过
            else:
                fast += 1

        return "".join(result) # 最后统一拼接返回字符串

# 方法二: 
class Solution:
    def single_reverse(self, s: list, start: int, end: int) -> None: # 原地反转, 所以没有return
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
    
    def reverseWords(self, s: str) -> str:
        result = ""
        fast = 0
        # 1. 首先将原字符串反转并且除掉空格, 并且加入到新的字符串当中
        # 由于Python字符串的不可变性，因此只能转换为列表进行处理
        s = list(s)
        s.reverse()
        while fast < len(s):
            if s[fast] != " ":# fast指针指的非空元素
                if len(result) != 0: # 非第一个单词, 新的单词的开始, 所以需要result+空格, 再加新单词
                    result += " "
                while fast < len(s) and s[fast] != " ":# 第一个单词, 直接记录, 并移动fast指针
                    # 注意: 这里要注意while语句里的顺序! 
                    # 如果是 while s[fast] != " " and fast < len(s): 会先访问 s[fast]，当 fast == len(s) 时直接 IndexError。应该先判断边界，再访问元素。
                    result += s[fast]
                    fast += 1
            else: # fast指针指的为空格元素
                fast += 1

        # 2.其次将每个单词进行翻转操作
        slow = 0 # 慢指针：标记一个单词的开头
        fast = 0 # 快指针：去寻找一个单词的结尾
        result = list(result) # 再次转成列表，为了使用前面的 single_reverse 助手
        
        while fast <= len(result): # 注意这里是 <=，因为要处理最后一个单词结束的情况
            # 这里的条件是：如果 fast 跑到了字符串末尾，或者 fast 指向了空格
            # 这意味着：slow 到 fast-1 这一段，正好是一个完整的单词！
            if fast == len(result) or result[fast] == " ":
                self.single_reverse(result, slow, fast-1) # 调用助手，把这个单词翻转回来
                slow = fast + 1 # 翻转完，慢指针跳过空格，准备抓下一个单词的开头
                fast += 1 # 快指针继续跑
            else:
                fast += 1 # 如果没遇到空格，快指针就一直往后跑
        
        return "".join(result)

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# "the sky is blue"\n
# @lcpr case=end

# @lcpr case=start
# "  hello world  "\n
# @lcpr case=end

# @lcpr case=start
# "a good   example"\n
# @lcpr case=end

#

# 卡玛网55题: 右旋字符串
# 字符串的右旋转操作是把字符串尾部的若干个字符转移到字符串的前面。给定一个字符串 s 和一个正整数 k，请编写一个函数，将字符串中的后面 k 个字符移到字符串的前面，实现字符串的右旋转操作。
# 例如，对于输入字符串 "abcdefg" 和整数 2，函数应该将其转换为 "fgabcde"。
# 输入：输入共包含两行，第一行为一个正整数 k，代表右旋转的位数。第二行为字符串 s，代表需要旋转的字符串。
# 输出：输出共一行，为进行了右旋转操作后的字符串。

# 获取输入的数字k和字符串
k = int(input())
s = input()

#通过切片反转第一段和第二段字符串
#注意：python中字符串是不可变的，所以也需要额外空间
# 方法一: 表示从索引 len(s)-k 开始一直到结尾+表示从开头一直到索引 len(s)-k（不包含 len(s)-k ）
s = s[len(s)-k:] + s[:len(s)-k]
print(s)
# 方法二: 取字符串最后 k 个字符+从开头取，一直取到倒数第 k 个字符之前（也就是去掉最后 k 个字符剩下的部分）, 不包含-k
s = s[-k:] + s[:-k]
print(s)

# Python 的字符串是不可变的（Immutable）, 但却没看到 s=list(s), 但 `s[...] + s[...]` 这个切片加拼接的过程，本身就申请了新的内存空间来存储结果（空间复杂度为 O(N)）。
# 当你执行 `s = ... + ...` 这种操作时，Python并没有在原来的内存地址上修改数据，而是在内存中创建了一个全新的字符串对象，把拼接好的结果存进去，然后让变量 `s` 指向这个新地址。