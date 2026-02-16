#
# @lc app=leetcode id=106 lang=python3
# @lcpr version=30307
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
#
# algorithms
# Medium (67.96%)
# Likes:    8652
# Dislikes: 156
# Total Accepted:    919.8K
# Total Submissions: 1.4M
# Testcase Example:  '[9,3,15,20,7]\n[9,15,7,20,3]\n[-1]\n[-1]'
#
# Given two integer arrays inorder and postorder where inorder is the inorder
# traversal of a binary tree and postorder is the postorder traversal of the
# same tree, construct and return the binary tree.
# 
# 
# Example 1:
# 
# Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]
# 
# 
# Example 2:
# 
# Input: inorder = [-1], postorder = [-1]
# Output: [-1]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= inorder.length <= 3000
# postorder.length == inorder.length
# -3000 <= inorder[i], postorder[i] <= 3000
# inorder and postorder consist of unique values.
# Each value of postorder also appears in inorder.
# inorder is guaranteed to be the inorder traversal of the tree.
# postorder is guaranteed to be the postorder traversal of the tree.
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
# 从中序与后序遍历序列构造二叉树
# 方法一: 原始切片法
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]: # 递归函数的参数是中序和后序数组, 返回类型是TreeNode 
        # 第一步: 递归终止条件: 后序数组为空, 后序若为空, 说明中序也为空, 只写后序即可
        if not postorder:
            return None
        
        # 第二步: 后序遍历的最后一个就是当前的中间节点(根节点元素)
        root_val = postorder[-1]
        root = TreeNode(root_val) # 定义根节点, 并传入根节点的值
        # 如果你写 root = TreeNode()，Python 会默认帮你创建一个 val 为 0 的节点。
        # 问题是：在算法逻辑中，这个 0 并不是你想要的根节点值，它只是一个临时占位符。
        # 风险：如果你之后忘记执行 root.val = root_val，你的树里就会混进一个错误的数字 0。
        # 对比：root = TreeNode(root_val) 是一步到位，确保这个节点从出生那一刻起，数据就是正确的。

        # 第三步: 找中序数组的"中"元素的位置, 并作为切割点
        # .index(root_val)：这是 Python 列表（List）的内置方法。它会在inorder 列表中查找第一个值为root_val的元素。返回值：返回该元素在列表中的索引（下标）。作用：在“中序遍历”序列中找到根节点的位置。这个位置就像一把“菜刀”，准备把序列切成左右两半
        separator_idx = inorder.index(root_val)
        # 注: 每次切片和index查找都是O(n), 时间复杂度O(n^2). .index() 是 O(N) 的，切片 [:] 也是 O(N) 的。如果递归过程中反复切割，效率会变低。 
        # 单层内：查找和切片是顺序执行，复杂度相加, 时间复杂度是O(n)。但是全局看, 单层复杂度O(n)与递归深度O(n)发生关联，导致最终结果呈现为O(n^2)
        # 虽然单层内是相加，但因为每一层都要做一遍O(k)的工作，所以总复杂度变成了“层数”与“每层工作量”的组合。我们以最坏的情况（树退化成链表，高度为 $n$）为例：第 1 层：处理 $n$ 个节点，耗时 $n$。第 2 层：处理 $n-1$ 个节点，耗时 $n-1$。第 3 层：处理 $n-2$ 个节点，耗时 $n-2$。...第 n 层：处理 1 个节点，耗时 1。总时间复杂度 = n + (n-1) + (n-2) + ... + 1 = n+(n-1)+(n-2)+...+1= n*(n+1)/2 = O(n)。
        # 第四步: 切割inorder数组, 得到inorder数组的左,右半边
        # 切割中序数组的左子树: [:separator_idx]：这是 Python 的**切片（Slicing）**语法。从列表的开头（索引 0）一直取到 separator_idx 之前（不包含 separator_idx 本身）。作用：提取出所有位于根节点左侧的元素，它们构成了左子树的中序遍历序列。
        inorder_left = inorder[:separator_idx]
        # [separator_idx + 1:]：这也是切片语法。含义：从 separator_idx + 1 开始，一直取到列表的末尾。加 1是因为 separator_idx 处是根节点，我们要跳过它，从它的下一个元素开始切。作用：提取出所有位于根节点右侧的元素，它们构成了右子树的中序遍历序列。
        inorder_right = inorder[separator_idx + 1:]
        
        # 第五步: 根据中序遍历切割后的长度，去切割后序遍历（Postorder）数组, 得到postorder数组的左,右半边
        # 它的核心逻辑是：虽然中序和后序的顺序不同，但同一棵子树包含的“节点数量”是绝对相等的
        # 切割左子树的后序序列: 在后序遍历中，序列的排列是 [左子树, 右子树, 根]。既然我们已经从中序遍历知道了左子树有 k 个节点，那么后序遍历的前 k 个节点也一定全属于左子树。
        postorder_left = postorder[:len(inorder_left)] # 从后序数组的开头，取走和左子树中序序列一样多的元素。左闭右开区间
        # 切割右子树的后序序列: 取中间那一段（跳过了左子树，也去掉了最后的根节点），剩下的就是右子树的后序序列。起点 len(inorder_left)：跳过刚才切走的左子树部分。终点 len(postorder) - 1：这是关键！后序遍历的最后一个元素是当前的根节点，我们在处理左右子树时，必须把它剔除掉。
        postorder_right = postorder[len(inorder_left): len(postorder)-1]
        
        # 第六步: 递归
        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)

        # 第七步: 返回答案
        return root

