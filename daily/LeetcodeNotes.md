# 📘 Leetcode Notes

统一记录所有题目的思路 & 总结。下面是一份 **`NOTES.md` 模板**，你可以直接放到仓库里（根目录），以后每刷一道题就在里面追加一段. 代码放在独立的 `.py` 文件，这里只写关键思路和复盘。

### 🚀 使用方法

1. 每刷一道题：

   - 在仓库根目录新建/修改 `NOTES.md`。
   - 复制上面一段模板，改成对应题目的编号 + 思路。

2. 对应代码放在单独的文件里，比如：

   ```
   php
   
   
   CopyEdit
   1.two-sum.py
   704.binary-search.py
   200.number-of-islands.py
   ```

这样你以后复习的时候，可以先扫 `NOTES.md` 里每道题的「思路 + 易错点」，再去看代码实现。

------

要不要我帮你写一个 **命令脚本**（比如 `new_note.py`），你输入题号+题名，它就自动往 `NOTES.md` 里追加一个空白模板？

---

## [1] Two Sum(返回元素版本)
- **题意**：在未排序的数组中找两个数，使它们的和等于目标值，返回这两个数。

- **思路**：哈希表存储“目标值 - 当前值”，边遍历边查找。

- **复杂度**：检测一个数在不在数组当中, 是用哈希表来实现. 实现方法是从左到右, 把每个数都往哈希表里丢进去一次, 检验下值在不在哈希表里: 时间 O(n)，空间 O(n), 因为哈希表不是作为输入也不是作为输出, 他是中间一个纯粹的耗费, 所以空间复杂度为O(n)

- **易错点**：
  - 不能用同一个元素两次。
  - 遍历时要先判断再存入字典。
  
  非常棒的问题 👏，我来帮你把 **Python** 和 **Java** 里的 HashSet（集合）用法梳理清楚。
  
  ------
  
  ## 1. Python 的集合（set）
  
  在 Python 里，集合类型叫做 **`set`**，本身就是内建类型，不需要导包。
  
  ### ✅ 创建方式
  
  ```python
  hashset = set()              # 创建一个空集合
  hashset = {1, 2, 3}          # 创建并初始化
  hashset = set([1, 2, 3, 3])  # 会自动去重，结果是 {1, 2, 3}
  ```
  
  ### ✅ 常见操作
  
  ```python
  hashset.add(4)       # 添加元素
  hashset.remove(2)    # 删除元素（不存在会报错）
  hashset.discard(2)   # 删除元素（不存在不会报错）
  print(3 in hashset)  # 判断是否存在，O(1) 时间
  ```
  
  ------
  
  ## 2. Java 的集合（HashSet）
  
  Java 没有内建集合，要用 **`HashSet`** 类（属于 `java.util` 包）。
  
  ### ✅ 创建方式
  
  ```java
  import java.util.Set;
  import java.util.HashSet;
  
  Set<Integer> set = new HashSet<>(); // 推荐写法（接口+实现）
  HashSet<Integer> set2 = new HashSet<>(); // 也可以
  ```
  
  > 你写的 `Set<Integer> set = new HashSet();` 差一点：
  
  - Java 泛型最好写上 `<Integer>`，避免“原始类型”警告。
    ✔ 正确写法：`Set<Integer> set = new HashSet<>();`
  
  ### ✅ 常见操作
  
  ```java
  set.add(1);          // 添加
  set.remove(2);       // 删除
  set.contains(3);     // 判断是否存在
  ```
  
  ------
  
  ## 3. Python vs Java 写法对比
  
  | 功能         | Python              | Java                                  |
  | ------------ | ------------------- | ------------------------------------- |
  | 创建空集合   | `hashset = set()`   | `Set<Integer> set = new HashSet<>();` |
  | 添加元素     | `hashset.add(x)`    | `set.add(x);`                         |
  | 删除元素     | `hashset.remove(x)` | `set.remove(x);`                      |
  | 判断是否存在 | `x in hashset`      | `set.contains(x)`                     |
  
  ------
  
  ## 4. 什么时候用 HashSet？
  
  当你需要：
  
  1. **去重**：自动保证元素唯一性
     - 例：找出数组里不同的数
  2. **快速查找**：判断某个元素是否存在，时间复杂度 **O(1)**
     - 例：两数之和 (Two Sum) → 用 HashSet 存已访问的数
  3. **集合操作**：交集、并集、差集（Python 有内置操作，Java 需要写逻辑）
     - 例：`set1 & set2`（交集），`set1 | set2`（并集）
  
  ------
  
  ✅ **总结**
  
  - Python：`hashset = set()`
  
  - Java：`Set<Integer> set = new HashSet<>();`
  
  - HashSet 适合 **去重 + 快速查找** 的场景，是算法题里常用的结构（尤其是数组、字符串处理）。
  
    ```python
    class Solution:
        def twoSum(self, nums: List[int], target: int) -> List[int]:
            hashset = set()
            for num in nums:
                # [2,4,5], target = 8, 如果在这里直接给hashset添加元素, 会错误返回[4,4]
                if target - num in hashset:
                    return num, target-num
                hashset.add(num)
            return [-1, -1]    
    ```
  
    

