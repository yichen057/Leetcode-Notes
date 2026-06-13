# Java 八股 Interview Q&A

> JVM, collections, concurrency, OOP — the classic Java interview circuit. Java 面试三板斧：JVM、集合、并发。

## 🎯 High-Frequency Questions 高频问题

### Q1: What's the difference between JDK, JRE, and JVM?

**A:** The JVM is the virtual machine that executes Java bytecode — it's what makes Java platform-independent. The JRE is the JVM plus the core class libraries needed to run Java programs. The JDK is the JRE plus development tools like the compiler `javac` and debugger. So: JDK ⊃ JRE ⊃ JVM.

**中文**: 包含关系记忆：**JDK（开发）⊃ JRE（运行）⊃ JVM（执行字节码）**。"Write once, run anywhere" 的原理：源码 → 字节码 → 各平台 JVM 解释/JIT 执行。

---

### Q2: Describe the JVM memory model (runtime data areas).

**A:** The JVM divides memory into: the Heap, shared by all threads, where objects live — this is what GC manages; the Method Area (Metaspace since Java 8) storing class metadata and constants; and per-thread areas — the JVM Stack holding stack frames with local variables, the PC register, and native method stacks. Stack overflow comes from deep recursion; OutOfMemoryError usually comes from the heap.

**中文**: 分两类：**线程共享**——堆（对象、GC 主战场）、方法区/元空间（类信息、常量池）；**线程私有**——虚拟机栈（局部变量、栈帧）、程序计数器、本地方法栈。Java 8 把永久代 (PermGen) 换成了元空间 (Metaspace，用本地内存)。

**Follow-up**: Where do `new` objects go? → Heap (Eden first). / String constant pool? → In the heap since Java 7.

---

### Q3: How does garbage collection work in Java?

**A:** GC automatically frees objects that are no longer reachable. Reachability is determined by tracing from GC Roots — stack references, static fields, etc. The heap is divided into Young Generation (Eden + two Survivor spaces) and Old Generation. Most objects die young, so minor GCs frequently sweep the young gen with a copying algorithm; survivors that live long enough get promoted to the old gen, collected less often by major/full GCs. Modern collectors like G1 aim for low, predictable pause times.

**中文**: ①判定垃圾：**可达性分析**（从 GC Roots 出发，不可达即垃圾；注意不是引用计数，Java 不用引用计数因为有循环引用问题）。②分代：新生代（Eden:S0:S1 = 8:1:1，复制算法）→ 熬过多次 minor GC 晋升老年代（标记-整理）。③常见收集器：G1（JDK9+ 默认）、ZGC（低延迟）。

**Follow-up**: Strong/soft/weak/phantom references? → 强引用不回收；软引用内存不足才回收（缓存）；弱引用下次 GC 即回收（WeakHashMap）；虚引用用于回收通知。

---

### Q4: HashMap internals — how does it work?

**A:** HashMap is an array of buckets. A key's hashCode is processed and mapped to a bucket index. Collisions are handled by chaining — each bucket holds a linked list, and since Java 8, a list longer than 8 converts to a red-black tree, improving worst-case lookup from O(n) to O(log n). Default capacity is 16 with load factor 0.75; exceeding it triggers a resize that doubles capacity and rehashes. It's not thread-safe — use ConcurrentHashMap for concurrency.

**中文**: **数组 + 链表 + 红黑树**（Java 8+，链表长度 > 8 且数组 ≥ 64 时树化）。默认容量 16，负载因子 0.75。和 Python dict 对比：Java 用链地址法，Python 用开放寻址。多线程下 HashMap 不安全（Java 7 扩容可能死循环，Java 8 可能丢数据）→ 用 ConcurrentHashMap。

**Follow-up**: Why must you override hashCode when overriding equals? → Equal objects must have equal hash codes, or HashMap lookups break. / ConcurrentHashMap how? → Java 8: CAS + synchronized on bucket heads, 锁粒度到桶。

---

### Q5: ArrayList vs LinkedList?

**A:** ArrayList is backed by a dynamic array: O(1) random access, amortized O(1) append, but O(n) insert/delete in the middle. LinkedList is a doubly-linked list: O(1) insert/delete at a known node, but O(n) access by index. In practice ArrayList wins almost always due to cache locality; LinkedList is mainly useful as a Deque.

**中文**: 数组 vs 双向链表。实战结论：**几乎永远用 ArrayList**（CPU 缓存友好）。LinkedList 的真实用途是当 Deque/队列用。扩容：ArrayList 每次扩 1.5 倍。

---

### Q6: String vs StringBuilder vs StringBuffer?

**A:** String is immutable — every concatenation creates a new object, so building a string in a loop with `+` is O(n²). StringBuilder is mutable and not thread-safe — the default choice for string building. StringBuffer is the synchronized, thread-safe version, rarely needed today.

**中文**: String 不可变（安全、可缓存 hash、字符串常量池复用）。循环拼接用 StringBuilder。Buffer = Builder + synchronized，基本退役。

