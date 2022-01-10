import doctest
import logging

from . import docstring, linked_list, tree, tries


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(docstring))
    tests.addTests(doctest.DocTestSuite(linked_list))
    tests.addTests(doctest.DocTestSuite(tree))
    tests.addTests(doctest.DocTestSuite(tries))
    return tests
