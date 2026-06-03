可以。你现在可以把 **Two Pointers 双指针** 分成三大类来记：

```text
Two Pointers 双指针
├── 1. 相向双指针：left 从左，right 从右，往中间走
├── 2. 同向双指针 + Sliding Window：维护连续窗口
└── 3. 同向双指针但不一定是窗口：一个指针扫描，一个指针记录/放置/追赶
```

你之前主要学的是第 2 类：sliding window。现在我们补齐第 1 类和第 3 类。

------

# **一、相向双指针 Opposite Direction Two Pointers**

## **1. 适用题型**

相向双指针通常用于：

```text
数组 / 字符串两端向中间靠近
```

常见关键词：

```text
sorted array
palindrome
two sum in sorted array
3Sum / 4Sum
reverse
partition
```

典型题：

| **题目**                        | **类型**          |
| ------------------------------- | ----------------- |
| LC 125 Valid Palindrome         | 左右检查是否回文  |
| LC 167 Two Sum II               | 有序数组两数和    |
| LC 15 3Sum                      | 排序 + 相向双指针 |
| LC 11 Container With Most Water | 两边往中间夹      |
| LC 344 Reverse String           | 原地反转字符串    |

------

## **2. 基础模板**

```python
left = 0
right = len(nums) - 1

while left < right:
    # 根据 nums[left] 和 nums[right] 的关系做判断
    
    if condition:
        ...
    elif need_move_left:
        left += 1
    else:
        right -= 1
```

核心问题是：

每一轮你要决定：移动左指针，还是移动右指针？

------

# **二、相向双指针模板 1：回文判断**

## **适用场景**

题目问：

```text
是否是 palindrome
左右字符是否对称
忽略大小写 / 非字母数字字符
```

## **模板**

```python
left = 0
right = len(s) - 1

while left < right:
    if s[left] != s[right]:
        return False

    left += 1
    right -= 1

return True
```

## **代表题：LC 125 Valid Palindrome**

如果要跳过非字母数字字符：

```python
class Solution:
    # Opposite-direction two pointers
    # TC: O(n)
    # SC: O(1)
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
```

### **记忆点**

```text
相向双指针判断回文：
左边找有效字符；
右边找有效字符；
比较；
相等就一起往中间走。
```

------

# **三、相向双指针模板 2：有序数组 Two Sum**

## **适用场景**

题目给你：

```text
sorted array
target
找两个数的和
```

## **为什么相向双指针有效？**

因为数组有序。

假设：

```python
total = nums[left] + nums[right]
```

如果：

```text
total < target
```

说明当前和太小。为了变大，只能让：

```python
left += 1
```

如果：

```text
total > target
```

说明当前和太大。为了变小，只能让：

```python
right -= 1
```

## **模板**

```python
left = 0
right = len(nums) - 1

while left < right:
    total = nums[left] + nums[right]

    if total == target:
        return [left, right]
    elif total < target:
        left += 1
    else:
        right -= 1
```

## **代表题：LC 167 Two Sum II**

```python
class Solution:
    # Opposite-direction two pointers on a sorted array
    # TC: O(n)
    # SC: O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]

            if total == target:
                return [left + 1, right + 1]
            elif total < target:
                left += 1
            else:
                right -= 1

        return [-1, -1]
```

------

# **四、相向双指针模板 3：3Sum / 去重组合题**

## **适用场景**

题目要求：

```text
找多个数之和等于 target
返回所有不重复组合
```

典型：

```text
LC 15 3Sum
LC 18 4Sum
```

## **基本思路**

3Sum 可以拆成：

```text
固定一个数 nums[i]
剩下两个数用 Two Sum II 的相向双指针
```

## **模板**

