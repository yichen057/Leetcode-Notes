#
# @lc app=leetcode id=841 lang=python3
# @lcpr version=30403
#
# [841] Keys and Rooms
#
# https://leetcode.com/problems/keys-and-rooms/description/
#
# algorithms
# Medium (75.71%)
# Likes:    6693
# Dislikes: 303
# Total Accepted:    688.8K
# Total Submissions: 909.8K
# Testcase Example:  '[[1],[2],[3],[]]\n[[1,3],[3,0,1],[2],[0]]'
#
# There are n rooms labeled from 0 to n - 1 and all the rooms are locked except
# for room 0. Your goal is to visit all the rooms. However, you cannot enter a
# locked room without having its key.
# 
# When you visit a room, you may find a set of distinct keys in it. Each key
# has a number on it, denoting which room it unlocks, and you can take all of
# them with you to unlock the other rooms.
# 
# Given an array rooms where rooms[i] is the set of keys that you can obtain if
# you visited room i, return true if you can visit all the rooms, or false
# otherwise.
# 
# 
# Example 1:
# 
# Input: rooms = [[1],[2],[3],[]]
# Output: true
# Explanation: 
# We visit room 0 and pick up key 1.
# We then visit room 1 and pick up key 2.
# We then visit room 2 and pick up key 3.
# We then visit room 3.
# Since we were able to visit every room, we return true.
# 
# 
# Example 2:
# 
# Input: rooms = [[1,3],[3,0,1],[2],[0]]
# Output: false
# Explanation: We can not enter room number 2 since the only key that unlocks
# it is in that room.
# 
# 
# 
# Constraints:
# 
# 
# n == rooms.length
# 2 <= n <= 1000
# 0 <= rooms[i].length <= 1000
# 1 <= sum(rooms[i].length) <= 3000
# 0 <= rooms[i][j] < n
# All the values of rooms[i] are unique.
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# 你观察得很仔细！在处理图论问题时，“有向图 (Directed)” 和 “无向图 (Undirected)” 的区别确实非常关键。
# 针对你的两个疑问，我们从底层逻辑来拆解：
# 1. 为什么 LC 841 没提 Undirected Graph？
# 核心区别：钥匙是“单向”的
# • 本题逻辑 (Directed Graph)：你在房间 0 找到了房间 1 的钥匙，这意味着你可以从 0 \to 1。但这并不意味着房间 1 里面一定有回 0 的钥匙。
# • 无向图 (Undirected Graph)：如果这道题是无向图，那就意味着只要 0 和 1 之间有一扇门，你从 0 能去 1，从 1 就一定能回 0。
# 结论：这道题本质上是一个 有向图 (Directed Graph)。虽然如此，DFS 和 BFS 算法在处理“连通性（能不能走到）”时，代码逻辑对有向和无向图是通用的。唯一的区别在于：
# • 在无向图中，如果不加 visited 集合，你会在两个房间之间反复横跳（0 \to 1 \to 0 \to 1 \dots），瞬间爆栈。
# • 在本题（有向图）中，虽然不一定有回路，但为了效率和防止潜在的环路，visited 依然是必须的。
# 2. 这里用到 Hash Map 了吗？
# 在 Python 的实现中，我们用的是 visited = set()。虽然它叫 set（集合），但它的底层实现就是 Hash Table（哈希表）。
# 为什么这里用 set 而不是普通的 list？
# 这是一个非常重要的 Tradeoff（权衡）：
# 数据结构	检查 x in data 的时间复杂度	理由
# List (列表)	O(N)	需要从头到尾扫一遍，房间多了会非常慢。
# Set / Hash Map	O(1) (常数级)	通过哈希函数直接定位，速度极快。
# 在面试中你可以这样回答：
# “虽然我用的是 set 来记录已访问的房间，但其底层利用了 Hash Map 的原理。这样我可以以 O(1) 的效率判断一个房间是否被访问过，从而保证整个算法的时间复杂度维持在 O(N + E)。”
# 3. 总结：什么时候用 Hash Map (dict)？
# 在这道题里，因为房间号是连续的数字（0, 1, 2...），我们其实有三种选择：
# 1. set()：最常用，代码简洁。
# 2. bool 数组 (如 visited = [False] * n)：在知道节点总数且节点是连续数字时，这种方式比 set 更省内存，速度也更快。
# 3. dict() (Hash Map)：如果房间名不是数字（比如是 "LivingRoom", "Kitchen"），或者你需要记录额外信息（比如“我是从哪个房间走过来开启这间房的”），那么就必须用 dict。
# 给转码路上的你：
# 你现在已经能够主动去思考“无向图”和“底层哈希表”了，这说明你的思维已经从“做出一道题”升级到了“理解系统设计”。
# • LC 797：因为是 DAG（无环），所以不需要 visited（哈希表）。
# • LC 841：因为可能有 环（Cycle），所以必须用 visited（哈希表）。
# 这就是图论最核心的两个分水岭。继续保持这种好奇心！下次当你看到一个图论题时，先问自己：“它会有环吗？” 如果答案是“可能”，请立刻反手写下一个 visited 集合。
#
# 这是一个非常容易混淆的误区：“加了 set（visited）就代表它是无向图吗？”
# 答案是：不一定。 实际上，set 的存在是为了处理环（Cycle），而“环”在有向图和无向图中都可能存在。
# 1. 为什么“有向图”也需要 set？
# 即使是单向通行的有向图，也可能形成一个圈。
# 场景模拟：
# • 房间 0 里的钥匙能开 1 号房 (0 \to 1)
# • 房间 1 里的钥匙能开 0 号房 (1 \to 0)
# • 你从 0 进去，拿到 1 的钥匙，去 1 号房；在 1 号房又拿到 0 的钥匙，又回到了 0 号房...
# 如果你不加 set（或者 bool 数组）来记录“我已经去过 0 号房了”，你的程序就会在 0 和 1 之间无限循环，直到系统内存耗尽崩溃。所以，set 是为了防止“重复访问”和“死循环”，这与图是否有向没有直接关系。
# 2. 回看这两道题的区别
# 我们可以把这两道题放在一起对比，你就彻底明白了：
# 题目	图的类型	是否有环？	是否需要 set？	为什么？
# LC 797 (所有路径)	DAG (有向无环图)	绝对无环	不需要	题目保证了你永远不会绕回来，所以放心走。
# LC 841 (钥匙和房间)	Directed Graph (有向图)	可能有环	必须加	房间钥匙可能形成 0 \to 1 \to 0 的循环。
# 3. Hash Map 还是 Boolean Array?
# 你之前问到有没有用到 Hash Map。在处理这类“节点是 0 到 N-1 数字”的题目时，工程师们经常会做这样一个 Tradeoff（权衡）：
# • 使用 set() (Hash Table 实现)： • 优点：代码最简洁，不需要提前知道有多少个房间。 • 缺点：哈希计算会有微小的额外开销。
# • 使用 visited = [False] * n (Boolean Array)： • 优点：速度最快，内存最省，因为直接通过索引（Index）访问内存地址。 • 缺点：必须提前知道房间的总数 n。
# 在 Python 中，这两种做法在面试中都是满分答案。
# 4. 总结：如何判断要不要加 set？
# 1) 我要找“所有路径”吗？ • 如果是（如 LC 797），通常不加 set（或者要在回溯后移出 set），因为我们要允许重复经过某个节点来构成不同的路径。
# 2) 我要找“能不能到达”或者“最短路”吗？ • 如果是（如 LC 841），一定要加 set。因为一旦进入过这个房间，我们就已经拿到了它的钥匙，没必要再进第二次。
# 3) 题目说了是“无环图（Acyclic）”吗？ • 如果是，可以不加。 • 如果没说，默认可能有环，必须加。

