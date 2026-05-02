# 二叉树完全指南（新手友好版）

---

## 一、什么是二叉树？

二叉树是一种树形数据结构，每个节点**最多有两个子节点**，分别叫做**左孩子**和**右孩子**。

```
        1          ← 根节点 (root)
       / \
      2   3        ← 子节点
     / \   \
    4   5   6      ← 叶子节点 (leaf)，没有子节点
```

### 基本术语

| 术语 | 含义 |
|------|------|
| 根节点 (Root) | 最顶部的节点，整棵树的起点 |
| 叶子节点 (Leaf) | 没有子节点的节点 |
| 父节点 (Parent) | 有子节点的节点 |
| 子节点 (Child) | 某个节点下面连接的节点 |
| 深度 (Depth) | 从根到该节点的距离（根的深度 = 0） |
| 高度 (Height) | 从该节点到最远叶子的距离（叶子的高度 = 0） |

### 深度 vs 高度

```
        1          depth=0,  height=3
       / \
      2   3        depth=1,  height=1 / height=0
     / \
    4   5          depth=2,  height=0

深度 → 从上往下数（离根多远）→ 根的深度 = 0
高度 → 从下往上数（离地多远）→ 叶子的高度 = 0
整棵树的高度 = 根节点的高度 = 最大深度
```

---

## 二、二叉树的存储方式

### 1. 数组存储

用数组下标表示父子关系，适合**完全二叉树**：

```
      10
     /  \
    20   30
   / \   /
  40 50 60

数组: [10, 20, 30, 40, 50, 60]
下标:   0   1   2   3   4   5

规则：
- 父节点下标 i → 左孩子 2i+1, 右孩子 2i+2
- 子节点下标 i → 父节点 (i-1)//2
```

### 2. 链式存储（最常用）

每个节点是一个对象，包含值、左指针、右指针：

```python
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None    # 左孩子指针
        self.right = None   # 右孩子指针
```

手动构建一棵树：

```python
#       5
#      / \
#     3   7
#    / \   \
#   2   4   8

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(8)
```

### 对比

| 特点 | 数组存储 | 链式存储 |
|------|---------|---------|
| 空间 | 稀疏树浪费空间 | 按需分配，不浪费 |
| 访问父子 | O(1) 下标计算 | 需要遍历 |
| 插入删除 | 需要移动元素 | 修改指针即可 |
| 适用场景 | 堆（完全二叉树） | 通用二叉树 |

---

## 三、二叉树的遍历

### 深度优先 DFS（三种）

核心区别：**"根"在什么时候处理**。

```
前序 Preorder:   根 → 左 → 右    （根在前）
中序 Inorder:    左 → 根 → 右    （根在中）
后序 Postorder:  左 → 右 → 根    （根在后）
```

示例树：

```
         1
        / \
       2   3
      / \   \
     4   5   6
```

| 遍历方式 | 结果 | 根节点1的位置 |
|---------|------|-------------|
| 前序 | 1 2 4 5 3 6 | 第一个 |
| 中序 | 4 2 5 1 3 6 | 中间 |
| 后序 | 4 5 2 6 3 1 | 最后一个 |

#### 递归写法

三种遍历结构完全相同，区别**只在 print 的位置**：

```python
# 前序：先打印，再递归左右
def preorder(node):
    if not node:
        return
    print(node.val)         # ← 根
    preorder(node.left)     #    左
    preorder(node.right)    #    右

# 中序：先递归左，再打印，再递归右
def inorder(node):
    if not node:
        return
    inorder(node.left)      #    左
    print(node.val)         # ← 根
    inorder(node.right)     #    右

# 后序：先递归左右，最后打印
def postorder(node):
    if not node:
        return
    postorder(node.left)    #    左
    postorder(node.right)   #    右
    print(node.val)         # ← 根
```

#### 迭代写法（以前序为例）

```python
def preorder_iterative(root):
    stack = [root]
    while stack:
        node = stack.pop()          # 后进先出
        print(node.val, end=" ")
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)  # 左孩子后入栈，所以先被弹出
```

#### 各遍历的使用场景

