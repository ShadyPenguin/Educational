"""
module level docstring

this should talk about the module
"""

from dataclasses import dataclass


@dataclass
class Example:
    """Class level description

    more stuff can go here
    """

    def __init__(self, foo: int) -> None:
        """considered public method so it needs docstring"""
        self.foo = foo

    def do_something(self):
        """
        The docstring for a function or method should summarize its behavior and document its arguments,
        return value(s), side effects, exceptions raised, and restrictions on when it can be called (all if applicable). Optional arguments should be indicated.
        It should be documented whether keyword arguments are part of the interface.
        """
        print("something")

    def _private_method(self):
        print("dont look")
