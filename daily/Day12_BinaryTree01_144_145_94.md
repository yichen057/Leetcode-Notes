# Day 12 二叉树的前中后序遍历: 递归法

前序preorder traversal: 中左右

中序inorder traversal: 左中右

后序postorder traversal: 左右中 

三道基础的二叉树前中后序的遍历方式

## 题144.  Definition for a binary tree node

本题是前序

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left # 左指针, 默认为空
#         self.right = right # 右指针, 默认为空
# 递归法三步走: 1) 确定递归函数的参数和返回值; 本题无返回值, 结果放参数里了, 参数表示每一层递归需要处理的当前的节点
#             2) 确定终止条件: 如果 node 为 None，则停止。如果你传的是数值，数值无法判断是否为“空节点”。
#             3) 确定单层递归逻辑： 在每一层取当前节点的 val，然后把左右孩子（作为新的节点）交给下一层处理。
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        # dfs函数传递的参数是节点而不是数值. 参数： 每一层递归需要处理的是“当前的节点”
        # 如果只传了 node.left.val（一个具体的数字），下一层递归就再也找不到它的左右子节点了，递归就此中断。
        def dfs(node): # node: 代表当前正在处理的整棵树的根节点
            if node is None:
                return
            
            # 前序的顺序: 中左右
            result.append(node.val) # node.value: 获取当前这棵树根节点的值
            dfs(node.left) # node.left: 代表当前节点的左子树
            dfs(node.right)
        # 调用函数
        dfs(root)
        return result
```



1. 关于二叉树本身的构造

   是的，这正是 Python 中类（Class）的**构造函数**。

   在 Python 中，`__init__` 是一个特殊的方法，每当你根据类创建一个新对象时，它都会自动运行。我们可以从以下几个维度来拆解这段代码：

   ### 1. 核心作用

   这段代码定义了一个名为 `TreeNode` 的类，用来模拟二叉树中的一个**节点**。它的主要任务是：

   - **分配数值**：给节点存入一个数据（`val`）。
   - **建立连接**：初始化指向左子节点（`left`）和右子节点（`right`）的指针。

   ### 2. 参数解析

   - **`self`**：代表实例本身。通过 `self.val`，你是在告诉 Python：“把传入的参数存到这个特定节点的属性里”。
   - **`val=0`**：这是默认参数。如果你创建节点时不给值（比如 `node = TreeNode()`），它默认就是 0。
   - **`left=None` 和 `right=None`**：默认情况下，新创建的节点是孤立的，没有左右孩子。

   ### 3. 如何使用它？

   有了这个构造函数，你就可以通过这种方式手动构建一棵树：

   Python

   ```python
   # 创建三个节点
   root = TreeNode(1)      # 根节点，值为1
   left_node = TreeNode(2) # 左节点，值为2
   right_node = TreeNode(3)# 右节点，值为3
   
   # 建立连接
   root.left = left_node
   root.right = right_node
   ```

   ### 4. 为什么你在[二叉树的递归遍历](https://programmercarl.com/二叉树的递归遍历.html#其他语言版本)里看到它？

   因为递归函数（比如你截图里的 `dfs`）需要通过 `.val`、`.left` 和 `.right` 来移动和读取数据。这个构造函数定义的**属性名称**直接决定了你递归代码里该怎么写。

   ------

   **一句话总结：** `__init__` 就是二叉树节点的“出厂设置”，它定义了一个节点该长什么样。

   既然你已经理解了节点的结构，**需要我带你结合截图里的 `dfs(node.left)` 逻辑，看看递归是如何利用这些 `.left` 属性一层层深入的吗？**



2. 为啥获取value不是.value而是.val呢

这主要不是由 Python 语言决定的，而是由**你正在使用的二叉树类（TreeNode）是如何定义的**决定的。

在 LeetCode、数据结构教材以及大多数算法面试题中，二叉树节点的定义通常如下：

Python

```
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val    # 这里定义了属性名是 val
        self.left = left
        self.right = right
