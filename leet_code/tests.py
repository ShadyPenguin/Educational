import doctest
import logging
from . import (
    longest_palindrome,
    longest_substring_without_repeating_characters,
    max_area,
    palindrome,
    three_sum,
    two_sum,
    roman_numerals,
    longest_common_prefix,
)


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(longest_palindrome))
    tests.addTests(doctest.DocTestSuite(longest_substring_without_repeating_characters))
    tests.addTests(doctest.DocTestSuite(max_area))
    tests.addTests(doctest.DocTestSuite(palindrome))
    tests.addTests(doctest.DocTestSuite(three_sum))
    tests.addTests(doctest.DocTestSuite(two_sum))
    tests.addTests(doctest.DocTestSuite(roman_numerals))
    tests.addTests(doctest.DocTestSuite(longest_common_prefix))
    return tests
