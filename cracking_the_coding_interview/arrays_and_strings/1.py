"""
Chapter 1

Solve the following problems using python.
Denote the speed and size in O() notation.
"""


def problem_1_1(s: str, use_dict: bool = False, use_deque: bool = False) -> bool:
    """
    Q: Implement an algorithm to determine if a string has all unique characters.
    What if you cannot use additional data structures?

    A: If I were to implement a solution efficiently I would utilize a dict to structure my data.
    >>> problem_1_1("abcdefg", use_dict=True)
    True
    >>> problem_1_1("abcdd", use_dict=True)
    False

    A: If we can't use additional data structures then I would probably start iterating destructively through the string and perform a lookup for each popped character
    >>> problem_1_1("abcdefga")
    False
    >>> problem_1_1("aa")
    False
    >>> problem_1_1("abcdefg")
    True

    A: Using deque
    >>> problem_1_1("abcdefga", use_deque=True)
    False
    >>> problem_1_1("aa", use_deque=True)
    False
    >>> problem_1_1("abcdefg", use_deque=True)
    True
    """

    def using_dict(s: str) -> bool:
        """
        Worst-case scenario is the duplicate element is the last character. This would result in N time
        Best-case scenario would be the first two elements being the same. This would result in 2 time, so this algorithm would be an average savings of 50%.
        Speed: O(n)
        Size: n where n is the length of s

        Can we improve this by sorting the string?
            What is the speed of a sort and how does it compare to creating and storing a dict?
        """
        seen = {}
        for char in s:
            if char in seen:
                return False
            seen[char] = 1
        return True

    if use_dict:
        return using_dict(s)

    def using_deque(s: str) -> bool:
        """
        a deque is specifically designed to perform fast appends and pops at the speed of O(1)
        This means worst case scenario lookupwould be O(1+1+1...) which reduces to O(n)
        """
        from collections import deque

        # should I sort this first?
        d = deque(sorted(list(s)))
        while d:
            c = d.popleft()
            if d and d[0] == c:
                return False
        return True

    if use_deque:
        return using_deque(s)

    # Default: don't use another data structure, just slice the string each iteration
    for idx, char in enumerate(s):
        remaining = s[
            idx + 1 :
        ]  # Constructs a new string each iteration. This could be more efficient by utilizing a data structure that isn't immutable
        if char in remaining:
            return False
    return True


def problem_1_3(left: str, right: str) -> bool:
    """
    Given two strings, write a method to decide if one is a permutation of the other.

    So, I could iterate through a range of indicies and construct a single hashmap to store the counts of a character.
    We can add from one str and remove from the other. This would result in all values should equal = 0
    >>> problem_1_3("abc", "cba")
    True
    >>> problem_1_3("a", "b")
    False
    >>> problem_1_3("aabbcc", "ccbbaa")
    True

    The below solution using a defaultdict should return with speed of O(n)
    """
    if len(left) != len(right):
        return False

    from collections import defaultdict

    _d = defaultdict(int)

    for i in range(len(left)):
        _d[left[i]] += 1
        _d[right[i]] -= 1

    for v in _d.values():
        if v != 0:
            return False
    return True


def problem_1_4(s: str) -> str:
    """
    replace all spaces in a string with %20
    >>> problem_1_4("foo bar  ")
    'foo%20bar'
    >>> problem_1_4("a s")
    Traceback (most recent call last):
      ...
    ValueError: Size of provided string is incorrect
    """
    from collections import deque

    response = deque([])
    for char in s:
        if len(response) == len(s):
            return "".join(response)

        if char == " ":
            response.append("%")
            response.append("2")
            response.append("0")
        else:
            response.append(char)
    raise ValueError("Size of provided string is incorrect")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