```

以下是为什么通常用 `.val` 而不是 `.value` 的几个原因：

### 1. 约定俗成（Naming Convention）

在算法界，为了书写简洁，开发者习惯使用缩写：

- **`val`** 代替 `value`（数值）
- **`curr`** 代替 `current`（当前指针）
- **`res`** 代替 `result`（结果）

这就像在数学里我们习惯用 $x$ 和 $y$ 而不是 `unknown_number_one` 一样，是一种**行业习惯**。

### 2. LeetCode 的标准

由于大部分人学习二叉树是通过 LeetCode（力扣）等平台，而这些平台的官方定义里统一使用了 `self.val`。为了让代码在平台上能跑通，大家都会遵循这个命名。如果你在代码里写 `.value`，解释器会报错：

> ```
> AttributeError: 'TreeNode' object has no attribute 'value'
> ```

### 3. 如何判断该写哪个？

其实，在实际工作中，写 `.val` 还是 `.value` 取决于**定义这个类的人**。

- 如果定义里写的是 `self.value = x`，你就得用 `.value`。
- 如果定义里写的是 `self.data = x`，你就得用 `.data`。

------

**一个小技巧：**

在面试或者看代码时，先看一眼类定义（`__init__` 函数）。定义的变量名是什么，你后面调用时就得写什么。

**下一步建议：**

你想看看如果不小心写错了报错信息是什么样的，或者想尝试自己写一个简单的 `TreeNode` 类来加深理解吗？



3. python语言里, 递归时dfs(node.left)为啥没有.val

在 Python 的递归实现中，`dfs(node.left)` 后面不需要加 `.val`，主要原因在于**函数参数的职责**和**递归的设计逻辑**：

### 1. 递归传递的是“节点”，而不是“数值”

在 `preorderTraversal` 逻辑中，`dfs` 函数定义的参数是 `node`。

- **`node` 的含义：** 它代表当前正在处理的整棵子树的根节点。
- **`node.left` 的含义：** 它代表当前节点的左子树（这也是一个 `TreeNode` 对象）。
- **为什么要传节点：** 递归需要不断深入到下一层，下一层依然需要知道这个节点的 `val`、`left` 和 `right`。如果你只传了 `node.left.val`（一个具体的数字），下一层递归就再也找不到它的左右子节点了，递归就此中断。

### 2. 数值的提取是在函数内部完成的

观察代码的执行流程：

1. 你调用 `dfs(node.left)`。
2. 程序跳转到 `dfs` 函数内部。
3. 此时，**当前的** `node` 已经变成了刚才传进来的左孩子。
4. 在这一层函数里，代码会通过 `res.append(node.val)` 提取出该节点的数值。

### 3. 符合递归的三要素

根据页面中提到的“递归三要素”：

- **参数：** 每一层递归需要处理的是“当前的节点”。
- **终止条件：** 如果 `node` 为 `None`，则停止。如果你传的是数值，数值无法判断是否为“空节点”。
- **单层逻辑：** 在每一层取当前节点的 `val`，然后把左右孩子（作为新的节点）交给下一层处理。

### 总结

- `dfs(node.left)`：意思是“去处理左边的那棵树”。
- `node.val`：意思是“获取当前这棵树根节点的值”。

如果写成 `dfs(node.left.val)`，就会把“一棵树”错当成“一个数字”传给函数，导致程序报错（因为数字没有 `.val` 属性，也无法进行后续的递归）。



4. void代表啥

在编程（特别是你正在看的 C++、Java 或 C# 代码）中，`void` 的核心含义是 **“空”** 或 **“无”**。

在二叉树遍历的递归函数中，你经常会看到 `void traversal(TreeNode* root)`，这具体代表以下几层意思：

### 1. 函数没有返回值

当一个函数的返回类型被标注为 `void` 时，意味着这个函数执行完操作后，**不会向调用它的地方返回任何数据**。

- **对比：** 如果是 `int sum()`，它必须最后 `return` 一个整数；如果是 `void`，它只需要完成它的任务（比如打印节点、把值存入数组）然后结束即可。

### 2. 在递归中的作用

在你查看的这段[二叉树递归遍历视频](https://www.bilibili.com/video/BV1Wh411S7xt/)中，`void` 非常常见。因为递归遍历通常有两种处理数据的方式：

- **直接打印/操作：** 函数只负责走遍每个节点，并在节点上做动作，不需要返回结果。
- **操作全局/引用变量：** 比如你在函数外定义了一个 `vector`（动态数组），递归函数通过引用的方式把节点值放进去。这时候函数本身不需要返回这个数组，所以用 `void`。

### 3. 语法细节

- **Return 语句：** 在 `void` 函数里，你可以写 `return;`（后面不跟任何值），这通常用于**提前结束函数**。

- **递归终止：** 在二叉树递归中，最常见的写法是：

  C++

  ```
  if (root == NULL) return; // 遇到空节点直接返回，不回传任何值
  ```

------

**简单来说：** `void` 就像是一个“只干活，不回话”的指令。

你想让我帮你分析一下视频里提到的**前序、中序、后序遍历**的具体代码实现，看看 `void` 是怎么串联起递归逻辑的吗？

## 题 94: 二叉树的中序遍历

本题是中序

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 二叉树的中序遍历: 顺序是左中右
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node):
            if node is None:
                return
            
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return result
```

