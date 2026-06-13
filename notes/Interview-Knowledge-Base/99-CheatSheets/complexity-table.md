# Complexity Cheat Sheet 复杂度速查表

## Data Structure Operations 数据结构操作

| Structure | Access | Search | Insert | Delete | 备注 |
|-----------|--------|--------|--------|--------|------|
| Array | O(1) | O(n) | O(n) | O(n) | append 均摊 O(1) |
| Sorted Array | O(1) | O(log n) | O(n) | O(n) | 二分查找 |
| Linked List | O(n) | O(n) | O(1)* | O(1)* | *已知节点位置 |
| Hash Table | — | O(1) avg | O(1) avg | O(1) avg | worst O(n) |
| BST (balanced) | O(log n) | O(log n) | O(log n) | O(log n) | 红黑树/AVL |
| Heap | O(1) top | O(n) | O(log n) | O(log n) pop | heapify 整体 O(n) |
| Stack / Queue | O(1) ends | O(n) | O(1) | O(1) | deque 两端 O(1) |
| Trie | — | O(L) | O(L) | O(L) | L = 词长 |
| Union-Find | — | ~O(1) | ~O(1) | — | 路径压缩+按秩 |

## Sorting 排序

| Algorithm | Best | Avg | Worst | Space | Stable |
|-----------|------|-----|-------|-------|--------|
| Quick Sort | n log n | n log n | n² | log n | ❌ |
| Merge Sort | n log n | n log n | n log n | n | ✅ |
| Heap Sort | n log n | n log n | n log n | 1 | ❌ |
| Timsort (Python/Java objects) | n | n log n | n log n | n | ✅ |
| Counting Sort | n+k | n+k | n+k | k | ✅ |
| Bubble/Insertion | n | n² | n² | 1 | ✅ |

## Algorithm Patterns 算法套路

| Pattern | Time | Space |
|---------|------|-------|
| Two Pointers / Sliding Window | O(n) | O(1)–O(k) |
| Binary Search | O(log n) | O(1) |
| BFS / DFS on graph | O(V + E) | O(V) |
| Topological Sort | O(V + E) | O(V) |
| Dijkstra (heap) | O((V+E) log V) | O(V) |
| Backtracking subsets | O(2ⁿ · n) | O(n) |
| Backtracking permutations | O(n! · n) | O(n) |
| 1D / 2D DP | O(n) / O(n·m) | 可滚动数组压缩 |
| Top-K with heap | O(n log k) | O(k) |
| Quickselect | O(n) avg | O(1) |

## Input Size → Expected Complexity 数据量反推复杂度

| n 大小 | 可接受复杂度 | 常见算法 |
|--------|-------------|---------|
| n ≤ 12 | O(n!) | 全排列回溯 |
| n ≤ 25 | O(2ⁿ) | 子集枚举 |
| n ≤ 100 | O(n³) | Floyd、区间 DP |
| n ≤ 10⁴ | O(n²) | 朴素 DP |
| n ≤ 10⁶ | O(n log n) | 排序、堆、二分 |
| n ≤ 10⁸ | O(n) / O(log n) | 一次遍历、双指针、数学 |

> 面试技巧：先问数据规模，**用 n 反推目标复杂度**，再选算法。约 10⁸ 次运算 ≈ 1 秒。
