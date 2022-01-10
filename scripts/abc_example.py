from abc import ABC, abstractmethod


class Interface(ABC):
    @abstractmethod
    def foo():
        """Does all the foo"""

class Bar(Interface):
    """Bar class"""
    def foo(self):
        return "I'm no foo!"

b = Bar()
print(b.foo())