## 题 145: 二叉树的后序遍历

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 二叉树的后序遍历: 顺序为左右中
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            dfs(node.right)
            result.append(node.val)
        
        dfs(root)
        return result
```



# 题102: 二叉树的层序遍历

```python
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

```



在 Python 中，`if not root:` **确实是用来判断 `root` 是否为空（或等价于“假”的值）**。

在二叉树这类算法题中，它最直接的含义就是：**如果当前节点（root）是 `None`，则执行下方的代码。**

------

### 1. 为什么可以这样写？

Python 的 `if` 语句会自动对变量进行“布尔测试”。以下值在 Python 中会被视为 **`False`**（假）：

- `None`（最常见的情况，表示空节点）
- `False`
- 数值 `0`
- 空字符串 `""`
- 空列表 `[]`、空字典 `{}` 等

在 [二叉树的层序遍历](https://programmercarl.com/0102.二叉树的层序遍历.html#_102-二叉树的层序遍历) 的代码中，`root` 通常是一个对象。如果它是 `None`，那么 `not root` 就会变成 `True`。

### 2. 常见的代码写法对比

在处理树节点时，以下几种写法在逻辑上通常是等价的，但 `if not root` 最为简洁：

| **写法**           | **风格**             | **语义**             |
| ------------------ | -------------------- | -------------------- |
| `if not root:`     | **推荐（Pythonic）** | 如果 root 为空       |
| `if root is None:` | **更严谨**           | 明确判断是否为 None  |
| `if root == None:` | 不推荐               | 性能略低于 `is None` |

### 3. 在算法中的实际应用

在你提供的 [Python 模板代码](https://programmercarl.com/0102.二叉树的层序遍历.html#python) 中：

Python

```
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: # 如果 root 是空的（即 None）
            return [] # 直接返回空列表，避免后续对 None 进行操作导致报错
        
        queue = collections.deque([root])
        # ... 后续逻辑