---

## [1] Two Sum(返回索引版本)

- **题意**：在未排序的数组中找两个数，使它们的和等于目标值，返回这两个数所在的索引index。

- **思路**：哈希表存储“目标值 - 当前值”，边遍历边查找。

- **复杂度**：检测一个数在不在数组当中, 是用哈希表来实现. 实现方法是从左到右, 把每个数都往哈希表里丢进去一次, 检验下值在不在哈希表里: 时间 O(n)，空间 O(n), 因为哈希表不是作为输入也不是作为输出, 他是中间一个纯粹的耗费, 所以空间复杂度为O(n)

- **易错点**：

  - 不能用同一个元素两次。
  - 遍历时要先判断再存入字典。

  非常棒的问题 👏，我来帮你把 **Python** 和 **Java** 里的 HashSet（集合）用法梳理清楚。

  太好了 👍，你写的这个 `twoSum` 已经是 **最经典的哈希表解法**了。我来分三部分给你解释：

  ------

  ## 1. Python 里的 `dict`（哈希表 / HashMap）

  ```python
  seen = {}
  ```

  - 在 Python 中，`dict` 就是哈希表（相当于 Java 里的 `HashMap<K,V>`）。

  - 它存储的是 **键值对**，查找和插入的平均时间复杂度都是 **O(1)**。

  - 语法：

    ```python
    seen[key] = value    # 插入或更新
    seen[key]            # 取值（key 不存在会报错）
    seen.get(key, -1)    # 取值（key 不存在返回默认值 -1）
    key in seen          # 判断 key 是否存在
    ```

  在 `twoSum` 里：

  ```python
  seen[num] = i
  ```

  表示存储：**当前数值 `num` → 它的索引 `i`**。
  这样如果以后遇到 `target - num`，就能马上找到之前那个数的下标。

  ------

  ## 2. 什么时候用哈希表？

  哈希表适合以下场景：

  1. **需要快速查找是否存在某个元素**
     - 例：查找数组里是否有重复元素（Contains Duplicate）。
  2. **需要把一个值映射到另一个值**
     - 例：在 Two Sum 里，把数值 `num` 映射到它的索引 `i`。
  3. **需要统计频率**
     - 例：统计字符串里每个字符出现的次数（`collections.Counter` 本质也是哈希表）。

  总结：当你需要 **“快速查找”** 或 **“键值映射”**，就该考虑哈希表。

  ------

  ## 3. `enumerate()` 的语法

  在 Python 里，遍历列表时默认只能拿到值：

  ```python
  for num in nums:
      ...
  ```

  如果还想要下标，就要用 `enumerate()`：

  ```python
  for i, num in enumerate(nums):
      print(i, num)
  ```

  输出：

  ```
  0 2
  1 4
  2 5
  ```

  这里 `enumerate(nums)` 返回一个迭代器，里面是 `(索引, 元素)` 的元组。
  所以 `for i, num in enumerate(nums)` 会自动解包成 `i` 和 `num`。

  > 相当于 Java 里的：
  >
  > ```java
  > for (int i = 0; i < nums.length; i++) {
  >     int num = nums[i];
  > }
  > ```

  ------

  ## 4. 回到 `twoSum` 的逻辑

  结合上面这些：

  ```python
  for i, num in enumerate(nums):        # i=索引, num=当前数
      complement = target - num         # 需要的补数
      if complement in seen:            # 看之前有没有出现过
          return [seen[complement], i]  # 返回补数的下标 + 当前下标
      seen[num] = i                     # 没出现过就记录下来
  ```

  这样保证了一次遍历就能解决问题，时间复杂度 O(n)，空间复杂度 O(n)。

  ------

  ✅ **总结**

  - `dict` = Python 的哈希表，适合做 **快速查找、映射、统计**。
  - `enumerate()` 用来同时拿到 **索引 + 值**，比 `range(len(nums))` 更优雅。
  - 在 `twoSum` 里：`dict` 保存 “数值 → 索引”，`enumerate()` 给我们 “索引 + 当前数”，两者配合正好解决问题。

  ------

  要不要我再帮你写一版 **对比代码**：

  - **不用哈希表的暴力解法**（O(n²))
  - **用哈希表的解法**（O(n))

  这样你就能直观体会为什么这里需要用 HashMap（dict）

