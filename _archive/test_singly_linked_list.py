# LeetCodeのテストケース
# https://leetcode.com/explore/learn/card/linked-list/209/singly-linked-list/1290/


import pytest

from src.data_structures.singly_linked_list import SinglyLinkedList


class TestSinglyLinkedList:
    def test_example_operations(self):
        """LeetCodeのサンプルケースを元にしたテスト"""
        linked_list = SinglyLinkedList()

        # addAtHead(1)
        linked_list.addAtHead(1)
        assert linked_list.head.val == 1
        assert linked_list.head.next is None

        # addAtTail(3)
        linked_list.addAtTail(3)
        assert linked_list.head.val == 1
        assert linked_list.head.next.val == 3

        # addAtIndex(1, 2)
        linked_list.addAtIndex(1, 2)
        assert linked_list.head.val == 1
        assert linked_list.head.next.val == 2
        assert linked_list.head.next.next.val == 3

        # get(1)
        assert linked_list.get(1) == 2

        # deleteAtIndex(1)
        linked_list.deleteAtIndex(1)
        assert linked_list.head.val == 1
        assert linked_list.head.next.val == 3

        # get(1)
        assert linked_list.get(1) == 3

    """
    LeetCodeのテストケース
    Input: ["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
           [[],[1],[3],[1,2],[1],[1],[1]]
    Expected: [null,null,null,null,2,null,3]
    """

    def test_leetcode_operations(self):
        # MyLinkedList()
        linked_list = SinglyLinkedList()
        assert linked_list is not None  # null の代わりに Python では None

        # addAtHead(1)
        result = linked_list.addAtHead(1)
        assert result is None  # 戻り値は null (Python では None)

        # addAtTail(3)
        result = linked_list.addAtTail(3)
        assert result is None

        # addAtIndex(1, 2)
        result = linked_list.addAtIndex(1, 2)
        assert result is None

        # get(1)
        result = linked_list.get(1)
        assert result == 2

        # deleteAtIndex(0)
        result = linked_list.deleteAtIndex(0)
        assert result is None

        # get(0)
        result = linked_list.get(0)
        assert result == 2