```

这段代码的作用是 **“边界检查”**。如果输入的树本身就是空的，程序就没必要往下创建队列或进行循环了，直接返回结果即可。

您是刚开始学习 Python 语法的二叉树实现吗？如果需要，我可以为您详细解释一下 Python 里的 `deque`（双端队列）在层序遍历中是怎么配合使用的。



在您查看的 [二叉树层序遍历](https://programmercarl.com/0102.二叉树的层序遍历.html) 代码中，`queue = collections.deque([root])` 的作用是 **初始化一个双端队列，并将二叉树的根节点作为第一个元素放进去**。

以下是拆解说明：

### 1. `collections.deque` 是什么？

它是 Python 标准库中提供的 **双端队列**（Double-Ended Queue）。

- **为什么用它：** 在二叉树的层序遍历中，我们需要频繁地从队列“头部”取出节点，并从“尾部”添加子节点。
- **性能优势：** `deque` 在头部弹出元素（`popleft()`）的时间复杂度是 $O(1)$。相比之下，如果使用普通的 Python 列表（`list`）并执行 `pop(0)`，时间复杂度是 $O(n)$，效率较低。

### 2. `([root])` 是什么操作？

- 这表示在创建队列的同时，将 `root`（根节点）包装成一个列表传递给 `deque` 的构造函数。
- 这样初始化完成后，队列里就已经有了一个起始元素，可以直接进入接下来的 `while queue:` 循环。

### 3. 在层序遍历中的具体工作流程

配合后续代码，这个队列的操作逻辑如下：

1. **入队起始：** 将 `root` 放入队列。
2. **出队处理：** 使用 `cur = queue.popleft()` 取出队首节点进行处理。
3. **扩展子节点：** 如果当前节点有左/右孩子，将其从尾部 `append` 进队列，等待下一层处理。

------

**想进一步了解吗？**

层序遍历的关键在于“先进先出”。如果您想对比一下，我可以为您展示如果不用 `deque` 而用普通列表实现，代码会有哪些性能上的隐患。



非常明确地告诉你：**在 Python 中，不能写 `while(size--)`。**

如果你尝试这样写，Python 解释器会报 `SyntaxError`（语法错误）。

这里有几个核心原因，理解它们能帮你更好地从 C++/Java 的思维切换到 Python：

### 1. Python 不支持 `--` 或 `++` 运算符

在 C++ 或 Java 中，`--` 是一个自减运算符。但在 Python 中：

- **没有 `++` 和 `--`**。
- 如果你写 `size--`，Python 会认为你想写 `size - (- )`，但这在语法上是不完整的。
- 在 Python 中，必须明确写成 `size -= 1`。

### 2. 表达式不返回值

在 C++/Java 中，`size--` 是一个表达式，它会先返回 `size` 的当前值，然后再执行减法。

而在 Python 中，赋值操作（如 `size -= 1`）是一个**语句**（Statement），它不返回值。所以即使你写 `while (size -= 1):` 也是非法的。

------

### 3. 如果非要用 `while` 模拟这个逻辑

在 Python 中，如果你想实现类似的效果，通常需要写成这样：

Python

```
size = len(queue)
while size > 0:
    node = queue.popleft()
    # ... 处理逻辑
    size -= 1  # 必须手动减 1
