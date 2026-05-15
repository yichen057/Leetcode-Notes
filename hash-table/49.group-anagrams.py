#
# @lc app=leetcode id=49 lang=python3
# @lcpr version=30403
#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (72.57%)
# Likes:    22124
# Dislikes: 758
# Total Accepted:    4.7M
# Total Submissions: 6.5M
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]\n[""]\n["a"]'
#
# Given an array of strings strs, group the anagrams together. You can return
# the answer in any order.
# 
# 
# Example 1:
# 
# 
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# 
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# 
# Explanation:
# 
# 
# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form
# each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to
# form each other.
# 
# 
# 
# Example 2:
# 
# 
# Input: strs = [""]
# 
# Output: [[""]]
# 
# 
# Example 3:
# 
# 
# Input: strs = ["a"]
# 
# Output: [["a"]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


# @lc code=start
from collections import defaultdict # defaultdict 是 Python 标准库 collections 里的一个字典类型。它的作用是：当 key 不存在时，自动创建默认值。
from typing import List # List 是用来写类型提示的, 也可以不写的。不影响核心运行逻辑. List 本身不负责分组、不负责计数、不负责存数据；它只是告诉读代码的人或者类型检查工具：这个变量/返回值应该是什么类型。
class Solution:
    # method 1: sorted list + defaultdict, 适用于strs[i] consists of 不止lowercase English letters, 更general.
    # Complexity Analysis
# Time Complexity: O(NKlogK), where N is the length of strs, and K is the maximum length of a string in strs. The outer loop has complexity O(N) as we iterate through each string. Then, we sort each string in O(KlogK) time.
# Space Complexity: O(NK), the total information content stored in groups
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]: # 函数返回一个二维字符串列表list of list
# #比如: [
# #     ["eat", "tea", "ate"],
# #     ["tan", "nat"],
# #     ["bat"]
# # ]
#         groups = defaultdict(list) # 可以帮你省掉初始化空 list 的步骤。
#     # defaultdict相当于dict这么写:
#     # groups = {}
#     # if "aet" not in groups:
#     #     groups["aet"] = []
#     # groups["aet"].append("eat")
#         for s in strs:
#             key = "".join(sorted(s)) # eg: s = "eat", sorted(s)->sorted_s=['a', 'e', 't'], key="aet"
#             groups[key].append(s)
#         return list(groups.values()) # 注意: 这里不可以写[groups.values], groups.values() 是一个 view。
        # list(groups.values()) 是把 view 展开成真正的 list。
        # [groups.values()] 是把整个 view 包成一个 list 元素。
        # [group.values()]结果大概为:是一个 list，里面只有一个元素，这个元素是 dict_values 对象。
# [
    # dict_values([
    #     ["eat", "tea", "ate"],
    #     ["tan", "nat"],
    #     ["bat"]
    # ])
    # ]

    # method 2: counting sort + defaultdict, 适用于本题的strs[i] consists of lowercase English letters.
    # Complexity Analysis
# Time Complexity: O(NK), where N is the length of strs, and K is the maximum length of a string in strs. Counting each string is linear in the size of the string, and we count every string.
# Space Complexity: O(NK), the total information content stored in ans.
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
        groups = defaultdict(list) # key 不存在时,默认 value 是 [] → 适合分组
        # 创建 defaultdict 是 O(1)；填充 defaultdict 才是 O(n) 或 O(nk)。 
        # groups这个dictionary的key是26个字母为index, freq为value的tuple(list), value是共有同一个key的list(str)
        for s in strs:
            # Record letter frequencies for lowercase letters.
            count = [0] * 26 
            for c in s:
                count[ord(c) - ord("a")] += 1
            key = tuple(count) # 因为 dictionary 的 key 必须是可哈希 hashable 不能变的对象，而 list 不是 hashable它是可变的，tuple 是 hashable。这里的tuple(count) 是字符串的“字母频率签名”, 长度是26 total entries, 每个元素代表26个字母的出现次数
            groups[key].append(s)
        return list(groups.values()) 
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# ["eat","tea","tan","ate","nat","bat"]\n
# @lcpr case=end

# @lcpr case=start
# [""]\n
# @lcpr case=end

# @lcpr case=start
# ["a"]\n
# @lcpr case=end

#

