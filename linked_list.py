from typing import Any


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value: Any) -> None:
        """
        Create a new None
        """
        new_node = Node(value)
        self.head = new_node
        self.tails = new_node
        self.length = 1

    def __len__(self) -> int:
        """
        Return the size of linked list
        """
        return self.length

    def append(self, value: Any) -> None:
        """
        Create a new Node and add Node to the end
        """
        pass

    def prepend(self, value: Any) -> None:
        """
        Create a new Node and add Node to the beginning
        """
        pass

    def insert(self, index: int, value: Any) -> None:
        """
        Create a new None and insert Node at given index
        """
        pass