# Since you are transitioning into software engineering and have practiced about 80 problems, LC 841 (Keys and Rooms) is a fantastic follow-up to LC 797. While LC 797 was about finding all paths, this one is about reachability.
'''
Here is the breakdown using the UMPIRE method.
1. Understand
• The Goal: You start in room 0. Each room has a set of keys. A key for room i allows you to open room i. Can you visit every room?
• Input: A list of lists rooms, where rooms[i] is the list of keys in room i.
• Output: True if you can enter all rooms, False otherwise.
• Key Insight: This is a Graph Traversal problem. Rooms are nodes, and keys are directed edges leading to other nodes.
2. Match
• Pattern: We need to see if the entire graph is "connected" starting from node 0.
• Data Structures: • Set or Boolean Array (visited): Crucial to avoid walking in circles (cycles). • Stack (for DFS) or Queue (for BFS): To keep track of rooms we have keys for but haven't explored yet.
• Algorithms: • DFS (Depth First Search): Explore as far as possible down one branch before backtracking. • BFS (Breadth First Search): Explore all immediate neighbors first (layer by layer).
3. Plan (Strategy & Tradeoffs)
The Big Tradeoff: DFS vs. BFS
For this specific "reachability" problem, both work, but here is why you might choose one over the other:
Algorithm	Data Structure	Pro	Con
DFS	Stack (or Recursion)	Memory efficient for "narrow" graphs; very intuitive with recursion.	Can hit StackOverflow if the graph is extremely deep.
BFS	Queue	Finds the "shortest path" to a room; avoids deep recursion issues.	Uses more memory if the graph is "wide" (one room has 1000 keys).
Decision: Since we just need to know if we can reach everything (not the shortest path), DFS is usually the most common "go-to" for its simplicity.
4. Implement (Python DFS)
We will use a set to track visited rooms because looking up an item in a set is O(1).

5. Review
• Example: rooms = [[1], [2], [3], []] • Start at 0 -> adds 0 to visited. • Key 1 found -> dfs(1) -> adds 1 to visited. • Key 2 found -> dfs(2) -> adds 2 to visited. • Key 3 found -> dfs(3) -> adds 3 to visited. • Result: len({0, 1, 2, 3}) == 4 -> True.
• Example: rooms = [[1,3],[3,0,1],[2],[0]] • Room 2 is only accessible via a key in room 2 itself? No, room 2 is accessible from room ?. If you trace it, you'll see if 2 is unreachable, len(visited) will be < len(rooms).
6. Evaluate
Time Complexity: O(N + E)
• N is the number of rooms, E is the total number of keys.
• Why? We visit each room once and we look at each key exactly once.
Space Complexity: O(N)
• Visited Set: Stores up to N room indices.
• Recursion Stack: In the worst case (rooms are a long line 0->1->2->3), the stack depth is N.
Why use a visited set here but not in LC 797?
This is the most important takeaway for your transition to Engineering:
1. LC 797 (All Paths): We wanted every possible way to get there. If we "blocked" a room after visiting it once, we would miss other valid paths through that same room.
2. LC 841 (Can Visit All): We only care if we can get into the room at least once. Once a room is open, it stays open. Checking it again is a waste of time and could lead to an infinite loop if Room A has a key to B and Room B has a key to A.
Pro-tip for your career change: When you start interviewing for SDE roles, being able to explain why you chose a set over a list for visited (look-up speed!) is exactly what interviewers are looking for. Keep it up!
'''
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()

        def dfs(room_index):
            # 1. mark current room as visited
            visited.add(room_index)
            # 2. Look at all keys in this room
            for key in rooms[room_index]:
                # 3. If we haven't been to that room yet, go there
                if key not in visited:
                    dfs(key)
        # Start the engine at room 0
        dfs(0)

        # If the number of visited rooms equals total rooms, return true
        return len(visited) == len(rooms)
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [[1],[2],[3],[]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,3],[3,0,1],[2],[0]]\n
# @lcpr case=end

#

