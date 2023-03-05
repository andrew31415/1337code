
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
        self.val = val
        # TODO: maybe raise if is not instance of same type
        # if not next and not isinstance(next, ListNode):
        #     raise TypeError(f"Element with {val=} doesn't have a valid next ")
        self.next = next

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

    def __init__(self, val_list=[]) -> None:
        """SinglyLinkedList constructor.

        Examples
        --------

        SinglyLinkedList(val_list=[1,2,3])

        Parameters
        ----------
        val_list : list | tuple | str, optional
            Sequence of objects to be stored in the list, by default []
        """
        
        self.list = None

        for val in val_list[::-1]:
            self.list = ListNode(val, self.list)

    def __repr__(self) -> str:
        return f"SinglyLinkedList{{list: {self.list}}}"

    def __str__(self) -> str:
        return f"SinglyLinkedList{{list: {self.list}}}"

# ceva = ListNode(val=10, next=None)
# print(ceva.val)

# test_list = SinglyLinkedList(val_list=[1,2,3,4])
# print(test_list.list)