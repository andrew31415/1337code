"""OOP implementation of Lists.
"""


class ListNode(object):
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
        self.next: ListNode = next

    def __repr__(self) -> str:
        return f"ListNode{{val: {self.val}, next: {self.next}}}"

    def __str__(self) -> str:
        return f"ListNode{{val: {self.val}, next: {self.next}}}"


class SinglyLinkedList(object):
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
        self.list_head: ListNode = ListNode()

        if not hasattr(val_list, "__getitem__"):
            # TODO: use logger
            print(f"Trying to create an SLL with a non indexable object {val_list=}")
            self.list_head = ListNode(val_list, None)
            self._length = 1
            return

        for val in val_list[::-1]:
            self.list_head = ListNode(val, self.list_head)
            self._length += 1

    def add_node(self, new_node_value: object) -> None:
        """Adds a new element at the end of the list.

        Parameters
        ----------
        new_list_node_value
            Contains a ListNode object.

        Returns
        -------
        None
        """
        list_end = self.list_head

        if list_end.val is None and self.length:
            list_end.val = new_node_value
            return

        while list_end.next:
            list_end = list_end.next

        list_end.next = ListNode(val=new_node_value, next=None)

        self._length += 1

    def add_nodes(self, new_nodes_values: object) -> None:
        """Add new nodes at the end of the list.

        Parameters
        ----------
        new_nodes_values : object
            Iterable object with values that will become `ListNode` object in
            the list. If it's not iterable then it will be added as a single
            node in the list.

        Returns
        -------
        None
        """
        list_end = self.list_head

        while list_end.next:
            list_end = list_end.next

        if hasattr(new_nodes_values, "__iter__"):
            iterator = iter(new_nodes_values)

            for item in iterator:
                list_end.next = ListNode(val=item, next=None)
                self._length += 1
                list_end = list_end.next

        else:
            print("Object is not iterable. Adding it as a single node instead.")
            self.add_node(new_node_value=new_nodes_values)

    def pop_left(self, nodes_to_pop: int) -> None:
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
            if nodes_to_pop > self.length or self.list_head is None:
                raise AttributeError(f"Trying to pop from an empty list: {self.list_head=}")

            self.list_head = self.list_head.next
            nodes_to_pop -= 1
            self._length -= 1

    @property
    def length(self) -> int:
        """Get the list's length (e.g. number of elements).

        Returns
        -------
        int
            Number of elements.
        """
        return self._length

    @length.setter
    def length(self, length: int) -> None:
        """Set's the list's length (e.g. number of elements).

        Parameters
        ----------
        length : int
            Number of linked elements in the linked list.
        """
        self._length = length

    def update_length(self):
        """Iterate over the list and adjust its length property value.
        """
        # TODO: implement this (iteration + length.setter)
        return

    def __repr__(self) -> str:
        return f"SinglyLinkedList{{list_head: {self.list_head}}}"

    def __str__(self) -> str:
        return f"SinglyLinkedList{{list_head: {self.list_head}}}"

# ceva = ListNode(val=10, next=None)
# print(ceva.val)

# test_list = SinglyLinkedList()
# print(test_list)

# test_list.add_node("new_element")
# # test_list.add_nodes(new_nodes_values=[1, 2, 3])
# print(test_list)
# test_list.add_node("new_element")
# print(test_list)

# test_list.add_nodes(new_nodes_values=[4, 5, 6])
# print(test_list)
# test_list.pop_left(nodes_to_pop=test_list.length)
# print(test_list.list_head)

# test_list.pop_left(nodes_to_pop=1)
# print(test_list.list_head)
