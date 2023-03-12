"""Unit testing for lists.py
"""

import pytest

from leetutils import lists


sll_default = [1, 2, 3, 4]
sll_default_len = len(sll_default)


@pytest.fixture
def sll():
    """Pytest fixture to create a 4 element SLL.

    Returns
    -------
    SinglyLinkedList
        A 4 element SLL constructed from [1, 2, 3, 4].
    """
    return lists.SinglyLinkedList(sll_default)


def test_can_add_node_to_sll():
    """Add node(s) to a singly linked list.
    """
    sll = lists.SinglyLinkedList()
    assert sll.length == 0

    sll.add_node("new_element")
    assert sll.length == 1

    sll.add_node("new_element")
    assert sll.length == 2

    # Add an element with val=[1,2,3]
    sll.add_node([1, 2, 3])
    assert sll.length == 3


def test_can_add_multiple_nodes_to_sll(sll):
    """Add node(s) to a singly linked list.
    """
    sll.add_nodes([5, 6, 7])
    assert sll.length == (sll_default_len + 3)


def test_iterate_over_sll(sll):
    """Using 2 different ways of iteration.

    * Using *for* loop.
    * Creating iterator object.

    Note
    ----
    Instead of catching StopIteration as one might suppose, pytest needs to
    catch the RuntimeError instead. The answer is covered in `this`_
    stackoverflow thread and `here`_ in the official Python documentation.

    .. _this: https://stackoverflow.com/a/66567704/7534151
    .. _here: https://docs.python.org/3/library/exceptions.html#StopIteration
    """
    for_iterator = sll.list_head
    for list_node in iter(sll):
        assert list_node is for_iterator.val
        for_iterator = for_iterator.next

    sll_iterator = iter(sll)
    assert next(sll_iterator) is sll.list_head.val
    assert next(sll_iterator) is sll.list_head.next.val
    assert next(sll_iterator) is sll.list_head.next.next.val
    assert next(sll_iterator) is sll.list_head.next.next.next.val

    with pytest.raises(StopIteration):
        # For whatever reason the following next() will return None inside pytest.
        # This doesn't happen outside pytest.
        # This is the 2nd to last next call before StopIteration is raised.
        assert next(sll_iterator) is None
        # The following instruction will throw a StopIteration.
        print(next(sll_iterator))


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
