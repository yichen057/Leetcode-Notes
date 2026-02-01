# 链表（链式存储）基本原理
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def createLinkedList(arr: 'List[int]') -> 'ListNode': # 类型注解（type hint），表示 arr 预期是一个整数列表。'List[int]' 这里用字符串写法，是为了避免循环 import；一般写 List[int] 就够。
        if arr is None or len(arr) == 0:
            return None
        
        # 输入一个数组，转换为一条单链表
        head = ListNode(arr[0]) # 取数组第一个元素，生成链表的第一个节点, 表示链表的起点（头节点）
        cur = head # cur 是一个工作指针，用来在链表上移动、添加新节点; 而head 永远保存头节点，不能动。
        for i in range(1, len(arr)):
            cur.next = ListNode(arr[i])
            cur = cur.next
        
        return head # 函数返回的时候，必须返回这个起点，否则你就失去了访问整条链表的入口。
# 调用

# 场景1: 单链表的遍历/查找/修改, 访问单链表的每一个节点，并打印其值
# 如果是要通过索引访问或修改链表中的某个节点，也只能用 for 循环从头结点开始往后找，直到找到索引对应的节点，然后进行访问或修改。

head = createLinkedList([1, 2, 3, 4, 5])
p = head
print("原始链表:")
while p is not None:
    print(p.val, end=" ")
    p = p.next
print("None")
# 场景2: 单链表头部插入新元素
# 创建一条单链表
head = createLinkedList([1, 2, 3, 4, 5])

# 在单链表头部插入一个新节点0
newNode = ListNode(0)
newNode.next = head
head = newNode

p = head
print("单链头部插入新元素0后:")
while p is not None: # 只要当前节点存在，就继续遍历. 用来遍历并打印所有节点（包括尾节点）
    print(p.val, end=" -> ")   # 打印当前节点的值
    p = p.next
print("None")  # 表示链表结束
# 现在链表变成了 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> None

# 场景3: 单链表尾部插入新元素
def appendToTail(head: ListNode, val: int) -> ListNode:
    newNode = ListNode(val)
    if not head:   # 如果链表为空，直接返回新节点
        return newNode

    p = head
    while p.next:   # 当p还有下一个节点时, 就往后走,最后 p 会停在尾节点本身找到尾节点. 
        p = p.next
    # 现在 p 就是链表的最后一个节点. 在 p 后面插入新节点
    p.next = newNode
    return head

def printLinkedList(head: ListNode):
    p = head
    while p:
        print(p.val, end=" -> ")
        p = p.next
    print("None")

# 假设 ListNode 已经定义好
head = createLinkedList([1, 2, 3, 4, 5])

# 在尾部插入新节点 6
head = appendToTail(head, 6)

# 打印链表
print("单链尾部插入新节点6后:")
printLinkedList(head)
# 现在链表变成了 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None

# 场景4: 单链表中间插入新元素
def appendToMiddle(head: ListNode, val: int, index: int) -> ListNode:
    newNode = ListNode(val)
    if not head:
        return newNode
    
    p = head #初始 p=1
    for _ in range(index - 1):
    # 第 1 次循环：p=2
    # 第 2 次循环：p=3 ✅（停在第 3 个节点）
        p = p.next
    # 此时 p 指向第 index 个节点, 组装新节点的后驱指针
    
    # 要避免丢掉 插入后的元素不丢失，你需要先保存 p.next保存原本的后继节点, 即把 p 的下一个节点保存下来
    # .next 在 右边，表示“读取”
    nextNode = p.next # nextNode = 4
    # 插入新节点, 即把 p 的下一个节点 改成 newNode
    # .next 在 左边，表示“赋值 / 修改”
    p.next = newNode # 3 -> 66, p=3，则 3.next 不再指向 4，而是改为指向 66。
    newNode.next = nextNode # 66 -> 4, 让 新节点（66）指向原来的后继节点（4）,这样链表就不断开了

