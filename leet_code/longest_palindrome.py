def longest_palindrome(s: str) -> str:
    """
    Find the longest substring palindrome inside given string

    https://leetcode.com/problems/longest-palindromic-substring/submissions/
    TODO: This answer is too slow. You must improve algorithm speed

    >>> longest_palindrome("abab")
    'aba'
    >>> longest_palindrome("babad")
    'bab'
    >>> longest_palindrome("cbbd")
    'bb'
    """
    if len(s) == 1:
        return s

    longest = ""
    for idx, _ in enumerate(s):
        if len(s) - idx < len(longest):
            return longest

        for end in reversed(
            range(idx + 1, len(s) + 1)
        ):  # O(n*n). Look for more efficient algorithm. perhaps use a data structure
            val = s[idx:end]
            if is_palindrome(val) and len(longest) < len(val):
                longest = val
    return longest


def is_palindrome(s: str):
    """
    Examine string from both ends and move towards the center
    Success Break case:
        when only 1 char left
        when 0 chars left
    Fail break case:
        when ends don't match

    >>> is_palindrome("aba")
    True
    >>> is_palindrome("bb")
    True
    >>> is_palindrome("cat")
    False
    """
    solved = {}
    if s in solved:
        return True

    for idx, c in enumerate(s):
        # idx goes from left to right
        # end goes from right to left.
        end_idx = len(s) - idx - 1
        if idx >= end_idx:
            solved[s] = 1
            return True

        end = s[end_idx]
        if c != end:
            return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
