#
# @lc app=leetcode id=252 lang=python3
# @lcpr version=30403
#
# [252] Meeting Rooms
#
# https://leetcode.com/problems/meeting-rooms/description/
#
# algorithms
# Easy (59.43%)
# Likes:    2128
# Dislikes: 117
# Total Accepted:    520K
# Total Submissions: 875K
# Testcase Example:  '[[0,30],[5,10],[15,20]]\n[[7,10],[2,4]]'
#
# Given an array of meeting time intervals where intervals[i] = [starti, endi],
# determine if a person could attend all meetings.
# 
# 
# Example 1:
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: false
# Example 2:
# Input: intervals = [[7,10],[2,4]]
# Output: true
# 
# 
# Constraints:
# 
# 
# 0 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti < endi <= 10^6
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

'''
UMPIRE template

  # Understand
inputs: list of list: intervals
outputs: boolean: whether each inner list has no intersection
constraints:
edge cases: 
1) touching intervals: if end_i = start_i+1, it is allowed;
2) empty list: return False

  # Match (any problems this reminds you of, any helpful patters to solve this e.g. two pointer technique, any data structures this reminds you of )
set 
  # Plan (pseudocode)
1) sort the intervals based on the start times
By sorting, you transform a complex 2D search into a linear one. You no longer need a set because any possible "intersection" is now guaranteed to be between adjacent elements in your sorted list. If intervals[i] doesn't overlap with intervals[i+1], it definitely won't overlap with intervals[i+2].
2) iterate through the sorted list from the first to the second-to-last element
3) compare the current meeting's end time with the next meeting's start time
4) return False if overlap, otherwise return True after the loop
  # Implement (python code)

  # Review (dry run of your code)

  # Evaluate (time and space complexity)
  TC: O(n log n) + O(n) = O(n log n)
  SC: O(n): Under the hood, Python’s sorting algorithm (Timsort) requires $O(n)$ auxiliary space in the worst case to perform its merges. 从底层来看，Python 的排序算法（泰姆排序）在最坏情况下需要 O(n) 的辅助空间来进行合并操作。
  In Python, the sort method sorts a list using the Tim Sort algorithm which is a combination of Merge Sort and Insertion Sort and has O(n) additional space. Additionally, Tim Sort is designed to be a stable algorithm.

'''
# @lc code=start
# method 1:
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Sorts specifically by the element at index 0
        intervals.sort(key=lambda x : x[0]) # modifying the input list directly rather than creating a new one. 
        # 这里也可以intervals.sort(), 默认 sort by the 1st element
        for i in range(len(intervals) - 1): # 注意这里的减一, 因为后面要用到[i+1]
            if intervals[i][1] > intervals[i+1][0]: # compare the current meeting's end time with the next meeting's start time, 即start < lastEnd时发生重合. 
            # 注意, 此处不是<=, 因为接触允许共存, 不算重合. eg: [1, 2][2, 3]可以安排两个会议, 这是和LC56题的区别, 本题类似LC435
                return False
        return True
# method 2: 推荐该方法, 考虑了边界问题, 代码更模板化具备迁移性
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        # Sorts specifically by the element at index 0
        intervals.sort(key=lambda x : x[0])
        lastEnd = intervals[0][1]
        for start, end in intervals[1:]:
            print("start:", start, "end:", end)
            if start < lastEnd:
                return False
            else:
                lastEnd = end
        return True     
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [[0,30],[5,10],[15,20]]\n
# @lcpr case=end

# @lcpr case=start
# [[7,10],[2,4]]\n
# @lcpr case=end

#

