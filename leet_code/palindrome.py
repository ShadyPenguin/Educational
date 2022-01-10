class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Determine if the integer is a palindrome

        >>> s = Solution()
        >>> s.isPalindrome(121)
        True
        >>> s.isPalindrome(-121)
        False
        >>> s.isPalindrome(10)
        False
        >>> s.isPalindrome(11)
        True
        >>> s.isPalindrome(1221)
        True

        Thoughts:
            Integer isn't the best data structure to determine if it is a palindrome.
            I need something with O(1) lookup. I also only want to make one conversion, so let's do a string
            We can also do this recursively

            given the test 121
            first convert to "121"
            for
        """
        return self.is_palindrome(str(x))

    def is_palindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        if s[0] == s[-1]:
            return self.is_palindrome(s[1:-1])
        return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
