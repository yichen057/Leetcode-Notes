#
# @lc app=leetcode id=797 lang=python3
# @lcpr version=30403
#
# [797] All Paths From Source to Target
#
# https://leetcode.com/problems/all-paths-from-source-to-target/description/
#
# algorithms
# Medium (83.60%)
# Likes:    7643
# Dislikes: 153
# Total Accepted:    690.5K
# Total Submissions: 826K
# Testcase Example:  '[[1,2],[3],[3],[]]\n[[4,3,1],[3,2,4],[3],[4],[]]'
#
# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find
# all possible paths from node 0 to node n - 1 and return them in any order.
# 
# The graph is given as follows: graph[i] is a list of all nodes you can visit
# from node i (i.e., there is a directed edge from node i to node
# graph[i][j]).
# 
# 
# Example 1:
# 
# Input: graph = [[1,2],[3],[3],[]]
# Output: [[0,1,3],[0,2,3]]
# Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
# 
# 
# Example 2:
# 
# Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
# Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
# 
# 
# 
# Constraints:
# 
# 
# n == graph.length
# 2 <= n <= 15
# 0 <= graph[i][j] < n
# graph[i][j] != i (i.e., there will be no self-loops).
# All the elements of graph[i] are unique.
# The input graph is guaranteed to be a DAG.
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
#from common.node import *

