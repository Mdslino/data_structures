from typing import Any

from src.exceptions import EmptyLinkedListError


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
        self.head: Node = new_node
        self.tail: Node = new_node
        self.__iter_node = None
        self.length: int = 1

    def __len__(self) -> int:
        """
        Return the size of linked list
        """
        return self.length

    def __iter__(self):
        if not self.is_empty:
            self.__iter_node = self.head
            return self
        raise EmptyLinkedListError(
            "The linked list is already empty and cannot be iterated"
        )

    def __next__(self):
        if self.__iter_node:
            old_node = self.__iter_node
            self.__iter_node = self.__iter_node.next
            return old_node

        raise StopIteration

    @property
    def is_empty(self) -> bool:
        return self.length == 0

    def append(self, value: Any) -> None:
        """
        Create a new Node and add Node to the end
        """
        new_node = Node(value)

        if self.is_empty:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def pop(self) -> Node:
        if self.is_empty:
            raise EmptyLinkedListError(
                "The linked list is already empty and cannot use pop method"
            )

        poped_node = self.tail

        if self.tail is self.head:
            self.head = self.tail = None
            self.length -= 1
            return poped_node

        for item in self:
            if item.next is self.tail:
                last_item = item

        self.tail = last_item
        self.tail.next = None
        self.length -= 1
        return poped_node

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
