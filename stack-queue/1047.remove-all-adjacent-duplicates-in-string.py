#
# @lc app=leetcode id=1047 lang=python3
# @lcpr version=30305
#
# [1047] Remove All Adjacent Duplicates In String
#
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/
#
# algorithms
# Easy (72.58%)
# Likes:    7014
# Dislikes: 273
# Total Accepted:    822.3K
# Total Submissions: 1.1M
# Testcase Example:  '"abbaca"\n"azxxzy"'
#
# You are given a string s consisting of lowercase English letters. A duplicate
# removal consists of choosing two adjacent and equal letters and removing
# them.
# 
# We repeatedly make duplicate removals on s until we no longer can.
# 
# Return the final string after all such duplicate removals have been made. It
# can be proven that the answer is unique.
# 
# 
# Example 1:
# 
# Input: s = "abbaca"
# Output: "ca"
# Explanation: 
# For example, in "abbaca" we could remove "bb" since the letters are adjacent
# and equal, and this is the only possible move.  The result of this move is
# that the string is "aaca", of which only "aa" is possible, so the final
# string is "ca".
# 
# 
# Example 2:
# 
# Input: s = "azxxzy"
# Output: "ay"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s consists of lowercase English letters.
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def removeDuplicates(self, s: str) -> str:
        # 方法一: 使用栈 
        # res = list()
        # for item in s:
        #     if res  and res[-1] == item:
        #         res.pop()
        #     else:
        #         res.append(item)
        # return "".join(res)
        # 方法二: 使用双指针模拟栈, 如果不让用栈可以作为备选方法. 
        # 用 `fast` 指针遍历字符串，用 `slow` 指针维护一个“结果栈”的顶部位置。
        res = list(s) # 将字符串转为列表list, 就能通过索引修改里面的字符了
        slow = fast = 0
        length = len(res)

        while fast < length: # 只要快指针 fast 还没有走完整个字符串，循环就继续
            res[slow] = res[fast] # 先把 fast 指向的字符“搬”到 slow 的位置
            # 这相当于尝试把当前字符 入栈。如果是一个新字符，它就留在这里了。如果是重复字符，我们会在下一步把它“消除”掉

            # 如果发现和前一个一样, 就退一格指针
            if slow > 0 and res[slow] == res[slow - 1]:
                slow -= 1 # slow -= 1 (消除): 如果一样，说明发现了一对相邻重复项。我们将 slow 向后退一步。
                # 效果: 这相当于 “出栈”。退一步后，当前的 slow 位置（原来的前一个字符）变成了“待写入”状态。下一次循环时，新的字符会覆盖在这个位置上，从而把这两个重复的字符都“抹去”了
            else:
                slow += 1
            fast += 1 # 不管刚才发生了消除还是保留，fast 指针永远要向前走，去处理原始字符串的下一个字符
        # slow 总是指向下一个要写入的位置（或者理解为当前栈的长度），所以处理完所有字符后，slow 会停在 2 的位置(实例: "abbaca"). 循环结束后，slow 指针的位置就是最终结果的长度
        return ''.join(res[0: slow]) # 把列表 res 中从下标 0 到 slow-1 的有效字符切出来(res[0: slow] 指的是左闭右开区间)，拼接成一个字符串并返回
        # ''.join(...)：这是 Python 字符串的一个方法。它的作用是将列表（或者可迭代对象）中的元素，用前面的分隔符（这里是空字符串 ''）连接起来。
        # 所以 res[0: slow] 截取出了有效字符列表 ['c', 'a']，然后 ''.join(['c', 'a']) 把它变成了字符串 "ca" 返回。
        
    
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# "abbaca"\n
# @lcpr case=end

# @lcpr case=start
# "azxxzy"\n
# @lcpr case=end

#

