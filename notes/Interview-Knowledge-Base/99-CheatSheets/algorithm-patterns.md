# Algorithm Pattern Templates 算法模板速查

> Muscle-memory templates in Python. 考前最后过一遍，每个模板要做到不看能默写。

## 1. Two Pointers 双指针

```python
# 对撞指针 converging — e.g. Two Sum II, 3Sum, Container With Most Water
left, right = 0, len(arr) - 1
while left < right:
    s = arr[left] + arr[right]
    if s == target: return [left, right]
    elif s < target: left += 1
    else: right -= 1

# 快慢指针 fast/slow — cycle detection (Floyd)
slow = fast = head
while fast and fast.next:
    slow, fast = slow.next, fast.next.next
    if slow == fast: return True  # has cycle
```

**何时用**: 有序数组求和/比较、原地删除、链表环/中点。

## 2. Sliding Window 滑动窗口

```python
# 变长窗口 variable-size — longest substring without repeating chars
window = {}
left = res = 0
for right, c in enumerate(s):
    window[c] = window.get(c, 0) + 1
    while window[c] > 1:              # 收缩条件 shrink condition
        window[s[left]] -= 1
        left += 1
    res = max(res, right - left + 1)
```

**模板心法**: 右指针扩张 → while 不合法就收缩左指针 → 每轮更新答案。求**最长**在收缩后更新；求**最短**在收缩中更新。

## 3. Binary Search 二分查找

```python
# 左边界 leftmost — bisect_left
left, right = 0, len(arr)            # 注意 right = len(arr)
while left < right:
    mid = (left + right) // 2
    if arr[mid] < target: left = mid + 1
    else: right = mid
return left  # first index where arr[i] >= target

# 答案二分 binary search on answer — Koko Eating Bananas
lo, hi = 1, max(piles)
while lo < hi:
    mid = (lo + hi) // 2
    if feasible(mid): hi = mid       # mid 可行 → 收紧上界
    else: lo = mid + 1
return lo
```

**何时用答案二分**: 求"最小的最大值/最大的最小值"，答案单调可验证 (feasible 函数)。

## 4. Prefix Sum 前缀和

```python
# prefix[i] = sum(nums[:i]);  sum(nums[i:j]) = prefix[j] - prefix[i]
prefix = [0]
for x in nums: prefix.append(prefix[-1] + x)

# 前缀和 + 哈希 — Subarray Sum Equals K
count = cur = 0
seen = {0: 1}
for x in nums:
    cur += x
    count += seen.get(cur - k, 0)
    seen[cur] = seen.get(cur, 0) + 1
```

## 5. BFS / DFS

```python
# BFS 层序 — shortest path in unweighted graph
from collections import deque
q = deque([start]); visited = {start}; step = 0
while q:
    for _ in range(len(q)):          # 一次处理一层
        node = q.popleft()
        if node == target: return step
        for nxt in neighbors(node):
            if nxt not in visited:
                visited.add(nxt); q.append(nxt)
    step += 1

# DFS 网格 — Number of Islands
def dfs(i, j):
    if not (0 <= i < m and 0 <= j < n) or grid[i][j] != '1': return
    grid[i][j] = '0'                 # mark visited
    for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
        dfs(i + di, j + dj)
```

**选择**: 无权最短路 → BFS；连通块/全路径/回溯 → DFS。

## 6. Topological Sort 拓扑排序 (Kahn's BFS)

```python
from collections import deque
indeg = [0] * n
graph = [[] for _ in range(n)]
for a, b in edges:                   # b -> a (a depends on b)
    graph[b].append(a); indeg[a] += 1
q = deque(i for i in range(n) if indeg[i] == 0)
order = []
while q:
    node = q.popleft(); order.append(node)
    for nxt in graph[node]:
        indeg[nxt] -= 1
        if indeg[nxt] == 0: q.append(nxt)
return order if len(order) == n else []   # [] means cycle 有环
```

## 7. Union-Find 并查集

```python
parent = list(range(n))
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]    # path compression
        x = parent[x]
    return x
def union(a, b):
    parent[find(a)] = find(b)
```

**何时用**: 动态连通性、判环（无向图）、分组合并。近 O(1) per op。

## 8. Backtracking 回溯

```python
# 子集/组合/排列 通用框架
def backtrack(start, path):
    res.append(path[:])                  # 子集：每个节点都收集
    for i in range(start, len(nums)):
        # if i > start and nums[i] == nums[i-1]: continue  # 去重(需先排序)
        path.append(nums[i])
        backtrack(i + 1, path)           # 组合用 i+1；可重复选用 i；排列用 visited
        path.pop()
```

**三问定模板**: ①收集时机（叶子 or 每个节点）②横向去重？③能否重复选。

## 9. Dynamic Programming 动态规划

```python
# 1D — House Robber
rob, skip = 0, 0
for x in nums:
    rob, skip = skip + x, max(rob, skip)
return max(rob, skip)

# 0/1 背包 knapsack — 逆序遍历容量
dp = [0] * (W + 1)
for w, v in items:
    for c in range(W, w - 1, -1):       # 0/1 背包倒序!
        dp[c] = max(dp[c], dp[c - w] + v)
# 完全背包 → 正序遍历容量

# 2D — Edit Distance
dp[i][j] = dp[i-1][j-1] if a[i-1]==b[j-1] else 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
```

**DP 四步**: 定义状态 → 转移方程 → 初始化/边界 → 遍历顺序。

## 10. Heap / Top-K

```python
import heapq
# Top-K largest: 维护大小为 k 的最小堆
heap = []
for x in nums:
    heapq.heappush(heap, x)
    if len(heap) > k: heapq.heappop(heap)
return heap[0]   # kth largest
# Python 只有最小堆；要最大堆 push -x
```

## 11. Monotonic Stack 单调栈

```python
# Next Greater Element — 找右边第一个更大的
stack = []                                # 存下标, 栈内递减
res = [-1] * len(nums)
for i, x in enumerate(nums):
    while stack and nums[stack[-1]] < x:
        res[stack.pop()] = x
    stack.append(i)
```

**何时用**: "下一个更大/更小元素"、柱状图最大矩形、接雨水。

## 12. Intervals 区间

```python
# 合并区间 — 先按起点排序
intervals.sort()
merged = [intervals[0]]
for s, e in intervals[1:]:
    if s <= merged[-1][1]: merged[-1][1] = max(merged[-1][1], e)
    else: merged.append([s, e])
```
