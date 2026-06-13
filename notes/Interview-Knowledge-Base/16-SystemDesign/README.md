# System Design 系统设计

> Framework + core building blocks. Intern 面试少考，New Grad 常考简化版（设计一个 API / 短链接 / 排行榜）。

## 🧭 Delivery Framework 答题框架 (≈35-45 min)

| Step | Time | What to do | 中文要点 |
|------|------|-----------|---------|
| 1. Requirements | 5 min | Functional + Non-functional (scale, latency, availability) | 先问清楚！QPS、用户量、读写比 |
| 2. Core Entities & API | 5 min | Define entities, REST endpoints | 名词→实体，动词→API |
| 3. High-Level Design | 10-15 min | Draw boxes: client → LB → service → DB/cache | 先画能 work 的简单版 |
| 4. Deep Dives | 10 min | Scale bottlenecks, edge cases | 面试官引导方向，主动提 trade-off |
| 5. Wrap-up | 2 min | Summarize, future work | 总结取舍 |

**Estimation 速算**: 1 day ≈ 10⁵ s；1M DAU × 10 req/day ≈ 100 QPS（峰值 ×2-3）；1 char = 1 byte；UUID 16 bytes。

## 🎯 Core Concepts Q&A 核心概念

### Q1: How do you scale a web service?

**A:** Start with vertical scaling, then horizontal: put stateless app servers behind a load balancer, store session state externally (Redis), cache hot reads, use read replicas for the database, then shard when a single primary can't handle writes. Use a CDN for static content and async queues to decouple slow work.

**中文**: 套路链：**垂直 → 无状态化 + LB 水平扩展 → 缓存 → 读写分离 → 分库分表 → CDN + 消息队列异步化**。背熟这条链，多数 scale 问题都能展开。

---

### Q2: Explain the CAP theorem.

**A:** In a distributed system, when a network Partition happens, you must choose between Consistency — every read sees the latest write — and Availability — every request gets a response. Since partitions are unavoidable, real systems choose CP (e.g., banking, ZooKeeper) or AP (e.g., DNS, shopping carts, Cassandra). Most practical systems aim for eventual consistency with high availability.

**中文**: P（分区容错）必选，实际是 **C 和 A 二选一**。钱相关选 C（宁可不可用不能错），社交 feed 选 A（晚几秒看到没关系，最终一致）。答题时用业务场景论证选择。

---

### Q3: SQL vs NoSQL — how do you choose?

**A:** SQL gives ACID transactions, joins, and strong schemas — choose it when data is relational and correctness matters: payments, inventory. NoSQL trades that for horizontal scalability and flexible schemas: key-value (Redis) for caching, document (MongoDB) for nested flexible data, wide-column (Cassandra) for huge write throughput, graph for relationship-heavy data. A common answer: default to Postgres until scale forces specialization.

**中文**: 默认答 **"先用 Postgres"**（面试官喜欢务实）。需要事务/复杂查询 → SQL；海量写入/简单查询模式/灵活 schema → NoSQL。补充：现代分布式 SQL (Spanner, CockroachDB) 在模糊这条界限。

---

### Q4: How does caching work? What are the main strategies and pitfalls?

**A:** Cache-aside is most common: read from cache, on miss read DB and populate cache; on write, update DB and invalidate the cache entry. Eviction is typically LRU with TTLs. Pitfalls: cache stampede — many requests hitting DB when a hot key expires, mitigated by locks or staggered TTLs; cache penetration — queries for nonexistent keys, mitigated by negative caching or bloom filters; and stale data from race conditions.

**中文**: 三大经典问题背诵：**缓存雪崩**（大量 key 同时过期 → TTL 加随机抖动）、**缓存击穿**（热 key 过期瞬间 → 互斥锁/永不过期+异步刷新）、**缓存穿透**（查不存在的 key → 布隆过滤器/缓存空值）。写策略：先更 DB 再删缓存 (cache-aside) 是默认答案。

---

### Q5: How does a load balancer work?

**A:** It distributes traffic across servers. L4 balances on IP/port — fast; L7 understands HTTP and can route by path or header. Algorithms: round robin, least connections, consistent hashing for sticky/sharded workloads. Health checks remove bad nodes. The LB itself is made highly available with redundant pairs.

**中文**: L4（传输层，快）vs L7（应用层，能按 URL/header 路由）。**一致性哈希**是高频深挖点：节点增删只迁移 1/n 数据，配虚拟节点防倾斜——要会手画哈希环。

---

### Q6: How do you design for high availability?

**A:** Eliminate single points of failure with redundancy at every layer: multiple app instances across availability zones, database replication with automated failover, health checks and timeouts, retries with exponential backoff and jitter, circuit breakers to stop cascading failures, and graceful degradation — serve cached or partial results instead of errors. Availability is measured in nines: 99.9% is about 8.7 hours of downtime a year.

**中文**: 关键词清单：**冗余、多可用区、自动故障转移、超时+重试（指数退避）、熔断、降级、限流**。"四个9" = 一年宕机 52 分钟。重试必须配幂等性设计（幂等键）。

---

### Q7: Message queues — why and when?

**A:** Queues decouple producers from consumers, absorb traffic spikes, and enable async processing — e.g., a checkout returns immediately while emails and analytics happen in the background. Kafka adds ordered, replayable logs for streaming. Key considerations: at-least-once delivery means consumers must be idempotent; watch for backlog and use DLQs for poison messages.

**中文**: 三大作用：**解耦、削峰、异步**。必备追问：消息重复（消费端幂等）、消息丢失（ack + 持久化）、消息顺序（Kafka 分区内有序）。

## 📋 Classic Problems 经典题

| Problem | 考点 |
|---------|------|
| URL Shortener (TinyURL) | 哈希 vs 自增 ID + base62、读多写少、缓存、301/302 |
| Rate Limiter | 令牌桶/滑动窗口、Redis + Lua、分布式计数 |
| Twitter Feed | fan-out on write vs read、推拉结合、热点用户 |
| Chat (WhatsApp) | WebSocket、消息顺序、在线状态、已读回执 |
| Top-K / Leaderboard | Redis ZSET、近似算法 (count-min sketch) |
| Web Crawler | BFS、去重 (bloom filter)、politeness、分布式调度 |

> 详细题解放本目录下单独文件，按 [TEMPLATE.md](../TEMPLATE.md) 补充；配合 [18-HelloInterview](../18-HelloInterview/) 笔记食用。
