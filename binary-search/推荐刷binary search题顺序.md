你已经完成的题覆盖了三类基础二分：

| **类型**     | **已完成题目** | **已掌握内容**                   |
| ------------ | -------------- | -------------------------------- |
| 普通数组查找 | 704、35、34    | 任意位置、插入位置、左右边界     |
| 按字段二分   | 981            | 找最后一个 `<= timestamp` 的记录 |
| 答案二分     | 875            | 找最小可行答案                   |

接下来不建议马上刷大量同类题，而是补齐二分的另外三种重要场景：

1. **旋转排序数组**
2. **趋势 / 峰值数组**
3. **答案二分的反方向：最大可行答案**

------

# **推荐刷题顺序**

| **顺序** | **题目**                                          | **难度** | **练习重点**          | **和你模板的关系**                |
| -------- | ------------------------------------------------- | -------- | --------------------- | --------------------------------- |
| 1        | **153. Find Minimum in Rotated Sorted Array**     | Medium   | 旋转数组找最小值      | 比较 `nums[mid]` 与 `nums[end]`   |
| 2        | **33. Search in Rotated Sorted Array**            | Medium   | 旋转数组找 target     | 判断哪一半有序                    |
| 3        | **852. Peak Index in a Mountain Array**           | Medium   | 单一山峰              | 比较 `arr[mid]` 与 `arr[mid + 1]` |
| 4        | **162. Find Peak Element**                        | Medium   | 普通数组中找任意 peak | 仍然根据坡度二分                  |
| 5        | **2226. Maximum Candies Allocated to K Children** | Medium   | 找最大可行答案        | 和 875 的方向相反                 |
| 6        | **1011. Capacity To Ship Packages Within D Days** | Medium   | 找最小可行答案        | 巩固 875 模板                     |
| 7        | **658. Find K Closest Elements**                  | Medium   | 二分找分界线 + 双指针 | 综合题                            |
| 8        | **702. Search in a Sorted Array of Unknown Size** | Medium   | 倍增找范围 + 二分     | 综合题                            |

其中 LC 153 要求在无重复旋转数组中以 `O(log n)` 找最小值；LC 33 要在旋转排序数组中查找 target；LC 162 则要求返回任意一个峰值的位置。   

------

# **第一阶段：先做 153 和 33**

你已经做过普通有序数组二分，下一步最适合进入：

```text
rotated sorted array
```

## **1. LC 153：Find Minimum in Rotated Sorted Array**

例如：

```python
nums = [4, 5, 6, 7, 0, 1, 2]
```

要返回：

```python
0
```

这题重点不是找 `target`，而是理解：



旋转数组虽然整体不完全有序，但最小值所在的一侧仍然可以通过 `mid` 和右端点的大小关系判断。



用你的模板时，关键变化位置是：

```python
while start + 1 < end:
    mid = (start + end) // 2

    # 调整点：不再和 target 比，而是和右端点比较
    if nums[mid] <= nums[end]:
        end = mid
    else:
        start = mid

return min(nums[start], nums[end])
```

这题建议你作为**下一题立即做**，因为判断逻辑比 LC 33 简单。

------

## **2. LC 33：Search in Rotated Sorted Array**

例如：

```python
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
```

返回：

```python
4
```

这题重点是：



每次二分后，至少有一半仍然是正常升序的。先找出有序的一半，再判断 target 是否在这一半中。



核心判断长这样：

```python
if nums[start] <= nums[mid]:
    # 左半边有序
    if nums[start] <= target < nums[mid]:
        end = mid - 1
    else:
        start = mid + 1
else:
    # 右半边有序
    if nums[mid] < target <= nums[end]:
        start = mid + 1
    else:
        end = mid - 1
```

这题不太适合强行套“找第一个 / 最后一个 target”的模板，因为它的关键不是往左或往右找边界，而是**识别哪一段有序**。

------

# **第二阶段：做 852 和 162**

你之前其实已经接触过这两题，现在可以正式独立写一遍。

## **3. LC 852：Peak Index in a Mountain Array**

例如：

```python
arr = [0, 2, 5, 3, 1]
```

返回山顶 index：

```python
2
```

它的判断点是：

```python
if arr[mid] > arr[mid + 1]:
    # 当前在下降坡，peak 在 mid 或左边
    end = mid
else:
    # 当前在上升坡，peak 在右边
    start = mid
```

用你的模板写：

```python
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start, end = 0, len(arr) - 1

        while start + 1 < end:
            mid = (start + end) // 2

            if arr[mid] > arr[mid + 1]:
                end = mid
            else:
                start = mid

        if arr[start] > arr[end]:
            return start
        return end
```

这题让你理解：

```text
二分不一定比较 target，也可以比较趋势。
```

------

## **4. LC 162：Find Peak Element**

LC 162 和 852 类似，但数组不一定只有一个山峰：

