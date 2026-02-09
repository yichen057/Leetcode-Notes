#
# @lc app=leetcode id=559 lang=python3
#
# [559] Maximum Depth of N-ary Tree
#
# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/description/
#
# algorithms
# Easy (73.10%)
# Likes:    2862
# Dislikes: 97
# Total Accepted:    348.9K
# Total Submissions: 475.3K
# Testcase Example:  '[1,null,3,2,4,null,5,6]'
#
# Given a n-ary tree, find its maximum depth.
# 
# The maximum depth is the number of nodes along the longest path from the root
# node down to the farthest leaf node.
# 
# Nary-Tree input serialization is represented in their level order traversal,
# each group of children is separated by the null value (See examples).
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: root = [1,null,3,2,4,null,5,6]
# Output: 3
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: root =
# [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: 5
# 
# 
# 
# Constraints:
# 
# 
# The total number of nodes is in the range [0, 10^4].
# The depth of the n-ary tree is less than or equal to 1000.
# 
# 
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
# 本题和104题相似
class Solution:
    # 方法一: 递归法Recursion: Bottom-up, +1 in the end
    def maxDepth(self, root: 'Node') -> int: #在 LeetCode 的 N 叉树定义中，这非常常见. Python 解析到该行代码时，`Node` 类还没完全定义好。如果不加引号，Python 会报错找不到 `Node`。
        if not root:
            return 0

        depth = 0 
        for child in root.children or []: # or []: 以防 root.children 为 None(Handle None case with empty list)
            depth = max (depth, self.maxDepth(child)) # Recursively find max depth of each child 收集所有子树中的最大值
            #注意: 1)这里调用函数要写self.因为maxDepth是类的方法;2)maxDepth里要写child而不是root.child, 在循环里应该使用循环变量 child
        return depth + 1 # +1代表的是当前这个根节点本身也占据一层
    
    # 方法二: 层序法 Level-order traversal(BFS): top-down traversal, +1 increment the depth counter at the beginning of each while-loop iteration
    def maxDepth(self, root: 'Node') -> int: # 注意: 二叉树采用TreeNode类型, N叉树用'Node'即可
        if not root:
            return 0
        
        depth = 0
        queue = collections.deque([root])

        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                for child in node.children:
                    queue.append(child)
        return depth
    
# @lc code=end

