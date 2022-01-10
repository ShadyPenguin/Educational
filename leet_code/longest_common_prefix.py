"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
https://leetcode.com/problems/longest-common-prefix/submissions/

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.

Current implementation:
    n = length of strs. where 1 <= n <= 200
    m = length of smallest str. where 0 <= m <= 200
    x = length of all remaining possible prefixes. where 0 <= x <= len(m)
    Currently, I am using an algorithm of speed O(nx + m) which reduces down to O(n)
    There are many optimizations I could make to the current implementation, however I think it would be better to use a different data structure altogether.

Improved solution:
    If instead of creating a set of words and performing lookups at a speed of O(n), we could create a Trie.
    This would make the new algorithm perform at a speed of O(n + xlog(n)) which reduces down to O(log(n)).
"""

from typing import List, Set


def find_common_prefix(strs: List[str]) -> str:
    """
    Runtime: 40 ms	14.4 MB

    Runtime speed is calculated as O(n + mx)
    >>> strs = ["flower","flow","flight"]
    >>> find_common_prefix(strs)
    'fl'
    >>> strs = ["dog","racecar","car"]
    >>> find_common_prefix(strs)
    ''
    """
    shortest = min(strs, key=lambda x: len(x))
    possible: Set[str] = set()

    _word = ""
    # generate possible
    for letter in shortest:
        _word += letter
        possible.add(_word)

    # Iterate with short-circuit through all words in strs
    for word in strs:
        if not possible:
            return ""
        _word = word[0]

        missing = set()
        # Iterate through all possibilities and remove the ones missing from the word
        for p in possible:
            if p != word[:len(p)]:
                missing.add(p)
        possible -= missing

    if not possible:
        return ""

    return max(possible, key=lambda x: len(x))


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return find_common_prefix(strs)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
