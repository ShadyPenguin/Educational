import doctest
import logging
from . import (
    longest_palindrome,
    longest_substring,
    max_area,
    palindrome,
    three_sum,
    two_sums,
    roman_numerals,
    longest_common_prefix,
)


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(longest_palindrome))
    tests.addTests(doctest.DocTestSuite(longest_substring))
    tests.addTests(doctest.DocTestSuite(max_area))
    tests.addTests(doctest.DocTestSuite(palindrome))
    tests.addTests(doctest.DocTestSuite(three_sum))
    tests.addTests(doctest.DocTestSuite(two_sums))
    tests.addTests(doctest.DocTestSuite(roman_numerals))
    tests.addTests(doctest.DocTestSuite(longest_common_prefix))
    return tests
