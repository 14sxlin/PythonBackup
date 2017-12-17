# 一般是使用for循环,这里使用递归


class Node:
    def __init__(self, v, next_node=None):
        self.v = v
        self.next_node = next_node


class LNode:
    def __init__(self, v, next_node=None, last_node=None):
        self.v = v
        self.next_node = next_node
        self.last_node = last_node

# 这种是指针回指的思路 改变了原来的数据 o(n)
def reverse1(head):
    parent = None
    current = head
    while current is not None:
        nextn = current.next_node
        current.next_node = parent  # 指针回指, 指向自己的parent
        parent = current
        current = nextn
    return parent

# 这种是指针回指的思路 递归版
def reverse1_1(current,parent):
    if current is None:
        return parent
    else:
        nextN = current.next_node
        current.next_node = parent
        return reverse1_1(nextN,current)

# 不改变数据结构的弄法  每次遍历链表,寻找末尾 这种双重循环 o(n^2) 是不改变的数据结构的
def reverse2(head):
    newCurrent = Node(-1)
    newLink = newCurrent
    last = head
    end = None
    while head != end:
        while last.next_node != end:
            last = last.next_node
        newCurrent.next_node = Node(last.v)
        newCurrent = newCurrent.next_node
        end = last
        last = head
    return newLink.next_node


# 改变数据结构的情况 这和reverse2的思路是一样的 , 新增了数据结构, 不改变原来的结构
def reverse3(head):
    parent = LNode(-1)
    current = head
    while current is not None:
        tempLNode = LNode(current.v,last_node=parent)
        parent.next_node = tempLNode
        parent = parent.next_node
        current = current.next_node

    # 重新形成链表
    LNodeLink = parent
    newlink = Node(LNodeLink.v)
    newhead = newlink
    while LNodeLink.last_node is not None:
        newlink.next_node = Node(LNodeLink.last_node.v)
        newlink = newlink.next_node
        LNodeLink = LNodeLink.last_node
    return newhead


def printLink(head):
    node = head
    while node is not None:
        print(node.v, end=" ")
        node = node.next_node
    print()


if __name__ == '__main__':
    link = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7)))))))
    printLink(link)
    # printLink(reverse1(link))
    printLink(reverse1_1(link,None))

    # printLink(reverse2(link))
    # printLink(reverse3(link))
