#
# @lc app=leetcode id=973 lang=python3
# @lcpr version=30403
#
# [973] K Closest Points to Origin
#
# https://leetcode.com/problems/k-closest-points-to-origin/description/
#
# algorithms
# Medium (69.03%)
# Likes:    9131
# Dislikes: 339
# Total Accepted:    1.7M
# Total Submissions: 2.5M
# Testcase Example:  '[[1,3],[-2,2]]\n1\n[[3,3],[5,-1],[-2,4]]\n2'
#
# Given an array of points where points[i] = [xi, yi] represents a point on the
# X-Y plane and an integer k, return the k closest points to the origin (0,
# 0).
# 
# The distance between two points on the X-Y plane is the Euclidean distance
# (i.e., √(x1 - x2)^2 + (y1 - y2)^2).
# 
# You may return the answer in any order. The answer is guaranteed to be unique
# (except for the order that it is in).
# 
# 
# Example 1:
# 
# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest k = 1 points from the origin, so the answer is just
# [[-2,2]].
# 
# 
# Example 2:
# 
# Input: points = [[3,3],[5,-1],[-2,4]], k = 2
# Output: [[3,3],[-2,4]]
# Explanation: The answer [[-2,4],[3,3]] would also be accepted.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= k <= points.length <= 10^4
# -10^4 <= xi, yi <= 10^4
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# There are two common solutions:
# 1. Min Heap, O(k log n) time and O(n) space.
# 2. Quick Select, average O(n) time and O(log n) recursion space.
# If k is much smaller than n, heap is often a good practical choice.
# If we want the best average time complexity, Quick Select is better.

# Method 1: min Heap method(heapify + pop k): 把所有 n 个元素放进 heap, 然后 pop k 次
# Time: O(n + k log n)
# Space: O(n)
# heap 里装了全部 n 个元素。
# 如果是维护大小为 k 的 heap ->那么时间复杂度是 O(n log k), 但是本题heap的大小是n, 所以反过来TC: O(k log n)
# heap操作的时间复杂度: heapify: O(n), heappush/heappop: O(log n), heap[0]: O(1)
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = [] 
        # min Heap的最小元素在顶部, 距离最小的点永远在堆顶minHeap[0], 其它元素顺序不保证。对于任意节点：父节点 <= 子节点
        for x, y in points:
            dist = (x ** 2) + (y ** 2) 
            minHeap.append([dist, x, y])
        
        heapq.heapify(minHeap) # reorder the list to make sure it is in the structure of a heap.自底向上建堆, 时间复杂度O(n), 不是O(log n)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap) # 堆大小接近n, 所以每次执行都是O(logn), 执行k次所以O(k log n )
            # 每次拿到当前距离最小的点. 删除最小元素, 把最后一个节点拿上来, 然后不断下沉heapify down, 得到下一个最小元素. 这里的树高度是log n, 所以每次执行O(log n)
            res.append([x, y])
            k -= 1

        return res
# Method 2: quick select
# 找前 k 个最小距离，所以目标下标是target = k - 1
# 本题的k始终表示全局前 k 个位置, 不是“当前区间里的第 k 个”。
# TC: 
# Average: O(n)
# Worst:   O(n²)
# SC: 
# Average: O(log n)
# Worst:   O(n)
# 因为有递归栈
# 比较LC215 vs. LC973
# LC215：
# 1) target = start + k - 1, 找第 k 大的“值”. k 是当前区间排名，所以递归到右边要调整 k。
# 2) 因为要返回一个具体数字, 所以if start == end:区间只剩一个元素, 答案已经确定, 直接return nums[start]
# 3) 并且最后要返回一个数, 因此当命中pivot区域时, return nums[right+1]

# LC973:
# 1) target = k - 1, 把前 k 小的“范围”放到数组前面. k 是全局边界，所以递归时不用调整 k。
# 2) 本题不需要返回某个元素, 而是return points[:k], 只调整数组, 所以当start == end 和start > end时都表示不用再partition, 直接return即可. 因此可以记住下面的模板: 
# 排序类：start >= end
# 找具体答案类：start == end
# 3) 并且最后要返回前 k 个元素:
# => 命中 pivot 区域时
# => 什么都不用返回
# => points[:k] 就已经是答案, return即可
# 4) return切片的基础知识, 容易错
#    [:k]: 取前 k 个, 即[0, k-1] 从开头开始, 取到 k-1 为止;
#    [k:]: 跳过前 k 个, 取剩下所有, 即[k:-1] 从 k 开始, 一直取到最后
# 以下为面试常见的几个:
# nums[:k]      # Top K
# nums[k:]      # Remaining
# nums[-k:]     # 最后 k 个
# nums[:-k]     # 去掉最后 k 个
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.quick_select(points, 0, len(points)-1, k)
        return points[:k] 
    
    # eg: point = [1, 3], Python 支持解包（unpacking）, a, b = [1, 3], 等价于a=1, b=3
    def distance(self, point:List[int])->int:
        x, y = point
        return x * x + y * y
    
    def quick_select(self, points:List[list[int]], start:int, end:int, k:int)->None:
        if start >= end:
            return
        
        left = start
        right = end
        pivot  = self.distance(points[(start+end)//2])

        while left <= right:
            while left <= right and self.distance(points[left]) < pivot:
                left += 1
            while left <= right and self.distance(points[right]) > pivot:
                right -= 1
            if left <= right:
                points[left], points[right] = points[right], points[left]
                left += 1
                right -= 1
        
        # 前k个点的目标范围是index 0 ~ k-1
        target = k - 1 # 找前 k 个最小距离，所以目标下标是k-1. 不用改 k，因为我们一直关心全局前 k 个点。
        if target <= right:
            self.quick_select(points, start, right, k)
        elif target >= left:
            self.quick_select(points, left, end, k)
        else:
            return 
    
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [[1,3],[-2,2]]\n1\n
# @lcpr case=end

# @lcpr case=start
# [[3,3],[5,-1],[-2,4]]\n2\n
# @lcpr case=end

#

