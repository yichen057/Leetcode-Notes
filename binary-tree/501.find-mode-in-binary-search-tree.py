#
# @lc app=leetcode id=501 lang=python3
# @lcpr version=30400
#
# [501] Find Mode in Binary Search Tree
#
# https://leetcode.com/problems/find-mode-in-binary-search-tree/description/
#
# algorithms
# Easy (58.46%)
# Likes:    4103
# Dislikes: 814
# Total Accepted:    384.4K
# Total Submissions: 657.6K
# Testcase Example:  '[1,null,2,2]\n[0]'
#
# Given the root of a binary search tree (BST) with duplicates, return all the
# mode(s) (i.e., the most frequently occurred element) in it.
# 
# If the tree has more than one mode, return them in any order.
# 
# Assume a BST is defined as follows:
# 
# 
# The left subtree of a node contains only nodes with keys less than or equal
# to the node's key.
# The right subtree of a node contains only nodes with keys greater than or
# equal to the node's key.
# Both the left and right subtrees must also be binary search trees.
# 
# 
# 
# Example 1:
# 
# Input: root = [1,null,2,2]
# Output: [2]
# 
# 
# Example 2:
# 
# Input: root = [0]
# Output: [0]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 10^4].
# -10^5 <= Node.val <= 10^5
# 
# 
# 
# Follow up: Could you do that without using any extra space? (Assume that the
# implicit stack space incurred due to recursion does not count).
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
# 二叉搜索树的解法(双指针): 中序遍历+pre指针, 引入 pre 指针来记录前一个节点，在递归过程中不断对比 cur 和 pre。
# 一次遍历找众数：这是最难的点。在普通数组里找众数，通常要遍历两遍（第一遍找最大频率，第二遍找对应的数）。但在 BST 中，代码随想录 介绍了一个技巧：
# 当 count == maxCount 时，添加元素。
# 当 count > maxCount 时，不仅要更新maxCount，而且要清空结果集（以下代码为result数组），因为结果集之前的元素都失效了。清空结果集并重新添加。
# 这种“边走边清空”的逻辑需要你对过程有极强的掌控力。
class Solution:
    def __init__(self):
        self.maxCount = 0 # 统计整个bst出现的最高频率
        self.count = 0 # 统计单个元素出现的频率
        self.pre = None # cur前一个节点
        self.result = [] # result数组放最终返回的结果
    def findMode(self, root)->List[int]:
        # 清空global variable全局变量
        self.maxCount = 0 # 统计整个bst出现的最高频率
        self.count = 0 # 统计单个元素出现的频率
        self.pre = None # cur前一个节点
        self.result = [] # result数组放最终返回的结果

        self.searchBST(root)
        return self.result # 返回题目要求的节点
    def searchBST(self, cur) -> None: # 遍历整个二叉树直接统计元素即可, 无需递归函数的返回, 结果在全局变量里
        # base case
        if cur is None:
            return
        # 单层中序递归(左中右)
        # 左
        self.searchBST(cur.left)
        # 中的处理逻辑
        if self.pre is None: # pre未指向任何节点, 即递归遍历的第一个元素
            self.count = 1
        elif self.pre.val == cur.val: # 如果值和前一个节点数值相同：说明还在统计同一个元素，count 累加。
            self.count += 1
        else: # self.pre is not None and pre.val != cur.val如果值和前一个不同：说明上一个元素已经统计完了，现在遇到了新元素，count 必须重置为 1
            self.count = 1
        self.pre = cur # pre是cur的影子, cur往前走一步, pre紧跟这挪到刚才cur站的位置, 确保pre是挨着cur的移动指针
        # 让 pre 移动的秘诀在于：在处理完当前节点的逻辑后，立刻把当前节点标记为“前一个节点”。

        if self.count == self.maxCount:
            self.result.append(cur.val)

        if self.count > self.maxCount: # 如果计数大于最大值频率
            self.maxCount = self.count # 更新最大频率
            self.result = [cur.val] # 此时result里放的不是真正想要统计的众数, 因为maxCount更新了, 因此之前result里的元素要清空, 并把当前cur.val加入result结果集
            # 上面一行self.result = [cur.val]可以替代下面两行: 
            # self.result.clear()      # 先把旧的全部倒掉
            # self.result.append(cur.val) # 再把新的放进去
        # 右
        self.searchBST(cur.right) # 右
        return # 这里的 return 写不写都行，建议不写。你可以删掉最后一行：这样代码更符合 Python 的简洁风格。也可以留着：如果你觉得这样能清晰地提醒自己“这个节点的递归到此为止了”


# 普通二叉树的解法(map+sort, 空间复杂度O(n)因为存了整棵树的频率), 虽然本题是二叉搜索树(中序遍历+pre指针, 空间复杂度O(1)), 会更难
# from collections import defaultdict
# class Solution:
#     def findMode(self, root: Optional[TreeNode]) -> List[int]:
#         # 1. 初始化unordered_map<int, int>map,  key是node.val, value是node.val的frequency. 
#         freq_map = defaultdict(int) # 初始化字段, 字段内部状态{Key:Value}, 说明字典为空, 初始化map时当key不存在时, 默认value=0
#         result = [] # 用来装题目需要返回的众数数组, 因为众数可能不止一个
#         if root is None:
#             return result
        