---

## [5] Longest Palindromic Substring

- **题意**：给定一个String, 找出它的longest 回文子串, 假定只有一个满足条件的最长回文串。

- 回文的定义：字符串 **从左往右** 和 **从右往左** 完全相同。

- SubString是子串, 连续字符, O(n^2); SubSequence 子序列, 非连续字符, O(2^n)

- **思路**：for 起点   O(n)

  ​		for 终点   O(n)

  ​			检测中间的子串是不是一个回文串    O(n)

  这种算法的时间复杂度是 O(n^3), 太暴力了, 面试通不过

  双指针算法: 

  - 相向型双指针(最常用). 如果left指针==right指针, 则L向右挪一格, R向左挪一格, 再比较是否相等, 不相等就退出, 相等就继续直到LR指针相遇为止

  abcd

  ^    ^

  L    R

  - 同向型双指针
  - 逆向/背向型双指针

- **复杂度**：时间 O(n^3)。待优化

- **优化算法: **

  1) \#基于中心点枚举法Enumeration: Expand around center, 该方法整合了上述算法的重复部分,用到了tuple二元组

     在暴力算法中, 找出浪费的算法, 把它优化掉,使用背向双指针法, 从中间出发往两边走

     背向双指针法,核心思想就是 以每个位置为中心，不断向两边扩展，找最大回文。时间复杂度 O(n²)，空间复杂度 O(1)

- 举例: x|a|b|b|a|c, 有n-1个偶数长度的回文串中心点

  ​                  ^  ^

  ​                  L  R

  当字母相等时, 两个指针分别往两边走, 而不是往中间走. L往左走, R往右走, 直到字母x和c不相等

