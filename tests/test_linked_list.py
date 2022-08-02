import pytest
from data_structures.linked_list import LinkedList, Node


def test_linked_list_creation():
    linket_list = LinkedList(1)

    assert linket_list.head.value == 1
    assert linket_list.tail.value == 1


def test_linked_list_len():
    linket_list = LinkedList(1)

    assert len(linket_list) == 1


def test_linked_list_iter():
    linked_list = LinkedList(1)

    count = 0

    for _ in linked_list:
        count += 1

    assert count == 1


def test_linked_list_append_on_empty(empty_linked_list):
    assert empty_linked_list.head is None
    assert empty_linked_list.tail is None

    empty_linked_list.append(1)

    assert empty_linked_list.head.value == 1
    assert empty_linked_list.tail.value == 1
    assert empty_linked_list.head is empty_linked_list.tail


def test_linked_list_append():
    linked_list = LinkedList(1)

    assert linked_list.head.value == 1
    assert linked_list.tail.value == 1
    assert linked_list.head is linked_list.tail

    linked_list.append(2)

    assert len(linked_list) == 2
    assert linked_list.head is not linked_list.tail
    assert linked_list.head.value == 1
    assert linked_list.tail.value == 2


def test_pop_linked_lint_empty(empty_linked_list):
    with pytest.raises(IndexError):
        empty_linked_list.pop()


def test_pop_linked_list():
    linked_list = LinkedList(1)

    assert linked_list.head.value == 1
    assert linked_list.tail.value == 1
    assert linked_list.head is linked_list.tail

    linked_list.append(2)

    assert len(linked_list) == 2
    assert linked_list.head is not linked_list.tail
    assert linked_list.head.value == 1
    assert linked_list.tail.value == 2

    node = linked_list.pop()

    assert isinstance(node, Node)
    assert linked_list.head.value == 1
    assert linked_list.tail.value == 1
    assert linked_list.head is linked_list.tail


def test_pop_linked_list_with_one_item():
    linked_list = LinkedList(1)

    assert linked_list.head.value == 1
    assert linked_list.tail.value == 1
    assert linked_list.head is linked_list.tail

    node = linked_list.pop()

    assert isinstance(node, Node)
    assert linked_list.is_empty
    assert linked_list.head is None
    assert linked_list.tail is None
    assert linked_list.head is linked_list.tail
