#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
# https://www.jiuzhang.com/solution/longest-palindromic-substring/
#
# algorithms
# Medium (31.05%)
# Likes:    12413
# Dislikes: 760
# Total Accepted:    1.4M
# Total Submissions: 4.5M
# Testcase Example:  '"babad"'
#
# Given a string s, return the longest palindromic substring in s.
# 
# 
# Example 1:
# 
# 
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: s = "cbbd"
# Output: "bb"
# 
# 
# Example 3:
# 
# 
# Input: s = "a"
# Output: "a"
# 
# 
# Example 4:
# 
# 
# Input: s = "ac"
# Output: "a"
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
from typing import Tuple

#外层枚举长度 O(n)，内层枚举起点 O(n)，每次检查回文最坏再做 O(n) → O(n³)。
#常见优化：改成“中心扩展”检查所有中心（2n-1 个），每次扩展 O(n) → O(n²)。
class Solution:
    def longestPalindrome(self, s):
        # 在类里定义实例方法 longestPalindrome。
# 第一个参数 self 指向实例本身（调用时写 obj.longestPalindrome(...)，Python 会自动把 obj 传给 self）。s 是传入的字符串参数。
#这里没写返回类型/参数类型，Python 允许省略（可用类型注解，但不是必须）。
        for length in range(len(s),0,-1):
        #for循环里的 range(start, stop, step) 生成等差数列：从 len(s) 到大于 0 前（不含 0），步长 -1（递减）, 也就是 length = n, n-1, …, 1，从最长子串开始尝试。
        # range(a, b, step) 不含 b；range(k) = 0..k-1。
            for i in range(len(s)-length+1):
            # 第二层 for。range(k) 等价于 range(0, k, 1)：从 0 到 k-1。len(s) - length + 1 是起点索引的上界，让切片 s[i : i+length] 不越界
                l,r=i,i+length-1
                # 多重赋值 / 解包：同时给 l 和 r 赋值。l 是左指针，r 是右指针，指向当前子串的两端（闭区间）。
                while l<r and s[l]==s[r]:
                # while 循环，两个条件都为真才继续（短路与 and）。边界相向移动的经典“回文检查”, 指针向中间靠拢。
                    l+=1
                    r-=1
                if l>=r:
                    return s[i:i+length]
                # 判断是否回文：当 l >= r 时，说明已经“穿越”或“相遇”，两端都匹配成功了。
                # s[a:b] 是切片，返回从索引 a 到 b-1 的子串；b 是开区间（不包含）。这里返回第一个满足条件的子串（因为外层从大到小找长度，先找到的就是最长）。
        return ""   # 如果所有长度都没找到回文（理论上长度 1 总是回文，所以几乎不会到这行），返回空字符串。    

if __name__ == "__main__": # 主程序main入口
    s = Solution() # 实例化类 Solution，得到对象 s。调用方法并打印返回值。
    print(s.longestPalindrome("babad"))   # 预期输出: "bab" 或 "aba"
    print(s.longestPalindrome("cbbd"))    # 预期输出: "bb"

# 输入s = "babad", 长度 len(s) = 5
# 外层循环：for length in range(5, 0, -1)
# 依次取值：length = 5 → 4 → 3 → 2 → 1
# ① length = 5
# 内层 for i in range(5 - 5 + 1) = range(1) → i = 0
# l = 0, r = 4 → 对应子串 "babad"
# while 循环：
# s[0]='b' vs s[4]='d' → 不等 → 循环直接跳出
# l=0, r=4 → l<r → 不是回文
# 👉 长度 5 不成立
# ② length = 4
# 内层 for i in range(5 - 4 + 1) = range(2) → i = 0, 1
# i=0: 子串 "baba"
# l=0, r=3 → s[0]='b', s[3]='a' → 不等
# 不是回文
# i=1: 子串 "abad"
# l=1, r=4 → s[1]='a', s[4]='d' → 不等
# 不是回文
# 👉 长度 4 不成立
# ③ length = 3
# 内层 for i in range(5 - 3 + 1) = range(3) → i = 0,1,2
# i=0: 子串 "bab"
# l=0, r=2 → s[0]='b', s[2]='b' ✅ → l=1, r=1
# 退出 while (l>=r) → 成立 → return "bab"
# 程序返回
# 在 length=3, i=0 时，找到 "bab"，直接返回。
# 所以最终输出是 "bab"（或者如果字符串不同，也可能返回 "aba"，取决于遇到的第一个符合的长度 3 回文）。

