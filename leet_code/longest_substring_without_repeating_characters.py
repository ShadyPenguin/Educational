import collections
from dataclasses import dataclass
from typing import List


def longest_substring_using_nested_for_loop(s: str) -> int:
    """
    Given a string s, find the length of the longest substring without repeating characters.

    https://leetcode.com/problems/longest-substring-without-repeating-characters/
    3946 ms	14.2 MB
    >>> longest_substring_using_nested_for_loop("abcabcbb")
    3
    >>> longest_substring_using_nested_for_loop("bbbbb")
    1
    >>> longest_substring_using_nested_for_loop("pwwkew")
    3
    """
    total = 0
    for idx, _ in enumerate(s):
        vals: List[str] = []
        for c2 in s[idx:]:
            if c2 not in vals:
                vals += [c2]
                total = max((total, len(vals)))
            else:
                total = max((total, len(vals)))
                break
    return total


def longest_substring_using_lists(s: str) -> int:
    """
    find the longest substring without repeating characters

    644 ms	14.3 MB
    >>> longest_substring_using_lists("abac")
    3
    >>> longest_substring_using_lists("abcabcbb")
    3
    >>> longest_substring_using_lists("bbbbb")
    1
    >>> longest_substring_using_lists("pwwkew")
    3
    """
    words = list()
    longest = 0
    for char in s:
        # for each character
        removals = []

        for word_idx in range(len(words)):
            # check all found words for the char
            word = words[word_idx]
            if char in word:
                # if it exists then set its length to longest if it is the longest
                longest = max(longest, len(word))
                removals.append(word)
            else:
                # else add char to word
                words[word_idx] += char

        for remove in removals:
            words.remove(remove)

        # add char into words
        words.append(char)
    return max(longest, *[len(word) for word in words])


def longest_substring_deque_rotations(s: str) -> int:
    """
    find the longest substring without repeating characters

    512 ms	14.5 MB
    >>> longest_substring_deque_rotations("abac")
    3
    >>> longest_substring_deque_rotations("abcabcbb")
    3
    >>> longest_substring_deque_rotations("bbbbb")
    1
    >>> longest_substring_deque_rotations("pwwkew")
    3
    """
    words = collections.deque()
    longest = 0
    for char in s:
        for _ in range(len(words)):
            word = words.popleft()
            if char not in word:
                words.append(word + char)
            else:
                longest = max(longest, len(word))
        words.append(char)

    for word in words:
        longest = max(longest, len(word))

    return longest


if __name__ == "__main__":
    import doctest

    doctest.testmod()
