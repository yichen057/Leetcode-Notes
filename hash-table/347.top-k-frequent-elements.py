#
# @lc app=leetcode id=347 lang=python3
# @lcpr version=30403
#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (66.38%)
# Likes:    19552
# Dislikes: 857
# Total Accepted:    3.6M
# Total Submissions: 5.4M
# Testcase Example:  '[1,1,1,2,2,3]\n2\n[1]\n1\n[1,2,1,2,1,2,3,1,3,2]\n2'
#
# Given an integer array nums and an integer k, return the k most frequent
# elements. You may return the answer in any order.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,1,1,2,2,3], k = 2
# 
# Output: [1,2]
# 
# 
# Example 2:
# 
# 
# Input: nums = [1], k = 1
# 
# Output: [1]
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
# 
# Output: [1,2]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
# 
# 
# 
# Follow up: Your algorithm's time complexity must be better than O(n log n),
# where n is the array's size.
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
# from common.node import *

# @lc code=start
from collections import Counter
import heapq
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # method 1: frquencymap+sorted, 排序法：把所有频率都排好。
        # Time: O(n + m log m +k)，简化为O(n+mlogm), 最坏情况下每个数字都不同, m=n, O(n log n);
        # Space: O(m+k), 最坏O(n), 其中:
        # n = nums 的长度; m = freq_dict 存 m 个不同数字, 即不同数字的个数，也就是 len(Counter(nums)), 通常m <= n; k = result 存 k 个结果. 
        # freq_dict = {} # freq_dict 存 m 个不同数字
        # for num in nums:
        #     freq_dict[num] = freq_dict.get(num, 0) + 1

        # sorted_dict = sorted(freq_dict.items(), key = lambda x:x[1], reverse = True) # sort the map's value, sorted_dict 也存 m 个 pair
        # # 上述结果是tuple of list[(1, 3), (2, 2), (3, 1)]. Python 排 tuple 时，默认先比较第一个元素，也就是 key。如果 key 相同，再比较第二个元素。
        ## 如果sorted(freq_dict.items()), 是默认按key从小到大排序, 想更明确, 也可以写sorted_items = sorted(freq_dict.items(), key=lambda x: x[0]), key=lambda x: x[0]表示按key排序
        # result = [] # result 存 k 个结果
        # for i in range(k):
        #     result.append(sorted_dict[i][0])

        # return result

        # method 2: counter + bucket sort by frequency. The best method. 
        # 本题核心思路: 用 frequency 当 index。count[freq] 存所有出现 freq 次的元素, 然后从高频往低频取。
        # 桶排序：利用 frequency 最大不超过 n，直接按频率分桶。适合于key 的范围有限或者 frequency 的范围有限, 本题一个数字的出现次数k最多就是len(nums), so frquency的范围就是[0, n]
        # bucket sort适合题型: 频率 frequency, 次数 count, 范围有限，比如 0~100, 分数/年龄/颜色只有几个值, 需要 better than O(n log n)
        # LC 347 Top K Frequent Elements
        # LC 451 Sort Characters By Frequency
        # LC 75 Sort Colors
        # LC 1122 Relative Sort Array
        # # bucket sort: 我不直接比较排序，而是把元素放进对应的“桶”里，frequency 当 index 分桶, 然后按桶的顺序取出来。
        # 时间和空间复杂度: O(n)
        freq_dict = {}
        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1

        # count = [[]] * 20000 # 错误示范: 创建一个length = 20000的list of list, 这样会创建20000个指向第一个位置同一个list的引用
        count = []
        # for i in range(20001): # 为了考虑到constraint, 其实不用这么长, 只需要len(nums)的长度放frequency的list of list
        for _ in range(len(nums)+1): # 因为frequency最大可能是len(nums)
            count.append([]) # 创建一个length = len(nums)的list of list, index是frquency, value是这个frquency对应的value数组
        #count = [[] for _ in range(len(nums)+1)] 上述两行可以整合成这一句, 这样每个 count 都是独立的 list, 其中count[i]存所有出现i次的数字

        for key, v in freq_dict.items(): # key:num, v: frquency
            count[v].append(key) # 如何给count这个list的index和value赋值, 尤其是value, 由于value是个list, 加value用append
            # v is the frequency(也就是count的index), count[v]: array of numbers relevent to v frequency 
        result = [] # length of result = k
        for i in range(len(count)-1, -1, -1): # 从高频往低频扫, 取够k个. 记忆这个倒序遍历的写法!
            for num in count[i]: # count[i] 若为空, 自动跳过
                result.append(num)

                if len(result) == k:
                    return result
        return []

        # method 3: heap method to retrieve top k frequent elements list
        # 维护一个大小为 k 的 min heap，heap 里存目前频率最高的 k 个元素. 堆法：只维护 top k。。
# LC347 heap 解法：
# freq_dict 统计频率；
# min heap 存 (freq, num)；
# heap 超过 k 就 pop；
# 最后 heap 里剩下的 num 就是 top k frequent。
        # 时间复杂度:Counter(nums): O(n); 遍历 m 个不同数字，每次 heap push/pop 是O(log k), 所以 heap 部分：O(m log k)
        # 所以总的时间复杂度O(n + mlog k), 最坏情况下 m = n的时间复杂度是: O(n log k), 如果 k 比 n 小很多，或者说k很小n很大, heap 比 sorting 更好, 即O(n log k) 会比 O(n log n) 好。
        # 空间复杂度: Coounter(nums): O(m), heap 最多保留k个元素, O(k), return list O(k), 总空间O(m+k), 最坏O(n)
        # edge case: 不建议写, 因为题目已说明: 1 <= k <= number of unique elements
        # 如果 k == len(nums)，说明每个元素都 unique 才可能合法；但返回 nums 虽然可能过，但没有必要，也容易让逻辑变复杂。
        # if k == len(nums):
        #     return nums

        # build a hash map: integer:frequency, O(n) time
        # count = Counter(nums) # 代替frequency_map, 统计各个num的频率

        # heap = []

        # for num, freq in count.items():
        #     heapq.heappush(heap, (freq, num)) # heap 里不要只存 num需要按 frequency 比较，所以 heap 里应该存(freq, num),  heapq 默认按照 tuple 的第一个元素排序。这样 heap[0] 永远是当前 heap 里 frequency 最小的那个。
        #     # 只想保留频率最高的 k 个元素。如果 heap 里超过 k 个，就把频率最小的那个踢出去。
        #     if len(heap) > k: # 如果heap size 超过 k个，就 pop 最小频率的元素
        #         heapq.heappop(heap)
        # # 此时heap = [(2, 2), (3, 1)]
        # return [num for freq, num in heap] # 最后 heap 里剩下的就是 top k frequent, 只需取出num. eg:取出 [2, 1]
        # 最后返回的这行是list comprehension，列表推导式。意思遍历 heap 里的每一个 (freq, num)，只取 num，组成一个新的 list。
        # [...]手动构造list eg: return [i, j]
        # [expr for x in iterable] 边遍历边加工生成list eg: [num for freq, num in heap]
        # list(iterable) 把现成iterable可迭代对象转成list eg: list(groups.values())
        # [object] 把整个对象包成一个元素 eg: [groups.values()], 把整个 dict_values 当成一个元素放进 list, 通常这不是想要的结果
       
              
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    print(solution.topKFrequent([3,0,1,0], 1))



#
# @lcpr case=start
# [1,1,1,2,2,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2,1,2,1,2,3,1,3,2]\n2\n
# @lcpr case=end

#