#时间复杂度是O(n^3)下比较好的coding quality方法:
    def LongestPalindrome(self,s):
        if s is None:
            return None
        
        for length in range(len(s),0,-1):
            for i in range(len(s)-length+1):
                if self.is_palindrome(s,i,i+length-1):
                    #类方法中药调用类里的其他方法, 必须写self.is_palindrome
                    return s[i:i+length]
                    #这里的s是方法参数, 是一个局部变量, 可以直接用, 不需要加self, 只有当s存成实例变量比如self.s=s时, 才需要写self.s, 此处不需要保存到对象属性, 直接用传参的s就行
        
        return ""
    
    def is_palindrome(self,s,left,right):
        while left < right and s[left] == s[right]:
            left += 1
            right -=1

        return left >= right

# 优化解法:背向双指针法,核心思想就是 以每个位置为中心，不断向两边扩展，找最大回文。时间复杂度 O(n²)，空间复杂度 O(1)
class Solution:
    def LongestPalindrome(self,s):
        if not s: # 检查输入是否为空字符串。如果为空，直接返回 ""。
            return ""
        start, longest =0,0  # start: 记录最长回文子串的起始位置。longest：记录当前找到的最长回文子串的长度。
        for middle in range(len(s)):#遍历每一个字符 middle，把它当作回文子串的“中心”。回文子串可以分为 奇数长度（中点是单个字符）和 偶数长度（中点是两个字符之间的缝隙）。所以后面有两个部分：odd 和 even。
            #odd
            left,right=middle,middle
            while left >= 0 and right < len(s) and s[left]==s[right]:
                left -= 1
                right += 1
            #从中心 middle 向两边扩展。条件是：left 不越界，right 不越界，并且两边字符相等。每次循环：左指针 left 往左走，右指针 right 往右走，直到不能扩展为止。
            #注意：循环结束时，s[left+1:right] 才是回文串，因为最后一次 left-- 和 right++ 已经越界或不满足条件了。此时的回文长度为right-(left+1)=right-left-1
            if longest<right-left-1: # longest是历史记录的最大长度, right-left-1是当前中心扩展得到的回文长度.这一步是判断当前找到的回文长度，是否比之前找到的最长的还要长。
                longest=right-left-1 # 如果新的回文更长 → 更新最大长度
                start=left+1 #因为最后一次 left -= 1 让 left 多退了一步，所以回文其实是从 left+1 开始。更新回文起始位置
            #👉 举例：字符串 "aba"
            # 初始：left=1, right=1 （middle=1）
            # while 第一次：s[1]==s[1] ✅ → left=0, right=2
            # while 第二次：s[0]==s[2] ('a'=='a') ✅ → left=-1, right=3
            # while 第三次：条件不成立，循环停。
            # 最后的回文其实是 s[left+1:right] = s[0:3] = "aba"。
            # 它的长度是：right - (left+1) = right - left - 1 = 3。
        
            #even
            left,right=middle,middle+1
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            if longest<right-left-1:
                longest = right-left-1
                start = left+1
        
        return s[start:start+longest]
    
    #上述代码的问题是, 代码有重复, 全局变量也要少写

#知识点:
#在 Python 里，tuple（元组）是一种不可变序列类型。所谓 二元组，就是长度为 2 的元组
#特点：
#1. 用小括号 () 表示。
#2. 元素可以是任意类型（数字、字符串、列表、对象……）。
#3. 不可变：创建后不能修改元素。
#4. Python 里 逗号才是元组的本质，小括号只是为了语法清晰或控制优先级。所以只要用逗号分隔，就自动是 tuple。eg: x = (1)只是 int; y = (1,) 才是 tuple

