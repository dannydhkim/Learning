"""
A Linked List is a series of node objects that point to each other.
A Linked List is also an object itself.
Each node object is very simple of containing a value and a pointer.
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def __repr__(self):
        node = self.head
        nodes = []
        while node:
            nodes.append(str(node.val))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def traverseList(self):
        node = self.head
        while node:
            yield node.val
            node = node.next

if __name__=='__main__':
    linkedlist = LinkedList()
    node1 = ListNode(1)
    linkedlist.head = node1
    node2 = ListNode(2)
    node1.next = node2
    node3 = ListNode(3)
    node2.next = node3
    node4 = ListNode(4)
    node3.next = node4
    node5 = ListNode(5)
    node4.next = node5
    print(repr(linkedlist))
    print(list(linkedlist.traverseList()))