# .next 在右边 → “访问/读取” 节点, 取出指针指向的节点
# .next 在左边 → “更新/修改” 指向, 修改指针的指向
    return head

# 假设 ListNode 已经定义好
head = createLinkedList([1, 2, 3, 4, 5])

# 在第 3 个节点后面插入一个新节点 66
# 先要找到前驱节点，即第 3 个节点
head = appendToMiddle(head, 66, 3 )

# 打印链表
print("插入第 3 个节点66后:")
printLinkedList(head)

# 现在链表变成了 1 -> 2 -> 3 -> 66 -> 4 -> 5

# 场景5: 单链表中间删除元素
# 删除一个节点，首先要找到要被删除节点的前驱节点，然后把这个前驱节点的 next 指针指向被删除节点的下一个节点。这样就能把被删除节点从链表中摘除了
# 即: “找到前驱 → 指针绕过 → 自动回收”
def deleteAtIndex(head: ListNode, index: int) -> ListNode:
    # 空链表 或 index 非法
    if not head or index <1:
        return head
    
    # 删除头节点
    if index == 1:
        return head.next
    
    # 移动指针, 找到 index-1要删节点 位置的前驱节点
    p = head
    for _ in range(index - 2):
        if not p.next:# 如果 p.next不存在, index越界
            return head # index 越界，直接返回原链表
        p = p.next
#     假设 index=4（想删第 4 个节点），那循环次数是 4-2=2。
# 初始 p=head=1
# 第 1 次循环后：p=2
# 第 2 次循环后：p=3
# 循环结束时，p 正好停在 第 3 个节点（也就是要删的第 4 个节点的前驱）。
    # 删除index节点操作（如果 p.next 存在才删除）
    if p.next:
        p.next = p.next.next # 绕过要删的节点，让前驱直接指向后继。
# p=3，p.next=4
# p.next.next=5
# 执行 p.next = p.next.next 后，3.next 就直接指向 5
# 节点 4 被“摘掉”了，没有任何节点再指向它，Python 的垃圾回收会自动回收它。
    return head

# 假设 ListNode 已经定义好
head = createLinkedList([1, 2, 3, 4, 5])
print("原始链表:")
printLinkedList(head)

# 删除第 4 个节点（值=4）
head = deleteAtIndex(head, 4)

# 打印链表
print("删除第 4 个节点后:")
printLinkedList(head)
# 现在链表变成了 1 -> 2 -> 3 -> 5 -> None

# 场景6: 单链表尾部删除元素: 找到倒数第二个节点，然后把它的 next 指针置为 null 就行了Just find the second-to-last node and set its next pointer to null:
def deleteTailNode(head: ListNode) -> ListNode:
    if not head or not head.next:# 链表为空或只有一个节点, 返回None
        return None

    p = head #初始 p=1
    while p.next.next is not None:
        p = p.next

# now p points to the second to last node 此时 p 指向倒数第二个节点
# detach the tail node from the linked list 把尾节点从链表中摘除
    p.next = None
    return head

# 假设 ListNode 已经定义好
head = createLinkedList([1, 2, 3, 4, 5])
print("原始链表:")
printLinkedList(head)

# 删除最后一个节点
head = deleteTailNode(head)

# 打印链表
print("删除最后一个节点后:")
printLinkedList(head)
# 现在链表变成了 1 -> 2 -> 3 -> 4 -> None

# 场景7: 单链表头部删除元素:
def deleteHeadNode(head: ListNode) -> ListNode:
    if not head:
        return None
    
    head = head.next
    return head

# 假设 ListNode 已经定义好
head = createLinkedList([1, 2, 3, 4, 5])

# 删除头部节点
head = deleteHeadNode(head)

# 打印链表
print("删除头部节点后:")
printLinkedList(head)
# 现在链表变成了 2 -> 3 -> 4 -> 5 -> None