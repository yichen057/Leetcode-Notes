#
# @lc app=leetcode id=981 lang=python3
# @lcpr version=30403
#
# [981] Time Based Key-Value Store
#
# https://leetcode.com/problems/time-based-key-value-store/description/
#
# algorithms
# Medium (49.92%)
# Likes:    5299
# Dislikes: 733
# Total Accepted:    743.5K
# Total Submissions: 1.5M
# Testcase Example:  '["TimeMap","set","get","get","set","get","get"]\n' +
  '[[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]'
#
# Design a time-based key-value data structure that can store multiple values
# for the same key at different time stamps and retrieve the key's value at a
# certain timestamp.
# 
# Implement the TimeMap class:
# 
# 
# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with the
# value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was
# called previously, with timestamp_prev <= timestamp. If there are multiple
# such values, it returns the value associated with the largest timestamp_prev.
# If there are no values, it returns "".
# 
# 
# 
# Example 1:
# 
# Input
# ["TimeMap", "set", "get", "get", "set", "get", "get"]
# [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo",
# 4], ["foo", 5]]
# Output
# [null, null, "bar", "bar", null, "bar2", "bar2"]
# 
# Explanation
# TimeMap timeMap = new TimeMap();
# timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along
# with timestamp = 1.
# timeMap.get("foo", 1);         // return "bar"
# timeMap.get("foo", 3);         // return "bar", since there is no value
# corresponding to foo at timestamp 3 and timestamp 2, then the only value is
# at timestamp 1 is "bar".
# timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along
# with timestamp = 4.
# timeMap.get("foo", 4);         // return "bar2"
# timeMap.get("foo", 5);         // return "bar2"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= key.length, value.length <= 100
# key and value consist of lowercase English letters and digits.
# 1 <= timestamp <= 10^7
# All the timestamps timestamp of set are strictly increasing.
# At most 2 * 10^5 calls will be made to set and get.
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
from collections import defaultdict

class TimeMap:

    def __init__(self):
        # key -> list of (value, timestamp)
        self.map = defaultdict(list)
        # self.map = {}

    # set() method : array
    # 每次set只是append, Time Complexity: O(1), space complexity: O(n), 所有set()存入的记录都需要保存, 假设总共调用了n次set()
    def set(self, key: str, value: str, timestamp: int) -> None:
        # if not key in self.map:
        #     self.map[key] = []
        #  # The problem guarantees timestamps are added in increasing order.
        self.map[key].append((value, timestamp)) # # 保存为 (value, timestamp)
        # timestamp 是查找和排序的关键字段，放在前面更直观。不过写成现在这样也不影响无妨
        
    # get() method 1: reverse traversal get() (也需要掌握!)
    # TC: O(n) for worst case, O(1) best case. 其中n 表示当前 key 对应的所有 (value, timestamp) 记录数量，不是整个 TimeMap 中所有记录的数量。
    # SC: O(1)
    def get(self, key: str, timestamp: int) -> str:
        if not key in self.map:
            return ""
        val_lst = self.map[key]
        for i in range(len(val_lst)-1, -1, -1):
            if val_lst[i][1] <= timestamp:
                return val_lst[i][0]
        return ""
    
    # get() method 2: binary search(推荐!): 找 timestamp <= target 的最后一个位置, 即the last timestamp <= target timestamp. # 我们要找最右边的 timestamp <= 查询时间, 所以相等时也向右找，最后先检查 end。
    # TC: 对于某个 key，假设它对应的历史记录数量是 m, 那么二分查找的时间复杂度是O(log m)
    def get(self, key: str, timestamp: int) -> str:
        if not key in self.map:
            return ""

        val_lst = self.map[key]
        # All the timestamps of set are strictly increasing.说明这个数组是有序的
        # 二分查找不要求整个元素本身一定是单个数字；只要求你用于比较和判断方向的字段是有序的。虽然整个元素不是数字，但它们的第二项 timestamp 是有序的. 只要我们二分时始终比较 timestamp，并且 timestamp 是递增的，就可以使用二分法。
        # 进入二分法环节
        start, end = 0, len(val_lst) - 1

        while start + 1 < end:
            mid = (start + end) // 2
             # 二分比较的是 timestamp
            if val_lst[mid][1] <= timestamp: # 遇到等于 target 时，不应该把 end 移到 mid, 不是在寻找第一个等于 target 的位置, 而是寻找最后一个<=timestamp的位置. 这里说明当前位置 mid 符合要求, 还需继续向右找, 右边可能还有更接近 timestamp 的合法答案，所以应该：
                start = mid # # mid is valid, but there may be a later valid timestamp.
            else: # 说明当前位置太晚了，不符合要求。答案只能在左边：
                end = mid # # mid is too large, so search on the left side.

        # 当循环结束时, start 和 end 相邻, 因为我们要求的是最后一个符合条件的位置，所以应该先检查更靠右的 end
        # 找最后一个 timestamp <= target 的元素, 所以优先检查更靠右的end, 而不是先检查start
        # We want the last timestamp <= target, so check the right position first.
        if val_lst[end][1] <= timestamp:
            return val_lst[end][0]
        if val_lst[start][1] <= timestamp:
            return val_lst[start][0]

        return ""

# Method 1: array of hashmap + linear search
class TimeMap:
    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        nums = self.map[key]
        for i in range(len(nums)-1, -1, -1):
            if nums[i][1] <= timestamp:
                return nums[i][0]
        return ""

# Method 2: hashmap of hashmap + linear search
class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.map:
            self.map[key] = {}
        self.map[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.map:
            return ""
        inner_map = self.map[key]
        for cur_time in range(timestamp, -1, -1):
            if cur_time in inner_map:
                return inner_map[cur_time]
        return ""

# Method 3: array of hashmap + binary search, 最推荐! 二分是得在有序数组里才可以用
from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.map:
            return ""
        nums = self.map[key]
        start, end = 0, len(nums)-1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid][1] <= timestamp:
                start = mid
            else:
                end = mid
        if nums[end][1] <= timestamp:
            return nums[end][0]
        if nums[start][1] <= timestamp:
            return nums[start][0]
        return ""

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# ["TimeMap","set","get","get","set","get","get"]\n[[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]\n
# @lcpr case=end

#

