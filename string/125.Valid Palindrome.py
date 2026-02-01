#
# @lc app=leetcode id=125 lang=python3
# @lcpr version=30202
#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (51.54%)
# Likes:    10732
# Dislikes: 8580
# Total Accepted:    4.6M
# Total Submissions: 8.8M
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# A phrase is a palindrome if, after converting all uppercase letters into
# lowercase letters and removing all non-alphanumeric characters, it reads the
# same forward and backward. Alphanumeric characters include letters and
# numbers.
# 
# Given a string s, return true if it is a palindrome, or false otherwise.
# 
# 
# Example 1:
# 
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# 
# 
# Example 2:
# 
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# 
# 
# Example 3:
# 
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric
# characters.
# Since an empty string reads the same forward and backward, it is a
# palindrome.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 2 * 10^5
# s consists only of printable ASCII characters.
# 
# 
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s is None:
            return False
        
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not self.isValid(s[left]):
                left += 1
            while left < right and not self.isValid(s[right]):
                right -= 1
            if left < right and s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
# 如果 a 和 b 是字母，toLowerCase 会把它们都转成小写再比较。(java)
# 例如 'A' 和 'a' → 'a' == 'a' → true。
# 如果 a 和 b 是数字字符，比如 '3' 和 '3'，那么 toLowerCase 不会改变它们，直接比较 '3' == '3'，结果也正确。
# 如果 a 和 b 是数字和字母混合，比如 '3' 和 'a'，自然返回 false。
# ✅ 所以：数字可以直接比较，不会出错。

    def isValid(self, char: str) -> bool: #Python 里函数参数类型标注必须是 类型对象（例如 int、str），不能用变量名当类型。
        # char 在 Python 里就是一个 字符串（长度为 1 的 str），所以参数类型应该是 str
        # Python 没有单独的 char 类型，只有 str。如果是单个字符，比如 "a"，它其实是一个长度为 1 的字符串。
        # Python 把 字符 = 长度为 1 的字符串。
        return char.isdigit() or char.isalpha()
    
# 熟练python和java的这几个常用函数
# python: isdigit(),            isalpha(),             lower(),                  upper()
# Java:   Character.isDigit(c), Character.isLetter(c), Character.toLowerCase(c), Character.toUpperCase(c)
# 在 Java 里，isLetter、isDigit、toLowerCase 都是 Character 类的静态方法。
# 静态方法属于类，而不是对象；所以调用时必须用 类名.方法名(...) 来表明它是哪个类的方法。
    

# @lc code=end



#
# @lcpr case=start
# "A man, a plan, a canal: Panama"\n
# @lcpr case=end

# @lcpr case=start
# "race a car"\n
# @lcpr case=end

# @lcpr case=start
# " "\n
# @lcpr case=end

#

