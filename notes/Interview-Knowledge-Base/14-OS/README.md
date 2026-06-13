# Operating Systems 操作系统八股

> Process/thread, memory, scheduling, deadlock — the OS classics. 操作系统经典八股，背就完事。

## 🎯 High-Frequency Questions 高频问题

### Q1: Process vs Thread?

**A:** A process is an instance of a running program with its own address space, file descriptors, and resources. A thread is the unit of CPU scheduling within a process — threads in the same process share the address space, heap, and open files, but each has its own stack, registers, and program counter. Threads are cheaper to create and switch between; processes are more isolated, so one crashing doesn't take down the others.

**中文**: 一句话：**进程是资源分配的最小单位，线程是 CPU 调度的最小单位**。线程共享：代码段、堆、全局变量、文件描述符；线程私有：栈、寄存器、PC。进程隔离性好但切换贵（要切页表、刷 TLB），线程轻量但一个崩可能全崩。

**Follow-up**: What about coroutines? → User-space scheduled, even lighter, no kernel involvement for switching.

---

### Q2: How do processes communicate? (IPC)

**A:** Main IPC mechanisms: pipes (parent-child, unidirectional), named pipes (FIFOs), message queues, shared memory — the fastest since data isn't copied through the kernel, but it needs synchronization like semaphores — signals for events, and sockets, which also work across machines.

**中文**: 管道、命名管道、消息队列、**共享内存（最快，需配信号量同步）**、信号、socket（可跨机器）。记忆顺序按"从简单到通用"。

---

### Q3: What happens during a context switch?

**A:** The kernel saves the current task's state — registers, program counter, stack pointer — into its PCB/TCB, selects the next task, restores its state, and for a process switch also switches the page table, which flushes the TLB. That TLB flush is why process switches are much more expensive than thread switches.

**中文**: 保存现场（寄存器、PC）→ 调度选下一个 → 恢复现场。进程切换还要**换页表 + TLB 失效**，所以比线程切换贵得多。

---

### Q4: What are the conditions for deadlock? How to prevent it?

**A:** Deadlock requires all four conditions simultaneously: mutual exclusion, hold and wait, no preemption, and circular wait. Breaking any one prevents deadlock — the most practical technique is imposing a global lock ordering to break circular wait. Other strategies: acquire all resources at once, use timeouts/tryLock, or detect-and-recover like databases do.

**中文**: 四条件背诵：**互斥、占有且等待、不可剥夺、循环等待**。最实用预防法：**按固定顺序加锁**（破坏循环等待）。银行家算法属于"避免"（动态判断安全状态）。数据库的做法是检测 + 回滚牺牲者。

**Follow-up**: Livelock? → Threads keep responding to each other and retrying without making progress.

---

### Q5: Explain virtual memory.

**A:** Virtual memory gives each process its own private address space, decoupled from physical RAM. The address space is divided into pages (typically 4KB) mapped to physical frames via page tables, with the TLB caching translations. Pages not in RAM live on disk; touching one triggers a page fault and the OS loads it in — possibly evicting another page. Benefits: isolation between processes, the illusion of more memory than physically available, and efficient sharing of common pages.

**中文**: 每个进程看到独立的虚拟地址空间，**页表**负责虚拟页 → 物理帧映射，**TLB** 是页表缓存。缺页中断 → 从磁盘调入 → 必要时按置换算法（LRU/Clock）淘汰。三大好处：进程隔离、内存超售、共享（如共享库只存一份）。

**Follow-up**: Page replacement algorithms? → FIFO（有 Belady 异常）、LRU（理论好实现贵）、Clock（LRU 近似，实际常用）。

---

### Q6: What's the difference between user mode and kernel mode? What is a system call?

**A:** User mode restricts direct access to hardware and privileged instructions; kernel mode has full access. A system call is the controlled gateway — a user program traps into the kernel (via a software interrupt or syscall instruction) to request services like file I/O, memory allocation, or process creation. The mode switch has overhead, which is why batching I/O matters for performance.

