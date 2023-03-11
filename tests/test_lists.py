"""Unit testing for lists.py
"""

import pytest

from leetutils import lists


@pytest.fixture
def sll():
    """Pytest fixture to create a 4 element SLL.

    Returns
    -------
    SinglyLinkedList
        A 4 element SLL constructed from [1, 2, 3, 4].
    """
    return lists.SinglyLinkedList([1, 2, 3, 4])


def test_can_add_node_to_sll():
    """Add node(s) to a singly linked list.
    """
    sll = lists.SinglyLinkedList()
    sll.add_node("new_element")
    sll.add_node("new_element")
    assert sll.length == 2

    # Add an element with val=[1,2,3]
    sll.add_node([1, 2, 3])
    assert sll.length == 3


def test_can_add_multiple_nodes_to_sll(sll):
    """Add node(s) to a singly linked list.
    """
    sll.add_nodes([5, 6, 7])
    assert sll.length == 7


def test_pop_elements(sll):
    """Pop a number of nodes from the end of the SLL.
    """
    sll.pop_left(nodes_to_pop=1)
    assert sll.length == 3

    # Pop all elements from list
    sll.pop_left(nodes_to_pop=sll.length)
    assert sll.length == 0


def test_pop_from_empty_list(sll):
    """Pop from an empty list.
    """
    sll.pop_left(nodes_to_pop=sll.length)

    with pytest.raises(AttributeError):
        # pop an element from an empty list
        sll.pop_left(nodes_to_pop=1)