**Follow-up**: Why is String immutable? → Security (class loading, network params), string pool reuse, safe hash caching for HashMap keys.

---

### Q7: `==` vs `equals()` vs `hashCode()`?

**A:** For objects, `==` compares references; `equals()` compares logical value if overridden — otherwise it defaults to reference comparison. The contract: if two objects are equal per `equals()`, they must return the same `hashCode()`. That's why both must be overridden together for use in hash-based collections.

**中文**: `==` 比地址（基本类型比值），`equals` 比内容（需重写）。约定：equals 相等 ⇒ hashCode 必须相等（反之不要求）。坑：`Integer` 缓存 [-128, 127]，所以 `Integer a = 127; a == b` 为 true 但 128 就是 false——包装类型永远用 equals。

---

### Q8: Difference between process and thread; how to create threads in Java?

**A:** A process is an independent program with its own memory space; threads are lightweight execution units within a process sharing its memory. In Java you create threads by extending Thread or, preferably, implementing Runnable/Callable and submitting to an ExecutorService thread pool, which reuses threads and avoids the cost of creating one per task.

**中文**: 实战答法要落到**线程池**：`ExecutorService` / `ThreadPoolExecutor`。线程池七参数：corePoolSize、maxPoolSize、keepAliveTime、unit、workQueue、threadFactory、rejectionHandler。执行流程：核心线程 → 队列 → 扩到 max → 拒绝策略。

**Follow-up**: Runnable vs Callable? → Callable returns a value and can throw checked exceptions, used with Future.

---

### Q9: What does `synchronized` do? What about `volatile`?

**A:** `synchronized` provides mutual exclusion and visibility: only one thread can hold the monitor lock of an object/class at a time, and changes are flushed to main memory on release. `volatile` is lighter — it guarantees visibility and prevents instruction reordering for a variable but does NOT provide atomicity. So `volatile int i; i++` is still racy. For atomic counters, use `AtomicInteger` with CAS.

**中文**: 三大并发性质对照：**synchronized = 原子性 + 可见性 + 有序性；volatile = 可见性 + 有序性（无原子性）**。volatile 经典用途：状态标志位、双重检查锁单例 (DCL) 中防止指令重排。CAS = 无锁乐观，ABA 问题用版本号 (AtomicStampedReference)。

**Follow-up**: synchronized 锁升级？→ 偏向锁 → 轻量级锁（自旋）→ 重量级锁。 / ReentrantLock vs synchronized? → Lock 可中断、可超时、可公平、可多条件变量。

---

### Q10: Explain the four pillars of OOP with Java examples.

**A:** Encapsulation — hide internal state behind private fields and public methods. Inheritance — a subclass reuses and extends a superclass with `extends`. Polymorphism — the same method call behaves differently depending on the runtime type, via overriding and dynamic dispatch. Abstraction — expose what, hide how, with abstract classes and interfaces.

**中文**: 封装、继承、多态、抽象。多态的实现机制：**动态绑定**（运行时根据实际类型查虚方法表）。重载 (overload) 是编译期静态分派，重写 (override) 才是运行时多态。

**Follow-up**: Abstract class vs interface? → 接口可多实现、默认无状态（Java 8+ 可有 default 方法）；抽象类单继承、可有构造器和字段。"is-a" 用抽象类，"can-do" 用接口。

---

### Q11: Checked vs unchecked exceptions?

**A:** Checked exceptions extend Exception and must be declared or caught at compile time — they represent recoverable conditions like IOException. Unchecked exceptions extend RuntimeException — programming errors like NullPointerException — and don't require handling. Errors like OutOfMemoryError are serious JVM problems you shouldn't catch.

**中文**: 体系：Throwable → Error（别管）+ Exception（Checked 必须处理 / RuntimeException 不强制）。finally 一定执行（除 System.exit）；try-with-resources 自动关流。

---

### Q12: How does ConcurrentHashMap achieve thread safety?

**A:** In Java 8+, it uses fine-grained locking: reads are mostly lock-free using volatile semantics, and writes use CAS to insert into an empty bucket, falling back to synchronizing on the bucket's head node when there's contention. This allows high concurrency compared to locking the whole map like Hashtable or Collections.synchronizedMap.

**中文**: Java 8 抛弃了分段锁 (Segment)，改为 **CAS + synchronized 锁桶头节点**，锁粒度更细。size 用 LongAdder 思想分散计数。对比：Hashtable 全表一把锁。

## 📝 Quick Reference 速查

| Topic | Key Point |
|-------|-----------|
| JVM memory | Heap (shared, GC) / Stack (per-thread) / Metaspace |
| GC | Reachability from GC Roots; young (copying) / old (mark-compact); G1 default |
| HashMap | array + list + red-black tree (≥8); cap 16, LF 0.75; not thread-safe |
| volatile | visibility + ordering, NO atomicity |
| synchronized | atomicity + visibility + ordering; lock upgrading |
| String | immutable; loop concat → StringBuilder |
| Integer cache | [-128, 127]; compare wrappers with equals |
