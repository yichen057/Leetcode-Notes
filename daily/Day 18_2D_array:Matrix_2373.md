# 题2373: largest local values in a matrix-2D Array / Matrix

```python
# @lc code=start
# 二维矩阵滑动窗口问题
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        # 1. Initialize the matrix , matrix size: (n-2)*(n-2)
        # Create a matrix of all zeros using list comprehension. 使用列表推导式创建一个全 0 矩阵
        res = [[0]*(n-2) for _ in range(n-2)]

        # 2. Traverse each cell (i, j) in the result matrix
        for i in range(n-2):
            for j in range(n-2):

                # 3. examine the original grid for each res[i][j]
                # The two inner loops are responsible for searching for the maximum value within a 3x3 area.
                current_max = 0 # initialize the max value
                for x in range(i, i+3):
                    for y in range(j, j+3):
                        if grid[x][y] > current_max:
                            current_max = grid[x][y]

                # 4.Insert the maximum value found into the result.
                res[i][j] = current_max
        
        return res

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    # 测试一下 Example 1
    grid1 = [
        [9, 9, 8, 1],
        [5, 6, 2, 6],
        [8, 2, 6, 4],
        [6, 2, 2, 2]
    ]
   # 调用时需要加上 solution.
    result = solution.largestLocal(grid1)
    print(f"Result: {result}")
    # 进阶：使用 assert 自动校验
    expected1 = [[9, 9], [8, 6]]
    assert solution.largestLocal(grid1) == expected1, "测试用例 1 失败！"
    print("✅ 所有测试通过！")



```

### LeetCode 2373. Largest Local Values in a Matrix 题目解析

