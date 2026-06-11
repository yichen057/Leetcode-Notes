这个问题可以用一句话判断：

**如果答案一定可以从 0 开始“越变越大”，用** **`0`****。如果答案需要从真实窗口里比较出来，或者要找最小值，用** **`inf`** **/** **`-inf`** **更安全。**

------

## **1. 求最长长度：通常初始化为** **`0`**

因为长度不可能是负数，而且如果找不到合法窗口，很多题答案本来就是 `0`。

例如 LC 3：

```python
maxLen = 0
```

因为最长无重复子串长度最小也是 `0`。

```python
maxLen = max(maxLen, r - l + 1)
```

适合：

```python
maxLen = 0
res = 0
answer = 0
```

常见题：

```text
LC 3 Longest Substring Without Repeating Characters
LC 424 Longest Repeating Character Replacement
LC 1004 Max Consecutive Ones III
```

这些题的答案都是“长度”，最小可以是 `0`，所以初始化为 `0` 很自然。

------

## **2. 求最短长度：通常初始化为** **`float("inf")`**

因为你要找的是最小值，如果一开始设成 `0`：

```python
minLen = 0
minLen = min(minLen, 当前长度)
```

那结果永远可能停在 `0`，这是错的。



比如 LC 209：

```python
minLen = float("inf")
```

每次找到合法窗口时：

```python
minLen = min(minLen, r - l + 1)
```

最后如果没找到，再返回 `0`：

```python
return 0 if minLen == float("inf") else minLen
```

适合：

```text
minimum length
shortest subarray
smallest window
```

常见题：

```text
LC 209 Minimum Size Subarray Sum
LC 76 Minimum Window Substring
```

口诀：

```text
求最短，用 inf。
最后没更新过，再返回 0 或空结果。
```

------

## **3. 求最大和 / 最大平均值：不要随便初始化为** **`0`**

这个最容易踩坑。

比如 LC 643：

```python
nums = [-5, -4, -3]
k = 2
```

窗口和是：

```text
[-5, -4] -> -9
[-4, -3] -> -7
```

最大和应该是：

```python
-7
```

如果你写：

```python
max_sum = 0
```

那最后会错误得到 `0`。

所以对于“最大和 / 最大平均值”这种答案可能是负数的题，应该：

### **方法一：用第一个真实窗口初始化，最推荐**

```python
current_sum = sum(nums[:k])
max_sum = current_sum
```

然后滑动：

```python
for r in range(k, len(nums)):
    current_sum += nums[r]
    current_sum -= nums[r - k]
    max_sum = max(max_sum, current_sum)
```

### **方法二：用负无穷**

```python
max_sum = float("-inf")
```

------

## **4. 求最小和 / 最小值：用第一个真实值或** **`float("inf")`**

类似地，如果你要求最小和，不要随便设成 `0`。

如果数组全是正数，`0` 会比所有真实窗口和都小，导致答案错误。

应该用：

```python
min_sum = float("inf")
```

或者用第一个真实窗口初始化：

```python
current_sum = sum(nums[:k])
min_sum = current_sum
```

------

## **5. 总结表**

| **目标**            | **推荐初始化**                  | **原因**             |
| ------------------- | ------------------------------- | -------------------- |
| 最长长度 `maxLen`   | `0`                             | 长度最小就是 0       |
| 计数 `count/res`    | `0`                             | 从 0 个开始累计      |
| 最短长度 `minLen`   | `float("inf")`                  | 要找更小的真实值     |
| 最大和 / 最大平均值 | 第一个窗口值 或 `float("-inf")` | 结果可能是负数       |
| 最小和 / 最小值     | 第一个窗口值 或 `float("inf")`  | 不能被 0 干扰        |
| 判断是否存在        | 不需要初始化答案                | 找到就 `return True` |

------

## **6. 你可以这样记**

```text
长度类：
    求最长：0
    求最短：inf

数值类：
    求最大：第一个真实值 或 -inf
    求最小：第一个真实值 或 inf

计数类：
    从 0 开始
```

------

## **7. 放到你最近学的题里**

### **LC 3 / LC 424：最长长度**

```python
maxLen = 0
res = 0
```

正确。

------

### **LC 209：最短长度**

```python
minLen = float("inf")
```

最后：

```python
return 0 if minLen == float("inf") else minLen
```

正确。

------

### **LC 643：最大平均值**

更推荐：

```python
current_sum = sum(nums[:k])
max_sum = current_sum
```

不要写：

```python
max_sum = 0
```

因为 `nums` 可能全是负数。

------

## **最终口诀**

```text
最长长度从 0 开始。
最短长度从 inf 开始。
最大/最小数值最好用第一个真实窗口初始化。
如果可能全负数，max 不要初始化为 0。
```