| 遍历方式 | 典型用途 | 原因 |
|---------|---------|------|
| 前序 | 复制树 / 序列化 | 先建根，再建子树 |
| 中序 | BST 排序输出 | 天然得到有序序列 |
| 后序 | 计算文件夹大小 / 删除树 | 先处理子节点才能处理父节点 |

### 广度优先 BFS（层序遍历）

一层一层从上往下、从左往右扫描，用**队列**实现：

```python
from collections import deque

def levelOrder(root):
    if not root:
        return []
    result = []
    queue = deque([root])

    while queue:
        level = []
        for _ in range(len(queue)):   # 逐层处理
            node = queue.popleft()    # 先进先出
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)

    return result

# 输出: [[1], [2, 3], [4, 5, 6]]
```

### DFS vs BFS 的数据结构对应

```
DFS + 栈(Stack)   → 后进先出 → 一路往深处走，走不通再回头
BFS + 队列(Queue) → 先进先出 → 一层层往外扩展
```

#### 为什么队列用 popleft() 而不是 pop()？

```
deque 内部:  [1, 2, 3]
              ↑        ↑
             头部      尾部
           popleft()   pop()
           取出1 ✓     取出3 ✗（变成栈了）
```

`pop()` 取尾部（后进先出 = 栈），`popleft()` 取头部（先进先出 = 队列）。

---

## 四、二叉树的类型

### 按数据规则分类

所有类型都是 BST 的变种，区别在于怎么保持平衡：

| 类型 | 核心规则 | 特点 |
|------|---------|------|
| BST | 左 < 根 < 右 | 基础版，不保证平衡，可能退化为链表 |
| AVL 树 | 任何节点高度差 ≤ 1 | 严格平衡，查找最快，旋转多 |
| 红黑树 | 颜色规则保证近似平衡 | 插入删除比 AVL 快，工程中最常用 |
| Splay 树 | 访问即提到根 | 频繁访问的数据很快 |

### 按结构形状分类

| 类型 | 规则 | 示例 |
|------|------|------|
| Full Tree（满二叉树） | 每个节点有 0 或 2 个子节点 | 不允许只有 1 个子节点 |
| Complete Tree（完全二叉树） | 除最后一层外都填满，最后一层从左到右连续 | 堆就是完全二叉树 |
| Perfect Tree（完美二叉树） | 所有内部节点有 2 个子节点，所有叶子同层 | 最"完美"的形状 |
| Balanced Tree（平衡二叉树） | 每个节点左右高度差 ≤ 1 | 保证操作效率 O(log n) |

```
    Full           Complete        Perfect        Balanced
      1                1              1              1
     / \              / \            / \            / \
    2   3            2   3          2   3          2   3
   / \              / \            / \ / \            / \
  4   5            4   5          4  5 6  7          6   7
```

### 包含关系

```
Perfect ⊂ Complete ⊂ Balanced

Perfect（完美）一定是 Complete（完全）
Complete（完全）一定是 Balanced（平衡）
反过来不成立
```

---

## 五、二叉搜索树 (BST)

### 核心规则

对于每个节点：**左子树所有节点 < 根 < 右子树所有节点**。

注意：不是只看直接子节点，而是**整棵子树所有节点**都要满足。

```
      50
     /  \
    30    70
   /  \
  20   40      ← 40 不仅要 > 30，还要 < 50

每个节点有一个允许的值范围 (min, max)：
- 节点50: (-∞, +∞)
- 节点30: (-∞, 50)
- 节点40: (30, 50)   ← 同时被父节点30和祖父节点50约束
```

### BST 的插入

从根节点开始比较，**一路走到空位**才插入：

```
插入 22 到这棵树：

22 vs 13 → 22 > 13 → 往右
22 vs 21 → 22 > 21 → 往右
22 vs 24 → 22 < 24 → 往左
24 的左边是空的 → 插在这里

         13
        /  \
       6    21
      / \   / \
     4   8 15  24
               / \
              22  26
```

### BST 的删除（三种情况）

**情况 1：叶子节点 → 直接删**

