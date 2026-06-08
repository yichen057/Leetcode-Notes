#
# @lc app=leetcode id=703 lang=python3
# @lcpr version=30403
#
# [703] Kth Largest Element in a Stream
#
# https://leetcode.com/problems/kth-largest-element-in-a-stream/description/
#
# algorithms
# Easy (61.07%)
# Likes:    6480
# Dislikes: 4081
# Total Accepted:    1M
# Total Submissions: 1.6M
# Testcase Example:  '["KthLargest","add","add","add","add","add"]\n' +
  '[[3,[4,5,8,2]],[3],[5],[10],[9],[4]]\n' +
  '["KthLargest","add","add","add","add"]\n' +
  '[[4,[7,7,7,7,8,3]],[2],[10],[9],[9]]'
#
# You are part of a university admissions office and need to keep track of the
# kth highest test score from applicants in real-time. This helps to determine
# cut-off marks for interviews and admissions dynamically as new applicants
# submit their scores.
# 
# You are tasked to implement a class which, for a given integer k, maintains a
# stream of test scores and continuously returns the kth highest test score
# after a new score has been submitted. More specifically, we are looking for
# the kth highest score in the sorted list of all scores.
# 
# Implement the KthLargest class:
# 
# 
# KthLargest(int k, int[] nums) Initializes the object with the integer k and
# the stream of test scores nums.
# int add(int val) Adds a new test score val to the stream and returns the
# element representing the k^th largest element in the pool of test scores so
# far.
# 
# 
# 
# Example 1:
# 
# 
# Input:
# ["KthLargest", "add", "add", "add", "add", "add"]
# [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
# 
# Output: [null, 4, 5, 5, 8, 8]
# 
# Explanation:
# 
# KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
# kthLargest.add(3); // return 4
# kthLargest.add(5); // return 5
# kthLargest.add(10); // return 5
# kthLargest.add(9); // return 8
# kthLargest.add(4); // return 8
# 
# 
# Example 2:
# 
# 
# Input:
# ["KthLargest", "add", "add", "add", "add"]
# [[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]]
# 
# Output: [null, 7, 7, 7, 8]
# 
# Explanation:
# KthLargest kthLargest = new KthLargest(4, [7, 7, 7, 7, 8, 3]);
# kthLargest.add(2); // return 7
# kthLargest.add(10); // return 7
# kthLargest.add(9); // return 7
# kthLargest.add(9); // return 8
# 
# 
# Constraints:
# 
# 
# 0 <= nums.length <= 10^4
# 1 <= k <= nums.length + 1
# -10^4 <= nums[i] <= 10^4
# -10^4 <= val <= 10^4
# At most 10^4 calls will be made to add.
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# 核心思想: 始终维护一个 size = k 的 min heap, heap[0] 就是第 k 大. 
# Top K的核心思想是heap永远保存最大的k个数: top k largest, 而不是所有数. 
# 本题运用size k min heap , 时间复杂度可以从init方法入手进行优化: 从O(n log n)优化到O(n log k)
# 本题中的求最大并不是找max heap, 我们真正需要的是Top k largest 中最小的那个, 即第k大, 所以heap[0]就能拿到最小值, Size K Min Heap是最优解
# init: TC: O(n log n)
# add(): TC: O(log k)
# SC: O(k)
# 目前的写法heapify + 不停pop
import heapq
class KthLargest:
    # 初始化的总时间复杂度: O(n + (n-k)log n), 简化为O(n log n)
    # minHeap with K largest integers: 应该在 __init__ 里只建一次minHeap of size k.
    # def __init__(self, k: int, nums: List[int]): 
    #     self.minHeap = nums
    #     self.k = k
    #     heapq.heapify(self.minHeap) # 注意: 此时括号里的数组不能用nums表示, 而是self.minHeap表示
    #     # heapify, nums->minHeap: TC: O(n)

    #     # 一开始minHeap长度为n, 需要pop (n-k)次, 每次pop的TC: O(log n), 所以Total TC: O((n-k)log n)
    #     while len(self.minHeap) > k: 
    #         heapq.heappop(self.minHeap)

    # init优化版: 时间复杂度: O(n log k), 因为整个过程中 heap 从来不超过 k。
    def __init__(self, k: int, nums: List[int]): 
        self.k = k
        self.minHeap = []
        # minHeap长度为k, 需要push n次, 每次pop的TC: O(log k), 所以Total TC: O(n log k)
        for num in nums:
            heapq.heappush(self.minHeap, num)
            if len(self.minHeap) > self.k:
                heapq.heappop(self.minHeap)

    # push/pop的时间复杂度O(log k), 因为要维持heap size = k, 所以不是O(log n)
    # SC: 由于heap里始终保留k 个元素, 所以SC: O(k)
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val) # TC: O(log k)因为heap最多只有k+1个元素, 多一个也会pop, 所以会维持heap size = k

        # edge case: heap may be initialized with less than k elements, so we only pop when length of heap > k
        if len(self.minHeap) > self.k: # 注意: 调用member variable要写self. , 这里的k写成self.k
            heapq.heappop(self.minHeap)

        return self.minHeap[0] # 剩下的heap里的就是前k大元素, 顶部[0]就是k大元素里的最小值, 也就是第k大.
        # heap[0] 是当前前 k 大里面最小的，所以它正好是 第 k 大。

# 以下是错误示范, 不是正确答案! 会超市Time Limit Exceeded
# class KthLargest:
#     def __init__(self, k: int, nums: List[int]): 
#         self.k = k
#         self.nums = nums
#     def add(self, val: int) -> int:
#         self.nums.append(val)
#         heap = [] # 每次 add() 都重新从头建一个 heap, 这太慢了. 每次 add 的时间复杂度接近：O(nlogk), 正确做法是每次add只需要O(log k)
#         for num in self.nums:
#             heapq.heappush(heap, num)
#             if len(heap) > self.k:
#                 heapq.heappop(heap) # TC: (n-k) log n
#         return heap[0]
#     def add(self, val: int) -> int:
#         heapq.heapify(self.nums) # 每次 add 都重新建堆，太浪费。应该在 __init__ 里只建一次。
#         heapq.heappush(self.nums, val)
#         if len(self.nums) > self.k:
#             heapq.heappop(self.nums)
#         return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# ["KthLargest","add","add","add","add","add"]\n[[3,[4,5,8,2]],[3],[5],[10],[9],[4]]\n["KthLargest","add","add","add","add"]\n[[4,[7,7,7,7,8,3]],[2],[10],[9],[9]]\n
# @lcpr case=end

#

