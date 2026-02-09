#
# @lc app=leetcode id=104 lang=python3
# @lcpr version=30307
#
# [104] Maximum Depth of Binary Tree
#
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (77.85%)
# Likes:    14163
# Dislikes: 285
# Total Accepted:    4.6M
# Total Submissions: 5.9M
# Testcase Example:  '[3,9,20,null,null,15,7]\n[1,null,2]'
#
# Given the root of a binary tree, return its maximum depth.
# 
# A binary tree's maximum depth is the number of nodes along the longest path
# from the root node down to the farthest leaf node.
# 
# 
# Example 1:
# 
# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# 
# 
# Example 2:
# 
# Input: root = [1,null,2]
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 10^4].
# -100 <= Node.val <= 100
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
# 使用迭代法的话，使用层序遍历是最为合适的，因为最大的深度就是二叉树的层数，和层序遍历的方式极其吻合。
# 在二叉树中，一层一层的来遍历二叉树，记录一下遍历的层数就是二叉树的深度
# 所以这道题的迭代法就是一道模板题，可以使用二叉树层序遍历的模板来解决的
# 本题和559题相似
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = collections.deque([root])
        depth = 0 # 代表二叉树的层数
        
        while queue:# 代表queue存在, 因此此时depth不可能为0, 所有depth的创建需要在while外面
            depth += 1 # 我看到这一层存在，先把层数记下，再去处理这一层的所有节点
            for _ in range(len(queue)): # 取每层的节点, len(queue)代表每层的节点个数
                cur = queue.popleft()

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

        return depth

# 方法二: 后序遍历的递归法求高度, 即最大深度 
class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: #不必判断两遍，只保留 getDepth 里的 if not node: return 0 就够；若你更喜欢在入口显式处理空树，两处都写也可以。
            return 0
        
        return self.getDepth(root)
    # 递归三步法: 1. 确定递归函数的参数和返回值 2. 确定终止条件 3. 确定单层递归的逻辑
    def getDepth(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        # 后序递归遍历求高度(即最大深度): 左右中, 先求左右子树的深度, 然后加上当前节点的深度
        leftDepth = self.getDepth(node.left) # 左
        rightDepth = self.getDepth(node.right) # 右
        height = 1+ max(leftDepth, rightDepth) # 中, 中在左和右的上面一层, 所以加1, 代表从下往上的处理逻辑
        return height

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,null,2]\n
# @lcpr case=end

#

