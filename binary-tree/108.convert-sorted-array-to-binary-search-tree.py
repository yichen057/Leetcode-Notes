#
# @lc app=leetcode id=108 lang=python3
# @lcpr version=30403
#
# [108] Convert Sorted Array to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
#
# algorithms
# Easy (75.53%)
# Likes:    11951
# Dislikes: 647
# Total Accepted:    1.7M
# Total Submissions: 2.3M
# Testcase Example:  '[-10,-3,0,5,9]\n[1,3]'
#
# Given an integer array nums where the elements are sorted in ascending order,
# convert it to a height-balanced binary search tree.
# 
# 
# Example 1:
# 
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:
# 
# 
# 
# Example 2:
# 
# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums is sorted in a strictly increasing order.
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

''' UMPIRE template

  # Understand
inputs: a sorted integer array: nums
outputs: convert nums to a height-balanced binary search tree.
constraints:
edge cases: 
1) method 2: if array is empty, return None
2) method 1: if the index of array: left > right, return None

  # Match (any problems this reminds you of, any helpful patters to solve this e.g. two pointer technique, any data structures this reminds you of )
DFS recursion
  # Plan (pseudocode)
 1. edge case
 2. define the root, its value should be mid = (left + right)//2 in order to get the height-balanced BST
 3. left/right subtree recursion
 4. return root
 5. main function calls the heper function
  # Implement (python code)

  # Review (dry run of your code)

  # Evaluate (time and space complexity)
  TC: O(n): You visit every element in the array exactly once to create a node for it.
  SC: O(log n)
  O(log n): for the recursion stack if we only consider "extra" space. Because the tree is guaranteed to be height-balanced, the recursion depth is strictl log N.
  O(n): if you include the space required to store the output tree itself. In interview settings, usually, the "extra space" is what they care about, which is O(log N)
'''
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 调用内部函数时不用self
# 本题中的数组是奇数长度or偶数长度的数组都可以, 不论取左中值还是右中值, 答案都对, 本题并未限制
# 这个过程就像是在不断收缩边界：
# •	当 left == right 时，说明当前区间只有一个数，这个数会被建成一个孤立的节点。
# •	只要一个节点被建成，它就一定会去尝试找“更小”和“更大”的数。
# •	如果 mid 已经到了边界，算出来的 mid - 1 就会小于 left，或者 mid + 1 会大于 right。
# •	这种**“越界”**现象就是递归停止的信号，告诉程序：“这下面已经没有数字可以挂载了，返回一个空指针吧。”
# 这种通过索引控制范围的方法，比直接切割数组（nums[:mid]）要高效得多，因为它全程只操作三个整数（left, right, mid），而不需要复制任何数组数据。
# index pointer method: 推荐!复杂度更优
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    
        def traversal(left, right): # 这里的left, right是BST的左右区间索引, 是左闭右闭区间, 此处区间定义一定要想清楚, 分隔边界才能把握好
            # nested function can access the outer function's parameter(which is nums) regardless. 
            # edge case
            if left > right: # when left == right: there is only one node , it is still valid to build a BST. not illegal range
                return None
            # recursion
            mid = left + (right - left) // 2 # integer devision , cus mid is an index
            # 我们会始终选择中间靠左的元素作为根节点。
            # 如此相加不会爆内存, 不过python可以直接用(left + right)//2
            # In Python, integers have arbitrary precision, so (left + right) // 2 will never actually "overflow" the memory like it would in C++ or Java. 
            # However, it is a great habit to keep for when you work in other languages!

            # create a root treenode with mid value
            root = TreeNode(nums[mid])
            # 函数定义前面缩进在 class 里面，和 sortedArrayToBST 平级：调用类方法时用 self.
            # 函数定义在某个函数里面，作为内部 helper：调用内部函数时不用 self.
            root.left = traversal(nums, left, mid - 1) 
            root.right = traversal(nums, mid+1, right)
            return root
        
        # call the helper function and pass in the left and right pointers
        root = traversal(0, len(nums) - 1) # 调用内部函数时不用 self.
        return root
# 调用类方法时需要调用self
class Solution:
    def traversal(self, nums: List[int], left: int, right: int) -> TreeNode:
        if left > right:
            return None
        
        mid = left + (right - left) // 2
        root = TreeNode(nums[mid])
        root.left = self.traversal(nums, left, mid - 1) # 调用类方法时用 self.
        root.right = self.traversal(nums, mid + 1, right)
        return root
    
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        root = self.traversal(nums, 0, len(nums) - 1) # 调用类方法时用 self.
        return root
# 递归精简版, 但是不推荐. 因为slicing method: TC = O(n log n), SC = O(n)
# # 1. 时间复杂度：从 O(n) 变成 O(n log n) 
# 虽然看起来每个节点只访问了一次，但 nums[:mid] 和 nums[mid+1:] 并不是简单的“引用”，而是深拷贝（Deep Copy）。
# •	在每一层递归中，Python 都会创建一个原数组一半大小的新数组。
# •	在第一层，拷贝了n个元素；第二层，两个分支加起来又拷贝了约 n个元素……以此类推。
# •	树的高度是 log n，所以每一层都有O(n) 的拷贝开销。
# •	实际时间复杂度：O(n log n)
# 2. 空间复杂度从O(log n) 变成O(n). 在递归的过程中，每一层切片产生的数组副本都会占用内存。虽然旧的副本会在递归返回后被回收，但在最深的一条路径上，所有切片的空间复杂度总和加起来趋近于n。
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        mid = len(nums) // 2

        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root