# @lc code=start
# 题目明确说了这是一个 DAG（有向无环图）。有向: 箭头是单向的。无环：你永远不会绕回到已经走过的路上。所以这道题不需要像一般的图题目那样使用 visited[] 数组来记录走过的点。
# 这是一个非常深刻的问题！通常我们处理“图”的题目（比如 LC 200 岛屿数量，或者找两个人的社交距离），如果不加 HashMap 或 set 去记录 visited（访问过的节点），程序就会因为“ A 连 B，B 又连 A”而陷入无限死循环。
# 但这一题确实不需要，让我们来拆解其中的缘由。
# 1. 为什么本题不需要 HashMap (Visited Set)?
# 通常在图论中，visited 集合是为了防止环路（Cycle）。
# 核心理由：题目性质是 DAG
# 题目明确说明这是一个 DAG（Directed Acyclic Graph，有向无环图）。
# • 有向：路径是单行道。
# • 无环：你永远不可能从一个点出发，绕一圈回到原点。
# 既然没有环，DFS 就像走一棵不断向下延伸的树，它永远不会撞见自己。因此，我们不需要额外花内存去记录哪个点走过，因为我们不可能走回头路。
# 额外理由：我们需要重复经过某个点
# 本题的要求是找“所有”路径。
# • 假设节点 0 可以到 1 和 2，而 1 和 2 都能到节点 3。
# • 路径 1: 0 -> 1 -> 3
# • 路径 2: 0 -> 2 -> 3 如果用了 visited 并在访问过 3 之后就不再访问，那么我们就只能找到其中一条路径，而丢掉了另一条。
# 2. 复杂度分析 (新手友好版)
# 对于这种“找出所有可能”的题目，复杂度通常都比较高，因为答案的数量本身就是指数级的。
# 时间复杂度：O(2^n * n)
# • 路径的数量 (2^n)：在一个有 n 个节点的图中，从起点到终点最多可能有 2^(n-2) 条路径（想象每个中间节点都有“选”或“不选”两种可能）。
# • 拷贝路径的操作 (n)：每当我们找到一条成功的路径时，我们需要执行 res.append(list(path))。这个 list(path) 的拷贝操作需要遍历整个路径，最长路径长度是 n。
# • 合起来：就是 O(2^n * n)。
# 白话讲解：这就像是在一个有很多分叉的迷宫里，总共有成千上万种走法，你每走通一种，还得把这一长串的路线抄一遍到笔记本上。
# 空间复杂度：O(n)
# 这里我们不计算用来存放最终答案的 res 空间（因为那是题目要求的产出）。
# • 递归栈深度 (n)：DFS 最深会递归到 n 层（即路径从 0 到 n-1 经过了所有节点）。每一层递归都会占用一点系统内存。
# • 路径列表 path (n)：我们维持的那个 path 变量，最长也就装下 n 个节点。
# • 合起来：就是 O(n)。
# 白话讲解：虽然最后你可能找到了上千条路径，但在任意一个瞬间，你手里其实只有一本笔记本（path）和一套正在进行的探险任务（递归栈），它们的规模都只取决于图中有多少个房间。
# 3. 学习小结
# • 什么时候要 HashMap？ 当图可能有“环”，且你只需要知道“能不能到”或者“最短是多少”时。
# • 什么时候不要？ 当图是 DAG（无环），且你需要“所有路径”时。
# 方法一: DFS递归
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
         # 1. 确定终点是谁
        # graph 的长度如果是 4，那么节点就是 0, 1, 2, 3。终点就是索引 3。
        target = len(graph) - 1
        res = []
        
        # 2. 定义 DFS 探险函数
        # curr_node: 你现在站在哪个房间（节点）
        # path: 记录当前正在走的这一条路径。
        def dfs(curr_node, path):
            # 3. 检查：我是不是到终点了？
            if curr_node == target:
                res.append(list(path)) # list(path)是副本, 否则后面path的变化这里的path也会跟着变, 我们需要存下这一刻的“快照”
                return # 在递归中，return 的作用是结束当前的函数调用，回到上一层调用它的地方。
            # 当你在 dfs(target, path) 里执行了 return，程序会立刻跳回到上一层（即 target 的父节点那一层）执行 dfs(neighbor, path) 的下一行代码。
            # 下一行代码正是 path.pop()。所以，return 并不是结束了整个找路的过程，它只是触发了上一层的回溯动作。

            # 4. 还没到终点？看看当前房间的门后都通往哪
            # graph[curr_node] 就像是房间里的指示牌，写着 [1, 2]
            for neighbor in graph[curr_node]:
                # 5. 决定进 neighbor 这个门
                path.append(neighbor)
                # 6. 递归：进门，重复上面的过程（看是不是终点，不是就继续找邻居）
                dfs(neighbor, path)
                # print("pop前", path)
                # 7. 【最关键的回溯】
                # 当上面的 dfs 执行完返回了，说明从 neighbor 出发的所有路都试过了。
                # 现在你要回到当前房间 curr_node，准备试下一个门。
                # 所以必须把小本本上最后那个房间号擦掉（pop）。
                path.pop() # 注意: backtracking回溯, 递归返回后，弹出 path 最后的元素（回溯）, pop() 默认删除并返回列表中的最后一个元素。
                # pop 紧跟在dfs之后, 每当结束一个递归, 就会执行一次pop, 即递归后每返回退一层楼, 就pop掉一个
                # print("pop后", path)
        
        # 8. 探险开始！从 0 号房间出发，本本上先写个 [0]
        dfs(0, [0]) # start to call dfs() function
        return res
    
# 方法二: DFS非递归(迭代法)
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        res = []
        # stack里存的是(当前节点, 到达该节点的路径)
        stack = [(0, [0])]

        while stack:
            curr_node, path = stack.pop()
            
            # 如果到达终点
            if curr_node == target:
                res.append(path)
                continue # 终点房间是不需要再看“门后通向哪”的（因为它没有邻居，或者我们不需要从终点再往后走）, 可以去处理栈里的下一个任务。continue 是为了告诉程序：“这个分支任务结束了，别磨叽，去栈里拿下一个任务。

            # 遍历邻居（为了保持和递归一样的顺序，可以逆序压栈，但这不影响结果正确性）
            for neighbor in graph[curr_node]:
                # 注意：这里直接新建路径列表 [curr_path + [neighbor]], path + [neighbor] 每次都在创建新列表，这会消耗更多的内存（空间换逻辑简洁）
                # path + [neighbor] 是为了给每个任务分配“独立内存”，避免互相干扰，从而省去了手动回溯的麻烦。这样每条路径都是独立的，不需要手动 pop 回溯
                stack.append((neighbor, path + [neighbor]))
                
        return res




