#
# @lc app=leetcode id=225 lang=python3
# @lcpr version=30305
#
# [225] Implement Stack using Queues
#
# https://leetcode.com/problems/implement-stack-using-queues/description/
#
# algorithms
# Easy (69.00%)
# Likes:    6830
# Dislikes: 1278
# Total Accepted:    1.1M
# Total Submissions: 1.6M
# Testcase Example:  '["MyStack","push","push","top","pop","empty"]\n[[],[1],[2],[],[],[]]'
#
# Implement a last-in-first-out (LIFO) stack using only two queues. The
# implemented stack should support all the functions of a normal stack (push,
# top, pop, and empty).
# 
# Implement the MyStack class:
# 
# 
# void push(int x) Pushes element x to the top of the stack.
# int pop() Removes the element on the top of the stack and returns it.
# int top() Returns the element on the top of the stack.
# boolean empty() Returns true if the stack is empty, false otherwise.
# 
# 
# Notes:
# 
# 
# You must use only standard operations of a queue, which means that only push
# to back, peek/pop from front, size and is empty operations are valid.
# Depending on your language, the queue may not be supported natively. You may
# simulate a queue using a list or deque (double-ended queue) as long as you
# use only a queue's standard operations.
# 
# 
# 
# Example 1:
# 
# Input
# ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 2, 2, false]
# 
# Explanation
# MyStack myStack = new MyStack();
# myStack.push(1);
# myStack.push(2);
# myStack.top(); // return 2
# myStack.pop(); // return 2
# myStack.empty(); // return False
# 
# 
# 
# Constraints:
# 
# 
# 1 <= x <= 9
# At most 100 calls will be made to push, pop, top, and empty.
# All the calls to pop and top are valid.
# 
# 
# 
# Follow-up: Can you implement the stack using only one queue?
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# 使用队列实现栈的下列操作：

# push(x) -- 元素 x 入栈
# pop() -- 移除栈顶元素
# top() -- 获取栈顶元素
# empty() -- 返回栈是否为空
# 注意:

# 你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty 这些操作是合法的。
# 你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
# 你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）
# 这道题目就是用一个队列就够了。
# 一个队列在模拟栈弹出元素的时候只要将队列头部的元素（除了最后一个元素外） 重新添加到队列尾部，此时再去弹出元素就是栈的顺序了。
# self.que.xx：当你需要操作底层的数据容器（那个 list 或 deque）时。
# self.xx：当你需要复用你在这个类里写好的其他方法时
class MyStack:

    def __init__(self):
        self.que = deque()

    def push(self, x: int) -> None:
        self.que.append(x)

    def pop(self) -> int:
        if self.empty(): # 复用本题里写好的empty()方法
            return None
        # while(len(self.que) >1): 错误! 这个条件不会改变, 在循环里是 popleft() 然后 append()，队列长度始终不变，所以 len(self.que) > 1 一直为真，变成死循环
        for _ in range(len(self.que)-1):# 这里只能用for循环, 弹出size-1个元素, 使得想要pop的元素从队尾到队首
            self.que.append(self.que.popleft()) # 弹出的元素再重新加回到队列里
        return self.que.popleft() # 只有deque(双端队列)有popleft()这个方法; queue 用的是 get(); 
    # deque 是双端队列，支持两端操作。但题目要求你“只使用队列的标准操作”，也就是只用队尾入队、队首出队。所以虽然 deque.pop() 能从右边弹出，但在题目的约束下我们不该用它
    # list/stack用pop()移除并返回最后一个元素; dictionary用pop(key)=value, 移除并返回指定key的value;set用pop()随机返回一个元素, 因为集合是无序的;
    # deque用pop()移除最右边一个(尾部)
    
    def top(self) -> int:
        # 写法一: 
        # if self.empty():
        #     return None
        # return self.que[-1] # 将que尾部的元素先弹出
        # 写法二: 
        if self.empty():
            return None
        result = self.pop() # 复用 pop() 获取栈顶元素 (此时一定能取到值)
        # 理解变量和容器的关系: 当你执行 temp = self.que.popleft() 时，temp 这个变量就“抓住了”那个元素。 无论你之后拿这个元素去做了什么（比如把它放回队列、打印它、还是用它做计算），只要你没有把 temp 变量本身覆盖掉（比如写 temp = 0），它手里的那个东西就一直都在。
        self.que.append(result) # 将取出的元素重新添加回队列末尾（恢复原状）

        return result
        # 写法三：
        if self.empty():
            return None
        for i in range(len(self.que)-1):
            self.que.append(self.que.popleft())
        temp = self.que.popleft()
        self.que.append(temp)
        return temp

    def empty(self) -> bool:
        return not self.que
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# ["MyStack","push","push","top","pop","empty"]\n[[],[1],[2],[],[],[]]\n
# @lcpr case=end

#

