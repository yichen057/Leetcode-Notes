# Python 八股 Interview Q&A

> Python language internals & idioms asked in SDE interviews. 面试热身环节最常被问的 Python 问题。

## 🎯 High-Frequency Questions 高频问题

### Q1: What is the GIL? How does it affect multithreading?

**A:** The GIL — Global Interpreter Lock — is a mutex in CPython that allows only one thread to execute Python bytecode at a time. This means multithreading in Python doesn't give true parallelism for CPU-bound tasks. For I/O-bound work, threads are still useful because the GIL is released during I/O waits. For CPU-bound parallelism, we use `multiprocessing`, which spawns separate processes each with its own interpreter and GIL.

**中文**: GIL 是 CPython 解释器级别的全局锁，任一时刻只允许一个线程执行字节码。记忆点：**CPU 密集 → multiprocessing，I/O 密集 → threading / asyncio**。因为 I/O 等待时（如网络请求、读文件）线程会释放 GIL，所以多线程对 I/O 任务有效。

**Follow-up**: Why does CPython have a GIL? → It simplifies memory management (reference counting isn't thread-safe without it). / What about asyncio? → Single-threaded cooperative concurrency, even cheaper than threads for high-concurrency I/O.

---

### Q2: How does Python manage memory? (Garbage Collection)

**A:** Python uses reference counting as its primary mechanism — every object tracks how many references point to it, and when the count hits zero the memory is freed immediately. Reference counting alone can't handle reference cycles (A points to B, B points to A), so Python also runs a generational cyclic garbage collector that periodically detects and collects unreachable cycles. The generational design (3 generations) is based on the observation that most objects die young.

**中文**: 两层机制：①**引用计数**为主，计数归零立刻回收；②**分代 GC** 兜底处理循环引用。分代（0/1/2 三代）原理：新对象大多短命，所以频繁扫描新生代、少扫描老年代。可以用 `gc` 模块手动控制。

**Follow-up**: What's a memory leak scenario in Python? → Cycles involving objects with `__del__`, growing global caches, closures holding references. / `weakref` 可以避免循环引用计数。

---

### Q3: What's the difference between list and tuple?

**A:** Lists are mutable, tuples are immutable. Because tuples are immutable they're hashable (as long as their elements are hashable), so they can be used as dict keys or set members, while lists cannot. Tuples are also slightly more memory-efficient and faster to create. Use tuples for fixed collections of heterogeneous data, lists for homogeneous sequences that change.

**中文**: 核心：**list 可变，tuple 不可变**。不可变 → 可哈希 → 能当 dict key / set 元素。tuple 创建更快、占内存更小（不需要预留增长空间）。

**Follow-up**: Is a tuple always hashable? → No — `(1, [2])` is unhashable because it contains a list.

---

### Q4: How does a Python dict work internally?

**A:** A dict is a hash table. Keys are hashed, and the hash determines the slot in an internal array. Collisions are resolved with open addressing — probing for the next available slot. When the table gets about two-thirds full, it resizes and rehashes. Average-case lookup, insert, and delete are O(1); worst case is O(n) with many collisions. Since Python 3.7, dicts preserve insertion order.

**中文**: 底层是**哈希表 + 开放寻址法**（不是链地址法，和 Java 不同——面试常考对比）。负载因子约 2/3 时扩容。Python 3.7+ 保证**插入顺序**（实现上用紧凑数组 + 索引表，顺带省内存）。

**Follow-up**: What can be a dict key? → Anything hashable (immutable built-ins, objects implementing `__hash__` and `__eq__`). / dict vs set? → set 就是只有 key 没有 value 的哈希表。

---

### Q5: Explain decorators.

**A:** A decorator is a function that takes a function and returns a new function, usually adding behavior around the original — logging, timing, caching, auth checks. The `@decorator` syntax is just sugar for `func = decorator(func)`. It works because Python functions are first-class objects. A common built-in example is `functools.lru_cache` for memoization.

**中文**: 装饰器 = **接收函数、返回函数的高阶函数**。`@deco` 等价于 `func = deco(func)`。写法记忆：外层收 func，内层 wrapper 收 `*args, **kwargs`，记得加 `@functools.wraps(func)` 保留原函数元信息。

```python
import functools

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__}: {time.time() - start:.4f}s")
        return result
    return wrapper
```

**Follow-up**: Decorator with arguments? → One more nesting level: a function returning a decorator. / Class-based decorator → implement `__call__`.

---

### Q6: What's the difference between deep copy and shallow copy?

**A:** A shallow copy creates a new container but the elements are still references to the same objects — so mutating a nested object affects both copies. A deep copy recursively copies everything, producing fully independent objects. In Python: `copy.copy()` vs `copy.deepcopy()`; slicing like `lst[:]` is a shallow copy.

**中文**: 浅拷贝只复制最外层容器，里面元素还是同一批对象的引用；深拷贝递归复制全部。经典坑：`[[0]*3]*3` 创建的是同一行的 3 个引用。

**Follow-up**: How to correctly init a 2D list? → `[[0]*3 for _ in range(3)]`.

---

### Q7: `is` vs `==`?

**A:** `==` compares values by calling `__eq__`; `is` compares identity — whether two names point to the exact same object in memory. Use `is` only for singletons like `None`, `True`, `False`.

**中文**: `==` 比值，`is` 比内存地址（`id()`）。坑：小整数 [-5, 256] 和短字符串会被缓存（interning），所以 `a is b` 有时碰巧为 True，但不能依赖。规范：判 None 永远用 `is None`。

---

### Q8: What are `*args` and `**kwargs`?

**A:** `*args` collects extra positional arguments into a tuple; `**kwargs` collects extra keyword arguments into a dict. They let functions accept a variable number of arguments and are essential for writing wrappers and decorators that forward arguments transparently.

**中文**: `*` 收位置参数成 tuple，`**` 收关键字参数成 dict。调用侧则是反向解包：`f(*lst, **dct)`。

---

### Q9: Explain generators and `yield`.

**A:** A generator is a function that uses `yield` to produce values lazily, one at a time, pausing and resuming its state between calls. It implements the iterator protocol, so you can loop over it. The key benefit is memory efficiency — you can process huge or infinite sequences without materializing them. Generator expressions `(x*x for x in data)` are the lazy version of list comprehensions.

**中文**: 含 `yield` 的函数返回生成器，**惰性求值**，每次 `next()` 执行到下一个 yield 暂停并保存现场。优点：省内存，可表示无限序列。`range`、文件逐行读取都是惰性思想。

**Follow-up**: Generator vs iterator? → Generator is a convenient way to create an iterator. / `yield from`? → Delegates to a sub-generator.

---

### Q10: What is a lambda? What are its limits?

**A:** A lambda is an anonymous single-expression function, commonly used as a short callback — for example as a sort key: `sorted(items, key=lambda x: x[1])`. It can only contain one expression, no statements, so anything complex should be a named function.

**中文**: 匿名函数，只能写一个表达式。最常见场景：`sorted` / `max` / `min` 的 `key`。

---

### Q11: Mutable default argument pitfall

**A:** Default argument values are evaluated once at function definition time, not per call. So `def f(x, acc=[])` shares one list across all calls — a classic bug. The fix is `acc=None` and creating the list inside the function.

**中文**: 默认参数在**函数定义时**求值一次，所有调用共享。可变默认参数（list/dict）必踩坑。标准写法：默认 `None`，函数体内 `if acc is None: acc = []`。

---

### Q12: How does `sort()` work in Python? Is it stable?

**A:** Python uses Timsort, a hybrid of merge sort and insertion sort that exploits existing runs in the data. It's O(n log n) worst case, O(n) on already-sorted data, and it's stable — equal elements keep their relative order. That's why sorting by multiple keys can be done in successive passes.

**中文**: Timsort = 归并 + 插入排序混合，利用数据中已有的有序段（run）。**稳定排序**。`list.sort()` 原地，`sorted()` 返回新列表。多级排序：`key=lambda x: (x[0], -x[1])`。

---

### Q13: `@staticmethod` vs `@classmethod` vs instance method?

**A:** An instance method receives `self` and operates on a specific object. A classmethod receives `cls` and is commonly used for alternative constructors like `from_json`. A staticmethod receives neither — it's just a regular function namespaced inside the class for organizational purposes.

**中文**: 三件套：`self`（实例）、`cls`（类，常用于工厂方法）、啥都不收（工具函数挂在类下）。

---

### Q14: Python is "pass by what"?

**A:** Python is pass-by-object-reference (also called pass-by-assignment). The function receives a reference to the same object — if the object is mutable, in-place modifications are visible to the caller; but rebinding the parameter to a new object doesn't affect the caller.

**中文**: 传的是**对象引用的拷贝**。可变对象原地改 → 外面可见；参数重新赋值 → 外面不变。一句话："传引用，但赋值只改本地名字"。

## 📝 Quick Reference 速查

| Topic | Key Point |
|-------|-----------|
| GIL | One thread executes bytecode at a time; use multiprocessing for CPU-bound |
| GC | Ref counting + generational cycle collector |
| dict | Hash table, open addressing, insertion-ordered (3.7+), O(1) avg |
| list vs tuple | mutable vs immutable; tuple hashable |
| Timsort | merge+insertion, stable, O(n log n) |
| copy | shallow = outer container only; deep = recursive |
| is vs == | identity vs equality; `is None` |
