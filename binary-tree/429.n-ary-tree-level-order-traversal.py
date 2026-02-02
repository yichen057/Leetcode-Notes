#
# @lc app=leetcode id=429 lang=python3
#
# [429] N-ary Tree Level Order Traversal
#
# https://leetcode.com/problems/n-ary-tree-level-order-traversal/description/
#
# algorithms
# Medium (71.31%)
# Likes:    3738
# Dislikes: 144
# Total Accepted:    360K
# Total Submissions: 503.9K
# Testcase Example:  '[1,null,3,2,4,null,5,6]'
#
# Given an n-ary tree, return the level order traversal of its nodes' values.
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
# Output: [[1],[3,2,4],[5,6]]
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: root =
# [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
# 
# 
# 
# Constraints:
# 
# 
# The height of the n-ary tree is less than or equal to 1000
# The total number of nodes is between [0, 10^4]
# 
# 
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
    # val: Optional[int] = None: Optional[int] 表示 “int 或 None”。默认值设为 None，意味着可以不传 val，或者暂时没有值。这样更通用：有些节点可能在构建时先占位，之后再赋值
    # children: Optional[List['Node']] = None: Optional[List['Node']] 表示 “子节点列表或 None”。默认 None 避免用可变默认参数（如 []）带来的共享问题。如果写成 children=[]，所有节点会共享同一个列表，这是 Python 的坑。
        self.val = val
        self.children = children
"""
# 注意: 本题在定义node时, 属性有两个: .val和.children
# 这道题依旧是模板题，只不过一个节点有多个孩子了
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
    # 本题中root给的类型是 Node，不是二叉树的 TreeNode。签名写 root: 'Node' 是对应该题的结点类；TreeNode 只用于二叉树题。
    # 'Node' 用引号是“前向引用”（类还没真正定义时先引用它）。
    # 是否写成 Optional[Node] 取决于平台签名习惯：这里根可能为 None，但 LeetCode 模板通常不写 Optional，你也可以改成 Optional['Node']，不影响解题。
        if not root:
            return []
        
        queue = collections.deque([root])
        result = []

        while queue:
            level = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                level.append(cur.val)

                for child in cur.children:
                    queue.append(child)

            result.append(level)

        return result
    
# @lc code=end