```

### 4. 为什么大家还是推荐 `for _ in range(len(queue)):`？

除了语法简洁外，还有一个**性能和安全**的小细节：

- **性能：** `range()` 是由 C 语言实现的优化迭代器，通常比手动维护一个 `while` 计数器稍微快一点。
- **安全：** 在 `for` 循环启动时，`len(queue)` 的值会被**一次性确定**。即使你在循环体内向 `queue` 添加了新元素（下一层的节点），循环次数也不会改变。这完美符合“只处理当前层”的需求，避免了逻辑死循环。

------

**总结：**

如果你在写 LeetCode 或二叉树算法，**请直接形成肌肉记忆**：

- ✅ **Python:** `for _ in range(len(queue)):`
- ❌ **Python:** `while(size--)` (语法错误)

**你想看看在 Python 中如何通过一行代码同时获取索引和元素（类似于其他语言的带下标循环）吗？**





这是一个非常棒的问题！这说明你可能习惯了 **C++ STL** 的写法（在 C++ 中，获取队首和弹出是两个独立的操作）。

在 Python 的 `collections.deque` 中，逻辑是不一样的。让我们对比一下：

### 1. 为什么不能写 `que.front().pop()`？

- **Python 的 `deque` 没有 `front()` 方法**：在 Python 中，如果你想“看一眼”队首元素但不弹出，使用的是索引 `queue[0]`。
- **`pop()` 是从右端（尾部）弹出**：Python 的 `pop()` 默认删除并返回**最右边**的元素。
- **方法链式调用的错误**：即便有这些方法，`que.front().pop()` 的逻辑在 Python 里会变成：先取到队首节点对象，然后尝试对这个**节点**执行 `pop()` 操作。这显然会报错，因为 `TreeNode` 对象没有 `pop` 方法。

------

### 2. Python 里的“一步到位”：`popleft()`

在 Python 中，我们使用 **`popleft()`** 这一个动作来完成两件事：

1. **获取** 队列最左边（队首）的元素。
2. **删除** 这个元素。

Python

```
# 一行代码搞定：取值 + 出队
cur = queue.popleft() 
```

------

### 3. 不同语言的习惯对比

为了帮你理清思路，我们可以看下不同语言处理“出队”的差异：

| **语言**      | **操作步骤**            | **代码示例**                             |
| ------------- | ----------------------- | ---------------------------------------- |
| **C++ (STL)** | 1. 看一眼队首   2. 弹出 | `auto cur = que.front();`   `que.pop();` |
| **Java**      | 一步到位                | `TreeNode cur = queue.poll();`           |
| **Python**    | **一步到位**            | **`cur = queue.popleft()`**              |

------

### 4. 总结：Python 处理队列的常用方法

如果你使用的是 `collections.deque`，记住这四个最核心的操作就够了：

- **入队（尾部）**: `queue.append(node)`
- **出队（头部）**: `node = queue.popleft()`  （**这就是你问的那个 `cur`**）
- **查看队首（不弹出）**: `first_node = queue[0]`
- **查看队尾（不弹出）**: `last_node = queue[-1]`

### 💡 小贴士

在 [代码随想录](https://programmercarl.com/) 的层序遍历模板里，每次循环的第一步都是 `cur = queue.popleft()`。这样 `cur` 拿到的就是当前要处理的节点，接下来你就可以通过 `cur.val` 访问它的值，或者通过 `cur.left` / `cur.right` 找到它的孩子。

**您在写代码时，是否遇到了 `AttributeError: 'NoneType' object has no attribute 'val'` 这样的报错？这通常和 `popleft()` 拿到的对象有关，需要我帮您分析一下吗？**





完全正确！你的理解非常到位。

我们可以把这个逻辑总结为一句话：**`level` 是“当下”，而 `queue` 是“未来”。**

### 1. 为什么它们不在一层？

二叉树的层序遍历（BFS）核心逻辑就是：当你处理第 n  层的节点时，它的孩子节点必然属于第 n+1 层。

- **`level` 数组**：它的生命周期非常短，只负责收集**当前这一层**（第 n层）所有节点的值。一旦这一层循环结束，`level` 就会被装进结果大列表 `res` 中，然后被清空重置。
- **`queue` 队列**：它是一个“缓冲区”。当你把第 n层的节点一个个从队首取出时，你同时把它们的第 n+1 层孩子节点一个个塞进队尾。

### 2. 空间上的错位

想象一个具体的场景：

- 当你正在处理第一层（根节点 `root`）时：
  - 你的 `for` 循环只运行 1 次。
  - `level` 存入 `root.val`。
  - `queue` 存入 `root.left` 和 `root.right`（它们是第二层的）。
- 当这一层 `for` 循环结束，`level` 功成身退。
- 下一轮 `while` 循环开始时，`queue` 里的内容恰好就是**整整一层的第二层节点**。

### 3. 如果误用了 `level.append(cur.left)` 会发生什么？

如果你真的写了 `level.append(cur.left)`，会出现两个严重的错误：

1. **数据类型错误**：`level` 应该是存数字的（比如 `[1, 2, 3]`），结果你存进去了节点对象（`TreeNode`），输出结果就不对了。
2. **逻辑断层**：最关键的是，你没有把孩子放到 `queue` 里。这意味着当你处理完当前层后，`queue` 就空了，你的 `while queue` 循环会直接停止，**整棵树剩下的部分你就再也找不到了**。

------

### 总结

- **`level.append()`**：只放 **`cur.val`**（当前层的值）。
- **`queue.append()`**：只放 **`cur.left/right`**（下一层的节点，留着待会儿处理）。

**这就好比：** 你在吃今天的饭（处理 `cur`），但你得把明天的菜买回来放进冰箱（把孩子存入 `queue`），而不能直接把生菜倒进今天的饭碗里（`level`）。

既然你已经理解了层序遍历的层级关系，**想挑战一下如何利用这个逻辑来计算二叉树的最大深度（高度）吗？** 其实代码只需要改动一个地方。



这是一个非常敏锐的问题！这触及到了 **“数据结构的概念”** 和 **“Python 的具体实现”** 之间的区别。

简单直接的回答：

- **概念上**：我们在用它做 **Queue（队列，先进先出）**。
- **工具上**：我们使用的是 **Deque（双端队列）** 这个类。
- **原因**：因为 Python 的 `deque` 是实现 `queue` 跑得**最快**的工具。

我来把这个逻辑拆解清楚：

### 1. 名字 vs. 身份

代码写的是：

Python

```
queue = collections.deque([root])
```

- **变量名 `queue`**：这是**你的意图**。你给它起名叫 `queue`，是因为在层序遍历算法里，你只需要它发挥“排队（先进先出）”的功能。
- **类名 `deque`**：这是**你用的工具**。它的全称是 **D**ouble-**E**nded **Que**ue（双端队列）。

**打个比方：**

这就好比你想**切菜**（意图：Queue），但是你手里没有普通的菜刀，所以你拿了一把**瑞士军刀**（工具：Deque）。

- 瑞士军刀（Deque）两头都能用，功能很强。
- 但你只用它的其中一个功能来切菜（Queue）。

### 2. 什么是 Deque（双端队列）？

普通的 **Queue** 只能“一边进，另一边出”（单行道）。

而 **Deque** 允许你在**两头**都进行“进”和“出”的操作（双向车道）。

- **Queue（队列）**: 入队 $\rightarrow$ [ 数据 ] $\rightarrow$ 出队
- **Deque（双端队列）**: 入/出 $\leftrightarrow$ [ 数据 ] $\leftrightarrow$ 入/出

### 3. 既然它是双端的，为什么我们要用它？

你可能会问：“杀鸡焉用牛刀？为什么不直接用一个简单的 Queue？”

原因只有一个：**为了速度（性能）。**

在 Python 中，实现队列有两种常见方式，但效率天差地别：

| **方式**          | **代码**          | **队首出队性能** | **评价**                                                     |
| ----------------- | ----------------- | ---------------- | ------------------------------------------------------------ |
| **用列表 (List)** | `list.pop(0)`     | **$O(n)$ 很慢**  | 列表底层是数组，移除第一个元素，后面的所有人都要往前挪一步。 |
| **用 Deque**      | `deque.popleft()` | **$O(1)$ 极快**  | Deque 底层是双向链表（或分段数组），拿走第一个元素不需要挪动其他人。 |

**结论：**

虽然 `deque` 功能多（它是双端的），但因为它做“队首弹出”这个动作比 `list` 快太多了，所以 Python 程序员**约定俗成**：

> **只要是在 Python 里写算法题需要用到队列，统统使用 `collections.deque`。**

### 4. Python 里有没有真的名为 `Queue` 的东西？

有的！Python 有一个库叫 `queue`，里面有个类叫 `Queue`。

Python

```
from queue import Queue
q = Queue()
```

**那为什么不用它？**

因为它主要是给**多线程编程**用的。为了保证多线程安全，它加了很多“锁”的机制，导致它运行起来**非常慢**。在 LeetCode 这种单线程算法题里，用它是累赘。

------

### 总结

- **你在做什么**：你在实现一个队列（Queue）。
- **你用的什么**：你用的是双端队列（Deque）。
- **为什么这么写**：因为 Python 的 `deque` 是实现队列**最快**的方式，我们就只用它的 `append`（尾部进）和 `popleft`（头部出）这两个功能，假装它是一个普通的队列。

现在这个逻辑是不是通顺了？这就好比虽然你有跑车（Deque），但你只开它去买菜（Queue），纯粹是因为它跑得快！





# 题 107: 二叉树的层次遍历II

```python
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 易混淆点：[::-1] vs .reverse()