```
删除 8：
       13               13
      /  \              /  \
     6    21    →      6    21
    / \                /
   4   8              4
```

**情况 2：只有一个子节点 → 用子节点顶替**

```
删除 24（只有右孩子 26）：
       21               21
      /  \              /  \
    15    24    →     15    26
            \
            26     ← 直接顶上去
```

**情况 3：有两个子节点 → 找替身**

找左子树最大值（前驱）或右子树最小值（后继）来替代

没有不能删, 只是越复杂的情况处理步骤越多

```
删除 13（根节点）：
 				 13
        /  \
       6    21
      / \   / \
     4   8 15  24
                 \
                  26

中序遍历：4, 6, 8, [13], 15, 21, 24, 26
                    ↑
           前驱=8         后继=15

用 15 替代：
         15
        /  \
       6    21
      / \     \
     4   8    24
                \
                26
```

```python
有两个子节点的：13（根）, 6, 21

例：删除 21
需要找替身：左子树最大值(15) 或 右子树最小值(24)

用 24 替代：
         13                    13
        /  \                  /  \
       6    21      →        6    24
      / \   / \             / \   / \
     4   8 15  24          4   8 15  26
                 \
                 26
```

总结这棵树

```python
节点    子节点情况         删除方式
────────────────────────────────
4      无子节点(叶子)      直接删
8      无子节点(叶子)      直接删
15     无子节点(叶子)      直接删
26     无子节点(叶子)      直接删
24     一个子节点(26)      26顶上来
6      两个子节点(4,8)     用4或8替代
21     两个子节点(15,24)   用15或24替代
13     两个子节点(6,21)    用8或15替代
```



### BST 删除代码（LeetCode 450）

```python
def deleteNode(self, root, key):
    if not root:
        return None
	# 第一步：找到要删的节点
  # 要删的值比当前节点小，去左边找。比当前节点大，去右边找。这就是 BST 的查找逻辑。
    if key < root.val:
        root.left = self.deleteNode(root.left, key)
    elif key > root.val:
        root.right = self.deleteNode(root.right, key)
    # 第二步：找到了，怎么删？
    else:# 进入 else 说明 root.val == key，当前节点就是要删的。
        # 情况1和2：没有左子树或没有右子树(叶子节点<return None, 相当于被删了>/只有左子树/只有右子树)
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        # 情况3：有两个子节点，找右子树最小值
        successor = root.right
        while successor.left:
            successor = successor.left
        root.val = successor.val # 不是真的删掉当前节点，而是把后继的值复制过来，覆盖自己
        root.right = self.deleteNode(root.right, successor.val)

    return root
```

本题理解见下:

## LeetCode 450 逐行拆解

先把完整代码放这里，然后一段一段讲：

```python
def deleteNode(self, root, key):
    if not root:
        return None

    if key < root.val:
        root.left = self.deleteNode(root.left, key)
    elif key > root.val:
        root.right = self.deleteNode(root.right, key)
    else:
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        successor = root.right
        while successor.left:
            successor = successor.left
        root.val = successor.val
        root.right = self.deleteNode(root.right, successor.val)

    return root
```

## 第一步：找到要删的节点

```python
if not root:
    return None
```

树是空的，或者找到底都没找到，返回 None。

```python
if key < root.val:
    root.left = self.deleteNode(root.left, key)
elif key > root.val:
    root.right = self.deleteNode(root.right, key)
```

要删的值比当前节点小，去左边找。比当前节点大，去右边找。这就是 BST 的查找逻辑。

用具体例子看，删除 15：

```
         13
        /  \
       6    21
      / \   / \
     4   8 15  24

key=15 vs 13 → 15 > 13 → 去右边
key=15 vs 21 → 15 < 21 → 去左边
key=15 vs 15 → 找到了！进入 else
```

## 第二步：找到了，怎么删？

进入 `else` 说明 `root.val == key`，当前节点就是要删的。

### 情况 1 和 2 合并处理

```python
if not root.left:
    return root.right
```

没有左子树？把右子树返回给上一层，**自己就被跳过了（等于被删了）**。

