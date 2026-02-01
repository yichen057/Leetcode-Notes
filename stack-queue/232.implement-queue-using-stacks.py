#
# @lc app=leetcode id=232 lang=python3
# @lcpr version=30305
#
# [232] Implement Queue using Stacks
#
# https://leetcode.com/problems/implement-queue-using-stacks/description/
#
# algorithms
# Easy (69.09%)
# Likes:    8490
# Dislikes: 481
# Total Accepted:    1.4M
# Total Submissions: 2M
# Testcase Example:  '["MyQueue","push","push","peek","pop","empty"]\n[[],[1],[2],[],[],[]]'
#
# Implement a first in first out (FIFO) queue using only two stacks. The
# implemented queue should support all the functions of a normal queue (push,
# peek, pop, and empty).
# 
# Implement the MyQueue class:
# 
# 
# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.
# 
# 
# Notes:
# 
# 
# You must use only standard operations of a stack, which means only push to
# top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, the stack may not be supported natively. You may
# simulate a stack using a list or deque (double-ended queue) as long as you
# use only a stack's standard operations.
# 
# 
# 
# Example 1:
# 
# Input
# ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 1, 1, false]
# 
# Explanation
# MyQueue myQueue = new MyQueue();
# myQueue.push(1); // queue is: [1]
# myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
# myQueue.peek(); // return 1
# myQueue.pop(); // return 1, queue is [2]
# myQueue.empty(); // return false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= x <= 9
# At most 100 calls will be made to push, pop, peek, and empty.
# All the calls to pop and peek are valid.
# 
# 
# 
# Follow-up: Can you implement the queue such that each operation is amortized
# O(1) time complexity? In other words, performing n operations will take
# overall O(n) time even if one of those operations may take longer.
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class MyQueue:
    # “栈”是抽象概念，底层可以用 list、deque，甚至自己实现的数组/链表。在 Python 刷题里，最常用的是直接用 list 来当栈。
# 使用栈实现队列的下列操作：

# push(x) -- 将一个元素放入队列的尾部。
# pop() -- 从队列首部移除元素。
# peek() -- 返回队列首部的元素。
# empty() -- 返回队列是否为空。

# Queue: 先进先出
    def __init__(self):
        """
        in 主要负责push, out 主要负责pop
        stack_in（输入栈）：只负责接收新来的元素。相当于“队尾”。
        stack_out（输出栈）：只负责提供要出去的元素。相当于“队头”。
        """
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        """
        有新元素进来，就往in里面push
        """
        self.stack_in.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.empty(): # self.empty() 是判断整个队列是否为空，所以应同时判断 stack_in 和 stack_out 两个栈都为空
            return None
        
        if self.stack_out:
            return self.stack_out.pop()
        # pop() 是 Python list 的方法，常用来当栈的 “弹出栈顶”。
        # 还能用这些数据结构当栈：
        # collections.deque：也有 append / pop，更适合频繁从两端操作
        # 自己封装的栈类（内部用 list 或 deque）
        # queue.LifoQueue：线程安全的栈（一般刷题不用）
        # 总结：LeetCode 里最常见就是 list 或 deque
        else: # stack_out is empty
            # 两种循环方式均可, 都是 O(n) 次 pop/append。Python 层面一般更推荐 while self.stack_in:，代码更直观，也不会反复计算 len 的范围。
            # for i in range(len(self.stack_in)):
            #     self.stack_out.append(self.stack_in.pop())
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()
        
    def peek(self) -> int: # peek的目的是看一眼, 然后假装没动过
        """
        Get the front element.查询数值
        """
        result = self.pop() # 直接使用已有的pop函数, pop函数最终是从stack_out出去的元素
        self.stack_out.append(result) # 秉着queue"先进先出"的顺序不被打乱, 从哪里拿出来的，就必须放回哪里去。
        return result

    def empty(self) -> bool:
        """
        只要in或者out有元素，说明队列不为空
        """
        return not (self.stack_in or self.stack_out)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# ["MyQueue","push","push","peek","pop","empty"]\n[[],[1],[2],[],[],[]]\n
# @lcpr case=end

#