# 虽然效果一样，但它们有个小区别：
# 写法	作用	是否改变原列表？
# b = a[::-1]	创建一个新的倒序列表，赋值给 b	不会。原列表 a 保持不变。
# a.reverse()	直接把 a 自己给翻转了	会。原列表 a 变了，且这个方法不返回新列表。
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return [] # 注意, 这里不能返回None, 因为函数的定义：-> List[List[int]]。这就承诺了函数一定会返回一个列表。None 不是列表
        queue = collections.deque([root])
        result = []
        while queue:
            level = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            result.append(level)
        return result[::-1] # 创建一个新的倒序列表, 将列表（List）倒序（反转）. [::-1] 的字面意思就是：“从后往前，一步一步地把所有元素取出来，组成一个新的列表。
        # .reverse(): 翻转原列表, 且这个方法不返回新列表

```



在 Python 中，`result[::-1]` 的意思非常简单直白：**将列表（List）倒序（反转）**。

### 1. 举个例子

假设你的 `result` 列表是这样的：

Python

```
result = [1, 2, 3, 4, 5]
```

当你执行 `new_list = result[::-1]` 时，`new_list` 就会变成：

Python

```
[5, 4, 3, 2, 1]
```

就像照镜子或者把一排积木完全反过来放一样。

------

### 2. 语法原理拆解：`[start : end : step]`

这是 Python 的 **切片 (Slicing)** 语法。完整的写法是 `[起始位置 : 结束位置 : 步长]`。

- **前两个冒号空着**：表示从头取到尾，包含整个列表。
- **最后的 `-1`**：这是关键！
  - **正数**（比如 1）：表示从左往右走。
  - **负数**（比如 -1）：表示**从右往左走**（逆向）。

所以，`[::-1]` 的字面意思就是：**“从后往前，一步一步地把所有元素取出来，组成一个新的列表。”**

------

### 3. 在二叉树算法题中的应用

既然你在学层序遍历，你看到这行代码很可能是在做 **[107. 二叉树的层序遍历 II](https://leetcode.cn/problems/binary-tree-level-order-traversal-ii/)**。

- **题目要求**：从下往上输出（Bottom-up）。
- **常规做法**：
  1. 我们正常的层序遍历（BFS）是从上往下的（Top-down），得到的 `result` 是 `[[第一层], [第二层], [第三层]]`。
  2. 但是题目非要我们从下往上输出。
  3. **偷懒技巧**：我们不需要重写复杂的算法，只需要把正常的 BFS 结果 **`result[::-1]`** 一下，就变成了 `[[第三层], [第二层], [第一层]]`，完美符合题目要求！

### 4. 易混淆点：`[::-1]` vs `.reverse()`

虽然效果一样，但它们有个小区别：

| **写法**          | **作用**                           | **是否改变原列表？**                            |
| ----------------- | ---------------------------------- | ----------------------------------------------- |
| **`b = a[::-1]`** | 创建一个**新**的倒序列表，赋值给 b | **不会**。原列表 a 保持不变。                   |
| **`a.reverse()`** | 直接把 a 自己给翻转了              | **会**。原列表 a 变了，且这个方法不返回新列表。 |

在 LeetCode 的 `return` 语句中，我们通常喜欢用 `return result[::-1]`，因为这样写最简洁，一行搞定。

**你是在做“从下往上遍历”的那道题吗？**



# 199 题: 二叉树的右视图

```python
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 层序遍历的时候，判断是否遍历到单层的最后面的元素，如果是，就放进result数组中，随后返回result就可以了。
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = collections.deque([root])
        result = []
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                cur = queue.popleft() # 此时queue的长度会随着popleft()而变短
        
                if i == level_size -1: # 注意📢: 这里不能直接使用len(queue), 因为它是在循环过程中实时计算的
                    result.append(cur.val)

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return result
```



这是一个非常深刻且关键的问题！这说明你不仅在写代码，还在思考代码背后的**执行机制**。

你的担心是完全合理的：**如果我们在循环里不断往队列塞东西（子节点），队列长度变了，循环次数会不会也变了？导致下一层的节点被混到这一层处理？**

答案是：**在 Python 的 `for _ in range(len(queue))` 写法中，是安全的。**

因为它其实**已经隐含了“先取 size”** 的动作。让我为你拆解其中的奥秘。

------

### 1. `range()` 的“快照”机制

Python 的 `for i in range(N)` 语句在执行的那一瞬间，遵循以下逻辑：

1. **先计算参数**：解释器会**立即**执行 `len(queue)`，拿到一个具体的数字（比如 3）。
2. **生成迭代器**：然后生成一个固定长度的迭代器（比如 `0, 1, 2`）。
3. **锁定次数**：循环的次数就在这一刻被**锁定**了。

即便你在循环体内部疯狂地 `queue.append(...)`，导致 `len(queue)` 变成了 100，这个 `for` 循环也只会执行 **3次**，因为它只认准了**一开始**生成的那个范围。

### 2. 对比：显式写法 vs 隐式写法

其实你心里想的那种“更稳妥”的写法，和 Python 的简洁写法在底层逻辑上是**完全等价**的：

#### 写法 A：显式记录 Size（你的想法，类似 C++/Java 风格）

Python

```
size = len(queue)  # 1. 先把当前这一层的数量记在一个变量里
for _ in range(size): # 2. 这里的 size 是个死数字，不会变
    cur = queue.popleft()
    # append 子节点... 
