#
# @lc app=leetcode id=98 lang=python3
# @lcpr version=30400
#
# [98] Validate Binary Search Tree
#
# https://leetcode.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (35.33%)
# Likes:    18252
# Dislikes: 1445
# Total Accepted:    3.2M
# Total Submissions: 9.1M
# Testcase Example:  '[2,1,3]\n[5,1,4,null,null,3,6]'
#
# Given the root of a binary tree, determine if it is a valid binary search
# tree (BST).
# 
# A valid BST is defined as follows:
# 
# 
# The left subtree of a node contains only nodes with keys strictly less than
# the node's key.
# The right subtree of a node contains only nodes with keys strictly greater
# than the node's key.
# Both the left and right subtrees must also be binary search trees.
# 
# 
# 
# Example 1:
# 
# Input: root = [2,1,3]
# Output: true
# 
# 
# Example 2:
# 
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
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
# 本题注意: 
# 1) 二叉搜索树的定义: 对于树中的任意一个节点，必须满足以下 两个条件：它的左子树中的 所有 节点的值都必须 小于 当前节点的值。它的右子树中的 所有 节点的值都必须 大于 当前节点的值。搜索树里不能有相同的元素
# 2) 递归函数什么时候需要返回值？什么时候不需要返回值？这里总结如下三点：
# 如果需要搜索整棵二叉树且不用处理递归返回值，递归函数就不要返回值。（这种情况就是本文下半部分介绍的113.路径总和ii）
# 如果需要搜索整棵二叉树且需要处理递归返回值，递归函数就需要返回值。 （这种情况我们在236. 二叉树的最近公共祖先 (opens new window)中介绍）
# 如果要搜索其中一条符合条件的路径，那么递归一定需要返回值，因为遇到符合条件的路径了就要及时返回。
# 3) 样例中最小节点 可能是int的最小值，如果这样使用最小的int来比较也是不行的。此时可以初始化比较元素为longlong的最小值。问题可以进一步演进：如果样例中根节点的val 可能是longlong的最小值 又要怎么办呢？
# 4) 二叉搜索树做中序遍历(左中右), 利用其特性可以推出, 元素是有序的, 即单调递增
# 5) 本题无需手动回溯, 因为vec需要记录所有访问过的节点, 而非"只记录当前一个分支, 走错了或走完了得擦掉换下一支走". 本题只利用了递归函数的自带物理回溯:即“从哪儿来，回哪儿去”。只要你使用递归，函数执行完后自动回到上一层，这就是“函数自带回溯”. “回溯” 发生在函数执行完最后一行（或者 return）后，系统自动弹出栈顶，自动回到上一层递归函数下面。
# 6) 递归可以想象成入栈出栈: 入栈是“带着期待”：我要看看你左边还有没有人。出栈是“完成承诺”：左边看完了，该我了，然后我要去负责右边。左右子树的关系：对于任何一个节点，它的整个左子树必须全部“出栈”完毕，它自己才能“出栈”；它自己出完后，才轮到它的整个右子树进入这个循环。

# 方法一: 递归法, 利用中序递增性质, 转换成数组. 本方法的关键是如何判断数组是否有序, 即单调递增
class Solution:
    def __init__(self):# 定义全局变量, vec数组
        self.vec = [] # 空间复杂度O(n)