- 举例: x|abcba|y, 有n个奇数长度的回文串中心点

  好嘞 👍 我来把 `"xabcbay"` 的 **整个 for 循环过程**整理成表格，把每个 `mid` 下奇数中心和偶数中心的 `get_palindrome_from` 结果都列出来。

  ------

  ### 字符串

  ```
  s = "x a b c b a y"
  index= 0 1 2 3 4 5 6
  ```

  ------

  ### 遍历过程

  | mid  | 中心字符 | 奇数中心 (mid, mid) | 返回结果 | 偶数中心 (mid, mid+1) | 返回结果 |
  | ---- | -------- | ------------------- | -------- | --------------------- | -------- |
  | 0    | `'x'`    | `"x"`               | (1, 0)   | `'x','a'` 不相等      | (0, 1)   |
  | 1    | `'a'`    | `"a"`               | (1, 1)   | `'a','b'` 不相等      | (0, 2)   |
  | 2    | `'b'`    | `"b"`               | (1, 2)   | `'b','c'` 不相等      | (0, 3)   |
  | 3    | `'c'`    | `"abcba"`           | (5, 1)   | `'c','b'` 不相等      | (0, 4)   |
  | 4    | `'b'`    | `"bcb"`             | (3, 3)   | `'b','a'` 不相等      | (0, 5)   |
  | 5    | `'a'`    | `"a"`               | (1, 5)   | `'a','y'` 不相等      | (0, 6)   |
  | 6    | `'y'`    | `"y"`               | (1, 6)   | 越界                  | (0, 7)   |

  ------

  举例: mid = 0 时的两次调用

  1. **奇数中心 `(0,0)` → `'x'`**
     - `get_palindrome_from` 返回 `(1,0)`
     - 比较：`max((0,0), (1,0))`
     - Python 的元组比较规则是 **先比第一个元素（长度）**，大的为大；如果相等，再比第二个元素。
     - 所以 `(1,0)` > `(0,0)` → 更新为 `(1,0)`。
  2. **偶数中心 left=0, right=1,length=right-left-1=0, start=left+1=1`(0,1)` → `'x','a'`**
     - 返回 `(0,1)`
     - 比较：`max((1,0), (0,1))`
     - 因为 `(1,0)[0] = 1` > `(0,1)[0] = 0`，所以 `(1,0)` 更大。

  ------

  ### 最终结果

  当 **mid=0** 时，`answer = (1,0)`。
  表示当前找到的最长回文子串是 `"x"`（长度 1，从 index=0 开始）。

  ------

  ✅ 总结：

  - **mid=0 时，answer 最终取 `(1,0)`**
  - 偶数中心不匹配 `(0,1)` 不会影响结果，因为长度 0 < 长度 1。

  ### 结果解读

  - `mid=3` 时，奇数中心 `"c"` 扩展出 `"abcba"`，返回 **(5, 1)** → 表示长度 5，从 index=1 开始。
  - 其他位置要么长度只有 1，要么偶数中心直接返回 `(0, start)`。
  - 最终 `answer = (5, 1)`，得到最长回文子串 `"abcba"`。

  ------

  ✅ 所以：

  - **偶数中心不匹配时**，不是 `(-1,0)`，而是 `(0, left+1)`。
  - **奇数中心最少也会返回 1**（自己）。
  - `max` 每次会挑最长的那个。

  这个问题问得非常关键 👍。我们来拆解一下 `length = right - left - 1` 为什么要这样写。

  ------

  ### 回忆函数逻辑

  ```python
  while left >= 0 and right < len(s) and s[left] == s[right]:
      left -= 1
      right += 1
  return right - left - 1, left + 1
  ```

  这里有一个细节：**while 循环结束时，`left` 和 `right` 已经往外多走了一步**。
  所以最后计算长度时，必须把这“一步”抵消掉。

  ------

  ### 举例：回文 `"abcba"`

  ```
  s = "xabcbay"`，中心 `mid=3 ('c')
  ```

  1. 初始：`left=3, right=3`
     - 匹配 `'c'=='c'` → OK
     - 更新 `left=2, right=4`
  2. 第二轮：`s[2]=='b', s[4]=='b'` → OK
     - 更新 `left=1, right=5`
  3. 第三轮：`s[1]=='a', s[5]=='a'` → OK
     - 更新 `left=0, right=6`
  4. 第四轮：`s[0]=='x', s[6]=='y'` → 不相等 → 停止

  此时：

  - `left=0, right=6`（注意，已经“走过头”了）
  - 实际有效的回文范围应该是 **`[left+1, right-1]` → `[1,5]`**

  ------

  ### 长度计算

  - 回文的起始下标 = `left+1 = 1`
  - 回文的结束下标 = `right-1 = 5`
  - 长度 = `(right-1) - (left+1) + 1`
    = `right - left - 1` ✅

  所以必须写 `right - left - 1`，而不是 `+1`。

  ------

  ### 如果写 `+1` 会怎样？

  假设写成：`length = right - left + 1`

  那上例中：

  - `right=6, left=0`
  - 长度 = `6 - 0 + 1 = 7` ❌（错误，明明最长回文只有 5）

  就会算“走过头”的部分。

  ------

  ✅ 总结：

  - **`-1` 是为了抵消 while 最后多走的一步**
  - 正确长度公式：`length = right - left - 1`

  

  

  2. #区间型动态规划法求解, 时间复杂度O(n^2), 空间复杂度O(n^2)
     #这是 DP 的核心！我们怎么用小问题的答案，来推导出大问题的答案呢？思考一下，一个字符串（比如 "ababa"）怎么样才算是回文串？它两头的字符必须相同 (第一个 'a' 和最后一个 'a')。

     去掉两头字符后，中间的部分也必须是回文串 ("bab")。

     于是，我们的“组合规则”就诞生了：

     dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]

     翻译成人话就是：s[i...j] 是不是回文串，取决于 ① 两头字符 s[i] 和 s[j] 是否相等，并且 ② 它中间的部分 s[i+1...j-1] 是不是回文串。

     #动态规划解决这个问题的过程就像填表：

     创建一张空表 dp。

     先把对角线（长度为1）和它旁边（长度为2）的答案填上。

     然后根据 dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1] 这个规则，从表里已有的答案，斜着向外推导出新的答案。

     在填表的过程中，顺手记录下你找到的最长的那个回文串。

     填完表，答案也就出来了。

     Think of the DP table (2D matrix):

     i = row (start index, top→down is bigger i).

     j = col (end index, left→right is bigger j).

     We need to fill the table bottom-left → top-right diagonals.

     That’s why i goes down to up (so dependencies are available).

     And j goes left → right for each row.

