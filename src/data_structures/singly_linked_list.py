# Structure Reference: leetCode
# https://leetcode.com/explore/learn/card/linked-list/209/singly-linked-list/1290/

# int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
# void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
# void addAtTail(int val) Append a node of value val as the last element of the linked list.
# void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
# void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:

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
        current_node.next = new_node
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
            print(current_node.val)
            print(current_node.next.val)
            print(current_node.next.next.val)
            current_node.next = current_node.next.next
        return