'''
path 变化：[0] -> [0,1] -> [0,1,3] (存入) -> [0,1] -> [0] -> [0,2] -> [0,2,3] (存入)
手动走一遍这个 test_graph = [[1, 2], [3], [3], []] 的流程，能让你彻底理解递归栈和回溯。
为了方便理解，我们将这个图想象成 4 个房间：
• 0 号房通往 1 和 2
• 1 号房通往 3（终点）
• 2 号房通往 3（终点）
• 3 号房是终点
追踪日志：探险全过程
我们将 path 的变化和代码的执行行号结合起来看：
第一阶段：从起点出发
1. 调用 dfs(0, [0]): • curr_node 是 0，path 是 [0]。 • 0 不是终点 3。 • 进入循环：0 的邻居有 [1, 2]。
第二阶段：探索第一条支路 (0 -> 1)
1. 选择邻居 1: • 执行 path.append(1)，此时 path = [0, 1]。 • 递归调用 dfs(1, [0, 1])。
2. 在 1 号房: • 1 不是终点 3。 • 进入循环：1 的邻居有 [3]。
3. 选择邻居 3: • 执行 path.append(3)，此时 path = [0, 1, 3]。 • 递归调用 dfs(3, [0, 1, 3])。
第三阶段：到达终点 & 第一次回溯
1. 在 3 号房 (终点!): • curr_node == target (3 == 3) 成立！ • res.append(list([0, 1, 3])) -> 大仓库收纳第一条路径。 • 执行 return：这个 return 让程序跳回调用它的地方（即 1 号房的 dfs(3) 那一行）。
2. 回到 1 号房: • 刚才执行完 dfs(3)，下一行是 path.pop()。 • Pop! 删掉 3，此时 path = [0, 1]。 • 1 号房的邻居 [3] 已经遍历完了，for 循环结束。 • 1 号房任务完成，自动返回 0 号房。
第四阶段：回到起点 & 探索第二条支路 (0 -> 2)
1. 回到 0 号房: • 刚才执行完 dfs(1)，下一行是 path.pop()。 • Pop! 删掉 1，此时 path = [0]。 • 继续 0 号房的循环：下一个邻居是 2。
2. 选择邻居 2: • 执行 path.append(2)，此时 path = [0, 2]。 • 递归调用 dfs(2, [0, 2])。
3. 在 2 号房: • 2 不是终点 3。 • 进入循环：2 的邻居有 [3]。
4. 选择邻居 3: • 执行 path.append(3)，此时 path = [0, 2, 3]。 • 递归调用 dfs(3, [0, 2, 3])。
第五阶段：再次到达终点 & 扫尾
1. 再次在 3 号房: • 成立！res.append(list([0, 2, 3])) -> 大仓库收纳第二条路径。 • 执行 return 返回到 2 号房。
2. 回到 2 号房: • 执行 path.pop() -> 删掉 3，path = [0, 2]。 • 2 号房循环结束，返回 0 号房。
3. 最后回到 0 号房: • 执行 path.pop() -> 删掉 2，path = [0]。 • 0 号房所有邻居遍历完毕。 • 全剧终！
总结：你的 print(path) 会输出什么？
如果你按照截图里的代码运行，你的控制台会打印出：
1. [0, 1] （这是从终点 3 回到 1 号房后 pop 完打印的）
2. [0] （这是从 1 号房回到 0 号房后 pop 完打印的）
3. [0, 2] （这是从终点 3 回到 2 号房后 pop 完打印的）
4. [0] （这是从 2 号房回到 0 号房后 pop 完打印的）
为什么这样思考问题？
这种思维方式叫**“分治”**：你不需要全局掌控所有路径，你只需要在每一个节点（每一个函数层）做好三件事：
1. 记录（我是谁，我要去哪）
2. 递归（把剩下的任务交给下一层）
3. 清理（回溯，假装我没来过，不影响接下来的搜索）
就像你在刷 LeetCode 已经 80 多题了，你会发现很多题（尤其是 DFS/回溯）都可以套用这个“进门、干活、出门”的逻辑。


通过 test_graph = [[1, 2], [3], [3], []] 来走一遍**非递归（迭代法）**的流程，你会发现它就像是在管理一个“待办事项清单”。
这里的 Stack（栈） 就是你的清单，遵循后进先出 (LIFO) 的原则。
追踪日志：迭代法全过程
初始状态：
• target = 3
• res = []
• stack = [(0, [0])] （任务：从 0 开始，目前路径 [0]）
第一轮 While 循环
1. Pop 栈顶：取出 (0, [0])。
2. 检查：0 不是 3。
3. 看邻居：0 的邻居是 [1, 2]。
4. 压栈 (Push)： • 邻居 1：把 (1, [0, 1]) 塞进栈。 • 邻居 2：把 (2, [0, 2]) 塞进栈。
• 当前栈状态：[(1, [0, 1]), (2, [0, 2])]（注意：2 是后进去的，下次先找它）。
第二轮 While 循环
1. Pop 栈顶：取出 (2, [0, 2])。
2. 检查：2 不是 3。
3. 看邻居：2 的邻居是 [3]。
4. 压栈 (Push)： • 邻居 3：把 (3, [0, 2, 3]) 塞进栈。
• 当前栈状态：[(1, [0, 1]), (3, [0, 2, 3])]。
第三轮 While 循环
1. Pop 栈顶：取出 (3, [0, 2, 3])。
2. 检查：3 == 3！找到一条路径！
3. 动作：res.append([0, 2, 3])。
4. Continue：跳过剩下的代码，不看邻居了，直接进下一轮循环。
• 当前栈状态：[(1, [0, 1])]。
第四轮 While 循环
1. Pop 栈顶：取出 (1, [0, 1])。
2. 检查：1 不是 3。
3. 看邻居：1 的邻居是 [3]。
4. 压栈 (Push)： • 邻居 3：把 (3, [0, 1, 3]) 塞进栈。
• 当前栈状态：[(3, [0, 1, 3])]。
第五轮 While 循环
1. Pop 栈顶：取出 (3, [0, 1, 3])。
2. 检查：3 == 3！又找到一条路径！
3. 动作：res.append([0, 1, 3])。
4. Continue：结束本次循环。
• 当前栈状态：[] (空了)。
最后结果：res = [[0, 2, 3], [0, 1, 3]]。
深度解析：为什么不用 pop 回溯？
请盯着这行代码看：
stack.append((neighbor, path + [neighbor]))
• 重点 1：数据隔离 在“第三轮”中，我们处理的是 (3, [0, 2, 3])。这时候栈里还躺着一个 (1, [0, 1])。 因为 [0, 2, 3] 是通过 path + [3] 产生的一个全新列表，它和栈里那个 [0, 1] 没有任何血缘关系。 当你把 [0, 2, 3] 扔进结果集时，[0, 1] 依然安安静静地躺在栈里，维持着它原本的样子。
• 重点 2：不需要“还原” 在递归写法里，你必须 pop 是因为你只有一本日记本，你得擦了才能写下一条路。 在迭代法里，你每次压栈都相当于给邻居发了一份复印好的路线图。邻居在复印件上怎么涂鸦，都不会弄脏你手里的原件。
总结
1. continue 是为了告诉程序：“这个分支任务结束了，别磨叽，去栈里拿下一个任务。”
2. path + [neighbor] 是为了给每个任务分配“独立内存”，避免互相干扰，从而省去了手动回溯的麻烦。
这种迭代法在处理深度巨大的图时非常安全（不会报 RecursionError），是后端开发中处理大规模数据流时更稳健的选择。既然你有 8 年产品经验，现在转码研究这些逻辑，你会发现这其实和业务流控的逻辑非常像！加油！
'''

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    test_graph = [[1, 2], [3], [3], []]
    result = solution.allPathsSourceTarget(test_graph)
    print("最终结果是:", result)



#
# @lcpr case=start
# [[1,2],[3],[3],[]]\n
# @lcpr case=end

# @lcpr case=start
# [[4,3,1],[3,2,4],[3],[4],[]]\n
# @lcpr case=end

#