这道题在 CodePath 的练习册中对应的是 [Problem 8: Local Maximums](https://courses.codepath.org/courses/tip103/unit/1#!session_one)。它是一个经典的**二维矩阵滑动窗口**问题。

------

### 1. 题目大意

给你一个 $n \times n$ 的整数矩阵 `grid`。你需要生成一个大小为 $(n-2) \times (n-2)$ 的新矩阵 `res`。

新矩阵中的每一个元素 `res[i][j]`，都必须是原矩阵中**以 `grid[i+1][j+1]` 为中心**的 $3 \times 3$ 区域内的**最大值**。

**直观理解**：

想象一个 $3 \times 3$ 的“扫描框”，在原矩阵上从左到右、从上到下滑动。每滑动到一个位置，就找出框里的最大值，填入新矩阵。

------

### 2. 核心思路

#### A. 确定新矩阵的大小

如果原矩阵是 $n \times n$，那么 $3 \times 3$ 的框在水平方向能移动 $n-2$ 次，垂直方向也能移动 $n-2$ 次。所以：

- 初始化一个 $(n-2) \times (n-2)$ 的全 0 矩阵。

#### B. 遍历新矩阵的坐标

我们需要填充 `res[i][j]`，其中：

- `i` 的范围是 `0` 到 `n-3` (即 `range(n - 2)`)
- `j` 的范围是 `0` 到 `n-3` (即 `range(n - 2)`)

#### C. 寻找 $3 \times 3$ 区域的最大值

对于每一个确定的 `res[i][j]`，它对应的原矩阵 $3 \times 3$ 区域的左上角坐标恰好就是 `grid[i][j]`。

所以你需要再用两层嵌套循环来遍历这个小方块：

- 行：从 `i` 到 `i + 2`
- 列：从 `j` 到 `j + 2`

------

### 3. 解题步骤（伪代码思路）

1. 获取原矩阵长度 `n = len(grid)`。
2. 创建一个空的 `res` 列表（或使用列表推导式生成二维 0 矩阵）。
3. **外层循环**：遍历 `row` 从 `0` 到 `n-3`。
4. **中层循环**：遍历 `col` 从 `0` 到 `n-3`。
5. **核心逻辑**：
   - 设定一个变量 `current_max = 0`。
   - **内层嵌套循环**：遍历从 `row` 到 `row + 3` 和 `col` 到 `col + 3` 的小矩阵。
   - 不断更新 `current_max`。
6. 将找到的 `current_max` 填入 `res[row][col]`。
7. 返回 `res`。

------

### 4. 技巧提示

- **Python 的 `max()` 函数**：可以接受多个参数，比如 `max(current_max, grid[x][y])`。
- **切片法 (Advanced)**：如果你想写得更 Pythonic，可以使用切片。例如 `grid[x][col:col+3]` 可以取出一行中的三个数。但初学者建议先用**四层嵌套循环**（外层扫大阵，内层扫小阵）把逻辑理顺。

------

### 5. 举例 (Example 1)

输入：

Plaintext

```
[[9, 9, 8, 1],
 [5, 6, 2, 6],
 [8, 2, 6, 4],
 [6, 2, 2, 2]]
```

- 当 `i=0, j=0` 时，框住左上角 $3 \times 3$：`[[9,9,8], [5,6,2], [8,2,6]]`，最大值是 **9**。
- 当 `i=0, j=1` 时，框住右上角 $3 \times 3$：`[[9,8,1], [6,2,6], [2,6,4]]`，最大值是 **9**。
- ...以此类推，最终输出 `[[9, 9], [8, 6]]`。

**你可以尝试先写出代码，如果遇到索引（Index）报错或者逻辑卡住了，随时发给我，我帮你 Debug！**

既然你准备挑战这道矩阵题，这里我为你提供一份清晰的 Python 代码参考。

这段代码采用了**四层嵌套循环**的直观解法（两层移动窗口，两层在窗口内找最大值），这非常符合面试中向面试官展示思路的逻辑。

### LeetCode 2373 / CodePath Prob 8 参考实现

Python

```python
def local_maximums(grid):
    n = len(grid)
    # 1. 初始化结果矩阵，大小为 (n-2) x (n-2)
    # 使用列表推导式创建一个全 0 矩阵
    res = [[0] * (n - 2) for _ in range(n - 2)]
    
    # 2. 遍历结果矩阵的每一个格子 (i, j)
    for i in range(n - 2):
        for j in range(n - 2):
            
            # 3. 对于每一个 res[i][j]，我们需要查看原 grid 中
            # 以 (i, j) 为左上角的 3x3 区域
            current_max = 0
            
            # 内部两层循环负责在 3x3 区域内搜寻最大值
            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    if grid[x][y] > current_max:
                        current_max = grid[x][y]
            
            # 4. 将找到的最大值填入结果
            res[i][j] = current_max
            
    return res

# 测试一下 Example 1
grid1 = [
    [9, 9, 8, 1],
    [5, 6, 2, 6],
    [8, 2, 6, 4],
    [6, 2, 2, 2]
]
print(local_maximums(grid1)) 
# 预期输出: [[9, 9], [8, 6]]
```

------

### 💡 核心代码解析

1. **索引范围 `range(n - 2)`**：
   - 如果 `n=4`（如上例），`range(4-2)` 就是 `0, 1`。
   - 当 `i=1` 时，内层的 `range(i, i + 3)` 会走到 `1, 2, 3`，正好是原矩阵的最后一行，不会越界。
2. **`current_max` 的初始化**：
   - 因为题目给的是正整数，初始化为 `0` 或 `grid[i][j]` 都可以。
3. **时间复杂度分析**：
   - 外层两层循环跑了 $(n-2)^2$ 次。
   - 内层两层循环固定跑 $3 \times 3 = 9$ 次。
   - 总复杂度是 $O(n^2)$，对于这类矩阵题目来说是最优解。

### 🚀 进阶写法（Pythonic）

如果你想让代码看起来更高级（比如在面试中展示你对 Python 切片的熟练度），可以把内层两层循环替换为：

Python

```
# 替换内部的两层循环
for x in range(i, i + 3):
    current_max = max(current_max, max(grid[x][j:j+3]))
```

这里 `grid[x][j:j+3]` 直接切出了那一行中的三个数，然后用内置的 `max()` 快速比较。

你可以尝试先**手写**一遍基础版本，确保对 `i` 和 `j` 的边界控制完全理解。明天早上练习时，如果这道题能一遍跑通，说明你的矩阵索引逻辑已经过关了！

需要我再帮你梳理一下明天计划中那几道 **BST（二叉搜索树）** 的核心代码模板吗？那个部分的逻辑和矩阵完全不同。



Q: 遍历结果矩阵的每一个格子 (i, j)

​    for i in range(n - 2):

​        for j in range(n - 2):

这里遍历是为了填充这个结果矩阵吗? 那内部两层循环是为了找具体点位做判断? 给我举个例子, 我想知道这个循环流程

你的理解完全正确！为了让你彻底搞清楚这**四层循环**是怎么分工的，我们用一个最简单的例子来拆解流程。

### 1. 宏观分工

- **外两层循环 (`i`, `j`)**：负责**“定位”**。它们决定了 $3 \times 3$ 窗口的**左上角**在原矩阵的什么位置。每移动一次，就代表我们要填好结果矩阵 `res` 里的一个格子。
- **内两层循环 (`x`, `y`)**：负责**“扫描”**。当窗口固定后，这两层循环把窗口内的 9 个数字看一遍，算出最大值。

------

### 2. 举个例子：$4 \times 4$ 变 $2 \times 2$

假设原矩阵 `grid` 是 $4 \times 4$ 的，我们要生成 $2 \times 2$ 的 `res`。

#### **第一步：外层 `i=0, j=0`**

这时我们要填 `res[0][0]`。

- **窗口左上角**：`grid[0][0]`。
- **内部循环 (`x` 从 0-2, `y` 从 0-2)**：
  - 检查 `grid[0][0], grid[0][1], grid[0][2]`
  - 检查 `grid[1][0], grid[1][1], grid[1][2]`
  - 检查 `grid[2][0], grid[2][1], grid[2][2]`
- **得出最大值**，填入 `res[0][0]`。

#### **第二步：外层 `i=0, j=1`** (窗口向右滑动一格)

这时我们要填 `res[0][1]`。

- **窗口左上角**：`grid[0][1]`。
- **内部循环 (`x` 从 0-2, `y` 从 1-3)**：
  - 检查 `grid[0][1], grid[0][2], grid[0][3]`
  - 检查 `grid[1][1], grid[1][2], grid[1][3]`
  - 检查 `grid[2][1], grid[2][2], grid[2][3]`
- **得出最大值**，填入 `res[0][1]`。

#### **第三步：外层 `i=1, j=0`** (窗口回到左边，向下移动一格)

这时我们要填 `res[1][0]`。

- **窗口左上角**：`grid[1][0]`。
- **内部循环 (`x` 从 1-3, `y` 从 0-2)**：
  - ... 扫描这 9 个点，找出最大值填入 `res[1][0]`。

------

### 3. 动态流程图

想象你在玩拼图，`res` 矩阵是你的底板。

1. **外循环**：你的手拿着一个 $3 \times 3$ 的放大镜在地图（原矩阵）上平移。
2. **内循环**：放大镜停下后，你的眼睛在放大镜覆盖的 9 个格子里找最大的数字。
3. **赋值**：找到后，把这个数字写在底板（结果矩阵）对应的格子里。

### 4. 为什么要用 `n - 2`？

因为窗口本身占了 3 格。如果你的 `i` 走到了 `n-1`（最后一排），那么内部循环 `i + 3` 就会超出地图边界。

- 当 `i = n - 3` 时，内部循环最高能看到 `(n-3) + 2 = n-1`，刚好是地图的边缘，**这叫安全驾驶**。

------

### 💡 核心总结

- **外层 `i, j`** 是在规划 **“结果”**：我要填哪个坑？
- **内层 `x, y`** 是在执行 **“搜索”**：这个坑对应的 9 个数里谁最大？

这种“窗口滑动”的思想在图像处理（卷积神经网络）中非常常见。

**明早练习时，你可以试着在内层循环里加一个 `print(f"Checking grid[{x}][{y}]")`，你会亲眼看到这个 3x3 的小窗口是如何在矩阵里“跳舞”的。**

需要我帮你把这个逻辑和明天要做的另一道题 [Defuse the Bomb (Problem 8 V2)](https://courses.codepath.org/courses/tip103/unit/1#!session_one) 做个对比吗？那道题是“一维”的滑动。

Q: 测试语句解释

这句话是编程中非常有用的**“自动检查闹钟”**。它能让你不需要用肉眼去盯着屏幕比对结果，而是让程序自己判断对错。

拆解开来看，它的逻辑如下：

### 1. `expected1 = [[9, 9], [8, 6]]`

这行代码定义了**“标准答案”**。

- 你告诉 Python：如果代码写对了，跑完 `grid1` 的结果**应该**长成 `[[9, 9], [8, 6]]` 这个样子。

### 2. `assert ...` (断言)

`assert` 在英文里是“断言、坚称”的意思。在代码里，它的语法是：

> ```
> assert [判断条件], [错误提示信息]
> ```

- **它的核心逻辑是**：程序会检查 `largestLocal(grid1) == expected1` 是否为 **True**。
- **如果相等（True）**：程序就像什么都没发生一样，继续往后执行。
- **如果不相等（False）**：程序会**立刻报错并停止运行**，并在控制台打印出你写的那句 `"测试用例 1 失败！"`。

### 3. `print("✅ 所有测试通过！")`

这行代码只有在上面的 `assert` **成功通过**（没有报错）的情况下才会运行。

- 如果你运行程序后看到了这句话，说明你的代码逻辑和预期答案完全吻合。

------

### 💡 为什么要这么写？（对比演示）

**不用 assert 的写法（手动挡）：**

Python

```
result = largestLocal(grid1)
print(result) 
# 你得自己盯着屏幕看：这是 [[9, 9], [8, 6]] 吗？
# 如果你测试 100 组数据，眼睛会看瞎的。
```

**使用 assert 的写法（自动挡）：**

Python

```
assert largestLocal(grid1) == [[9, 9], [8, 6]]
assert largestLocal(grid2) == [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
print("✅ 全部通过") 
# 你只需要点一下运行。如果没有报错，就说明 100% 正确。
```

### 🚀 明早练习小贴士：

在做 [Problem Set Version 1](https://courses.codepath.org/courses/tip103/unit/1#!session_one) 的题目时，把网页给出的 **Example Output** 全部写成 `assert` 语句。这样你每写完一个功能，运行一下脚本，看到 `✅` 标志，心里就会非常有底气！

需要我帮你把 [Problem 8: Local Maximums](https://courses.codepath.org/courses/tip103/unit/1#session_one) 网页里的**两个**测试用例都写成这种 `assert` 格式吗？

Q: \# 使用列表推导式创建一个全 0 矩阵

​    res = [[0] * (n - 2) for _ in range(n - 2)]

展开推导, 如何做到填充0到matrix的

这个列表推导式（List Comprehension）是 Python 中非常优雅且高效的写法。为了让你透彻理解它是如何“填充”出一个二维矩阵的，我们把它**展开为标准的 `for` 循环**。

### 1. 逻辑展开（等价代码）

这段推导式：

```
res = [[0] * (n - 2) for _ in range(n - 2)]
```

实际上等价于以下逻辑：

Python

```python
# 假设 n = 4, 那么 n - 2 = 2
res = [] 

# 外层循环：决定有多少“行”
for _ in range(n - 2):
    
    # 这一步内部操作：创建一个包含 (n-2) 个 0 的新列表（一行）
    new_row = [0] * (n - 2)  # 相当于 [0, 0]
    
    # 将这一行存入 res 中
    res.append(new_row)
```

------

### 2. 深度拆解：它是如何一步步填充的？

我们以 `n = 5` 为例（即生成一个 $3 \times 3$ 的矩阵）：

#### 第一步：处理 `[0] * (n - 2)`

在 Python 中，列表乘以一个整数表示**重复**。

- `[0] * 3` 会立刻生成一个一维列表：`[0, 0, 0]`。
- 这就是矩阵的一条“横梁”（一行）。

#### 第二步：处理 `for _ in range(n - 2)`

这告诉 Python：“把上面的‘横梁’制作过程重复执行 3 次”。

#### 第三步：嵌套组装

1. **第一次循环**：生成 `[0, 0, 0]`，放入外层列表 $\rightarrow$ `[[0, 0, 0]]`
2. **第二次循环**：再生成一个 `[0, 0, 0]`，放入外层列表 $\rightarrow$ `[[0, 0, 0], [0, 0, 0]]`
3. **第三次循环**：再生成一个 `[0, 0, 0]`，放入外层列表 $\rightarrow$ `[[0, 0, 0], [0, 0, 0], [0, 0, 0]]`

------

### ⚠️ 一个非常重要的“坑”（面试必考）

你可能会想，既然 `*` 是重复，为什么不直接写 `res = [[0] * 3] * 3` 呢？

**千万不要这样做！**

- 如果你写 `[[0]*3] * 3`，Python 确实会给你 3 行，但它们其实是**同一个对象的 3 个引用（影子）**。
- 如果你修改了 `res[0][0] = 9`，你会发现**每一行**的第一个数字都变成了 9！

**而使用列表推导式 `for _ in range(...)` 的好处是：**

它在每一次循环时都会**重新创建一个全新的列表对象**，这样你修改第一行时，第二行才不会跟着变。

------

### 💡 总结

- **外层 `for`**：负责盖楼（增加行数）。
- **内层 `[0] \* k`**：负责铺地板（每一行填入 0）。
- **结果**：一个每一行都独立、互不干扰的全 0 矩阵。

明天早上的代码中，你可以先用这个推导式初始化 `res`，然后通过 `res[i][j] = current_max` 把真正的最大值填进去，替换掉原来的 0。

你想试着写一下明天要练习的 **Problem 6: Vegetable Harvest** 的代码吗？那题也是矩阵遍历，但比这题简单一点，可以用来练手。



Q: 用python.11会报错, 是不是还是得连最新的python环境:

def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:

这个问题**跟 Python 3.11 / 3.14 一点关系都没有**，你现在遇到的是一个**非常经典、非常基础、但新手必踩的坑** 👍

而且你已经把关键信息都截图出来了，我们直接对症下药。

------

## **先给你一句“定心丸”**

> ❌ **不是 Python 3.11 太旧**

> ❌ **不需要切回最新 Python**

> ✅ **是你少了一行 import**

------

## **报错在说什么？（翻成人话）**

你的报错是：

```
NameError: name 'List' is not defined
```

对应代码是这一行👇

```
def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
```

Python 的意思是：

> **我看到你写了 List，但你没告诉我 List 是什么**

------

## **为什么会这样？**

### **List**

###  **不是 Python 内置的**

- list（小写）✅ 是内置
- List（大写）❌ 不是内置

List 来自这里：

```
from typing import List
```

------

## **正确修法（两种，你选一种）**

### **✅ 方案一（最 LeetCode / 最推荐）**

在**当前 cell 最上面**加一行：

```
from typing import List
```

完整示例：

```
from typing import List

def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    res = [[0] * (n - 2) for _ in range(n - 2)]

    for i in range(n - 2):
        for j in range(n - 2):
            current_max = 0
            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    current_max = max(current_max, grid[x][y])
            res[i][j] = current_max

    return res
```

✔️ **Python 3.11 完全 OK**

✔️ LeetCode 官方就是这么写的

### **✅ 方案二（Python 3.9+ 的现代写法）**

你也可以**不用 typing.List**，直接用内置 list：

```
def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
```

📌 Python 3.11 **完全支持**

但注意：

- LeetCode 题解 / 模板 **更常见方案一**
- 初学阶段我更推荐 **方案一**

------

## **重点澄清一个“误解”（很重要）**

你刚才的判断是：

> “用 python.11 会报错，是不是得连最新 python？”

❌ **不是版本问题**

❌ **不是环境问题**

❌ **不是 VS Code / Notebook 的问题**

✅ **是 Python 类型注解的语法规则**

------

## **给你一个“刷题专用铁律”**

以后你在 Python 里看到：

```
List
Optional
Dict
Tuple
Set
```

👉 **第一反应就是：**

```
from typing import List, Optional, Dict, Tuple, Set
```

（用到哪个 import 哪个）