```python
nums.sort()
res = []

for i in range(len(nums)):
    if i > 0 and nums[i] == nums[i - 1]:
        continue

    left = i + 1
    right = len(nums) - 1

    while left < right:
        total = nums[i] + nums[left] + nums[right]

        if total == 0:
            res.append([nums[i], nums[left], nums[right]])

            left += 1
            right -= 1

            while left < right and nums[left] == nums[left - 1]:
                left += 1

            while left < right and nums[right] == nums[right + 1]:
                right -= 1

        elif total < 0:
            left += 1
        else:
            right -= 1

return res
```

## **代表题：LC 15 3Sum**

```python
class Solution:
    # Sort + opposite-direction two pointers
    # TC: O(n^2)
    # SC: O(1) excluding output, or O(n) depending on sorting implementation
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            # Skip duplicate fixed values.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # Skip duplicate left values.
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate right values.
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return res
```

### **记忆点**

```text
3Sum = 排序 + 固定一个数 + 剩下两个数相向双指针。
```

------

# **五、相向双指针模板 4：两端取舍题**

## **适用场景**

题目给一个数组，让你从两端选或比较，常见于：

```text
最大面积
容器盛水
两边高度/距离相关
```

典型题：

```text
LC 11 Container With Most Water
```

## **模板**

```python
left = 0
right = len(nums) - 1
answer = 0

while left < right:
    # 用 left 和 right 计算当前答案
    answer = max(answer, current_value)

    # 移动更限制答案的那一边
    if nums[left] < nums[right]:
        left += 1
    else:
        right -= 1
```

## **LC 11 示例**

```python
class Solution:
    # Opposite-direction two pointers
    # TC: O(n)
    # SC: O(1)
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            h = min(height[left], height[right])
            max_area = max(max_area, width * h)

            # Move the shorter side because it limits the area.
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
```

------

# **六、同向双指针但不一定是 Sliding Window**

这类题也是两个指针都往右走，但重点不一定是维护一个连续区间。

它常见有几种形式：

```text
1. 快慢指针 / 覆盖法
2. 去重 / 原地修改数组
3. 链表快慢指针
4. 两条链表同步走
5. 一个指针扫描，一个指针寻找下一个有效位置
```

------

# **七、同向双指针模板 1：快慢指针覆盖法**

## **适用场景**

题目要求：

```text
原地修改数组
remove duplicates
remove element
move zeroes
保留符合条件的元素
```

关键词：

```text
in-place
remove
move
overwrite
do not return a new array
```

典型题：

| **题目**                                     | **类型**             |
| -------------------------------------------- | -------------------- |
| LC 26 Remove Duplicates from Sorted Array    | 原地去重             |
| LC 27 Remove Element                         | 原地删除指定元素     |
| LC 283 Move Zeroes                           | 把 0 移到末尾        |
| LC 80 Remove Duplicates from Sorted Array II | 每个元素最多保留两次 |

------

## **核心思想**

```text
fast 负责扫描所有元素
slow 负责记录下一个应该写入的位置
```

模板：

```python
slow = 0

for fast in range(len(nums)):
    if nums[fast] should be kept:
        nums[slow] = nums[fast]
        slow += 1

return slow
```

------

## **代表题：LC 27 Remove Element**

```python
class Solution:
    # Fast-slow pointers / overwrite
    # TC: O(n)
    # SC: O(1)
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0

        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1

        return slow
```

### **怎么理解？**

```text
fast：去找所有不等于 val 的元素
slow：把这些保留下来的元素依次放到数组前面
```

------

## **代表题：LC 283 Move Zeroes**

```python
class Solution:
    # Fast-slow pointers / overwrite
    # TC: O(n)
    # SC: O(1)
    def moveZeroes(self, nums: List[int]) -> None:
        slow = 0

        # First pass: move all non-zero numbers to the front.
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1

        # Second pass: fill the rest with zeroes.
        for i in range(slow, len(nums)):
            nums[i] = 0
```

### **记忆点**

```text
fast 找有效元素；
slow 放有效元素。
```

------

## **代表题：LC 26 Remove Duplicates from Sorted Array**