# 方法二: 下标索引+哈希表法加速查找
class Solution:
    def buildTree(self, inorder, postorder):
        # 1. 用哈希表加速查找
        val_to_idx = {val: i for i, val in enumerate(inorder)}
        # 例子：如果 inorder = [9, 3, 15]，那么 val_to_idx 就是 {9:0, 3:1, 15:2}。
        # 好处：以后想知道 3 在哪，直接看一眼 val_to_idx[3] 就知道是 1 了，不用去数数组。
        # 在原始代码中，我们用 inorder.index(root_val) 满大街找根节点，太慢了。优化后把中序数组里的每个值和它的位置记在字典上。
        def helper(in_left, in_right, post_left, post_right):
            # in_left, in_right：当前子树在中序数组里的“头”和“尾”。post_left, post_right：当前子树在后序数组里的“头”和“尾”。
            # 终止条件：如果左边界大于右边界，说明没有节点了
            if in_left > in_right or post_left > post_right:
                return None
            
            # 2. 确定根节点值（后序遍历的最后一个）
            root_val = postorder[post_right]
            root = TreeNode(root_val)
            
            # 3. 找到中序遍历中的分割点. 
            # 这是下标法的核心！idx 是根节点在中序数组的位置
            idx = val_to_idx[root_val]
            
            # 4. 计算左子树的大小（这是切割的关键线索）;left_size：左子树到底有几个节点？
            left_size = idx - in_left
            # 根节点的位置 idx 减去左边界 in_left，中间剩下的就是左子树的成员数量。有了这个数量，我们就能在后序数组里精准地切开左、右子树了

            # 5. 递归构造左右子树，只传边界下标
            # 中序和后序的左子树：
            # 中序左子树范围 [in_left, idx - 1], 从原来的左边界 in_left 到根节点左边那一个 idx - 1
            # 后序左子树范围 [post_left, post_left + left_size - 1], 从原来的左边界 post_left 开始，数出 left_size 这么长（所以结尾是 post_left + left_size - 1)
            root.left = helper(in_left, idx - 1, post_left, post_left + left_size - 1)
            
            # 中序和后序的右子树：
            # 中序右子树范围 [idx + 1, in_right]
            # 后序右子树范围 [post_left + left_size, post_right - 1]
            root.right = helper(idx + 1, in_right, post_left + left_size, post_right - 1)
            
            return root

        return helper(0, len(inorder) - 1, 0, len(postorder) - 1)


# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [9,3,15,20,7]\n[9,15,7,20,3]\n
# @lcpr case=end

# @lcpr case=start
# [-1]\n[-1]\n
# @lcpr case=end

#

