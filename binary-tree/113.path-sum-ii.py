#
# @lc app=leetcode id=113 lang=python3
# @lcpr version=30307
#
# [113] Path Sum II
#
# https://leetcode.com/problems/path-sum-ii/description/
#
# algorithms
# Medium (61.69%)
# Likes:    8578
# Dislikes: 170
# Total Accepted:    1.1M
# Total Submissions: 1.8M
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22\n[1,2,3]\n5\n[1,2]\n0'
#
# Given the root of a binary tree and an integer targetSum, return all
# root-to-leaf paths where the sum of the node values in the path equals
# targetSum. Each path should be returned as a list of the node values, not
# node references.
# 
# A root-to-leaf path is a path starting from the root and ending at any leaf
# node. A leaf is a node with no children.
# 
# 
# Example 1:
# 
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: [[5,4,11,2],[5,8,4,5]]
# Explanation: There are two paths whose sum equals targetSum:
# 5 + 4 + 11 + 2 = 22
# 5 + 8 + 4 + 5 = 22
# 
# 
# Example 2:
# 
# Input: root = [1,2,3], targetSum = 5
# Output: []
# 
# 
# Example 3:
# 
# Input: root = [1,2], targetSum = 0
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000
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
class Solution:
    # 把 self.path 和 self.result 放在 __init__ 里，是在告诉阅读代码的人：
    #“这两个变量是这个类的‘公共看板’。”
    #它们不是某个函数的临时局部变量，而是属于整个 Solution 对象的。这样你在写 traversal 函数时，使用 self.path 就会显得理所当然。
    #用self.变量也同样可以表示全局变量, 放在 __init__：是为了代码结构清晰，符合面向对象编程的习惯, 即属性应该在构造函数里定义, 只在创建对象时执行一次
    # 但要注意, 在一定不要只在 `__init__` 里写 `self.result = []` 而主函数不管. 因为如果主函数不清空.clear()一下, 会累加之前测试用例的结果
    def __init__(self):
        # global variable全局变量
        self.result = [] # 最终要返回的大列表：[[5,4,11,2], [5,8,4,5]]
        self.path = [] # 记录当前走过的路径：[5, 4, 11, 2]

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.result.clear() # 或者是 self.result = []
        self.path.clear() # 或者是 self.path = []
        # 主函数里写.clear()的原因: 
        #1. 防御性编程：防止上面提到的“跨用例污染”。
        #2. 原地操作：.clear() 会清空原列表的内容但保留列表对象本身, 原地清空。对象还是原来那个，但内容被抹除。
        # 虽然在刷题时 self.result = []（重新赋值,指向一个新对象。）和 self.result.clear() 效果一样，但在大型工程中，如果别的地方也引用了这个列表，用 .clear() 能保证引用的同步性。
        if not root:
            return []
        # 核心：根节点必须手动处理（因为它没有“爸爸”在递归前处理它）
        self.path.append(root.val) # 根节点先入队
        self.traversal(root, targetSum - root.val) # 带着剩余的钱开启递归
        return self.result
    
    # 递归法, 无论前中后序, 无中
    def traversal(self, cur, count) -> None:
        # base case
        if not cur.left and not cur.right and count == 0:
            self.result.append(self.path[:]) # 找到了！把当前的 path 复制一份放进 result
            # 注意：必须用 [:] 复制一份, 并生成一个新的列表对象，放进result的是这个独立的复印件;否则 result 里的 path 会随回溯, 不断pop()弹出节点, 最后变为空列表
            return # return只是结束当前cur这一层, 但并不是函数就结束了, 会翻篇到上一层调用递归的地方, 把递归函数后的两行跑了`count += cur.left.val` 和 `self.path.pop()`
        
        # 单层逻辑
        # 左
        if cur.left:
            # --- 1. 递归前：准备 ---
            self.path.append(cur.left.val) # [处理]：把左孩子塞进路径
            count -= cur.left.val # [处理]：从余额里减去左孩子的值
             # --- 2. 递归中：下楼 ---
            self.traversal(cur.left, count) # [递归]：让左孩子去处理它自己的子树
             # --- 3. 递归后：连续回溯 ---
            count += cur.left.val  # [回溯]：把左孩子的值加回来
            self.path.pop()  # [回溯]：把路径里的左孩子一个一个弹出去，恢复现场, 保证回到父节点时路径是干净的
            # 后面没代码了，于是自动 return, 回到上一层, 连续执行回溯
            # 回溯并不是你手动写了一个循环去 pop，而是利用函数返回的自然特性，带动了每一层代码末尾那两行“善后逻辑”的生效
        # 右
        if cur.right:
            self.path.append(cur.right.val)
            count -= cur.right.val
            self.traversal(cur.right, count)
            count += cur.right.val
            self.path.pop()


# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [5,4,8,11,null,13,4,7,2,null,null,5,1]\n22\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n5\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n0\n
# @lcpr case=end

#