```python
nums = [1, 2, 1, 3, 5, 6, 4]
```

可能有多个 peak，返回任意一个即可。



你已经调试过这题，建议现在不看旧代码，重新手写一次，检查你是否真正掌握了：

```python
nums[mid] > nums[mid + 1]
```

代表什么。

------

# **第三阶段：巩固答案二分**

你做过 LC 875：

```text
找最小可行速度
```

接下来应该做一题方向相反的：

## **5. LC 2226：Maximum Candies Allocated to K Children**

它和你之前看到的 Wood Cut 几乎是同一个模型：

```text
给若干堆糖，每个孩子必须拿到相同数量；
最多能让每个孩子拿多少糖？
```

这题找的是：

```text
最大可行答案
```

和 Koko 对比：

| **题目**     | **问题**           | **要找什么** | `mid` **可行时**        |
| ------------ | ------------------ | ------------ | ----------------------- |
| 875 Koko     | 多快才能按时吃完   | 最小可行速度 | `end = mid`，继续往左   |
| 2226 Candies | 每个孩子最多分多少 | 最大可行数量 | `start = mid`，继续往右 |

用你的模板，核心部分会是：

```python
if canDistribute(mid):
    # mid 可行，但可能还能分更多
    start = mid
else:
    end = mid
```

最后因为找最大可行答案，要先检查：

```python
end
```

------

## **6. LC 1011：Capacity To Ship Packages Within D Days**

做完 2226 后，再做 LC 1011。

它和 Koko 一样，是：

```text
找最小可行答案
```

区别只在于 `canFinish()` 的计算方式更复杂一些：

| **题目** | **候选答案**      | **可行性判断**         |
| -------- | ----------------- | ---------------------- |
| 875      | 每小时吃香蕉速度  | 能否在 `h` 小时内吃完  |
| 1011     | 船的载重 capacity | 能否在 `days` 天内运完 |

你要发现：

```python
if canShip(mid):
    end = mid
else:
    start = mid
```

和 Koko 的主体完全一样。

------

# **第四阶段：做综合题**

## **7. LC 658：Find K Closest Elements**

这题你之前已经学过代码逻辑，建议放在这里重新独立完成。

它综合了：

```text
找第一个 >= target 的位置
+
左右双指针扩展
```

也就是把 LC 35 的 lower bound 思维真正用到一道更复杂的问题里。

------

## **8. LC 702：Search in a Sorted Array of Unknown Size**

这题综合了：

```text
倍增确定搜索范围
+
普通二分 / 左边界二分
```

你之前已经推导过：

```text
倍增次数 x = O(log k)
```

其中 `k` 是 target 所在的 index。重新独立写出来，会帮助你巩固为什么数组未知长度时仍然可以二分。

------

# **之后再做的进阶题**

前面八题完成后，再进入这些变体：

| **题目**                                         | **练习重点**                               |
| ------------------------------------------------ | ------------------------------------------ |
| **154. Find Minimum in Rotated Sorted Array II** | 旋转数组有重复元素，为什么无法直接排除一半 |
| **81. Search in Rotated Sorted Array II**        | LC 33 的重复元素版本                       |
| **74. Search a 2D Matrix**                       | 把二维矩阵当作一维有序数组二分             |
| **240. Search a 2D Matrix II**                   | 注意这题更适合从右上角移动，不是经典二分   |
| **410. Split Array Largest Sum**                 | 较难的答案二分                             |
| **4. Median of Two Sorted Arrays**               | 高难度，不建议现在马上做                   |

------

# **你接下来一周的练习安排**

按你目前进度，我建议这样练，不要一次做太多新题：

| **天数** | **题目**   | **目标**                              |
| -------- | ---------- | ------------------------------------- |
| Day 1    | 153        | 独立写出旋转数组找最小值              |
| Day 2    | 33         | 理解“先判断哪一半有序”                |
| Day 3    | 852 + 162  | 对比单峰和多峰，掌握趋势二分          |
| Day 4    | 2226       | 把 875 的最小可行答案改成最大可行答案 |
| Day 5    | 1011       | 巩固最小可行答案模板                  |
| Day 6    | 658        | lower bound + two pointers            |
| Day 7    | 702 + 复盘 | 倍增 + 二分；整理模板笔记             |

------

# **最值得先做的下一题**

现在直接开始：

```text
LeetCode 153. Find Minimum in Rotated Sorted Array
```

因为它恰好连接你已经掌握的普通二分和下一阶段的旋转数组二分：

```text
704 / 35 / 34
        ↓
153：旋转数组找最小值
        ↓
33：旋转数组找 target
```

做题时先不要看答案，尝试用你的模板回答三个问题：

```text
1. start 和 end 代表的候选范围是什么？
2. mid 应该和谁比较：target，还是 nums[end]？
3. 为什么某一侧可以被排除？
```