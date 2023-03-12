"""OOP implementation of Lists.
"""

import logging

import utils.leet_logger


class ListNode(object):
    """An object containing a value and an identifier to another object of the
    same ListNode type.
    """

    def __init__(self, val=None, next=None, log_active=False) -> None:
        """ListNode constructor.

        Parameters
        ----------
        val : any, optional
            Object stored in node, by default None
        next : ListNode, optional
            Identifier to another ListNode like element, by default None
        log_active : bool, optional
            Activate or deactivate the console logging, by default False
        """
        self.node_logger = logging.getLogger(f"{utils.leet_logger.LOGGER_MAIN_NAME}.NodeLogger")
        self.activate_logger(log_active=log_active)

        self.val: object = val

        # TODO: maybe raise if is not instance of same type
        # if next is not None and not isinstance(next, ListNode):
        #     raise TypeError(f"Element with {val=} doesn't have a valid next ")
        self.next: ListNode = next
        self.node_logger.info(f'Created new ListNode: {self}')

    def __repr__(self) -> str:
        return f"ListNode{{val: {self.val}, next: {self.next}}}"

    def __str__(self) -> str:
        return f"ListNode{{val: {self.val}, next: {self.next}}}"

    def activate_logger(self, log_active=False):
        self.node_logger.disabled = not log_active


class SinglyLinkedList(object):
    """Contains a singly linked list of ListNode type elements.

    Notes
    -----

    element_1: [value, element_2_identifier]
    element_2: [value, element_3_identifier]
    element_3: [value, element_4_identifier]
    element_4: [value, None]
    """
    ############################################################################
    # Magic
    ############################################################################
    def __init__(self, val_list=None, log_active=False) -> None:
        """SinglyLinkedList constructor.

        Examples
        --------

        SinglyLinkedList(val_list=[1,2,3])

        Parameters
        ----------
        val_list : list | tuple | str, optional
            Sequence of objects to be stored in the list, by default []
        log_active : bool, optional
            Activate or deactivate the console logging, by default False
        """
        self.list_logger = logging.getLogger(f"{utils.leet_logger.LOGGER_MAIN_NAME}.ListLogger")
        self.activate_logger(log_active=log_active)

        self._length: int = 0
        self.list_head: ListNode = ListNode()

        if val_list is None:
            self.list_logger.info("Creating an empty SLL.")
            self._length = 0
        elif not hasattr(val_list, "__getitem__"):
            self.list_logger.info(f"Creating an SLL with a non indexable object {val_list=}")
            self.list_head = ListNode(val_list, None)
            self._length = 1
        else:
            for val in val_list[::-1]:
                self.list_head = ListNode(val, self.list_head)
                self._length += 1

    def __iter__(self) -> object:
        return SinglyLinkedListIterator(self.list_head)

    def __repr__(self) -> str:
        return f"SinglyLinkedList{{list_head: {self.list_head}}}" if self.length else "SinglyLinkedList: Empty List"

    def __str__(self) -> str:
        return f"SinglyLinkedList{{list_head: {self.list_head}}}" if self.length else "SinglyLinkedList: Empty List"

    ############################################################################
    # Properties
    ############################################################################
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
        self.update_length()
        # TODO: if length != self.length: warning: trying to set a different real length of list
        self._length = length
        if self._length < 0:
            raise ValueError("List length cannot be negative.")

    ############################################################################
    # Class Methods
    ############################################################################
    def activate_logger(self, log_active=False):
        """Activate or deactivate the console logging.

        Parameters
        ----------
        log_active : bool, optional
            Activation flag, by default False

        Returns
        -------
        None
        """
        self.list_logger.disabled = not log_active

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

        if list_end.val is None and self.length == 0:
            self.list_logger.info(f"Updating empty list with value: {new_node_value}")
            list_end.val = new_node_value
            self.list_logger.info(f"Printing list:\n{self}")
        else:
            while list_end.next:
                list_end = list_end.next

            self.list_logger.info(f"Adding a new ListNode with value: {new_node_value}")
            list_end.next = ListNode(val=new_node_value, next=None)
            self.list_logger.info(f"Printing list:\n{self}")

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
                self.list_logger.info(f"Adding a new ListNode with value: {item}")
                list_end.next = ListNode(val=item, next=None)
                self._length += 1
                list_end = list_end.next
        else:
            self.list_logger.info(f"Adding a new ListNode with the non-iterable value = {new_nodes_values}")
            self.add_node(new_node_value=new_nodes_values)

        self.list_logger.info(f"Printing list:\n{self}")

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
        self.list_logger.info(f"Popping last {nodes_to_pop} from list. Current number of nodes = {self.length}")

        while nodes_to_pop:
            if nodes_to_pop > self.length or self.list_head is None:
                raise AttributeError(f"Trying to pop from an empty list: {self.list_head=}")

            self.list_head = self.list_head.next
            nodes_to_pop -= 1
            self._length -= 1
        self.list_logger.info(f"Printing list:\n{self}")

    def update_length(self):
        """Iterate over the list and adjust its length property value.
        """
        # TODO: implement this (iteration + length.setter)


class SinglyLinkedListIterator(object):
    """Iterator class for the SinglyLinkedList class.
    """
    def __init__(self, list_head):
        self.current = list_head

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        item = self.current.val
        self.current = self.current.next
        return item


test_list = SinglyLinkedList(log_active=False)
# print(test_list)

test_list.add_node("new_element")
# test_list.add_nodes(new_nodes_values=[1, 2, 3])
# print(test_list)

# test_list.add_nodes(new_nodes_values=[4, 5, 6])
