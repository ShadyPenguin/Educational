"""
My implementation of a trie

What do I think about a trie and how would I use this data structure?

Search:
    The speed will be O(1) (constant) for each letter in the key.
    The key is n letters long.

    The speed reduces to O(log(n))

Insert:
    The traversal speed will be the same as Search: O(M * log(n))

    Given 'm' keys of length 'n': O(m * log(n))

Size:
    The size of a Trie will be:

        TrieNodes
            TrieNode: (linear scaling)
                Children: size(26-length list) - Fixed size
                is_end_of_word: bool - Fixed size

        Trie:
            Given 'n' nodes in the Trie
            n * size(TrieNodes): linear scaling

Useful examples:
    I don't know yet, I will keep this structure in my mind while solving alrorithmic problems.

What a Trie looks like:
        *
      /    \
    a       c
   / \       \
  e   f       l
  |   | \    / \
  m   o  n  c   a
  |
  s
"""

from dataclasses import dataclass
from string import ascii_lowercase
from typing import List, Optional


@dataclass
class TrieNode:
    def __init__(self) -> None:
        self.children: List[Optional["TrieNode"]] = [None] * 26
        self.is_end_of_word: bool = False

    def __eq__(self, other: "TrieNode") -> bool:
        """Internal values aren't enough to differentiate between class instances."""
        return self is other


class Trie:
    def __init__(self) -> None:
        """
        Create a Trie

        >>> t = Trie()
        >>> t.insert("cat")
        >>> n = t.search("ca")
        >>> n.is_end_of_word
        False
        >>> n = t.search("cat")
        >>> n.is_end_of_word
        True
        >>> t.search("cabbie")
        Traceback (most recent call last):
        ...
        ValueError: Word not found
        """
        self.root = TrieNode()

    def index(self, char: str) -> int:
        """
        Return the index value of a 0-25 based index of lower case alphabet

        >>> t = Trie()
        >>> t.index("a"), t.index("z")
        (0, 25)
        """
        return ascii_lowercase.index(char)

    def char(self, index: int) -> str:
        """
        Return the character of a 0-25 based index of lower case alphabet

        >>> t = Trie()
        >>> t.char(0), t.char(25)
        ('a', 'z')
        """
        return ascii_lowercase[index]

    def insert(self, key: str):
        """
        Add the key into the root node
        """
        _node = self.root
        for char in key:
            child_index = self.index(char)
            child = _node.children[child_index]
            if child is None:
                child = TrieNode()
                _node.children[child_index] = child
            _node = child
        _node.is_end_of_word = True

    def search(self, key: str) -> TrieNode:
        """
        Traverse the TrieNode and find the node for the provided key
        """
        _node = self.root
        for char in key:
            child_index = self.index(char)
            child = _node.children[child_index]
            if child is None:
                raise ValueError("Word not found")
            _node = child
        return _node


if __name__ == "__main__":
    import doctest

    doctest.testmod()