这句话同时处理了两种情况：

```
情况1 - 叶子节点（左右都没有）:
  not root.left → True
  return root.right → return None → 节点被删了

情况2 - 只有右子树:
  not root.left → True
  return root.right → 右子树顶上来
if not root.right:
    return root.left
```

同理，没有右子树，让左子树顶上来。

### "return 给上一层"是什么意思？

这是最关键的理解点。回看上面的代码：

```python
root.left = self.deleteNode(root.left, key)
```

`deleteNode` 返回什么，`root.left` 就指向什么。所以当被删节点 `return root.right` 的时候，**父节点的指针就自动指向了被删节点的子节点**，被删节点就脱离了树。

```
删除节点 24（只有右孩子 26）:

删除前:                     删除后:
  21                         21
 /  \                       /  \
15   24  ← return 26      15   26
       \
       26

24 说: "我要被删了，把我的右孩子 26 返回给我爸 21"
21 收到后: root.right = 26
24 就被跳过了
```

### 情况 3：有两个子节点

```python
successor = root.right
while successor.left:
    successor = successor.left
```

走到右子树的**最左边**，找到右子树中最小的节点，这就是**后继**。

```
删除 21:
      21          右子树中一路往左走
     /  \
    15   24  → 24 没有左孩子，24 就是后继
           \
           26
root.val = successor.val
```

不是真的删掉当前节点，而是**把后继的值复制过来**，覆盖自己。

```
      21   →   24       把 24 的值抄到 21 的位置
     /  \      /  \
    15   24   15   24    但现在有两个 24 了！
           \         \
           26        26
root.right = self.deleteNode(root.right, successor.val)
```

右子树里还有一个多余的后继节点（原来的 24），递归删掉它。后继节点最多只有右子树（因为它是最左的，不可能有左子树），所以删它一定是情况 1 或情况 2，很简单。

```
最终结果:
      24
     /  \
    15   26      干净了，BST 规则依然成立
```



successor = root.right        

while successor.left:            

successor = successor.left

这段代码**就是在找右子树的最小值**，往左走到底就是最小值。

## 为什么往左走就能找到最小值？

因为 BST 的规则是**左 < 根 < 右**，所以越往左越小：

```
      21
     /  \
    15   24
        /  \
       22   26

右子树是以 24 为根的这棵：
      24
     /  \
    22   26

最小值在哪？一路往左走到底 → 22
```

## 逐行看代码

```python
successor = root.right        # 第一步：先走到右子树的根
while successor.left:         # 第二步：有左孩子就一直往左走
    successor = successor.left
```

用上面的例子，删除 21：

```
successor = root.right        # successor = 24
successor.left 是 22，存在    # 继续往左
successor = successor.left    # successor = 22
successor.left 是 None        # 停下来，22 就是最小值
```

## 再看一个更深的例子

```
删除 50:
        50
       /  \
      30   70
           / \
          60  80
         /
        55

successor = 70          # 先到右子树根
successor = 60          # 往左走
successor = 55          # 继续往左
successor.left = None   # 停，55 就是右子树最小值
```

## 一句话总结

BST 里找最小值 = **一路往左走到底**，找最大值 = **一路往右走到底**。`while successor.left` 就是在说"只要还能往左走，就继续走"，走不动了就是最小值。



Q: root.right = self.deleteNode(root.right, successor.val)为啥只能靠递归来删重复节点呢?

其实不是"只能"用递归，而是递归**最省事**。我们来看看不用递归会怎样。

## 直接删不行吗？

你可能想这样做：

```python
successor = root.right
while successor.left:
    successor = successor.left
root.val = successor.val
# 然后直接删掉 successor？
successor = None   # ❌ 没用！这只是把变量清空了，树没变
```

`successor = None` 只是让这个**变量**不再指向那个节点，但**父节点的指针还连着它**，树结构没有任何改变。

```
修改前:                    successor = None 之后:
      24                        24
     /  \                      /  \
    22   26                   22   26    ← 22 还在！父节点还连着它
    
你需要的是让 24.left = None，而不是让 successor 变量 = None
```