```python
class Solution:
    # Fast-slow pointers / overwrite
    # TC: O(n)
    # SC: O(1)
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        slow = 1

        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow - 1]:
                nums[slow] = nums[fast]
                slow += 1

        return slow
```

这里：

```text
nums[0 : slow] 是已经整理好的不重复区域。
fast 负责扫描后面的元素。
```

------

# **八、同向双指针模板 2：链表快慢指针**

## **适用场景**

题目是 linked list，并且问：

```text
是否有环
找环入口
找中点
倒数第 k 个节点
```

典型题：

| **题目**                               | **类型**            |
| -------------------------------------- | ------------------- |
| LC 141 Linked List Cycle               | 判断是否有环        |
| LC 142 Linked List Cycle II            | 找环入口            |
| LC 876 Middle of the Linked List       | 找链表中点          |
| LC 19 Remove Nth Node From End of List | 删除倒数第 N 个节点 |

------

## **模板 A：判断链表是否有环**

```python
slow = head
fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

    if slow == fast:
        return True

return False
```

## **LC 141 示例**

```python
class Solution:
    # Fast and slow pointers
    # TC: O(n)
    # SC: O(1)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
```

------

## **模板 B：找环入口**

```python
slow = head
fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

    if slow == fast:
        slow = head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow

return None
```

## **LC 142 示例**

```python
class Solution:
    # Floyd's Cycle Detection
    # TC: O(n)
    # SC: O(1)
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                slow = head

                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                return slow

        return None
```

------

## **模板 C：找链表中点**

```python
slow = head
fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

return slow
```

这里：

```text
slow 一步一步走
fast 两步两步走
fast 到尾巴时，slow 在中间
```

------

# **九、同向双指针模板 3：两条链表同步走**

## **适用场景**

题目有两条链表，问：

```text
是否相交
返回交点
```

典型题：

```text
LC 160 Intersection of Two Linked Lists
```

## **核心思想**

```text
pA 走 A，再走 B
pB 走 B，再走 A
```

这样两个指针最终走过的长度相同：

```text
len(A) + len(B)
```

## **模板**

```python
pA = headA
pB = headB

while pA != pB:
    pA = pA.next if pA else headB
    pB = pB.next if pB else headA

return pA
```

## **代码**

```python
class Solution:
    # Two pointers switching heads
    # TC: O(m + n)
    # SC: O(1)
    def getIntersectionNode(
        self,
        headA: ListNode,
        headB: ListNode
    ) -> Optional[ListNode]:
        pA = headA
        pB = headB

        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA

        return pA
```

### **记忆点**

```text
pA 走 A + B
pB 走 B + A
如果有交点，会在交点相遇；
如果没有交点，会一起变成 None。
```

------

# **十、同向双指针模板 4：一个指针固定，一个指针向前找**

这种和 sliding window 很像，但有时候不强调窗口，而强调：

```text
i 枚举当前位置
j 找下一个满足条件的位置
```

典型：

```text
LintCode Two Sum Difference
一些去重、跳过连续相同元素、寻找下一段
```

## **模板**

```python
j = 0

for i in range(n):
    j = max(j, i + 1)

    while j < n and condition_not_met:
        j += 1

    if j < n and condition_met:
        update_answer()
```

这种在九章课程中经常被叫：

```text
同向双指针
```

它和 sliding window 的区别是：

```text
sliding window 强调维护 [left, right] 这一段连续区间的状态；
这种同向双指针不一定维护完整窗口状态，可能只是用 j 找下一个位置。
```

------

# **十一、Two Pointers 分类总表**