# 关于 __init__：
# 在 LeetCode 环境中，其实不建议在 __init__ 里定义 vec。因为 LeetCode 实例化你的类一次，但会运行多次 isValidBST。虽然你在函数里清空了，但更安全的做法是直接把 vec 定义在 isValidBST 内部，并作为参数传给 traversal，或者直接把 traversal 定义在 isValidBST 的里面。
# 更优雅的 Python 写法（闭包）：你可以把 traversal 写在 isValidBST 内部，这样就不需要 self. 来回传来传去了：
    def isValidBST(self, root: Optional[TreeNode]) -> bool: # 递归函数
        self.vec = [] # 注: 一定要在启动递归前, 清空数组一次. 如果不清空：测完用例 A 之后，self.vec 里存着 A 的节点。
        self.traversal(root)
        # 判断数组是否是单调递增的
        for i in range(1, len(self.vec)): # 注意这里遍历要从1开始, 因为要比较前一个元素, 保证最开始前一个元素是索引为0的
            if self.vec[i] <= self.vec[i-1]: 
                # 注: 1) 如果这里判断的只要有一对是递增的你就返回 True，万一后面是减小的呢？所以这里不能先判断对的情况, 而是先判断反例的情况, 一遇到错的就返回False;
                # 注: 2) 注意要小于等于, 搜索树里不能有相同元素
                return False
        return True
    
    def traversal(self, root:Optional[TreeNode]) -> None: # 无返回值
    # 递归的终止条件
        if root is None: # 空的根节点, 什么二叉树都可以(包括二叉搜索树, 平衡二叉树, 完全二叉树, 满二叉树), 如果返回类型是Boolean, 应返回true
            return 
        # 单层递归逻辑
        self.traversal(root.left)  # left
        self.vec.append(root.val)   # middle, 将二叉搜索树转换为有序数组
        self.traversal(root.right) # right   
        # 注: 本题无需手动回溯, 因为vec需要记录所有访问过的节点, 而非"只记录当前一个分支, 走错了或走完了得擦掉换下一支走". 本题只利用了递归函数的自带物理回溯:即“从哪儿来，回哪儿去”。只要你使用递归，函数执行完后自动回到上一层，这就是“函数自带回溯”
# 方法二: 递归法, 设定极小值, 利用中序递增性质, 判断节点的有序性进行比较. 本方法的关键也是如何判断节点是否是单调递增
class Solution:
    def __init__(self):
        self.maxVal = float('-inf') # 因为-2^31 <= Node.val <= 2^31 - 1, 后台测试数据有int最小值, 这里最大值的初始化需要比int的最小值还小, 因此设一个无限小

    def isValidBST(self, root: Optional[TreeNode]) -> bool: # 递归函数
        # 递归终止条件:
        if root is None:
            return True
        # 单层递归逻辑:
        left = self.isValidBST(root.left) # left
        # 中序遍历, 验证遍历的元素是否从小到大
        if self.maxVal < root.val: # 遍历节点是递增的, 保证在遍历左子树的第一个节点时一定比maxVal大
            self.maxVal = root.val # maxVal记录当前节点的前一个节点的数值
        else: 
            return False
        right = self.isValidBST(root.right) # right

        return left and right # 表示左右子树都符合条件
#  方法三: 双指针, 不额外定义变量, 而是在遍历二叉树时,前一个节点和后一个节点进行比较. 且如果root是longlongmin, 上述方法二也不可行,  因为一开始就会返回False
#  本方法直接取该树的最小值, 中序遍历 + 记录前一个节点. 本方法的关键是如何用pre记录前一个节点: 双指针记录root比pre大, 两个指针同时移动同时比较
#  在递归过程中，我们定义两个指针：root(当前指针)：递归正在访问的节点; pre(前驱指针)：中序遍历中，root的上一个节点（也就是紧挨着它的“左边”那个人）。
#  核心逻辑:只要是二叉搜索树，那么pre的值必须永远小于cur的值。
class Solution:
    def __init__(self):
        self.pre = None # 用来记录前一个节点
    def isValidBST (self, root) -> bool:
        if root is None:
            return True
        
        left = self.isValidBST(root.left) # left

        if self.pre is not None and self.pre.val >= root.val:# middle
            return False
        self.pre = root # 此时pre is None, 把第一个节点root赋值给pre, 这样下一层循环, root就是pre上面一层的值

        right = self.isValidBST(root.right) # right

        return left and right



# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [2,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [5,1,4,null,null,3,6]\n
# @lcpr case=end

#

