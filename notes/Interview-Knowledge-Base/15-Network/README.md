# Computer Networks 计算机网络八股

> TCP/UDP, HTTP/HTTPS, DNS — "what happens when you type a URL" territory. 网络八股核心就一条主线：从输入 URL 到页面渲染。

## 🎯 High-Frequency Questions 高频问题

### Q1: What happens when you type a URL and press Enter?

**A:** First, DNS resolution: browser cache → OS cache → recursive query to DNS servers to get the IP. Then a TCP connection is established with the three-way handshake; if HTTPS, a TLS handshake follows to negotiate keys. The browser sends an HTTP request; the server responds with HTML; the browser parses it, fetches referenced resources (CSS/JS/images), builds the DOM and render tree, and paints the page. Finally connections are reused (keep-alive) or closed with the four-way wave.

**中文**: 这是网络面试的**总纲题**，串起所有知识点：DNS → TCP 三次握手 → TLS 握手 → HTTP 请求/响应 → 浏览器渲染 → 四次挥手。答的时候按层展开，面试官会从中挑一个深挖。

---

### Q2: Explain the TCP three-way handshake. Why three, not two?

**A:** Client sends SYN with initial sequence number x; server replies SYN-ACK with its own sequence y and ack x+1; client sends ACK y+1, and the connection is established. Two-way isn't enough because the server couldn't confirm the client received its sequence number — and a stale, delayed SYN could trick the server into opening a dead connection and wasting resources.

**中文**: SYN → SYN+ACK → ACK。为什么三次：①双方都要确认**自己的发送和接收能力**都正常（两次只能确认一方）；②防止网络中滞留的旧 SYN 让服务器白白建立连接。本质：可靠地同步双方初始序列号 (ISN)。

**Follow-up**: SYN flood attack? → 攻击者只发 SYN 不回 ACK，耗尽半连接队列；防御：SYN cookies。

---

### Q3: Explain the four-way handshake (connection teardown). Why TIME_WAIT?

**A:** Either side sends FIN; the peer ACKs it, finishes sending remaining data, then sends its own FIN, which gets ACKed. It's four steps because TCP is full-duplex — each direction closes independently. The active closer enters TIME_WAIT for 2×MSL to ensure the final ACK can be retransmitted if lost, and to let old duplicate segments die out before the same port pair is reused.

**中文**: FIN → ACK → FIN → ACK。四次是因为**全双工**，两个方向分别关。TIME_WAIT（2MSL，约 1-4 分钟）两个作用：①最后的 ACK 丢了能重发；②让旧连接的迷路报文在网络中消亡，避免污染新连接。服务器大量 TIME_WAIT → 调 SO_REUSEADDR / 连接池。

---

### Q4: TCP vs UDP — differences and when to use each?

**A:** TCP is connection-oriented and reliable: ordered delivery, retransmission, flow control, and congestion control — at the cost of latency and overhead. UDP is connectionless, best-effort, message-oriented, with a tiny 8-byte header. Use TCP for correctness-critical data: web, APIs, file transfer. Use UDP when latency beats reliability: video calls, gaming, DNS — and QUIC/HTTP3 builds reliability on top of UDP.

**中文**: TCP：面向连接、可靠（确认+重传+排序）、流量控制、拥塞控制、字节流。UDP：无连接、不可靠、报文边界、头部仅 8 字节。选型一句话：**要对就 TCP，要快就 UDP**。亮点：QUIC (HTTP/3) 在 UDP 上自建可靠性，兼得低延迟和可靠。

---

### Q5: How does TCP guarantee reliability?

**A:** Five mechanisms: sequence numbers to order data and detect loss; cumulative ACKs; retransmission on timeout (RTO) or on three duplicate ACKs (fast retransmit); checksums to detect corruption; flow control via the sliding receive window so the sender doesn't overwhelm the receiver; plus congestion control to avoid overwhelming the network.

**中文**: 背五件套：**序列号、确认应答、超时重传（+快重传）、校验和、滑动窗口（流控）**。流量控制管接收方，拥塞控制管网络——两个窗口取小者决定实际发送量。

---

### Q6: Explain TCP congestion control.

**A:** Four phases: slow start — the congestion window doubles every RTT from a small start; once past the ssthresh threshold, congestion avoidance — linear growth; on three duplicate ACKs, fast retransmit and fast recovery — halve the window and continue linearly; on a timeout, reset the window to 1 MSS and re-enter slow start. Modern variants include CUBIC (Linux default) and BBR.

**中文**: 慢启动（指数）→ 拥塞避免（线性，过 ssthresh 后）→ 快重传/快恢复（收到 3 个重复 ACK，窗口减半）→ 超时则归 1 重来。记忆图像："指数爬坡 → 线性爬坡 → 摔一跤减半 → 摔大跤归零"。

