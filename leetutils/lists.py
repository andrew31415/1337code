"""OOP implementation of Lists.
"""

class ListNode:
    """An object containing a value and an identifier to another object of the
    same ListNode type.
    """

    def __init__(self, val=None, next=None) -> None:
        """ListNode constructor.

        Parameters
        ----------
        val : any, optional
            Object stored in node, by default None
        next : ListNode, optional
            Identifier to another ListNode like element, by default None
        """
        self.val: object = val

        # TODO: maybe raise if is not instance of same type
        # if not next and not isinstance(next, ListNode):
        #     raise TypeError(f"Element with {val=} doesn't have a valid next ")
        self.next: object = next

    def __repr__(self) -> str:
        return f"ListNode{{val: {self.val}, next: {self.next}}}"

    def __str__(self) -> str:
        return f"ListNode{{val: {self.val}, next: {self.next}}}"


class SinglyLinkedList:
    """Contains a singly linked list of ListNode type elements.

    Notes
    -----

    element_1: [value, element_2_identifier]
    element_2: [value, element_3_identifier]
    element_3: [value, element_4_identifier]
    element_4: [value, None]
    """

    def __init__(self, val_list=None) -> None:
        """SinglyLinkedList constructor.

        Examples
        --------

        SinglyLinkedList(val_list=[1,2,3])

        Parameters
        ----------
        val_list : list | tuple | str, optional
            Sequence of objects to be stored in the list, by default []
        """
        self._length: int = 0
        self.list_head: ListNode = None

        if not hasattr(val_list, "__getitem__"):
            #TODO: use logger
            print(f"Trying to create an SLL with a non iterable object {val_list=}")
            self.list_head = ListNode(val_list, None)
            self._length = 1
            return

        for val in val_list[::-1]:
            self.list_head = ListNode(val, self.list_head)
            self._length += 1

    def add(self, list_node: ListNode):
        """Adds a new element at the end of the list.

        Parameters
        ----------
        list_node : ListNode
            Contains an object and an identifier.

        Returns
        -------
        None
        """
        list_end: ListNode = self.list_head

        while list_end.next:
            list_end = list_end.next

        list_end.next = ListNode(val=list_node, next=None)

        self._length += 1

    def pop_left(self, nodes_to_pop: int):
        """Removes the first element from the list.

        Parameters
        ----------
        number_of_nodes : int, optional
            Number of nodes to be popped, by default None

        Returns
        -------
        None
        """
        while nodes_to_pop:
            try:
                self.list_head = self.list_head.next
                nodes_to_pop -= 1
                self._length -= 1
                print(self)
            except AttributeError:
                print(f"Trying to pop from an empty list: {self.list_head=}")
                raise

    @property
    def length(self) -> int:
        """Get the list's length (e.g. number of elements).

        Returns
        -------
        int
            Number of elements.
        """
        return self._length

    def __repr__(self) -> str:
        return f"SinglyLinkedList{{list: {self.list_head}}}"

    def __str__(self) -> str:
        return f"SinglyLinkedList{{list: {self.list_head}}}"

# ceva = ListNode(val=10, next=None)
# print(ceva.val)

# test_list = SinglyLinkedList(val_list=[1,2,3,4])
# print(test_list)

# test_list.pop_left(nodes_to_pop=test_list.length)
# print(test_list.list_head)

# test_list.pop_left(nodes_to_pop=1)
# print(test_list.list_head)
