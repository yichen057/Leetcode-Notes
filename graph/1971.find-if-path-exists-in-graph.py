#
# @lc app=leetcode id=1971 lang=python3
# @lcpr version=30403
#
# [1971] Find if Path Exists in Graph
#
# https://leetcode.com/problems/find-if-path-exists-in-graph/description/
#
# algorithms
# Easy (55.08%)
# Likes:    4329
# Dislikes: 253
# Total Accepted:    691.1K
# Total Submissions: 1.3M
# Testcase Example:  '3\n[[0,1],[1,2],[2,0]]\n0\n2\n6\n[[0,1],[0,2],[3,5],[5,4],[4,3]]\n0\n5'
#
# There is a bi-directional graph with n vertices, where each vertex is labeled
# from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D
# integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional
# edge between vertex ui and vertex vi. Every vertex pair is connected by at
# most one edge, and no vertex has an edge to itself.
# 
# You want to determine if there is a valid path that exists from vertex source
# to vertex destination.
# 
# Given edges and the integers n, source, and destination, return true if there
# is a valid path from source to destination, or false otherwise.
# 
# 
# Example 1:
# 
# Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
# Output: true
# Explanation: There are two paths from vertex 0 to vertex 2:
# - 0 → 1 → 2
# - 0 → 2
# 
# 
# Example 2:
# 
# Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0,
# destination = 5
# Output: false
# Explanation: There is no path from vertex 0 to vertex 5.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 2 * 10^5
# 0 <= edges.length <= 2 * 10^5
# edges[i].length == 2
# 0 <= ui, vi <= n - 1
# ui != vi
# 0 <= source, destination <= n - 1
# There are no duplicate edges.
# There are no self edges.
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
'''
UMPIRE template

# Understand
inputs: n: # of vertices, from 0 to n-1; edges: List[List[int]]; source: start int; destination: target int
outputs:boolean, find the path from start to the destination
constraints:
# 1 <= n <= 2 * 10^5
# 0 <= edges.length <= 2 * 10^5
# edges[i].length == 2
# 0 <= ui, vi <= n - 1
# ui != vi
# 0 <= source, destination <= n - 1
# There are no duplicate edges.
# There are no self edges.
edge cases:
1) source == destination, return True
2) edges: empty adjacent list, return False
3) source and dest are not connected, return False
4) source or dest is isolated vertices , return False

  # Match (any problems this reminds you of, any helpful patters to solve this e.g. two pointer technique, any data structures this reminds you of )
graph traversal: dfs/ bfs; undirected graph; can we reach; both dfs/bfs both work
 1) edge -> adjacency list: dict[int, list[int]] 
 2) dfs(recursion stack) or bfs(deque)
 3) visited set
  # Plan (pseudocode)
eg: Use BFS
1) edge case: if source == destination: return True
2) build adjacency list from edges
graph = {}
for each [u, v] in edges:
    graph[u].append(v)
    graph[v].append(u) # undirected → add both directions
3) bfs
visited = {source} # track visited nodes
queue = deque([source]) # queue starts with source

while queue:
    node = queue.popleft()
    for neighbor in graph[node]:
        if neighbor == desti: return True
        if neighbor not in visited:mark visited and enqueue
            visited.add(neighbor)
            queue.append(neighbor)
return False
  # Implement (python code)

  # Review (dry run of your code)
- Example 1: n=3, [[0,1],[1,2],[2,0]], 0→2 → True ✓
- Example 2: n=6, disconnected, 0→5 → False ✓
  # Evaluate (time and space complexity)
- Time: O(n + m)
Building adjacency list: visit each edge once → O(m)
BFS: each node enqueued at most once (thanks to visited), each edge examined at most twice (undirected) → O(n + m)
- Space: O(n + m) = O(n) + O(n) + O(m)
n = number of nodes, m = number of edges (len(edges))

空间复杂度 = 程序运行时,所有数据结构同时占用的最大内存总和。不只看你写了几个 =,而要看每个数据结构最坏情况会装多少东西。
'''
from collections import deque
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # base case: 时间复杂度O(1)
        if source == destination:
            return True
        
        # Build adjacency list: 时间复杂度O(m), 循环跑了len(edges)次, 也就是m次
        # defaultdict(list)是dict的子类, 本质就是个hash map, not list of lists. 没指定大小, 按需创建, 通过key查value. 比如访问graph[5]时它才创建键5
        # 内部长这样:
        #{
        # 0: [1,2], 1: [0, 3], 2: [0], 3:[1]
        #}
        graph = defaultdict(list) # A regular dict raises KeyError if you access a missing key. defaultdict(list) auto-creates an empty list for missing keys, so you can .append() without checking.
        # 和边数 m 相关的是 graph。graph 保存了所有的边m, 又因为是无向图,每条边 [u, v] 我们都要存两次(u→v 和 v→u)。所以 m 条边在邻接表里占 2m 个位置 = O(m)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u) # undirected, add both directions
        
        # bfs
        visited = {source} # Curly braces with a value create a set. (Note: {} alone is an empty dict, not a set. Use set() for an empty set
        queue = deque([source])
        # visited 和 queue 都和节点数 n 相关,因为它们装的都是节点。最多存n个节点, visited和queue的空间复杂度均为O(n)
        # visited 保证了每个节点只入队一次,只被处理一次,只会展开它的邻居一次。
        # 所以"展开邻居"这件事在整个 BFS 中的总次数,就是"每个节点展开它一次邻居"的总和 = 所有节点的度数之和 = 2m。
        # 不是每次 while 都跑 n 次 for,而是 for 的总次数被 2m 这个总量约束。
        while queue: # 每次 while 循环弹出一个节点。一个节点最多被加入 queue 一次(因为有 visited 拦着,不会重复加), 所以 while 循环最多跑 n 次(n 是节点总数)。
            node = queue.popleft() # deque popleft is O(1)

            for neighbor in graph[node]:# for循环的总执行次数是2m次. 因为在无向图里, 把每个节点的邻居数加起来等于边数的两倍
                if neighbor == destination:
                    return True
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        # 把 while 和 for 加起来, while循环n次, for循环2m次, 加起来n+2m, 去掉常数-> O(n+m)
        # ⚠️ 注意:不是 O(n × m),是 O(n + m)! 因为这两层循环之所以不是相乘关系而是相加关系,是因为 for 循环的总次数被"边数总和"封顶了,而不是每次 while 都跑 n 次 for。
        return False
    
    # 如果题目用的是邻接矩阵(n×n 二维数组)而不是邻接表,时间复杂度会变吗? 会变成 O(n²)!
    # 因为邻接矩阵里查邻居必须扫整行:for j in range(n): if matrix[i][j] == 1,就算这个节点只有 1 个邻居,也要扫 n 个格子。
    # 每个节点扫 n 个 → n × n = O(n²)。
    # 这就是为什么稀疏图(边少)用邻接表更快,稠密图(边多接近 n²)用邻接矩阵差不多。
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# 3\n[[0,1],[1,2],[2,0]]\n0\n2\n
# @lcpr case=end

# @lcpr case=start
# 6\n[[0,1],[0,2],[3,5],[5,4],[4,3]]\n0\n5\n
# @lcpr case=end

#

