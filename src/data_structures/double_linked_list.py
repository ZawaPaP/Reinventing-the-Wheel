# Structure Reference: leetCode
# https://leetcode.com/explore/learn/card/linked-list/210/doubly-linked-list/1294/


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoubleLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        if self.head is None:
            return -1
        current_node = self.head
        current_index = 0
        while current_node:
            if current_index == index:
                return current_node.val
            if not current_node.next:
                return -1
            current_node = current_node.next
            current_index += 1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node
        return

    def addAtTail(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val)
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        new_node = Node(val)
        current_node.next = new_node
        new_node.prev = current_node
        return

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        current_node = self.head
        current_index = 0
        while current_node and current_index < index - 1:
            current_node = current_node.next
            current_index += 1
        if not current_node:
            return
        new_node = Node(val)
        new_node.next = current_node.next
        if current_node.next:
            current_node.next.prev = new_node
        current_node.next = new_node
        new_node.prev = current_node
        return

    def deleteAtIndex(self, index: int) -> None:
        if index == 0 and self.head:
            self.head = self.head.next
            return
        current_node = self.head
        current_index = 0
        while current_index < index - 1:
            if not current_node.next:
                return
            current_node = current_node.next
            current_index += 1

        if current_node and current_node.next:
            current_node.next.prev = current_node
            current_node.next = current_node.next.next
        return
