#13 · Implement strStr()

# https://www.lintcode.com/problem/13/

# algorithms
# Easy (24%)

#For a given source string and a target string, you should output the first index(from 0) of target string in the source string.If the target does not exist in source, just return -1.
class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    #Python2 和 Python3 在函数命名规则上完全一样，语法都支持这两种写法。
    #区别在于：
    #Python 社区习惯 → 用 snake_case 做函数名。
    #Java/C++ 习惯 → 用 CamelCase 做函数名。
    def str_str(self, source: str, target: str) -> int:
        # Write your code here
        if not target:
            return 0
        for i in range(len(source)):
            if source[i:i+len(target)]==target:
                return i
        return -1
    
    #上述方法未考虑i+len(target)可能越界超出len(source)的情况, python不会报错, java会报错; 
    #另外一个可优化空间是: subString(java)或者str[i:j]这种切片, 都是新创建的字符串对象, 会额外增加空间复杂度, 用每次都切片再比较, 效率上比直接逐字符比较要差
    #优化方法, 考虑越界情况, 且用逐字符比较的方式节省空间提升效率
    # 时间复杂度：O(n·m) 也就是O(n^2), 暴力匹配 (Brute Force)。空间复杂度：O(1), 除了循环变量 i、j 和常数标志，没有额外使用数据结构。除了循环变量 i、j 和常数标志，没有额外使用数据结构。
    def strStr(self, source: str, target: str) -> int:
        if not target:
            return 0
        for i in range(len(source) - len(target) + 1): # 外层循环 n-m+1 次, 把i当作target在source里的起点位置, 这个值也是本题要计算和返回的值
            for j in range(len(target)): # 内层循环 m 次, 每次都比到最后一个才失败
                if source[i + j] != target [j]:
                    break
            else:
                return i        
        return -1
    #语法: 
    # Python 的 for-else 语义是：
    # for-else 的 else 不是跟 if 配对，而是跟 整个循环 配对。
    # 当 for 循环执行完且没有被 break 打断时，执行 else。当循环没有执行完且没有触发break时, 继续循环
    # 它并不是「每次循环里判断一次」，而是「等整个循环执行结束后，再决定是否执行 else」。
    #为什么 Python 要这样设计？
    # 目的是解决「搜索 / 查找」这类场景：
    # 如果找到了目标 → break。
    # 如果整个循环都没找到 → else。
    # 如果 else 写在 break 前，就变成了普通的 if-else，失去了「循环结束后才判断」的特性。

    # 用例 source = "abcde", target = "bcd" 展开。
    # ① 外层循环 i = 0
    # source[0..2] = "abc"
    # 内层循环：
    # j = 0: source[0] = 'a' vs target[0] = 'b' → ❌ 不相等
    # → notEqual = true，break
    # notEqual = true → 不返回，继续下一个 i。
    # ② 外层循环 i = 1
    # source[1..3] = "bcd"
    # 内层循环：
    # j = 0: source[1] = 'b' vs target[0] = 'b' → ✅
    # j = 1: source[2] = 'c' vs target[1] = 'c' → ✅
    # j = 2: source[3] = 'd' vs target[2] = 'd' → ✅
    # 内层循环跑完，notEqual = false
    # 👉 执行 if (!notEqual) return i; → 返回 i = 1。
    # ③ 外层循环 i = 2
    # 其实不会执行了，因为代码已经在 i=1 时 return 1。
    # ✅ 最终输出
    # 返回 1，因为 target = "bcd" 出现在 source = "abcde" 的下标 1。