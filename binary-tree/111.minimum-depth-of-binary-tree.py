#
# @lc app=leetcode id=111 lang=python3
# @lcpr version=30307
#
# [111] Minimum Depth of Binary Tree
#
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (52.18%)
# Likes:    7788
# Dislikes: 1362
# Total Accepted:    1.6M
# Total Submissions: 3.1M
# Testcase Example:  '[3,9,20,null,null,15,7]\n[2,null,3,null,4,null,5,null,6]'
#
# Given a binary tree, find its minimum depth.
# 
# The minimum depth is the number of nodes along the shortest path from the
# root node down to the nearest leaf node.
# 
# Note: A leaf is a node with no children.
# 
# 
# Example 1:
# 
# Input: root = [3,9,20,null,null,15,7]
# Output: 2
# 
# 
# Example 2:
# 
# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 10^5].
# -1000 <= Node.val <= 1000
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

# 相对于 104.二叉树的最大深度 ，本题还也可以使用层序遍历的方式来解决，思路是一样的。
# 需要注意的是，只有当左右孩子都为空的时候，才说明遍历的最低点了。如果其中一个孩子为空则不是最低点
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = collections.deque([root])
        depth = 0

        while queue:
            depth += 1
            for _ in range(len(queue)):
                cur = queue.popleft()

                if not cur.left and not cur.right: # 只有当左右孩子都为空的时候，才说明遍历的最低点了。如果其中一个孩子为空则不是最低点
                    return depth
                
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

        return depth
# 方法二: 后序递归遍历, 从底部向上计数, 求的是根节点的最小高度, 符合题目要求的最小深度
# 最小深度: 根节点到最近叶子节点的最小距离;
# 叶子节点: 左右孩子都为空
Class Solution2:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.getDepth(root)
    def getDepth(self, node:Optional[TreeNode]) -> int:
        if not node:
            return 0
        leftDepth = self.getDepth(node.left) # 左
        rightDepth = self.getDepth(node.right) # 右
        # 中的逻辑: 注意此时不能直接写height = 1+min(leftDepth, rightDepth), 因为这种情况如果左不为空右为空或者左为空右不为空时, 会把根节点单边为null空的子节点统计进去, 本题不考虑这种情况
        if node.left is None and node.right: # 左子树为空, 右字数不为空
            return 1 + rightDepth
        if node.left and node.right is None: # 右子树为空, 左子树不为空
            return 1+ leftDepth
        result =  1+ min(leftDepth, rightDepth) # 左右子树都不为空
        return result
# 当左右子树都为空时, 此时他就是叶子节点, 上述逻辑仍然适用: 1+0=1

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [2,null,3,null,4,null,5,null,6]\n
# @lcpr case=end

#