**中文**: 用户态不能直接碰硬件/特权指令，必须通过**系统调用**陷入内核态。read/write/fork/mmap 都是系统调用。态切换有开销 → 这是 buffer/批量 I/O、零拷贝技术存在的原因。

---

### Q7: Common CPU scheduling algorithms?

**A:** FCFS — simple but causes convoy effect; SJF — optimal average waiting time but needs to know job lengths and can starve long jobs; Round Robin — fair time slices, good for interactivity; Priority scheduling — risk of starvation, mitigated by aging; and Multi-Level Feedback Queue, which combines them and is closest to what real OSes use.

**中文**: 先来先服务、短作业优先（平均等待最优但会饿死长任务）、时间片轮转（交互友好）、优先级（需 aging 防饿死）、**多级反馈队列**（实际系统的近似做法：新任务高优先级短时间片，用满降级）。

---

### Q8: How is a thread synchronized? Mutex vs semaphore vs condition variable?

**A:** A mutex provides mutual exclusion — one owner at a time, and only the owner unlocks it. A semaphore is a counter allowing up to N concurrent holders — with N=1 it resembles a mutex but has no ownership concept. A condition variable lets threads sleep until a condition holds, always used with a mutex, and re-checked in a while loop to handle spurious wakeups. The producer-consumer problem is the classic exercise combining all of these.

**中文**: 互斥锁（一人持有）、信号量（计数器，P/V 操作，可允许 N 个并发）、条件变量（等待某条件成立，配合 mutex，用 while 防虚假唤醒）。**生产者-消费者**是必会手写题：两个信号量 (empty/full) + 一个 mutex。

**Follow-up**: Spinlock vs mutex? → 自旋锁忙等不睡眠，适合临界区极短的场景，省去上下文切换。

---

### Q9: What happens when you `fork()`? What about `exec()`?

**A:** `fork()` creates a child process that's a copy of the parent — same code, copied address space — returning 0 in the child and the child's PID in the parent. Modern systems use copy-on-write so pages are only physically copied when either side writes. `exec()` replaces the current process image with a new program. The shell runs commands with fork + exec, and `wait()` reaps the child to avoid zombies.

**中文**: fork 复制进程（**写时复制 COW**，不真的立刻拷内存），子进程返回 0、父进程返回子 PID。exec 替换进程映像。shell 执行命令 = fork + exec + wait。**僵尸进程**：子死了父没 wait；**孤儿进程**：父先死，由 init 收养。

---

### Q10: What is I/O multiplexing? select vs poll vs epoll?

**A:** I/O multiplexing lets one thread monitor many file descriptors at once. `select` and `poll` scan all descriptors each call — O(n), and select caps at 1024. `epoll` (Linux) registers descriptors once and gets notified only of ready ones — O(1) per event, which is why nginx and Redis use it to handle tens of thousands of connections.

**中文**: 一个线程盯多个 fd。select（轮询 + 1024 上限）→ poll（去掉上限仍轮询）→ **epoll（事件驱动，红黑树 + 就绪链表，只返回就绪 fd）**。这是高并发服务器（nginx、Redis）的基石，也是 Reactor 模式的底层。

**Follow-up**: LT vs ET? → 水平触发（没处理完会反复通知）vs 边缘触发（只通知一次，须一次读完，配非阻塞 IO）。

## 📝 Quick Reference 速查

| Topic | Key Point |
|-------|-----------|
| Process vs Thread | 资源分配 vs CPU 调度最小单位; threads share heap, own stack |
| Deadlock | 4 conditions; prevent via lock ordering |
| Virtual memory | page table + TLB; page fault loads from disk |
| fork | COW copy; 0 in child, PID in parent; zombie = un-waited child |
| Syscall | user → kernel trap; expensive → batch I/O |
| epoll | event-driven, O(1); powers nginx/Redis |
| Producer-Consumer | 2 semaphores + 1 mutex — be able to write it |
