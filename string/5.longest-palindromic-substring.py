#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (36.26%)
# Likes:    31331
# Dislikes: 1929
# Total Accepted:    4.1M
# Total Submissions: 11.3M
# Testcase Example:  '"babad"'
#
# Given a string s, return the longest palindromic substring in s.
# 
# 
# Example 1:
# 
# 
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: s = "cbbd"
# Output: "bb"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 1000
# s consist of only digits and English letters.
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
# LC 125 Valid Palindrome: 相向双指针，两边往中间
# LC 5 Longest Palindromic Substring: 中心扩展，中心往两边
# 第一优先级：中心扩展法 helper 版本，必须会写。
# 这题最核心的记忆点：
# 每个回文都有一个中心。
# 中心可能是一个字符，也可能是两个字符之间。
# 枚举所有中心，向两边扩展。
# 第二优先级：理解不带 helper 的版本，方便 debug。
# 第三优先级：知道暴力法 O(n³)，可以用来解释优化来源。
# 第四优先级：DP 了解即可，不建议作为首选。
# tuple 版本可看可不看。
# expand around center method中心扩散法: 枚举中心 O(n), 每个中心向两边扩展 O(n), 总共 O(n²)
# TC: O(n^2): 
# 外层for i循环会遍历每个位置, 所以是O(n); 
# 每个位置会做两次中心扩散:1)odd: l, r = i, i ; 2) even:l, r = i, i + 1每次扩展最坏可能扩到整个字符串长度，所以单次中心扩展最坏是O(n)
# 所以总时间复杂度: O(n) * O(n) = O(n^2)
# SC: O(1) excluding output
# SC: O(n) including returned substring
# 而如果是暴力枚举算法: 暴力枚举所有 substring，然后判断是不是 palindrome。
# 枚举长度 O(n), 枚举起点 O(n), 检查当前子串是否回文 O(n), 总共 O(n³)

# I use expand around center.
# For each index, I consider two possible centers:
# one for odd-length palindromes and one for even-length palindromes.
# For each center, I expand outward while both characters are equal.
# There are O(n) centers, and each expansion can take O(n), so the time complexity is O(n²).
# I only use a few variables, so the space complexity is O(1) excluding the output.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            # odd length palindrome, like "aba"
            l , r = i, i # i is our center position now
            # while left and right pointer is in bound and check it is a palindrome
            while l >= 0 and r < len(s) and s[l] == s[r]: # 真正回文范围是：left 右边一个位置 到 right 左边一个位置, 即l+1, r-1
                if (r - l + 1) > resLen: # if the length of palindrome > current length
                    res = s[l : r+1] # update the result
                    # Python 字符串切片会创建一个新的字符串，所以 res 最长可能保存长度为 n 的答案
                    resLen = r - l + 1 # update the result length
            # 从中间往两边走:expand pointers outward: left pointers shift to the left and right pointers shift to the right
                l -= 1
                r += 1

            # while结束时,left 和 right 处于第一个“不合法”的位置: 要么越界了, 要么字符不相等了. 真正的回文边界要往回收一格: l+1到r-1。
            # edge case: even lenghth palindrome, like "abba"
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r+1]
                    resLen = r - l + 1
                # expand pointers outward
                l -= 1
                r += 1
        return res

# 完整抽取版”，但要用 nonlocal, 把重复代码尽量完整放进 helper：推荐!
# 从“减少重复代码”的角度，nonlocal 版本抽得更彻底。
# 如果是为了刷 LeetCode，可以用 nonlocal 版本，因为短、直观；如果是为了面试，我建议用“helper 返回范围”的版本，更容易解释。
 # Expand Around Center
    # TC: O(n^2)
    # SC: O(1) excluding output
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0
        
        def expand(l: int, r: int) -> None:
            nonlocal res, resLen # nonlocal 用在嵌套函数里，让内部函数可以修改外层函数的变量。
            # 这里如果不写nonlocal, Python 认为 resLen 是 expand() 内部的局部变量。
            

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > resLen: # 但这句你要读取一个局部变量 resLen，但它还没有被赋值。如果前面没写nonlocal的话, 会报错
                    res = s[l: r+ 1] # 因为 Python 切片右边不包含，所以闭区间 [l, r] 要写成：s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        for i in range(len(s)):
            expand(i, i)       # odd length
            expand(i, i + 1)   # even length
        return res

# expand around center + helper method:推荐, 最佳!
# “helper 返回范围”的版本: 只扩展，返回 left/right
# 本方法的好处:
# helper 不修改外部变量，只返回结果。
# 主函数统一更新最终答案。
# 代码更容易 debug，也更像面试中的 clean code。
# 从“代码职责清晰”的角度，返回范围版本更推荐。
# Expand Around Center
    # TC: O(n^2)
    # SC: O(1) excluding output
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        start = 0
        maxLen = 0

        for i in range(len(s)):
            # Odd length palindrome, like "aba"
            l, r = self.expand(s, i , i)
            if r - l + 1 > maxLen:
                start = l
                maxLen = r - l + 1
            # Even length palindrome, like "abba"
            l, r = self.expand(s, i, i+1)
            if r - l + 1 > maxLen:
                start = l
                maxLen = r - l + 1
        return s[start: start + maxLen]

    def expand(self, s: str, l: int, r: int) -> tuple[int, int]:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        # while 停下来的时候，left 和 right 已经多走了一步: 要么越界, 要么字符不相等了
        # 所以真正的回文范围是: left 右边一个位置 到 right 左边一个位置
        return l+1, r-1


# # tuple method: 
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if not s:
#             return s
        
#         answer = (0,0)
        
#         for mid in range(len(s)):
#             answer = max(answer, self.get_palindrome_from(s,mid,mid))
#             # python的tuple比较规则: 先比较第一个元素, 如果第一个元素相等，再比较第二个元素
#             answer = max(answer, self.get_palindrome_from(s,mid,mid+1))
#         return s[answer[1]: answer[1]+answer[0]]

#     def get_palindrome_from(self, s: str, left: int, right: int) -> Tuple[int, int]:
#         while left >= 0 and right < len(s) and s[left] == s[right]:
#             left -= 1
#             right +=1
#         return (right - left -1, left + 1)

# @lc code=end