- **易错点**：

  - 没有考虑edge case。
  - 变量名定义的不直观.
  - 嵌套太多, 三层循环。
  - 没有空格和空行.
  - 代码有重复, 全局变量也要少写

- **知识点**：

  ## 什么是二元组

  在 Python 里，`tuple`（元组）是一种**不可变序列类型**。
  所谓 **二元组**，就是长度为 **2** 的元组。

  ```
  python
  
  
  CopyEdit
  pair = (3, 5)
  print(pair[0])  # 3
  print(pair[1])  # 5
  ```

  特点：

  - 用小括号 `()` 表示。
  - 元素可以是任意类型（数字、字符串、列表、对象……）。
  - 不可变：创建后不能修改元素。

---

## [Lintcode13] Implement strStr()

- **题意**：For a given `source` string and a `target` string, you should output the first index(from `0`) of target string in the source string.If the target does not exist in source, just return `-1`.

- **思路**：target为空, 返回0; 把i当作target在source里的起点位置, j是range(len(target)), 双层循环, 直到找到target的string完全相等, 则返回i, 否则返回-1

  

  优化方法1:  考虑越界情况, 且用逐字符比较的方式节省空间提升效率

  优化方法2: 字符串与字符串的比较的, 由于是需要逐个字符去比, 最差的时间复杂度是O(n)

  但是整数与整数比较, 时间复杂度是常数级O(1), 由于整数的值在机器里是固定宽度表示（在 C 实现里底层存的是二进制位），所以比较开销就是**常数时间**。

  所以考虑可以引进Hash function, 哈希表的数据结构中, 把任何的结构变成整数. 一张哈希表可以看做是一个大数组, 需要用一个hash function把string对应到某一个位置上, 下次String再来的时候, 可以直接去这个位置上去找, 是否存在于数组当中. 可使用静置转换的形式去做hash function

  Eg: abcde, 任何一个字符是可以用0-255的整数表示, 不需要做类型转换就可以和整数相乘, 乘出来的结果也是整数.乘多少都可以, 31可以当作match number, 常用来做静置转换的基数(经验值).  hashcode of abcde=a x 31^4 + b x 31^3 + c x 31^2 + d x 31 + e x 31^ 0, 将字符串转换成整数,下次再调用hashFunction, 还是同一个值. 但是同一个整数, 对应的字符串就不唯一了. hashfunction只保证key->value唯一即可. 如果结果很大, 可以对结果取模, (hashcode of abcde)%(10^6)

- **复杂度**：

  时间复杂度：O(n·m), 暴力匹配 (Brute Force)。

  空间复杂度：O(1), 除了循环变量 i、j 和常数标志，没有额外使用数据结构。除了循环变量 i、j 和常数标志，没有额外使用数据结构。

- **易错点**：

  - 未考虑i+len(target)可能越界超出len(source)的情况, python不会报错, java会报错; 

  - 另外一个可优化空间是: subString(java)或者str[i:j]这种切片, 都是新创建的字符串对象, 会额外增加空间复杂度, 用每次都切片再比较, 效率上比直接逐字符比较要差

  - 考虑边界情况

  - python中for...else的用法: Python 的 for-else 语义是：

    for-else 的 else 不是跟 if 配对，而是跟 整个循环 配对。

    当 for 循环执行完且没有被 break 打断时，执行 else。当循环没有执行完且没有触发break时, 继续循环

    它并不是「每次循环里判断一次」，而是「等整个循环执行结束后，再决定是否执行 else」。

     #为什么 Python 要这样设计？

    目的是解决「搜索 / 查找」这类场景：

    如果找到了目标 → break。

    如果整个循环都没找到 → else。

    如果 else 写在 break 前，就变成了普通的 if-else，失去了「循环结束后才判断」的特性。

## 

- **题意**：在有序数组中查找目标值，若存在返回下标，否则 -1。
- **思路**：二分查找，维护左右边界，逐步缩小范围。
- **复杂度**：时间 O(log n)，空间 O(1)。
- **易错点**：
  - while 循环条件写成 `<=` 而不是 `<`。
  - mid 计算 `(left + right) // 2`，避免死循环。

---

