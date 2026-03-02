#
# @lc app=leetcode id=701 lang=python3
#
# [701] Insert into a Binary Search Tree
#
# https://leetcode.com/problems/insert-into-a-binary-search-tree/description/
#
# algorithms
# Medium (73.36%)
# Likes:    6410
# Dislikes: 187
# Total Accepted:    833K
# Total Submissions: 1.1M
# Testcase Example:  '[4,2,7,1,3]\n5'
#
# You are given the root node of a binary search tree (BST) and a value to
# insert into the tree. Return the root node of the BST after the insertion. It
# is guaranteed that the new value does not exist in the original BST.
# 
# Notice that there may exist multiple valid ways for the insertion, as long as
# the tree remains a BST after insertion. You can return any of them.
# 
# 
# Example 1:
# 
# 
# Input: root = [4,2,7,1,3], val = 5
# Output: [4,2,7,1,3,5]
# Explanation: Another accepted tree is:
# 
# 
# 
# Example 2:
# 
# 
# Input: root = [40,20,60,10,30,50,70], val = 25
# Output: [40,20,60,10,30,50,70,null,null,25]
# 
# 
# Example 3:
# 
# 
# Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
# Output: [4,2,7,1,3,5]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree will be in the range [0, 10^4].
# -10^8 <= Node.val <= 10^8
# All the values Node.val are unique.
# -10^8 <= val <= 10^8
# It's guaranteed that val does not exist in the original BST.
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 方法一: 递归法
# 本题无需改变树的结构, 只要遇到空节点插入节点即可
# 无需遍历整棵树, BST是有方向的, 根据插入元素的值决定递归方向
# class Solution:
#     def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
#         # base case:
#         if root is None: # # 如果根节点为空，创建新节点作为根节点并返回. 当遇到叶子节点为空, 则在此处插入节点, 再将新插入的节点向上一层返回
#             node = TreeNode(val)
#             return node
        
#         # 向左遍历递归
#         if val < root.val:
#             root.left = self.insertIntoBST(root.left, val)

#         # 向右遍历递归
#         if val > root.val:
#             root.right = self.insertIntoBST(root.right,val)

#         return root
# 方法二: 迭代法
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        cur = root # 在二叉树的操作中，将 root 赋值给 cur（或其他辅助指针）, 是为了保护“树根”以便最后返回
        # 题目要求返回的是整棵树的根节点。
        # 在迭代过程中，我们需要不断地向下移动（例如 cur = cur.left）来寻找插入位置。
        # 如果直接使用 root 变量进行移动，当循环结束时，root 指针可能已经指向了树的底层节点甚至 None。
        # 后果： 你会“弄丢”整棵树的入口，无法返回题目要求的完整结果。
        while cur is not None:
            if val < cur.val:
                if not cur.left: # 如果此时父节点的左子树为空, 则在此插入新节点, 再向上返回给当前节点的左子树
                    cur.left = TreeNode(val)
                    return root
                else:
                    cur = cur.left
            elif val > cur.val:
                if not cur.right:
                    cur.right = TreeNode(val)
                    return root
                else:
                    cur = cur.right
                    
# 遍历与引用的分离
# 在算法实现中，通常会将变量的功能进行分离：
# root： 负责持有这棵树的句柄（Handle），作为常量或固定引用存在。
# cur (Current)： 负责执行具体的扫描任务，就像一个在树林里带路的“向导”，它会不断变换位置。

# @lc code=end