#         # 2. 遍历数并填充map
#         self.searchBT(root, freq_map)

#         # 3. 将map转为列表vec以便排序, 列表里每一个元素是(key, value)的tuple元组: 元组是将多个元素组合在一起的序列。它的外形特征是使用圆括号，元素之间用逗号隔开.
#         # 元组具有immutable不可变性:一旦写死，就不能修改的列表. 因为我们只希望读取这些配对信息，而不希望在排序过程中不小心改动了键值对。
# #         vec = list(freq_map.items()) #map.items()是把字典里所有的“键值对”一次性全部拿出是一个iterable(视图对象), 会把每一对Key和Value包装成一个元组（Tuple），整体看起来像是一个列表：例如[(1, 3), (2, 5)]. 返回的是一个“视图对象”（Iteratable），它不是真正的列表。所以如果你想进行排序，通常需要套一个list()
# #         # - **`map.keys(): 只拿所有的“键”（元素本身）。
# #         # - **`map.values(): 只拿所有的“值”（频率）。
# #         # - **`map.items(): 全拿出来，一对一对地打包成元组，方便后续的排序和处理。

# #         # 变成列表后, 就可以利用sort(), 告诉 Python：“请看元组里的第二个数字（频率），按它的大小给我排个序。”
# #         # 4. 按照频率（元组第二个元素）从大到小排序：
# #         vec.sort(key=lambda x:x[1], reverse=True)
# # # key=lambda x: x[1]（关键点）：
# # # key 参数告诉 Python：“不要按照整个元组排，按照我指定的规则排”; 如果不写 key，Python 默认会先比较元组的第一个数。
# # # lambda x：这里的 x 代表列表中的每一个元素（即每一个元组，如 (1, 3)）。
# # # x[1]：取出元组中索引为 1 的数（即第二个数字，也就是频率）。
# # # reverse=True：默认排序是从小到大。因为我们要找“众数”，需要把频率最高的排在最前面，所以设为 True 进行降序排列。

# #         # 5. 取出最高频率的元组里索引为1的元素, 放到result结果数组中
# #         result.append(vec[0][0]) # vec[0][0] 代表第一对元组里的元素（Key）

# #         for i in range (1, len(vec)): # 从1开始, 因为0的元组是比较基准, 没必要和自己比
# #             # 如果后续元素的频率等于最高频率，把元素的值加入结果集
# #             if vec[i][1] == vec[0][1]: # vec[0][1]代表它的频率（Value）, 遍历pair, 取每一对的第一个索引的值与第一对第一个索引的值(已排序, 目前最大)进行比较
# #                 result.append(vec[i][0]) # 取pair里的索引为0的元素
# #             else:
# #                 break # 频率变小了, 则直接跳出循环, 因为已经排好序了
#         # 345步可以用max()函数直接找出map里的最大value, 即最高频率, 再将所有符合最高频率对应的元素key添加到result里. 该方法更好, 因为时间复杂度O(N), 前面的345步由于有排序, 时间复杂度O(NlogN)
#         # 时间复杂度：从 O(Nlog N)优化到了 O(N)。因为 max() 遍历一遍，freq_map.items() 遍历一遍，两个 O(N) 相加依然是 O(N)。空间复杂度：依然是O(N)，用于存储字典。
#         max_freq = max(freq_map.values())
#         for key, freq in freq_map.items():
#             if freq == max_freq:
#                 result.append(key)
#         return result
        
#     def searchBT(self, cur, freq_map)->None:
#         # 至于用前中后序哪种遍历也不重要，因为就是要全遍历一遍，怎么个遍历法都行，层序遍历都没毛病！此处使用前序遍历
#         if cur is None:
#             return
#         # 中: 统计元素频率
#         freq_map[cur.val] += 1
#         # 左
#         self.searchBT(cur.left, freq_map)
#         # 右
#         self.searchBT(cur.right,freq_map)

# 如何统计元素频率的: 可以拆解为以下三个步骤：
# 查找与获取：程序查看 freq_map 字典中是否已经存在 cur.val 这个键（Key）。
# 默认值处理（这是 defaultdict 的魔力）：
# 如果不存在这个键，defaultdict(int) 会自动创建一个新条目，并将值初始化为 0。
# 如果已存在，则获取当前存储的数值。
# 自增更新：执行 + 1 操作，然后把新结果存回该键。
# 举个例子：
# 假设遍历一棵树，节点值依次是 [1, 2, 2]：
# 遇到第一个 1：字典里没 1，创建 freq_map[1] = 0，然后 0 + 1。现在字典：{1: 1}。
# 遇到第一个 2：字典里没 2，创建 freq_map[2] = 0，然后 0 + 1。现在字典：{1: 1, 2: 1}。
# 遇到第二个 2：字典里已有 2，值为 1，执行 1 + 1。最终字典：{1: 1, 2: 2}。


# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [1,null,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#