#基于中心点枚举法Enumeration: Expand around center, 该方法整合了上述算法的重复部分,用到了tuple二元组
#这段代码用 二元组 (长度, 起点) 保存结果。遍历每个可能的中心，调用 get_palindrome_from 扩展。最后用切片返回回文子串。
class Solution:
    def LongestPalindrome(self,s):
        if not s: # 如果 s 是空字符串
            return s # 直接返回它自己
        
        answer = (0,0) #用一个 二元组 (length, start_index) 来保存当前最长回文子串的信息。answer[0] 表示回文的 长度; answer[1] 表示回文的 起始位置。
        for mid in range(len(s)): # 遍历字符串的每个位置 mid，尝试把它作为回文的中心。
            #self → Python 类方法的固定写法(在 class 里面定义的方法，第一个参数必须是实例对象本身，习惯命名为 self)，代表实例本身, 可以访问类里的方法和属性。
            # s → 是要处理的字符串，属于参数, 不是类属性，所以需要额外传。
            answer = max(answer, self.get_palindrome_from(s,mid,mid)) # 奇数长度回文, 中心是一个字符
            answer = max(answer, self.get_palindrome_from(s,mid,mid+1)) # 偶数长度回文, 中心是两个字符
            # answer 是当前找到的最长回文（二元组存长度和起点）。每次都比较：旧的 answer, 新找到的奇数回文和新找到的偶数回文. 谁长就更新 answer。
            # Python 的元组比较规则是 先比第一个元素（长度），大的为大；如果相等，再比第二个元素。
            
        return s[answer[1]:answer[0]+answer[1]] # 根据 (长度, 起点) 从字符串里切片出回文子串。
        # 举例：answer = (3, 2) → 回文长度 3，从下标 2 开始 → s[2: 5]。

    def get_palindrome_from(self, s, left, right):#如果第一个参数不写self, Python 还是会自动传一个对象进去，这样 s 实际接收到的是实例对象，不是字符串！调用的时候会报错，因为你以为的 s 是字符串，其实变成了 Solution 实例。
        while left>=0 and right<len(s) and s[left] == s[right]:
            left -=1
            right +=1
        return right-left-1,left+1 # 返回 (长度, 起点), right - left - 1 → 回文的长度; left + 1 → 回文的起始位置。
        # # 等价于 return (right - left - 1, left + 1)

    #从 left 和 right 向两边扩展，直到不满足回文条件。循环结束时：s[left+1 : right] 就是一个最长的回文子串。

#区间型动态规划法求解, 时间复杂度O(n^2), 空间复杂度O(n^2)
#这是 DP 的核心！我们怎么用小问题的答案，来推导出大问题的答案呢？
# 思考一下，一个字符串（比如 "ababa"）怎么样才算是回文串？
# 它两头的字符必须相同 (第一个 'a' 和最后一个 'a')。
# 去掉两头字符后，中间的部分也必须是回文串 ("bab")。
# 于是，我们的“组合规则”就诞生了：
# dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
# 翻译成人话就是：s[i...j] 是不是回文串，取决于 ① 两头字符 s[i] 和 s[j] 是否相等，并且 ② 它中间的部分 s[i+1...j-1] 是不是回文串。
class Solution:
    def LongestPalindrome(self,s):
        if not s: # 这句话可展开为 s is null or s == ""
             return ""
        # Step 1: Initialization初始化
        length = len(s)
        start,max_length=0,1 #start 和 max_length 用来记录我们找到的最长回文串的起始位置和长度。我们先假设最长的就是单个字符，所以长度为 1。
        is_palindrome = [[False]*length for _ in range(length)] # is_palindrome 就是我们前面说的 DP 表格，开始时默认所有子串都不是回文。
    # For example: 
    # a = [False] * 3 = [False, False, False]
    # matrix = [a] * 3 = [False * 3] * 3, #soft copy, 只new了一次数组, 这三行其实都是同一个列表的引用, 所以改matrix[0][0] = True, 三行的第一个元素都会变成True
    # >>>
    # [
    #     [False, False, False]
    #     [False, False, False]
    #     [False, False, False]
    # ]

    # matrix[0][0] = True
    # >>>
    # [
    #     [True, False, False] #这三个数组的地址都是相同的, eg 0x12345678
    #     [True, False, False]
    #     [True, False, False]
    # ]

    # matrix[0], matrix[1], matrix[2]都指的是同一个数组

    # matrix = [[Fasle] * 3 for i in range(3)]把False*3这个操作执行三次, 相当于new了三个数组, 每个数组的地址是不同的, 完成了二维矩阵的初始化
    # for i in range(3) -> 生成三行, 每一行都是独立的新列表; [False] * 3 -> 每行有3个False, 结果就是以下: 
    # [
    # [False, False, False],
    # [False, False, False],
    # [False, False, False]
    # ]

        # Step 2: Base cases
        # 1) 长度为1的子串
        for i in range(length):
            is_palindrome[i][i]=True # 任何单个字符（如 "a", "b"）本身就是一个回文串。所以 dp[0][0], dp[1][1], dp[2][2]... 都设置为 True。
        # 2) 长度为2的子串
        for i in range(length-1):
            if s[i] == s[i+1]:
                is_palindrome[i][i+1]=True # 检查所有相邻的两个字符。如果它们相等（比如 "aa"），那它就是一个长度为 2 的回文串。我们就在 DP 表格里记下来，并更新 max_length 为 2。
                start,max_length=i,2

        # Step 3: Main loop:主循环的目标是处理所有长度大于等于 3 的子串。
        # 根据已有的长度1和2, 推到长度大于等于3的所有子串.
        # i 是子串的起点，j 是子串的终点。那么子串 s[i...j] 的长度就是 j - i + 1。
        # i 从后往前，j 从 i 的位置往后
        for i in range(length-3,-1,-1):#range(start, stop, step) 生成等差数列：从 len(s) 到大于 0 前（不含 0），步长 -1（递减）, 也就是 length = n, n-1, …, 1，从最长子串开始尝试。
            # i decreases because dp[i][j] depends on dp[i+1][j-1].That means: smaller i (left index) depends on larger i (further right).Therefore, you must loop i from large → small (inverted).
            for j in range(i+2,length): 
            # j increases because once i is fixed, expanding j rightward doesn’t break the dependency chain. j goes from left→right.
                # range() 函数有三种用法：range(stop), range(start, stop)步长默认为1, range(start, stop, step)
                # 核心规则:
                if is_palindrome[i+1][j-1] and s[i]==s[j]:
                    is_palindrome[i][j]=True
                
                if j-i+1>max_length:
                    max_length=j-i+1
                    start=i
        return s[start:start+max_length]