## 要直接删，就得记住父节点

```python
successor = root.right
parent = root                    # 记住父节点

while successor.left:
    parent = successor           # 父节点跟着走
    successor = successor.left

root.val = successor.val

# 现在要断开 parent 和 successor 的连接
if parent == root:
    parent.right = successor.right   # 后继就是右子树根
else:
    parent.left = successor.right    # 后继是某个节点的左孩子
```

还要分两种情况：

```
情况A: 后继就是右孩子本身（没有往左走）
      21                    24
     /  \                  /  \
    15   24    →          15   26
           \
           26
parent == root，所以 parent.right = successor.right

情况B: 后继在更深的位置（往左走了）
      21                    22
     /  \                  /  \
    15   24    →          15   24
        /  \                     \
       22   26                   26
parent == 24，所以 parent.left = successor.right
```

## 对比两种写法

```python
# 递归写法：一行搞定
root.right = self.deleteNode(root.right, successor.val)

# 非递归写法：要多记一个 parent，还要分两种情况
successor = root.right
parent = root
while successor.left:
    parent = successor
    successor = successor.left
root.val = successor.val
if parent == root:
    parent.right = successor.right
else:
    parent.left = successor.right
```

## 为什么递归能一行搞定？

因为 `deleteNode` 这个函数本身就会处理**找到节点 → 断开连接 → 返回新子树**这整套逻辑。后继节点最多只有右子树（它是最左的，不可能有左子树），所以递归进去后会命中 `if not root.left: return root.right` 这个简单情况，一步就删完了。

```python
# 递归删 successor 时发生了什么：
# successor 没有左子树 → 命中 if not root.left → return root.right
# 父节点自动指向 successor 的右子树 → 删除完成
```

所以不是"只能"用递归，而是递归复用了已有的删除逻辑，不用额外记父节点，不用分情况讨论，代码最简洁。

## 完整流程图

```
进入 deleteNode(root, key)
│
├── root 是空的？ → return None
│
├── key < root.val？ → 去左子树找，root.left = deleteNode(左, key)
│
├── key > root.val？ → 去右子树找，root.right = deleteNode(右, key)
│
└── key == root.val → 找到了！
    │
    ├── 没有左子树？ → return 右子树（包含叶子节点的情况）
    │
    ├── 没有右子树？ → return 左子树
    │
    └── 左右都有？
        ├── 找到右子树最小值（后继）
        ├── 把后继的值复制到当前节点
        └── 递归删掉右子树中的后继
```

核心思路就是：**用 return 来改变父节点的指针指向**，从而实现"删除"。节点不是凭空消失的，而是被上一层的指针跳过了。



### BST 的使用场景

| 场景 | 说明 |
|------|------|
| 数据库索引 | B 树 / B+ 树（BST 的多叉升级版） |
| 有序映射 | Java TreeMap, C++ std::map（红黑树） |
| 范围查询 | 快速找到某个区间内的所有数据 |
| 排行榜 | 快速查排名、取 TopK |

---

## 六、平衡二叉树

### 定义

**每个节点**的左右子树高度差不超过 1（不只是根节点）。

```
    ✅ 平衡               ❌ 不平衡
      10                    10
     /  \                  /
    5    15               5
   / \     \             /
  3   7    20           3        ← 根节点: 左高2, 右高0, 差2
```

### 判断平衡的代码

用 `-1` 作为"不平衡信号"向上传递，实现 O(n) 一次遍历：

```python
def isBalanced(root):
    def height(node):
        if not node:
            return 0
        left = height(node.left)
        right = height(node.right)
        # 子树不平衡或当前节点不平衡，返回 -1
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1

    return height(root) != -1
```

为什么用 `max`？因为高度是**到最远叶子的距离**，要取更高的那棵子树。

为什么用 `-1`？发现不平衡后立刻停止，避免重复计算，从 O(n²) 优化到 O(n)。

---

## 七、堆 (Heap)

### 定义

堆是一棵**完全二叉树**，父节点和子节点之间有大小关系：

