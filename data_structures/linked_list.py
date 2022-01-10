"""
This will probably be the last time I use doctest.

PROS:
    easy to write
    visually helpful for examples

CONS:
    Error statements are kinda hard to read
    It can become verbose
    Updating tests started to become cumbersome even within this file alone. I imagine it would be unmaintainable for larger code bases

When is it useful:
    I will use this when writing single algorithms. I.E. in a coding interview

Overall thoughts for the exercise:
    I enjoyed this project. I didn't really understand what a linked list was before I started on it and now I realize it's kinda useless to me.
    This helped strengthen my understanding of Big O Notation.
"""
from dataclasses import dataclass
from typing import Iterator, Optional


@dataclass
class Node:
    data: int
    next_element: Optional["Node"] = None

    def append(self, data: int) -> "Node":
        if self.next_element is None:
            self.next_element = Node(data)
            self.next_element
        else:
            return self.next_element.append(data)

    def __str__(self):
        return str(self.data)


class LinkedList:
    """
    My implementation of a LinkedList

    Speeds: n == length of LinkedList
    Append  -> O(n)
    Prepend -> O(1)
    Remove  -> O(n)
    Insert  -> O(n)
    LPop    -> O(1)

    A LinkedList would be useful if I wanted to perform Last In First Out operation on a series of elements. So, it is a slightly more robust s
    Example: Placing and removing pieces of paper from a stack

    Other than that, I'm not sure what benefits a linked list has.
    """

    head: Optional[Node]

    def __init__(self, data: int = None):
        self.head = None if data is None else Node(data)

    def prepend(self, data: int) -> Node:
        """
        Insert a new Node at the front the LinkedList

        >>> l = LinkedList(1)
        >>> l.prepend(5)
        Node(data=5, next_element=Node(data=1, next_element=None))
        >>> print(l)
        [5, 1]
        """
        self.head = Node(data, self.head)
        return self.head

    def append(self, data: int):
        """
        Append a new node with the provided data to the tail of the LinkedList

        >>> l = LinkedList()
        >>> l.append(1)
        >>> print(l)
        [1]
        """
        if self.head is None:
            self.head = Node(data)
        else:
            self.head.append(data)

    def insert(self, after_value: int, data: int) -> bool:
        """
        Insert a new node after the provided value

        >>> l = LinkedList(1)
        >>> l.append(3)
        >>> l.insert(1, 2)
        True
        >>> print(l)
        [1, 2, 3]
        """
        for node in self:
            if node.data == after_value:
                node.next_element = Node(data, node.next_element)
                return True
        return False

    def remove(self, data: int) -> bool:
        """
        Remove the node containing the provided data

        >>> l = LinkedList(1)
        >>> l.append(2)
        >>> l.append(3)
        >>> print(l)
        [1, 2, 3]
        >>> l.remove(1)
        True
        >>> l.remove(10)
        False
        >>> print(l)
        [2, 3]
        """
        if self.head.data == data:
            self.head = self.head.next_element
            return True

        for node in self:
            if node.next_element is None:
                return False  # Break case

            if node.next_element.data == data:
                node.next_element = node.next_element.next_element
                return True

    def lpop(self) -> Node:
        """
        Remove the head

        >>> l = LinkedList(1)
        >>> l.append(2)
        >>> l.append(3)
        >>> l.lpop()
        Node(data=1, next_element=Node(data=2, next_element=Node(data=3, next_element=None)))
        >>> print(l)
        [2, 3]
        """
        _head = self.head
        self.head = _head.next_element
        return _head

    def __iter__(self):
        """
        >>> l = LinkedList(1)
        >>> l.append(2)
        >>> l.append(3)
        >>> l.append(4)
        >>> for node in l:
        ...    print(node.data)
        1
        2
        3
        4
        """
        node = self.head
        while node is not None:
            yield node
            node = node.next_element

    def __str__(self):
        """
        >>> l = LinkedList(1)
        >>> l.append(2)
        >>> _ = l.prepend(3)
        >>> _ = l.prepend(4)
        >>> l.append(5)
        >>> print(l)
        [4, 3, 1, 2, 5]
        """
        return f"{[el.data for el in self]}"


if __name__ == "__main__":
    import doctest

    doctest.testmod()