## [125] Valid Palindrome
- **题意**：判断一个字符串忽略大小写和非法字符之后是否是一个回文串
- **思路**：相向双指针法。
- **复杂度**：**时间复杂度**：每个字符最多被比较一次或两次 → `O(n)`；空间复杂度 `O(1)`, 因为双指针法不占用额外空间, 不生成新的数据结构 。
- **易错点**：
  
  如下

------

## 1. 实例方法（非 `static`）

定义时 **没有 `static`** 的方法，例如：

```java
public class Dog {
    public void bark() {
        System.out.println("woof");
    }
}
```

- 调用时必须有一个对象实例：

  ```java
  Dog d = new Dog();
  d.bark();   // ✅ 正确
  Dog.bark(); // ❌ 错误，不能用类名直接调用
  ```

- 在同一个类的其他实例方法里，可以省略 `this.`：

  ```java
  public void play() {
      bark();         // ✅ 编译器默认理解为 this.bark()
      this.bark();    // ✅ 等价
  }
  ```

------

## 2. 静态方法（`static`）

定义时 **带 `static`**，属于类本身，而不是某个对象。例如：

```java
public class MathUtil {
    public static int square(int x) {
        return x * x;
    }
}
```

- 调用时推荐用类名：

  ```java
  int result = MathUtil.square(5); // ✅ 推荐写法
  ```

- 在同一个类里，可以直接调用，不需要类名：

  ```java
  public static void main(String[] args) {
      square(5); // ✅ 等价于 MathUtil.square(5)
  }
  ```

------

## 3. 特殊情况：标准库里的工具类方法

比如你之前问的：

```java
Character.isLetter(c);
Character.toLowerCase(c);
Math.max(a, b);
Arrays.sort(arr);
```

这些都是 **静态方法**，所以必须用类名调用（`Character.`、`Math.`、`Arrays.`）。

------

## 4. 规则总结

- **实例方法** → 需要对象调用：`obj.method()`；在类内部可以省略写成 `method()` 或 `this.method()`。
- **静态方法** → 推荐用类名调用：`ClassName.method()`；在类内部可以省略类名直接调用。

------

👉 所以你可以用一句话记住：

- **有 `static` → 属于类 → 用类名调用（推荐）**
- **没 `static` → 属于对象 → 需要对象调用**

------

好问题 👍，我来帮你彻底搞清楚。

------

### 1. 在 **同一个类** 内部

如果你在 **`Character` 类里面写代码**（比如 JDK 源码开发者在写 `Character` 本身），那么调用它的静态方法时，类名可以省略：

```java
// 假设现在就在 Character 类内部
isLetter(c);        // 等价于 Character.isLetter(c)
toLowerCase(c);     // 等价于 Character.toLowerCase(c)
```

------

### 2. 在 **别的类** 里用

你写业务代码的时候，大部分情况都是在 **别的类**里调用 `Character`、`Math`、`Arrays` 这些工具类。

- 这时候 **必须写类名**，因为它们是别的类的静态方法。

例如：

```java
public class Demo {
    public static void main(String[] args) {
        char c = 'A';
        System.out.println(Character.isLetter(c)); // ✅ 正确
        System.out.println(Character.toLowerCase(c)); // ✅ 正确

        int max = Math.max(3, 5);  // ✅ 正确
        int[] arr = {3, 1, 2};
        Arrays.sort(arr);          // ✅ 正确
    }
}
```

如果你直接写 `isLetter(c)`，编译器会报错，因为当前类里没有这个方法。

------

### 3. 能不能省略类名？

有两种方式可以“省略”：

#### ✅ 方式一：**静态导入 (static import)**

```java
import static java.lang.Character.isLetter;
import static java.lang.Character.toLowerCase;
import static java.lang.Math.max;
import static java.util.Arrays.sort;

public class Demo {
    public static void main(String[] args) {
        char c = 'A';
        System.out.println(isLetter(c));      // 类名省略了
        System.out.println(toLowerCase(c));   // 类名省略了

        int m = max(3, 5); // 类名省略了
        int[] arr = {3, 1, 2};
        sort(arr);         // 类名省略了
    }
}
```

#### ✅ 方式二：**在相同类里面**

比如在 `Math` 类内部，直接调用 `max(a,b)` 就行（JDK 源码里就是这样）。

------

### 结论 ✅

- **默认情况下（你写业务代码时）类名不能省略**。
- **想省略** → 只能用 `static import`，或者你就在那个类里面。