```
最大堆：父 ≥ 子，根是最大值       最小堆：父 ≤ 子，根是最小值
      90                            1
     /  \                         /   \
    70   80                      3     2
   / \   /                     / \   /
  50 60 30                    5   4 8
```

### 堆 vs BST

```
BST:  左 < 根 < 右    → 左右之间有规则
堆:   父 ≥ 子（或 ≤） → 只管上下，左右之间没规则
```

### 堆用数组存储

完全二叉树没有空洞，用数组刚好不浪费空间：

```
      90
     /  \
    70   80           数组: [90, 70, 80, 50, 60, 30]
   / \   /
  50 60 30

父节点 i → 左孩子 2i+1, 右孩子 2i+2
子节点 i → 父节点 (i-1)//2
```

### 核心操作

**插入：放末尾，上浮 (Sift Up)**

```
插入 95：
      90                      95
     /  \                    /  \
    70   80       →         70   90
   / \   / \               / \   / \
  50 60 30  95            50 60 30  80
```

**删除堆顶：末尾替换堆顶，下沉 (Sift Down)**

```
删除 90：
      30                      80
     /  \                    /  \
    70   80       →         70   30
   / \                     / \
  50  60                  50  60
```

### Python 中使用堆

```python
import heapq

nums = [5, 3, 8, 1, 9]
heapq.heapify(nums)              # 变成最小堆
smallest = heapq.heappop(nums)   # 弹出最小值 1
heapq.heappush(nums, 2)          # 插入 2

# 最大堆：取负数
max_heap = []
for n in [5, 3, 8, 1, 9]:
    heapq.heappush(max_heap, -n)
largest = -heapq.heappop(max_heap)  # 9
```

### 堆的使用场景

| 场景 | 说明 |
|------|------|
| 优先队列 | O(1) 拿到最大/最小值 |
| TopK 问题 | 维护大小为 K 的堆 |
| 堆排序 | O(n log n) 原地排序 |
| 合并 K 个有序链表 | 每次选最小的头节点 |

### 堆 vs BST 怎么选？

```
只关心最大/最小值        → 用堆     "谁是第一名？"
需要查找任意值           → 用 BST  "分数 500 的人在哪？"
需要范围查询             → 用 BST  "200-400 之间有谁？"
需要有序遍历             → 用 BST  "按分数从低到高列出"
```

---

## 八、关键概念速查表

### 时间复杂度对比

| 操作 | BST (平衡) | 堆 | 排序数组 |
|------|-----------|-----|---------|
| 查找 | O(log n) | O(n) | O(log n) |
| 插入 | O(log n) | O(log n) | O(n) |
| 删除 | O(log n) | O(log n) | O(n) |
| 取最值 | O(log n) | O(1) | O(1) |

### 遍历方式英文对照

| 中文 | 英文 |
|------|------|
| 前序遍历 | Preorder Traversal |
| 中序遍历 | Inorder Traversal |
| 后序遍历 | Postorder Traversal |
| 层序遍历 | Level Order Traversal |
| 广度优先搜索 | Breadth-First Search (BFS) |
| 深度优先搜索 | Depth-First Search (DFS) |

### 底层数据结构关系

```
数组 / 链表  → 底层存储方式（怎么存）
栈 / 队列    → 抽象规则（怎么存取）

栈 (LIFO)  → 后进先出 → 像叠盘子 → 用于 DFS
队列 (FIFO) → 先进先出 → 像排队   → 用于 BFS
```

### 常见 LeetCode 题目

| 题号 | 题目 | 知识点 |
|------|------|--------|
| 104 | Maximum Depth of Binary Tree | 树的高度/深度 |
| 110 | Balanced Binary Tree | 平衡判断 |
| 102 | Binary Tree Level Order Traversal | BFS 层序遍历 |
| 144/94/145 | Preorder/Inorder/Postorder Traversal | DFS 三种遍历 |
| 450 | Delete Node in a BST | BST 删除 |
| 700 | Search in a BST | BST 查找 |
| 701 | Insert into a BST | BST 插入 |
| 98 | Validate BST | BST 验证 |
| 215 | Kth Largest Element | 堆 / TopK |