```

#### 写法 B：Python 简洁写法（当前代码）

Python

```
# len(queue) 在这行代码运行时被求值一次，变成了数字（比如3）
# range(3) 生成了，循环次数锁死为 3
for _ in range(len(queue)): 
    cur = queue.popleft()
    # append 子节点...
```

**结论：** 写法 B 就是写法 A 的“语法糖”，Python 帮你省去了定义 `size` 变量这一步，但在逻辑上它确实是**先取了 size**。

------

### 3. 什么时候会出问题？（危险写法）

你的担心在某些特定的写法下**确实会发生**。如果我们不用 `range`，而是每次循环都重新去查队列长度，那就完蛋了。

#### ❌ 错误写法（动态检查长度）

如果你用的是类似 C 语言风格的动态判断（虽然 Python 不能直接这样写 `for`，但假设用 `while` 模拟）：

Python

```
# 假设 queue 里原本有 1 个 root
# 危险！不要这样写层序遍历！

i = 0
while i < len(queue): # 每一次循环，都会重新计算 len(queue)！
    cur = queue.popleft() # 取出一个
    queue.append(cur.left) # 加入一个
    queue.append(cur.right) # 加入一个
    # 此时 len(queue) 变大了！循环永远停不下来！
    i += 1
```

在这个错误写法中，因为 `len(queue)` 每次循环都会**重新计算**，导致刚加进去的孩子节点，马上就在**这一轮**被当作当前层节点处理了，层级彻底乱套。

------

### 总结

你现在的代码：

Python

```
for _ in range(len(queue)):
```

之所以安全，是因为 **`range` 在进入循环前，对 `len(queue)` 做了一次“快照”（Snapshot）**。它就像给当前队列里的节点盖了个戳：“只有你们是这一层的，后面新来的都要排队等下一轮”。

所以，你可以放心地使用这种简洁写法，它既准确又高效！



# 题637: 二层树的层平均值

```python
# 本题就是层序遍历的时候把一层求个总和再取一个均值。
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        queue = collections.deque([root])
        result = []
        while queue:
            level = []
            level_sum = 0
            level_size = len(queue)
            for i in range(level_size):
                cur = queue.popleft()
                level.append(cur.val)
                level_sum += cur.val # 注意: 此处每层的sum是加node的值,  而不是加1
                # if i == level_size-1: # 算每层的平均值, 不用判断是否是最后一个值, 而是直接在一层遍历完后算平均值即可!
                #     level_avg = level_sum / level_size
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            #result.append(level_avg)
            result.append(level_sum/level_size)
        return result
