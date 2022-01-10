import doctest
import logging

from . import binary_search, fib


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(binary_search))
    tests.addTests(doctest.DocTestSuite(fib))
    return tests