'''
走一遍流程是理解递归最好的方式。我们以 nums = [-10, -3, 0, 5, 9] 为例，这段代码本质上是在做二分查找式的构建。
由于 mid = left + (right - left) // 2，我们会始终选择中间靠左的元素作为根节点。
1. 第一层递归 (根节点)
• 输入: left = 0, right = 4
• 计算: mid = 0 + (4 - 0) // 2 = 2
• 动作: 创建根节点 root = TreeNode(nums[2]) (即 0)。
• 下一步: 递归构建 root.left 和 root.right。
2. 构建左子树 (0 的左边)
• 输入: left = 0, right = 1 (即子数组 [-10, -3])
• 计算: mid = 0 + (1 - 0) // 2 = 0
• 动作: 创建节点 -10。
• 递归其左: traversal(nums, 0, -1) -> left > right -> 返回 None。
• 递归其右: traversal(nums, 1, 1)： • mid = 1 + (1 - 1) // 2 = 1 • 创建节点 -3。 • -3 的左右孩子均为 None (因为 left > right)。
• 结果: 0.left 接住了 -10，而 -10.right 接住了 -3。
3. 构建右子树 (0 的右边)
• 输入: left = 3, right = 4 (即子数组 [5, 9])
• 计算: mid = 3 + (4 - 3) // 2 = 3
• 动作: 创建节点 5。
• 递归其左: traversal(nums, 3, 2) -> 返回 None。
• 递归其右: traversal(nums, 4, 4)： • mid = 4 + (4 - 4) // 2 = 4 • 创建节点 9。 • 9 的左右孩子均为 None。
• 结果: 0.right 接住了 5，而 5.right 接住了 9。
4. 最终结构展示
递归函数的执行顺序是 Pre-order (先序) 的：先创建当前节点，再向下延伸。但连接过程是自底向上完成的。
最终得到的树（中序遍历即为原数组）：
      0
     / \
   -10  5
     \   \
     -3   9

关键点拨：
1. 高度平衡: 因为我们每次都取 mid，所以左右子树的节点数量差永远不会超过 1。
2. 递归终止: 当 left > right 时，说明当前区间已经没有数字了，所以返回 None 给父节点的 left 或 right 指针，完成“封口”。

要理解这一步，核心在于观察 mid 左右区间的索引是如何变化的。
在你的代码中，递归调用是：
• left_subtree = traversal(nums, left, mid - 1)
• right_subtree = traversal(nums, mid + 1, right)
我们以节点 5 为例子，带入数字拆解一下：
1. 为什么 5 的左孩子是 None？
此时我们处于处理节点 5 的层级：
• 当前区间： left = 3, right = 4 (对应数组中的 [5, 9])
• 计算中间点： mid = 3 + (4 - 3) // 2 = 3
• 创建节点： root = TreeNode(nums[3]) (也就是 5)
接下来去寻找 5 的左孩子：
• 传入参数：traversal(nums, left, mid - 1)
• 代入数值：traversal(nums, 3, 3 - 1) \rightarrow traversal(nums, 3, 2)
• 判断： 此时 left (3) > right (2)。
• 结论： 满足 if left > right: return None。所以 5 的左孩子被赋值为 None。
2. 为什么 5 的右孩子是 9？
接下来去寻找 5 的右孩子：
• 传入参数：traversal(nums, mid + 1, right)
• 代入数值：traversal(nums, 3 + 1, 4) \rightarrow traversal(nums, 4, 4)
进入新的一层递归（处理节点 9）：
• 当前区间： left = 4, right = 4
• 计算中间点： mid = 4 + (4 - 4) // 2 = 4
• 创建节点： root = TreeNode(nums[4]) (也就是 9)
3. 为什么 9 的左右孩子都是 None？
现在我们在节点 9 这层递归里，它会继续尝试拆分：
• 找 9 的左孩子： • 调用 traversal(nums, 4, 4 - 1) \rightarrow traversal(nums, 4, 3) • 4 > 3，返回 None。
• 找 9 的右孩子： • 调用 traversal(nums, 4 + 1, 4) \rightarrow traversal(nums, 5, 4) • 5 > 4，返回 None。
总结规律
这个过程就像是在不断收缩边界：
• 当 left == right 时，说明当前区间只有一个数，这个数会被建成一个孤立的节点。
• 只要一个节点被建成，它就一定会去尝试找“更小”和“更大”的数。
• 如果 mid 已经到了边界，算出来的 mid - 1 就会小于 left，或者 mid + 1 会大于 right。
• 这种**“越界”**现象就是递归停止的信号，告诉程序：“这下面已经没有数字可以挂载了，返回一个空指针吧。”
这种通过索引控制范围的方法，比直接切割数组（nums[:mid]）要高效得多，因为它全程只操作三个整数（left, right, mid），而不需要复制任何数组数据。
你现在能看出来，为什么 left == right 的时候不能直接返回 None 吗？
'''           

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [-10,-3,0,5,9]\n
# @lcpr case=end

# @lcpr case=start
# [1,3]\n
# @lcpr case=end

#

