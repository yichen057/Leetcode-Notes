#
# @lc app=leetcode id=102 lang=python3
# @lcpr version=30307
#
# [102] Binary Tree Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (72.01%)
# Likes:    16864
# Dislikes: 366
# Total Accepted:    3.2M
# Total Submissions: 4.5M
# Testcase Example:  '[3,9,20,null,null,15,7]\n[1]\n[]'
#
# Given the root of a binary tree, return the level order traversal of its
# nodes' values. (i.e., from left to right, level by level).
# 
# 
# Example 1:
# 
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# 
# 
# Example 2:
# 
# Input: root = [1]
# Output: [[1]]
# 
# 
# Example 3:
# 
# Input: root = []
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 2000].
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
# 上述为声明了一个类TreeNode, 并初始化做了构造函数, 定义了节点产生时的默认状态:  val=0 /left=None /right=None

# 如果使用的是 `collections.deque`，记住这四个最核心的操作就够了：
# - **入队（尾部）**: `queue.append(node)`
# - **出队（头部）**: `node = queue.popleft()`  （**这就是你问的那个 `cur`**）
# - **查看队首（不弹出）**: `first_node = queue[0]`
# - **查看队尾（不弹出）**: `last_node = queue[-1]`
# 层序遍历法: 是一层一层地“扫描”，先扫完第一层，再扫第二层
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    # root 是 TreeNode 类的一个实例（Instance）, 虽然它叫 root（根），但它本质上和你后面遍历到的 cur、node 是同一种东西，只是因为它排在最前面，是我们抓取整棵树的“入口”，所以给了它一个特殊的名字叫 root
    # root有三个属性: 1) 数据 (val)：比如数字 1; 2)左指针 (left)：指向左下方的另一个盒子（对象）; 3)右指针 (right)：指向右下方的另一个盒子（对象）
    # root是变量名。 Optional[TreeNode]: 这是类型提示（Type Hint）。它的意思是：root 这个变量，要么是 TreeNode 类型的对象，要么是 None（空）。它绝对不是一个整数（int），也不是一个列表（list）
        if not root:# 判断root是否为空, 还可以写为: if root is None:明确判断是否为None
            return []
        queue = collections.deque([root]) # queue 队列：它是一个“缓冲区”。当你把第n层的节点一个个从队首取出时，你同时把它们的第 n+1 层孩子节点一个个塞进队尾
        # collections.deque() 需要一个可迭代对象作为初始元素集合。root是单个节点，不可迭代，所以要用 [root] 把它包装成一个列表，表示“队列里先放一个元素 root”。
        # 等价写法还有：queue = collections.deque(); queue.append(root). 如果 root 可能是 None，通常还会先判断再入队。
        # 虽然deque功能多（它是双端的），但因为它做“队首弹出”这个动作比list快太多了，所以 Python 程序员约定俗成: 只要是在 Python 里写算法题需要用到队列，统统使用collections.deque
        # Python 有一个库叫 queue，里面有个类叫 Queue, 不用它是因为: 它主要是给多线程编程用的。为了保证多线程安全，它加了很多“锁”的机制，导致它运行起来非常慢。在 LeetCode 这种单线程算法题里，用它是累赘
        # 你在做什么：你在实现一个队列（Queue）。你用的什么：你用的是双端队列（Deque）。为什么这么写：因为 Python 的 deque 是实现队列最快的方式，我们就只用它的 append（尾部进）和 popleft（头部出）这两个功能，假装它是一个普通的队列
        result = []
        while queue:
            level = [] # level 数组：它的生命周期非常短，只负责收集当前这一层（第n层）所有节点的值。一旦这一层循环结束，level 就会被装进结果大列表 res 中，然后被清空重置。
            for _ in range(len(queue)): # 在 Python 中，不能写 while(size--). Python 不支持 -- 或 ++ 运算符, 在 Python 中，必须明确写成 size -= 1。
                # range 在进入循环前，对 len(queue) 做了一次“快照”（Snapshot), 先计算参数len(range), 然后生成迭代器, 然后循环的次数就在这一刻被锁定了
                # range() 是由 C 语言实现的优化迭代器，通常比手动维护一个 while 计数器稍微快一点. 用python写while的话: while size>0: ..... size -= 1
                cur = queue.popleft() # 取值+出队一行搞定; Python 的 deque 没有 front() 方法; TreeNode 对象没有 pop 方法
                level.append(cur.val) # level.append(...)存储的是数字
                if cur.left: # 如果左孩子不为空
                    queue.append(cur.left) # 当前节点cur和它的左右孩子都不在同一层, cur.left 和 cur.right 是第 N+1 层的节点。它们不能混进第 N 层的 level 结果里。它们必须去 queue（候车室） 排队，等待下一轮 for 循环（下一层）开始时，才能变成主角。
                    # 进 level：是因为它是现在的成果（数值）; 进 queue：是因为它是未来的任务（对象），需要排队等下一轮处理。
                    # queue.append(...): 必须存完整的节点对象（TreeNode）。因为只有存了对象，下一轮我们才能通过它访问 node.val、node.left 和 node.right
                if cur.right:
                    queue.append(cur.right)
            result.append(level)
        return result

# 递归法
#在递归过程中，虽然程序是“一路深钻”到底的（比如先处理完最左边的一条线），但由于我们随身携带了 level 这个深度信息，每到一个新节点，我们都能通过 levels[level] 准确地把它归类到它所属的那一层去。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        levels = [] # levels 是一个二维列表。它的**索引（Index）**代表树的深度（层数）。它的元素是另一个列表，存放着对应层级的所有节点值。例如：levels[0] 存放第一层的值，levels[1] 存放第二层的值。
        
        # 定义在函数内部，不需要 self. 如果是写在 levelOrder 外面（作为类的方法） -> 必须加 self
        # 这里的 node 和 level 没写类型，完全没问题！# Python 解释器会自动处理，只要你传对了就行。def traverse(node, level):
        def traverse(node: Optional[TreeNode], level:int) -> None:
        # 参数 level 是一个整数, 用来访问列表levels的下标(索引),记录了当前递归到了哪一层。这是递归法能“找对位置”的关键; 
        # node 通常是 Tree Node 类的实例, 它是一个object对象, 负责提供数据和路径, 有以下属性：node.val（数据），node.left（左指针），node.right（右指针）,它不是数字索引。你不能用它来做加减法（比如你不能写 node + 1）
# Optional[TreeNode] 在 Python 的 typing 模块里的定义其实等同于： Union[TreeNode, None] （翻译：这个参数要么是 TreeNode，要么是 None）
# 如果当前的 node 是一个叶子节点（比如它下面没有左孩子了），那么 node.left 的值就是 None。 当你把 None 传给 traverse 函数时，参数 node 就接收到了 None。

# 如果你写 node: TreeNode，意思是：“我保证传进来的永远是一个真正的节点对象”。

# 如果你写 node: Optional[TreeNode]，意思是：“传进来的可能是个节点对象，但也可能是 None”。

# 显然，后者才符合事实
            if not node:
                return
            if len(levels) == level: # 当你第一次进入一个新的深度时，levels 的长度会等于当前的 level。此时，代码会往 levels 里添加一个空列表，为这一层“开辟空间”。
                levels.append([])

            levels[level].append(node.val) # 直接利用 level 作为索引，把当前节点的值放进对应层级的列表里。
            traverse(node.left, level+1) # 向左递归
            traverse(node.right, level +1) # 向右递归
        
        # 调用时也不需要 self
        traverse (root, 0)
        return levels

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