------

### 1. `Character` 可以是数字吗？

在 Java 里，`char` 类型表示 **任意一个 Unicode 字符**，不仅仅是字母，还可以是数字、符号、甚至中文。

比如：

```java
char c1 = 'A';  // 字母
char c2 = '3';  // 数字字符
char c3 = '$';  // 符号
char c4 = '中'; // 汉字
```

所以 **`Character` 完全可以是数字字符**。

------

### 2. `isEqual(char a, char b)` 比较数字行不行？

来看你的方法：

```java
private boolean isEqual(char a, char b) {
    return Character.toLowerCase(a) == Character.toLowerCase(b);
}
```

- 如果 `a` 和 `b` 是字母，`toLowerCase` 会把它们都转成小写再比较。
  例如 `'A'` 和 `'a'` → `'a' == 'a'` → `true`。
- 如果 `a` 和 `b` 是数字字符，比如 `'3'` 和 `'3'`，那么 `toLowerCase` 不会改变它们，直接比较 `'3' == '3'`，结果也正确。
- 如果 `a` 和 `b` 是数字和字母混合，比如 `'3'` 和 `'a'`，自然返回 `false`。

✅ 所以：**数字可以直接比较，不会出错**。

------

### 3. `Character.toLowerCase()` 可以传数字吗？

可以传！

- `Character.toLowerCase('A')` → `'a'`
- `Character.toLowerCase('a')` → `'a'`
- `Character.toLowerCase('3')` → `'3'`（不会改变，因为不是字母）
- `Character.toLowerCase('$')` → `'$'`（同样不会改变）

也就是说，**`toLowerCase` 对非字母字符不会报错，只是原样返回**。

------

### 4. 结合你的代码

所以在 `isPalindrome` 里：

- 如果字符串里全是数字（例如 `"12321"`），`isValid` 会判断为合法字符，`isEqual` 直接比较 `'1'=='1'`，结果完全正确。
- `toLowerCase` 对数字没影响，只是做了“保险处理”，保证字母比较时不区分大小写。

------

✅ **总结**

- `char` 可以是数字字符。
- `isEqual` 方法可以比较两个数字，没问题。
- `toLowerCase` 传数字不会报错，会原样返回。

------

要不要我给你写一段小测试代码，打印出 `Character.toLowerCase()` 对 **字母/数字/符号**的结果，这样你就能直观看到效果？

------

## 📌 用法

1. 把 `new_note.py` 放到你的仓库根目录（和 `NOTES.md` 在同一级）。

2. 每次想给新题加笔记，只需运行：

   ```bash
   python3 new_note.py 704 "Binary Search"
   ```

3. 它会在 `NOTES.md` 末尾自动追加一段空模板：

```markdown
---

## [704] Binary Search
- **题意**：
- **思路**：
- **复杂度**：时间 O()，空间 O()
- **易错点**：
```

------

这样你就不用每次手动复制粘贴模板了 🚀。

要不要我帮你再写一个配套的 `new_code.py` 脚本？输入题号+题名，它会生成对应的 `.py` 文件，里面自带你喜欢的 `# @lc` 代码模板。



------

## **[680]. Valid Palindrome II（最多删一个字符成为回文）**

- **题意**：判断一个字符串忽略大小写和非法字符之后是否是一个回文串

- **思路**：

  先找“第一处不同”；

  然后尝试**删左**或**删右**其中一边；

  只要有一个删法能让剩下的区间是回文，就返回 `True`。

- **复杂度**：**时间复杂度**：每个字符最多被比较一次或两次 → `O(n)`；空间复杂度 `O(1)`, 因为双指针法不占用额外空间, 不生成新的数据结构 。

