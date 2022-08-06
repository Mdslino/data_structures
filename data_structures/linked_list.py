from typing import Any, Optional


class Node:
    __slots__ = ("value", "next")

    def __init__(self, value: Any) -> None:
        self.value = value
        self.next: Optional["Node"] = None

    def __repr__(self):
        return f"Node(value={self.value}, next={self.next})"

    def __str__(self):
        return repr(self)

    def __eq__(self, other):
        return (
            isinstance(other, Node)
            and self.value == other.value
            and self.next == other.next
        )


class LinkedList:
    def __init__(self, value: Any) -> None:
        """
        Create a new None
        """
        new_node = Node(value)
        self.head: Optional[Node] = new_node
        self.tail: Optional[Node] = new_node
        self.__iter_node = None
        self.length: int = 1

    def __len__(self) -> int:
        """
        Return the size of linked list
        """
        return self.length

    @property
    def is_empty(self) -> bool:
        return self.length == 0

    @property
    def is_single_node(self) -> bool:
        return self.tail == self.head

    def append(self, value: Any) -> bool:
        """
        Create a new Node and add Node to the end
        """
        new_node = Node(value)

        if self.is_empty:
            self.head = self.tail = new_node
        elif self.is_single_node:
            self.head.next = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

        return True

    def pop(self) -> Node:
        if self.is_empty:
            raise IndexError("pop from empty linked list")

        poped_node = self.tail

        if self.is_single_node:
            self.head = self.tail = None
            self.length -= 1
            return poped_node

        next_node = self.head
        while next_node:
            if next_node.next is self.tail:
                break
            next_node = next_node.next

        self.tail = next_node
        self.tail.next = None
        self.length -= 1

        return poped_node

    def prepend(self, value: Any) -> bool:
        """
        Create a new Node and add Node to the beginning
        """
        new_node = Node(value)

        if self.is_empty:
            self.head = self.tail = new_node
            self.length += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1

        return True

    def insert(self, index: int, value: Any) -> None:
        """
        Create a new None and insert Node at given index
        """
        pass


linked_list = LinkedList
