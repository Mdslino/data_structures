import pytest
from src.linked_list import LinkedList

@pytest.fixture
def empty_linked_list():
    linked_list =LinkedList(1)
    linked_list.head = None
    linked_list.tail = None
    linked_list.length = 0

    return linked_list