| **类型**             | **指针方向** | **是否一定有窗口** | **典型用途**           | **代表题**               |
| -------------------- | ------------ | ------------------ | ---------------------- | ------------------------ |
| 相向双指针           | 两端向中间   | 不一定             | 回文、有序两数和、3Sum | LC 125, 167, 15          |
| 同向双指针：滑动窗口 | 都向右       | 是                 | 连续子串/子数组        | LC 3, 424, 567, 438, 209 |
| 同向双指针：快慢覆盖 | 都向右       | 不一定             | 原地删除/移动/去重     | LC 26, 27, 283           |
| 同向双指针：链表快慢 | 都向前       | 不一定             | 环、中点、倒数节点     | LC 141, 142, 876         |
| 同向双指针：换头同步 | 都向前       | 不一定             | 两链表交点             | LC 160                   |

------

# **十二、如何判断该用哪种双指针？**

## **1. 题目是连续子串 / 连续子数组？**

关键词：

```text
substring
subarray
contiguous
连续
```

优先考虑：

```text
Sliding Window
```

然后再判断：

```text
固定长度？
求最长？
求最短？
统计数量？
```

------

## **2. 题目是有序数组 + 两数关系？**

关键词：

```text
sorted
two sum
target
sum
difference
```

考虑：

```text
相向双指针
```

如果是求和：

```text
sum 小了 left++
sum 大了 right--
```

------

## **3. 题目是回文 / 反转？**

关键词：

```text
palindrome
reverse
from both ends
```

考虑：

```text
相向双指针
```

------

## **4. 题目要求原地修改数组？**

关键词：

```text
in-place
remove
move zeroes
overwrite
return new length
```

考虑：

```text
fast-slow pointers
```

口诀：

```text
fast 找要保留的元素；
slow 放到正确位置。
```

------

## **5. 题目是链表环 / 中点？**

关键词：

```text
cycle
middle
nth from end
```

考虑：

```text
链表快慢指针
```

------

# **十三、你可以背的最终口诀**

## **相向双指针**

```text
两端开始；
根据条件决定移动左边还是右边；
常用于回文、有序数组、两数和、3Sum。
```

## **同向双指针：滑动窗口**

```text
维护连续窗口；
right 加元素；
left 根据条件删元素；
常用于 substring/subarray。
```

## **同向双指针：快慢覆盖**

```text
fast 扫描；
slow 写入；
常用于原地删除、移动、去重。
```

## **链表快慢指针**

```text
slow 一步；
fast 两步；
常用于环和中点。
```

------

# **十四、建议你的刷题路线**

你现在已经刷了不少 sliding window，可以按这个顺序补齐双指针体系。

## **相向双指针**

```text
LC 125 Valid Palindrome
LC 167 Two Sum II
LC 15 3Sum
LC 11 Container With Most Water
```

## **同向双指针：快慢覆盖**

```text
LC 27 Remove Element
LC 26 Remove Duplicates from Sorted Array
LC 283 Move Zeroes
LC 80 Remove Duplicates from Sorted Array II
```

## **同向双指针：链表**

```text
LC 141 Linked List Cycle
LC 142 Linked List Cycle II
LC 160 Intersection of Two Linked Lists
LC 876 Middle of the Linked List
```

## **Sliding Window**

```text
LC 3
LC 424
LC 567
LC 438
LC 643
LC 209
LC 1004
LC 904
LC 76
```

------

# **十五、最终做题判断表**

你遇到新题时，可以这样判断：

| **题目信号**                                  | **优先想法**       |
| --------------------------------------------- | ------------------ |
| substring / subarray / 连续                   | Sliding Window     |
| fixed length / k-size / permutation / anagram | 固定长度窗口       |
| longest substring / max length                | 变长窗口，坏了才缩 |
| minimum length / shortest                     | 变长窗口，好了还缩 |
| sorted array + target sum                     | 相向双指针         |
| palindrome / reverse                          | 相向双指针         |
| in-place remove / move / deduplicate          | 快慢指针覆盖       |
| linked list cycle / middle                    | 快慢指针           |
| two linked lists intersection                 | 换头同步指针       |

你可以把最核心的三句话记住：

```text
相向：两端夹。
窗口：right 加，left 修。
覆盖：fast 找，slow 放。
```