```



主要错在这几处（都是逻辑问题，不是语法）：

- collections 没导入：collections.deque 会报 NameError。
- level_sum += 1 你加的是次数，不是节点值，应该是 [level_sum += cur.val](https://file+.vscode-resource.vscode-cdn.net/Users/yichen/.vscode/extensions/openai.chatgpt-0.4.68-darwin-arm64/webview/#)。
- if i == level_size: 永远不会成立，因为 i 最大是 level_size - 1。
- level_avg 只在 if 里赋值，结果可能未定义就 append。

最小修法：

- 直接在 for 结束后 result.append(level_sum / level_size)
- 删掉 level 列表和那段 if i == level_size。



Q: 那为啥leetcode199题, 二叉树的右视图, 在取每层最后一个数的时候, 就会用到if i == level_size-1呢? 我这个算平均值就不用, 在for循环后面直接append呢

A: 因为“右视图”这道题只需要**每层一个特定节点**（最右边），所以你必须在遍历本层时识别“最后一个”。最直接的判断就是 if i == level_size - 1，此时把 [cur.val](https://file+.vscode-resource.vscode-cdn.net/Users/yichen/.vscode/extensions/openai.chatgpt-0.4.68-darwin-arm64/webview/#) 加进结果。

而“平均值”需要**本层所有节点**的和，只有把这一层全部遍历完才知道总和，所以自然是在 for 循环结束后统一 append(level_sum / level_size)。

总结：

- 右视图：要在**遍历过程中**抓到“最后一个” → 用 i == level_size - 1
- 平均值：要在**遍历结束后**拿到总和 → 循环外 append