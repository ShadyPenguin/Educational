from dataclasses import dataclass
from enum import Enum, auto
from typing import Callable, Generator, Optional


@dataclass
class Node:
    value: int
    left: "Node" = None
    right: "Node" = None

    def append(self, value: int):
        """
        >>> n = Node(5)
        >>> n.append(4)
        >>> n.append(6)
        >>> n
        Node(value=5, left=Node(value=4, left=None, right=None), right=Node(value=6, left=None, right=None))
        """
        if value <= self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.append(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.append(value)

    def contains(self, value: int) -> bool:
        """
        Given The tree
          (5)
          / \
        (4) (6)

        >>> n = Node(5)
        >>> n.append(4)
        >>> n.append(6)
        >>> n.contains(6)
        True
        >>> n.contains(4)
        True
        >>> n.contains(5)
        True
        >>> n.contains(10)
        False
        """
        if self.value == value:
            return True

        if self.value > value:
            return False if self.left is None else self.left.contains(value)
        else:
            return False if self.right is None else self.right.contains(value)

    def in_order(self) -> Generator["Node", None, None]:
        """
        Return a generator which will traverse the tree in-order

        TODO
        # >>> n = Node(5)
        # >>> n.append(4)
        # >>> n.append(6)
        # >>> n.append(7)
        # >>> gen = n.in_order()
        # >>> [str(_n) for _n in gen]
        # ['4', '5', '6', '7']
        """
        # print left
        if isinstance(self.left, Generator):
            for el in self.left:
                yield el
        elif self.left is not None:
            yield self.left

        # always print middle
        yield self

        # print right
        if isinstance(self.right, Generator):
            for el in self.right:
                yield el
        elif self.right is not None:
            yield self.right

    def pre_order(self) -> Generator["Node", None, None]:
        """
        TODO
                (5)
            (4)     (6)
        (3)             (7)
        # >>> n = Node(5)
        # >>> n.append(4)
        # >>> n.append(6)
        # >>> n.append(7)
        # >>> n.append(3)
        # >>> [str(_n) for _n in n.pre_order()]
        # '53467'
        """
        yield self
        if self.left is not None:
            yield self.left
        if self.right is not None:
            yield self.right

    def post_order(self) -> Generator["Node", None, None]:
        pass

    def __str__(self) -> str:
        """
        >>> n = Node(1)
        >>> print(n)
        1
        """
        return str(self.value)


@dataclass
class BinarySearchTree:
    """
    My Implementation of a binary search tree
    """

    root: Node = None

    class TraversalType(Enum):
        IN_ORDER = auto()
        PRE_ORDER = auto()
        POST_ORDER = auto()

        def traverse(self, node: Node) -> Generator[Node, None, None]:
            if self == self.__class__.IN_ORDER:
                return node.in_order()
            elif self == self.__class__.PRE_ORDER:
                return node.pre_order()
            elif self == self.__class__.POST_ORDER:
                return node.post_order()

    def contains(self, value: int) -> bool:
        pass

    def remove(self, value: int) -> Optional[Node]:
        pass

    def balance(self):
        pass

    def traverse(
        self, order: TraversalType = TraversalType.IN_ORDER, action: Callable = str
    ):
        """
        TODO
        """
        if self.root is not None:
            for node in order.traverse(self.root):

                print(action(node))

    def append(self, value: int) -> Node:
        if self.root is None:
            self.root = Node(value)
            return self.root

        return self.root.append(value)

    def __str__(self) -> str:
        pass

    @classmethod
    def create_example(cls):
        """
        Create the base balanced tree for testing
        """
        t = cls()
        t.append(100)
        t.append(50)
        t.append(150)
        t.append(25)
        t.append(75)
        t.append(125)
        t.append(175)
        t.append(20)
        t.append(30)
        t.append(70)
        t.append(80)
        t.append(120)
        t.append(130)
        t.append(170)
        t.append(180)
        return t


if __name__ == "__main__":
    import doctest

    doctest.testmod()