#动态规划解决这个问题的过程就像填表：

# 创建一张空表 dp。
# 先把对角线（长度为1）和它旁边（长度为2）的答案填上。
# 然后根据 dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1] 这个规则，从表里已有的答案，斜着向外推导出新的答案。
# 在填表的过程中，顺手记录下你找到的最长的那个回文串。
# 填完表，答案也就出来了。
# Think of the DP table (2D matrix):
# i = row (start index, top→down is bigger i).
# j = col (end index, left→right is bigger j).
# We need to fill the table bottom-left → top-right diagonals.
# That’s why i goes down to up (so dependencies are available).
# And j goes left → right for each row.


#宋老师解法
# class Solution:
#     def longestPalindrome1(self, s: str) -> str:#这句话定义一个类方法，接收一个字符串参数 s，返回值也是字符串。
#         max_length = 0
#         result_index = (0, 0)
#         for mid in range(len(s)):
#             left, right = self.get_palindrome(s, mid, mid)
#             if right - left + 1 > max_length:
#                 max_length = right - left + 1
#                 result_index = (left, right)

#             left, right = self.get_palindrome(s, mid, mid + 1)
#             if right - left + 1 > max_length:
#                 max_length = right - left + 1
#                 result_index = (left, right)
        
#         return s[result_index[0]:result_index[1] + 1]
    
#     def get_palindrome(self, s: str, left: int, right: int) -> Tuple[int, int]: #类型标注用中括号：Tuple[int, int], 实际数据用小括号：(1, 2)
#         while left >= 0 and right < len(s) and s[left] == s[right]:
#             left -= 1
#             right += 1
#         return left + 1, right - 1

#     def longestPalindrome(self, s: str) -> str:
#         length = len(s)
#         start, max_length = 0, 1
#         is_palindrome = [[False] * length for _ in range(length)]
#         for i in range(length):
#             is_palindrome[i][i] = True
        
#         for i in range(length - 1):
#             is_palindrome[i][i + 1] = s[i] == s[i + 1]
#             if is_palindrome[i][i + 1]:
#                 start, max_length = i, 2

#         for i in range(length - 3, -1, -1):
#             for j in range(i + 2, length):
#                 is_palindrome[i][j] = is_palindrome[i + 1][j - 1] and s[i] == s[j]
#                 if is_palindrome[i][j] and j - i + 1 > max_length:
#                     max_length = j - i + 1
#                     start = i

#         return s[start:start + max_length]
    
# # @lc code=end