---

### Q7: HTTP vs HTTPS? How does TLS work?

**A:** HTTPS is HTTP over TLS, providing encryption, integrity, and server authentication. The TLS handshake: the server presents a certificate signed by a trusted CA; the client verifies it, then the two sides use asymmetric crypto to agree on a shared symmetric session key — TLS 1.3 typically uses ECDHE for forward secrecy — and all subsequent data is encrypted symmetrically, since symmetric crypto is much faster.

**中文**: 核心思想：**非对称加密交换密钥，对称加密传输数据**。证书解决"公钥是谁的"问题：CA 用私钥给服务器公钥签名，浏览器内置 CA 公钥可验证。TLS 1.3 把握手压缩到 1-RTT。中间人攻击防御靠证书链验证。

**Follow-up**: 对称 vs 非对称？→ AES 快用于数据；RSA/ECC 慢用于换钥和签名。

---

### Q8: Common HTTP status codes and methods?

**A:** Status codes: 200 OK, 201 Created, 301 permanent redirect, 302 temporary redirect, 304 Not Modified (cache), 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 429 Too Many Requests, 500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable. Methods: GET (read, idempotent), POST (create), PUT (replace, idempotent), PATCH (partial update), DELETE (idempotent).

**中文**: 分类记：1xx 信息、2xx 成功、3xx 重定向、4xx 客户端错、5xx 服务端错。高频追问：**GET vs POST**（语义/幂等性/参数位置/缓存）、**幂等性**（GET/PUT/DELETE 幂等，POST 不幂等——重试设计的基础）、301 vs 302、401（没登录）vs 403（没权限）。

---

### Q9: HTTP/1.1 vs HTTP/2 vs HTTP/3?

**A:** HTTP/1.1 added keep-alive but suffers head-of-line blocking — requests on one connection are serialized. HTTP/2 introduces binary framing and multiplexing — many streams over one TCP connection, plus header compression and server push — but TCP-level HOL blocking remains: one lost packet stalls all streams. HTTP/3 runs on QUIC over UDP: independent streams with no TCP HOL blocking, 0/1-RTT handshakes, and connection migration across network changes.

**中文**: 演进主线是消灭**队头阻塞 (HOL blocking)**：1.1 管道化失败 → 2 多路复用解决应用层 HOL，但 TCP 丢包仍卡所有流 → 3 换 QUIC (UDP)，流之间真正独立。加分项：QUIC 连接迁移（WiFi 切 4G 不断线，靠 connection ID 而非四元组）。

---

### Q10: How does DNS work?

**A:** DNS translates domain names to IPs. Resolution order: browser cache → OS/hosts → local recursive resolver, which iteratively queries root servers → TLD servers (.com) → authoritative servers for the domain, then caches the result per the TTL. DNS uses UDP port 53 for queries, falling back to TCP for large responses and zone transfers.

**中文**: 递归查询（客户端→本地DNS）+ 迭代查询（本地DNS→根→顶级域→权威）。各级都有缓存，TTL 控制。记录类型：A（IPv4）、AAAA（IPv6）、CNAME（别名）、MX（邮件）、NS。DNS 也是负载均衡手段之一（轮询返回多个 IP）。

---

### Q11: What are cookies and sessions? What about JWT?

**A:** HTTP is stateless. Cookies are key-value pairs the server sets and the browser auto-sends back, used to carry a session ID; the actual user state lives server-side in the session store. JWT instead encodes the claims in a signed token stored client-side — the server only verifies the signature, making it stateless and horizontally scalable, but tokens can't easily be revoked before expiry.

**中文**: Cookie（浏览器存，自动携带）→ Session（服务端存状态，Cookie 只放 sessionId）→ JWT（状态放 token 里签名防篡改，服务端无状态易扩展，代价是**难注销**，需配短过期+refresh token 或黑名单）。安全属性：HttpOnly 防 XSS 偷 cookie，SameSite 防 CSRF。

## 📝 Quick Reference 速查

| Topic | Key Point |
|-------|-----------|
| 3-way handshake | SYN / SYN-ACK / ACK; sync ISNs, confirm both directions |
| 4-way wave | full-duplex closes independently; TIME_WAIT = 2MSL |
| TCP reliability | seq + ACK + retransmit + checksum + sliding window |
| Congestion | slow start → avoidance → fast recovery; CUBIC/BBR |
| HTTPS | asymmetric to exchange key, symmetric for data; CA cert chain |
| HTTP evolution | 1.1 keep-alive → 2 multiplexing → 3 QUIC/UDP no HOL |
| DNS | recursive + iterative, cached by TTL, UDP 53 |
| 401 vs 403 | unauthenticated vs unauthorized |
