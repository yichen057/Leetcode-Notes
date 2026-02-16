#
# @lc app=leetcode id=513 lang=python3
# @lcpr version=30307
#
# [513] Find Bottom Left Tree Value
#
# https://leetcode.com/problems/find-bottom-left-tree-value/description/
#
# algorithms
# Medium (72.14%)
# Likes:    3986
# Dislikes: 300
# Total Accepted:    435K
# Total Submissions: 603K
# Testcase Example:  '[2,1,3]\n[1,2,3,4,null,5,6,null,null,7]'
#
# Given the root of a binary tree, return the leftmost value in the last row of
# the tree.
# 
# 
# Example 1:
# 
# Input: root = [2,1,3]
# Output: 1
# 
# 
# Example 2:
# 
# Input: root = [1,2,3,4,null,5,6,null,null,7]
# Output: 7
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 10^4].
# -2^31 <= Node.val <= 2^31 - 1
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
# 方法一: 层序遍历法
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = collections.deque([root]) # queue里存的是数的节点, 每一轮存的是当前层的所有节点
        result = 0 # 每次进入循环体，i 从 0 开始，i == 0 这个条件必然命中，result 必然被赋值。此时 0 只是一个转瞬即逝的占位符，它不会影响最终结果. 这里不初始化也没关系
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                cur = queue.popleft() # cur 弹出后确实没有"存"到别的地方，因为不需要。
                #弹出它的目的只有两个：1.检查值：如果是该层第一个节点（i == 0），就把 cur.val 记录到 result; 2.把它的子节点加入队列：为下一层的遍历做准备。
                # BFS 过程中，当一个对象没有任何变量引用它时，就会被自动回收。内存里同时存在的节点大约就是队列里那一两层的量，处理完的节点会被垃圾回收机制 GC 回收
                if i == 0:
                    result = cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return result
# 第1轮 queue: [根节点]        → pop根节点，把它的左右孩子放进去
# 第2轮 queue: [左1, 右1]      → 逐个pop，把各自的孩子放进去
# 第3轮 queue: [左2, 右2, ...]  → 同上
# ...
# 最后一轮 queue: [最底层节点们] → i==0 时记录的就是最底层最左边的值
# 所以 queue 本质上是个滑动窗口——永远只保存"当前层"和"下一层"的节点，处理完的节点就丢掉了。最终我们只关心 result 这一个值

# 方法二: 递归法: 求最大深度的最左侧第一个叶子节点
# 本题使用前序后序中序均可, 因为本题无需处理"中"的逻辑, 只需先遍历"左"即可
# 注: 本题不能一直向左遍历, 因为未必能遍历到最后一行; 最左侧的叶子节点未必是左孩子, 但这个不影响"先左后右"的顺序去遍历
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # instance attributes实例属性, 成员变量, 所以需要在变量前self.
        self.max_depth = float('-inf')
        self.result = None # 在递归法中，result是通过比较筛选出来的。在 Python 中，处理这种“筛选出来的最值”，用 None 表示“尚未找到”是更严谨的工业级写法
        # 在迭代法里，你把 result 初始化为 None、999 或者 float('-inf') 结果都是一样的，因为第一行第一个节点（根节点）绝对会把它覆盖掉。
        # 但在递归法中，使用 None 主要是为了防止 0 与树中真实的节点值 0 产生混淆，确保我们在 return 时拿到的是从树里长出来的数字。
        self.traversal(root, 1) # 成员方法member method, 成员函数, 定义在 Solution 类之下。在主函数中通过 self.traversal 调用
        return self.result
    def traversal(self, node, depth) -> None: # depth: 始终表示当前遍历的深度; 注: 无返回值
        # 递归遍历的终止条件: 遍历到第一个叶子节点就停止遍历
        if not node.left and not node.right:
            if depth > self.max_depth: # 只有第一个到达新高度的才能赋值给result. 注: 使用全局变量global variable要加self., 如果不加self.除非是local variable
                self.max_depth = depth
                self.result = node.val
                return
        # 递归的单层递归. 本题先左后右, 无中. 左边的孩子总是第一个到达新高度
        # left
        if node.left:
            depth += 1
            self.traversal(node.left, depth) 
            depth -= 1 # 回溯(隐藏在递归函数的下面): 当前深度是depth, 如果只加不减会改变当前的深度
        # right
        if node.right:
            depth += 1
            self.traversal(node.right, depth)
            depth -= 1
        # 上面这段可以精简为:
        # self.traversal(node.right, depth+1)
        # self.traversal(node.right, depth+1) # 括号里写depth+1, 并未改变depth的值, 且回溯过程隐藏在递归函数里
# 如果是寻找最后一层最右侧的节点, 使用层序遍历法, 这次可以先右后左
# 每一层先放右孩子，再放左孩子。这样每一层弹出的第一个节点（i == 0）就是最右边的节点。
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = collections.deque([root]) # queue里存的是数的节点, 每一轮存的是当前层的所有节点
        result = 0 # 每次进入循环体，i 从 0 开始，i == 0 这个条件必然命中，result 必然被赋值。此时 0 只是一个转瞬即逝的占位符，它不会影响最终结果. 这里不初始化也没关系
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                cur = queue.popleft() # cur 弹出后确实没有"存"到别的地方，因为不需要。
                #弹出它的目的只有两个：1.检查值：如果是该层第一个节点（i == 0），就把 cur.val 记录到 result; 2.把它的子节点加入队列：为下一层的遍历做准备。
                # BFS 过程中，当一个对象没有任何变量引用它时，就会被自动回收。内存里同时存在的节点大约就是队列里那一两层的量，处理完的节点会被垃圾回收机制 GC 回收
                if i == 0:
                    result = cur.val
                if cur.right:
                    queue.append(cur.right)
                if cur.left:
                    queue.append(cur.left)
               
        return result
# 寻找最底层最右节点, 使用递归遍历法, 先右后左  
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # instance attributes实例属性, 成员变量, 所以需要在变量前self.
        self.max_depth = float('-inf')
        self.result = None # 在递归法中，result是通过比较筛选出来的。在 Python 中，处理这种“筛选出来的最值”，用 None 表示“尚未找到”是更严谨的工业级写法
        # 在迭代法里，你把 result 初始化为 None、999 或者 float('-inf') 结果都是一样的，因为第一行第一个节点（根节点）绝对会把它覆盖掉。
        # 但在递归法中，使用 None 主要是为了防止 0 与树中真实的节点值 0 产生混淆，确保我们在 return 时拿到的是从树里长出来的数字。
        self.traversal(root, 1) # 成员方法member method, 成员函数, 定义在 Solution 类之下。在主函数中通过 self.traversal 调用
        return self.result
    def traversal(self, node, depth) -> None: # depth: 始终表示当前遍历的深度; 注: 无返回值
        # 递归遍历的终止条件: 遍历到第一个叶子节点就停止遍历
        if not node.left and not node.right:
            if depth > self.max_depth: # 只有第一个到达新高度的才能赋值给result. 注: 使用全局变量global variable要加self., 如果不加self.除非是local variable
                self.max_depth = depth
                self.result = node.val
                return
        # 递归的单层递归. 本题先右后左, 无中. 右边的孩子总是第一个到达新高度
        # right
        if node.right:
            depth += 1
            self.traversal(node.right, depth)
            depth -= 1
        # left
        if node.left:
            depth += 1
            self.traversal(node.left, depth) 
            depth -= 1 # 回溯(隐藏在递归函数的下面): 当前深度是depth, 如果只加不减会改变当前的深度
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [2,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,null,5,6,null,null,7]\n
# @lcpr case=end

#

