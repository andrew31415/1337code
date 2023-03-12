"""Unit testing for lists.py
"""

import pytest

from leetutils import lists


SLL_DEFAULT = [1, 2, 3, 4]
SLL_DEFAULT_LEN = len(SLL_DEFAULT)


@pytest.fixture
def sll_default():
    """Pytest fixture to create a 4 element SLL.

    Returns
    -------
    SinglyLinkedList
        A 4 element SLL constructed from [1, 2, 3, 4].
    """
    return lists.SinglyLinkedList(SLL_DEFAULT)


def test_can_add_node_to_sll():
    """Add node(s) to a singly linked list.
    """
    sll = lists.SinglyLinkedList(set([1, 2, 3]))

    sll = lists.SinglyLinkedList()
    assert sll.length == 0
    assert repr(sll) == "SinglyLinkedList: Empty List"
    assert str(sll) == "SinglyLinkedList: Empty List"

    sll.add_node("new_element")
    assert sll.length == 1

    sll.add_node("new_element")
    assert sll.length == 2

    # Add an element with val=[1,2,3]
    sll.add_node([1, 2, 3])
    assert sll.length == 3
    with pytest.raises(ValueError):
        sll.length = -10


def test_can_add_multiple_nodes_to_sll(sll_default):
    """Add node(s) to a singly linked list.
    """
    sll_default.add_nodes([5, 6, 7])
    assert sll_default.length == (SLL_DEFAULT_LEN + 3)
    sll_default.add_nodes(10)
    assert sll_default.length == (SLL_DEFAULT_LEN + 4)


def test_iterate_over_sll(sll_default):
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
    for_iterator = sll_default.list_head
    for list_node in iter(sll_default):
        assert list_node is for_iterator.val
        for_iterator = for_iterator.next

    sll_iterator = iter(sll_default)
    assert next(sll_iterator) is sll_default.list_head.val
    assert next(sll_iterator) is sll_default.list_head.next.val
    assert next(sll_iterator) is sll_default.list_head.next.next.val
    assert next(sll_iterator) is sll_default.list_head.next.next.next.val

    with pytest.raises(StopIteration):
        # For whatever reason the following next() will return None inside pytest.
        # This doesn't happen outside pytest.
        # This is the 2nd to last next call before StopIteration is raised.
        assert next(sll_iterator) is None
        # The following instruction will throw a StopIteration.
        print(next(sll_iterator))


def test_pop_elements(sll_default):
    """Pop a number of nodes from the end of the SLL.
    """
    sll_default.pop_left(nodes_to_pop=1)
    assert sll_default.length == 3

    # Pop all elements from list
    sll_default.pop_left(nodes_to_pop=sll_default.length)
    assert sll_default.length == 0


def test_pop_from_empty_list(sll_default):
    """Pop from an empty list.
    """
    sll_default.pop_left(nodes_to_pop=sll_default.length)

    with pytest.raises(AttributeError):
        # pop an element from an empty list
        sll_default.pop_left(nodes_to_pop=1)
