#
# @lc app=leetcode id=654 lang=python3
# @lcpr version=30307
#
# [654] Maximum Binary Tree
#
# https://leetcode.com/problems/maximum-binary-tree/description/
#
# algorithms
# Medium (86.26%)
# Likes:    5411
# Dislikes: 350
# Total Accepted:    356.8K
# Total Submissions: 413.6K
# Testcase Example:  '[3,2,1,6,0,5]\n[3,2,1]'
#
# You are given an integer array nums with no duplicates. A maximum binary tree
# can be built recursively from nums using the following algorithm:
# 
# 
# Create a root node whose value is the maximum value in nums.
# Recursively build the left subtree on the subarray prefix to the left of the
# maximum value.
# Recursively build the right subtree on the subarray suffix to the right of
# the maximum value.
# 
# 
# Return the maximum binary tree built from nums.
# 
# 
# Example 1:
# 
# Input: nums = [3,2,1,6,0,5]
# Output: [6,3,5,null,2,0,null,null,1]
# Explanation: The recursive calls are as follow:
# - The largest value in [3,2,1,6,0,5] is 6. Left prefix is [3,2,1] and right
# suffix is [0,5].
# ⁠   - The largest value in [3,2,1] is 3. Left prefix is [] and right suffix
# is [2,1].
# ⁠       - Empty array, so no child.
# ⁠       - The largest value in [2,1] is 2. Left prefix is [] and right suffix
# is [1].
# ⁠           - Empty array, so no child.
# ⁠           - Only one element, so child is a node with value 1.
# ⁠   - The largest value in [0,5] is 5. Left prefix is [0] and right suffix is
# [].
# ⁠       - Only one element, so child is a node with value 0.
# ⁠       - Empty array, so no child.
# 
# 
# Example 2:
# 
# Input: nums = [3,2,1]
# Output: [3,null,2,null,1]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000
# All integers in nums are unique.
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 构造树一般采用的是前序遍历，因为先构造中间节点，然后递归构造左子树和右子树。
# 方法一: 切片法, 时间和空间复杂度都是O(n^2)
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]: # 1. 确定递归函数的参数和返回值, 传入的为已知正整数的数组, 即递归对象是数组区间
        # 2. 递归的终止条件: 区间长度为1, 保证数组至少有一个元素, 如果传进来的数组大小为1, 说明构造的是根节点
        if len(nums) == 1:
            return TreeNode(nums[0]) # 数组里唯一的元素
        # node = TreeNode(0) # 是表示这里有一个节点，只是它的值暂时是 0
        # 3. 单层递归逻辑: 在每一层递归中，有两个O(k)的操作（$k$ 为当前数组长度）：找最大值：for 循环遍历整个数组，耗时 $O(k)$。创建切片：nums[:idx]。Python 的切片会申请新内存并复制元素，耗时 $O(k)$。最坏情况（数组 [1,2,3,4,5]）：第 1 层处理 $n$ 个数，耗时 $n$。第 2 层处理 $n-1$ 个数，耗时 $n-1$。... 累加结果为 $\frac{n(n+1)}{2}$，即 $O(n^2)$

        # 中: 找到数组中最大的值和对应的下标
        maxValue = 0  # 题目说传入的是已知的正整数数组
        maxValueIndex = 0
        for i in range(len(nums)): # 找最大值：依然是 for i in range(left, right)，耗时 O(k)。
            if nums[i] > maxValue:
                maxValue = nums[i]
                maxValueIndex = i
        # node.val = maxValue # 对应的上面创建的node = TreeNode(0)
        node = TreeNode(maxValue)
        # 构造左子树和右子树, 保证左右区间至少有一个元素. 里面的 if判断必须写, 防止切出空数组. 因为递归终止条件并没有判断not root, return None
        # 左: 最大值所在的下标左区间, 构造左子树
        if maxValueIndex > 0: # 表示最大值的左边还有数, 如果没有数了就没必要去递归构造左子树, 因为左边是空的
            new_leftlist = nums[:maxValueIndex] # 左闭右开区间, 切片, 同时也新创建了数组
            node.left = self.constructMaximumBinaryTree(new_leftlist)
        # 右: 最大值所在的下标右区间, 构造右子树
        if maxValueIndex < len(nums) - 1: # 表示最大值的右边还有数, 如果最大值就在数组最右边, 那么右区间是空的
            new_rightlist = nums[maxValueIndex+1:]
            node.right = self.constructMaximumBinaryTree(new_rightlist)
        return node
    
# 方法二(优化, 更优): 使用下标, 时间复杂度O(n^2), 空间复杂度O(n)
class Solution:
    def constructMaximumBinaryTree(self, nums:List[int]) -> TreeNode:
        return self.traversal(nums, 0, len(nums))
    def traversal(self, nums: List[int], left:int, right:int) -> TreeNode:
        if left >= right:
            return None
        # 1. 初始化：假设第一个元素（下标为 left）就是最大的
        maxValueIndex = left
        # 2. 既然已经假设 left 是最大的了，那么比较的时候就不需要再和自己比. 所以循环从 left + 1 开始，去和后面的元素比
        for i in range(left+1, right):
            if nums[i] > nums[maxValueIndex]:
                maxValueIndex = i
        root = TreeNode(nums[maxValueIndex])
        # “切割”动作：仅仅是传了两个整数 left 和 right。这是O(1)操作，没有搬运数据的过程
        # 时间复杂度虽然在量级上（大 O 表示法）可能还是 $O(n^2)$，但系数小了很多，因为它省去了昂贵的内存拷贝时间
        # 空间复杂度为O(n)：全程只用那一个原始数组 nums，没有产生任何 new_nums。递归栈：依然是O(n)。结果：总空间消耗仅为O(n)。
        root.left = self.traversal(nums, left, maxValueIndex)
        root.right = self.traversal(nums, maxValueIndex+1, right)
        return root
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [3,2,1,6,0,5]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,1]\n
# @lcpr case=end

#

