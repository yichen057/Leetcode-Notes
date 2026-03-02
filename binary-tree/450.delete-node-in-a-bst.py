#
# @lc app=leetcode id=450 lang=python3
# @lcpr version=30400
#
# [450] Delete Node in a BST
#
# https://leetcode.com/problems/delete-node-in-a-bst/description/
#
# algorithms
# Medium (54.25%)
# Likes:    10355
# Dislikes: 383
# Total Accepted:    836K
# Total Submissions: 1.5M
# Testcase Example:  '[5,3,6,2,4,null,7]\n3\n[5,3,6,2,4,null,7]\n0\n[]\n0'
#
# Given a root node reference of a BST and a key, delete the node with the
# given key in the BST. Return the root node reference (possibly updated) of
# the BST.
# 
# Basically, the deletion can be divided into two stages:
# 
# 
# Search for a node to remove.
# If the node is found, delete the node.
# 
# 
# 
# Example 1:
# 
# Input: root = [5,3,6,2,4,null,7], key = 3
# Output: [5,4,6,2,null,null,7]
# Explanation: Given key to delete is 3. So we find the node with value 3 and
# delete it.
# One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
# Please notice that another valid answer is [5,2,6,null,4,null,7] and it's
# also accepted.
# 
# 
# 
# Example 2:
# 
# Input: root = [5,3,6,2,4,null,7], key = 0
# Output: [5,3,6,2,4,null,7]
# Explanation: The tree does not contain a node with value = 0.
# 
# 
# Example 3:
# 
# Input: root = [], key = 0
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 10^4].
# -10^5 <= Node.val <= 10^5
# Each node has a unique value.
# root is a valid binary search tree.
# -10^5 <= key <= 10^5
# 
# 
# 
# Follow up: Could you solve it with time complexity O(height of tree)?
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
# 删除BST的节点: 删了节点后将改变树的结构, 且删后仍为BST
# 递归法 (本题看笔记本是实例更清楚)
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Base Case:(此处的递归终止条件比较复杂): 本题不去遍历整棵树, 而是在遍历的过程中寻找要删的节点, 当找到要删的节点时就是终止条件, 所以删除节点的逻辑就是终止条件
        # 删除操作的逻辑之所以是终止条件，是因为 “删除”这个动作本身就是递归寻找过程的终点。一旦完成删除动作，当前子树的状态就确定了，剩下的就是一层层向上把这个结果传递回去。
#         在递归函数中，终止条件通常有两种：
# 1) 没找到：走到空节点了（`if root is None: return None`），说明任务失败，原样返回。
# 2) 找到了：既然找到了要删除的节点，那么本层递归的核心任务已经完成了。处理完删除逻辑后，不需要再向下递归，直接把处理后的结果（可能是新节点，也可能是 None）返回给上一层即可。
        # 情况一: "处理空树"及“没找到要删的节点
        if root is None:
            return root
        # 情况二: 找到了要删的节点. 说明当前的这个 `root` 变量所指向的节点内存地址，其值正好等于我们要找的 `key`, 所以，此时的 `root` 就是“目标靶子”
        if root.val == key:
            # 2.1 待删节点为叶子节点: 左右子节点为空, 未改变BST的结构
            if root.left is None and root.right is None:
                return None
            # 2.2 待删节点: 左子节点不空, 右子节点为空
            elif root.left and root.right is None: # 此处root.left可以省略不写
                return root.left
            # 2.3 待删节点: 左为空, 右不为空
            elif root.right and root.left is None: # 此处root.right可以省略不写
                return root.right
            # 2.4 待删节点: 左不为空, 右也不为空(核心!)
            else: # 利用BST左小右大的特性, root为待删节点
                cur = root.right # 先进入root的右子树, 为root的左子树找新家
                while cur.left is not None : # 这段循环的目标是找到右子树中数值最小的节点(右子树中最左侧的节点), 通过不断向左深入, 最终停下来的cur节点, 就是整棵右子树中值最小的节点
                    # 删掉 `root` 后：
                    # 1. 我们要把root的整个左子树搬走。
                    # 2. 搬到哪里呢？搬到root右子树的最左边节点的左孩子位置上。只要左边还有路, 就一直往左走
                    # 3. 因为右子树的最左节点是右边所有数里最小的，但它依然比左子树里的所有数都大。所以把左子树接在它的左边，依然符合 BST 的定义。
                    # 其实，找接班人有两种方案，效果是等价的：
                    # 方案 A（代码采用的）：找右子树的最小节点（Right Minimum）。
                    # 方案 B: 找左子树的最大节点（Left Maximum）。
                    cur = cur.left # cur由root的右子节点, 变为右子节点的左子节点. 这里的cur就是右子树里最小的节点
            cur.left = root.left # root的右子树里最小节点的左子树为原来root的左子树
            # 待删节点此时左子树已为空右子树不为空, 父节点指向要删节点的右孩子, 不经过待删节点
            root = root.right # root改指向原root的右子节点, 并赋值给root
            return root # 把原root的右子节点返回至上一层, 使得被删元素被跳过
        # 单层递归
        # 向左遍历
        if key < root.val:
            root.left = self.deleteNode(root.left, key) # 递归函数有返回值, 左子树指向左子树删掉key之后新的根节点
        # 向右遍历
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        # 返回删除key后的新的BST的根节点
        return root
     
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [5,3,6,2,4,null,7]\n3\n
# @lcpr case=end

# @lcpr case=start
# [5,3,6,2,4,null,7]\n0\n
# @lcpr case=end

# @lcpr case=start
# []\n0\n
# @lcpr case=end

#