- **易错点**：

  - 要注意边界条件。

  - 要注意避开重复内容

  - 当发现不同字符时，应该尝试跳过左或右各一次。

    所以我们不能只返回布尔值，而是需要**第一次发现不同的位置**。

  下面这段代码是 **LeetCode 680. Valid Palindrome II（最多删一个字符成为回文）** 的一种写法。
  我按**函数—>语句块—>关键语法**的顺序，给你“新手友好版”逐行讲解。

  ------

  ## 代码（方便你对照讲解）

  ```python
  class Solution:
      def validPalindrome(self, s):
          if s is None:
              return False
  
          left, right = self.findDifference(s, 0, len(s) - 1)
          if left >= right:
              return True
  
          return self.isPalindrome(s, left + 1, right) or \
                 self.isPalindrome(s, left, right - 1)
  
      def isPalindrome(self, s, left, right):
          left, right = self.findDifference(s, left, right)
          return left >= right
  
      def findDifference(self, s, left, right):
          while left < right:
              if s[left] != s[right]:
                  return left, right
              left += 1
              right -= 1
          return left, right
  ```

  ------

  ## 顶层结构

  ### `class Solution:`

  - **定义类**。LeetCode 的 Python 题默认会实例化这个类并调用其中的方法。

  ------

  ## 主函数：`validPalindrome(self, s)`

  入口：判断字符串 `s` 是否能**删除最多一个字符**后变成回文。

  ```python
  def validPalindrome(self, s):
  ```

  - 定义成员方法；`self` 是**实例自身**的引用（Java 里的 `this`）。

  ```python
      if s is None:
          return False
  ```

  - `is` 比较**对象身份**（是否就是同一个对象），这里检查是否为 `None`。
  - `return False`：如果没有字符串，直接返回不是回文。

  ```python
      left, right = self.findDifference(s, 0, len(s) - 1)
  ```

  - **多重赋值**：一次接收两个返回值（Python 支持返回元组）。
  - 从左右指针 `0` 和 `len(s)-1` 开始，找到**第一对不相等的下标**（如果没有不相等，就会返回最终相遇的位置）。

  ```python
      if left >= right:
          return True
  ```

  - 如果没有发现不等（或已经互相越过），说明原串本来就是回文，直接 `True`。

  ```python
      return self.isPalindrome(s, left + 1, right) or \
             self.isPalindrome(s, left, right - 1)
  ```

  - **核心思想**：第一次遇到不等时，我们**最多能删一个字符**。
    - 方案 A：**跳过左边**这个字符（`left+1`）看看剩下的是否回文。
    - 方案 B：**跳过右边**这个字符（`right-1`）看看剩下的是否回文。
  - `or`：只要有一个方案成立，就返回 `True`。
  - 反斜杠 `\`：行连接符，让长语句换行更美观（也可以用括号包起来就不需要 `\` 了）。

  ------

  ## 子函数：`isPalindrome(self, s, left, right)`

  检查区间 `[left, right]` 是否是**严格回文**（这一步不再允许删除）。

  ```python
  def isPalindrome(self, s, left, right):
      left, right = self.findDifference(s, left, right)
  ```

  - 仍旧调用“找第一处不等”的函数。

  ```python
      return left >= right
  ```

  - 如果能一路匹配到两个指针相遇/交错，说明该区间是回文。
  - **为什么这样判断？**
    - `while left < right` 循环结束只有两种可能：
      1. 提前返回（遇到不等）→ 不会走到这里；
      2. `left >= right`（整个区间匹配完成）→ 回文。

  ------

  ## 工具函数：`findDifference(self, s, left, right)`

  从两端向中间走，**找到第一对不相等字符的下标**；若始终没差异，返回最终的相遇位置。

  ```python
  def findDifference(self, s, left, right):
      while left < right:
  ```

  - **循环条件**：两个指针还没有相遇/交错就继续。

  ```python
          if s[left] != s[right]:
              return left, right
  ```

  - 一旦发现**不相等**，马上把这对下标返回（给调用者决定删哪一边）。

  ```python
          left += 1
          right -= 1
  ```

  - 指针内收：匹配通过就往中间推进。

  ```python
      return left, right
  ```

  - 能走到这里说明**从未遇到不等**，返回的是**最终相遇位置**（意味着该区间是回文）。

  ------

  ## 关键语法/知识点回顾

  - **多重返回值**：`return left, right` 实际返回一个元组 `(left, right)`；左侧可用 `a, b = ...` 解包。
  - **短路求值**：`A or B` 当 `A` 为真时不会计算 `B`，节省时间。
  - **指针法**：`left`、`right` 两端向中间移动，典型的回文/对撞指针套路。
  - **时间复杂度**：每个字符最多被比较一次或两次 → `O(n)`；空间 `O(1)`。

  ------

  ## 一句话总结

  - 先找“第一处不同”；
  - 然后尝试**删左**或**删右**其中一边；
  - 只要有一个删法能让剩下的区间是回文，就返回 `True`。

  如果你愿意，我可以把这份代码换成**带超详细中文注释版**或改成 **Java / C++** 对照实现，帮你更牢固地理解。