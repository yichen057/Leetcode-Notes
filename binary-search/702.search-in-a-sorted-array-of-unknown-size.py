#
# @lc app=leetcode id=702 lang=python3
# @lcpr version=30403
#
# [702] Search in a Sorted Array of Unknown Size
#
# https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/description/
#
# algorithms
# Medium (73.12%)
# Likes:    941
# Dislikes: 51
# Total Accepted:    113.5K
# Total Submissions: 155.2K
# Testcase Example:  '[-1,0,3,5,9,12]\n9\n[-1,0,3,5,9,12]\n2'
#
# This is an interactive problem.
# 
# You have a sorted array of unique elements and an unknown size. You do not
# have an access to the array but you can use the ArrayReader interface to
# access it. You can call ArrayReader.get(i) that:
# 
# 
# returns the value at the i^th index (0-indexed) of the secret array (i.e.,
# secret[i]), or
# returns 2^31 - 1 if the i is out of the boundary of the array.
# 
# 
# You are also given an integer target.
# 
# Return the index k of the hidden array where secret[k] == target or return -1
# otherwise.
# 
# You must write an algorithm with O(log n) runtime complexity.
# 
# 
# Example 1:
# 
# Input: secret = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in secret and its index is 4.
# 
# 
# Example 2:
# 
# Input: secret = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in secret so return -1.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= secret.length <= 10^4
# -10^4 <= secret[i], target <= 10^4
# secret is sorted in a strictly increasing order.
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

# TC: O(log k), where k is an index of target value. There are two operations here: to define search boundaries and to perform binary search.
# SC: O(1): since it's an constant space solution
# log k的计算过程:
'''
K = index of target, x = 倍增次数
2^(x-1) - 1 < k <= 2^x - 1
两边同时＋1
2^(x-1) < k+1 <= 2^x
左边的不等式两边同时*2
2^x < 2*(k+1)
两边分别取以2为底的log
x < log2 (2 * (k + 1) 
x < log2 2 + log2 (k+1)
x < 1 + log2 (k+1)
所以 x 约等于log2(k+1), 也就x = O(log k)
'''
class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        # initialize the searching range, 代表元素个数, 也表示当前先检查前 1 个元素. rangeTotal - 1表示右边界
        rangeTotal = 1
        # 倍增法Exponential backoff: 如果target在查找范围之外, 则查找范围翻倍. 倍增的时间复杂度为O(x)约等于O(log k)
        while reader.get(rangeTotal - 1) < target:
            rangeTotal = rangeTotal * 2
        # print("rangeTotal: ", rangeTotal)

        # binary search method (模板写法)
        # 此处start也可以设为rangeTotal // 2, 因为根据倍增的推论, start可以直接在最后算出来的rangeTotal的一半位置作为起点, target一定在[rangeTotal//2, rangeTotal - 1]这个范围内, 这样的话二分的时间范围会稍微小一点, 不过对于时间复杂度无影响
        # 此处可以先按模板写成0, 写为0也不会影响时间复杂度
        # 如果target前rangeTotal中, 则index范围是[0, rangeTotal - 1], binary search的时间复杂度:O(log 2^x) = O(x) 约等于(log k), 空间复杂度O(1)
        start, end = 0, rangeTotal - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if reader.get(mid) < target:# 说明target在右边, 丢弃左边
                start = mid
                # print("start: ", start)
            # 如果target <= 中点值, 丢弃右边, 去左边
            else:
                end = mid # 为什么这里reader.get(mid) == target时不直接返回呢? 因为在中点左边还可能存在更靠左的target值
                # print("end: ", end)
        
        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end
        return -1
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [-1,0,3,5,9,12]\n9\n
# @lcpr case=end

# @lcpr case=start
# [-1,0,3,5,9,12]\n2\n
# @lcpr case=end

#

