"""
Asteroid Collision

https://leetcode.com/problems/asteroid-collision/

We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.



Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.


Constraints:

2 <= asteroids.length <= 104
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0
"""
import collections
from collections import deque
from dataclasses import dataclass, field
from re import A, I
from typing import Deque, List, Optional, Tuple


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """Wrapper method to leverage deques and allow copy-paste compatability"""
        return list(asteroid_collision(deque(asteroids)))


def collide(left: int, right: int) -> Tuple[Optional[int]]:
    """Return the result of a collision

    Returns
        tuple of (negative, positive) remaining after collision
    """
    small, big = sorted((left, right))
    if abs(small) > big:
        return (small, None)
    if abs(small) < big:
        return (None, big)
    return (None, None)


def detect_collision(left: int, right: int) -> bool:
    # positive - negative
    if left > 0 and right < 0:
        return True
    # negative - positive
    if left < 0 and right > 0:
        return True
    return False


def asteroid_collision(asteroids: Deque[int]) -> Deque[int]:
    """
    Determine the eventual outcome of asteroids travelling through space

    Given:
        There are two directions: Negative and Positive
        There is one value: Size

    Returns:
        The eventual outcome wherein the smaller sized asteroids explode upon collision with larger asteroids.

    Theory:
        Approaching this problem from both ends with a double-ended queue will allow for speed O(1) pops on both ends.
        This is valuable because we can consider positive direction will go toward the right end and negative toward the left end.

    Runtime Result:
        best case: O(n)
        worst case: O(n*n)

        The best case scenario would be an array with all all negatives on the left of the positives
        132 ms	18.4 MB

    Thoughts:
        I didn't enjoy sovling this procedurally. I made two helper methods to help my brain, but I still got lost at times while developing this soultion.
        I now want to try solving this with the same algorithm but leveraging OOP.

    >>> s = Solution()
    >>> s.asteroidCollision([1,2,-1,-2])
    [1]
    >>> s.asteroidCollision([5, 10, -5])
    [5, 10]
    >>> s.asteroidCollision([8, -8])
    []
    >>> s.asteroidCollision([10, 2, -5])
    [10]
    """
    answer = []
    # Deque for the left side of asteroid comparison
    # This should only contain positive values
    remaining = deque()

    # Iterate through asteroids
    while asteroids:
        asteroid = asteroids.popleft()
        # asteroid is a positive direction asteroid
        if asteroid > 0:
            remaining.append(asteroid)
            asteroid = None  # short circuit

        # asteroid is negatively charged asteroid. Time to start comparing with remaining
        while asteroid:
            # compare with positive direction remaining
            if remaining:
                _remaining_element = remaining.pop()
                # If we detect a collision we need to evaluate the result
                if detect_collision(_remaining_element, asteroid):
                    _negative, _positive = collide(_remaining_element, asteroid)
                    # print(_negative, _positive)
                # If the remaining asteroid is negative it will need to be compared vs the remaining
                if _negative:
                    asteroid = _negative
                elif _positive:
                    # The positive astroid remains
                    remaining.append(_positive)
                    asteroid = None
                else:
                    asteroid = None
            else:
                # There are no remaining. Determine where to place asteroid.
                if asteroid < 0:
                    answer.append(asteroid)
                else:
                    remaining.append(asteroid)
                asteroid = None

    return answer + list(remaining)


@dataclass(order=True)
class Asteroid:
    size: int

    def __str__(self):
        """
        Ensure it prints pretty

        >>> a = Asteroid(5)
        >>> print(a)
        5
        """
        return f"{self.size}"

    def collide(self, other: "Asteroid") -> Optional["Asteroid"]:
        """
        Return the result of a collision

        >>> big, small = Asteroid(10), Asteroid(5)
        >>> big.collide(small)
        Asteroid(size=10)
        >>> small.collide(big)
        Asteroid(size=10)
        >>> left, right = Asteroid(5), Asteroid(5)
        >>> left.collide(right)
        """
        self_abs, other_abs = abs(self.size), abs(other.size)
        if self_abs > other_abs:
            return self
        if self_abs < other_abs:
            return other
        return None

    def get_direction(self) -> int:
        """
        Relay the direction of the astroid

        >>> a = Asteroid(-10)
        >>> a.get_direction()
        -1
        >>> a = Asteroid(10)
        >>> a.get_direction()
        1
        """
        return -1 if self.size < 0 else 1


@dataclass
class Space:
    """
    Solve the problem with objects

    >>> asteroids = [Asteroid(n) for n in deque([1,2,-1,-2])]
    >>> s = Space(asteroids)
    >>> s.proceed_to_heat_death()
    >>> print(s)
    [1]
    >>> asteroids = [Asteroid(n) for n in deque([5, 10, -5])]
    >>> s = Space(asteroids)
    >>> s.proceed_to_heat_death()
    >>> print(s)
    [5, 10]
    >>> asteroids = [Asteroid(n) for n in deque([8, -8])]
    >>> s = Space(asteroids)
    >>> s.proceed_to_heat_death()
    >>> print(s)
    []
    >>> asteroids = [Asteroid(n) for n in deque([10, 2, -5])]
    >>> s = Space(asteroids)
    >>> s.proceed_to_heat_death()
    >>> print(s)
    10
    """

    asteroids: Deque[Asteroid]
    ending: Deque[Asteroid] = None

    def __str__(self):
        return f"{[int(str(a)) for a in self.asteroids if a is not None]}"

    def proceed_to_heat_death(self):
        """This function will enact all actions that would occur throughout the entirety of time"""
        # Entropy will be true until all events have occurred
        remaining = None
        while self.asteroids:
            asteroid = self.asteroids.popleft()
            remaining = self.compare_with_asteroids(asteroid)
        self.ending.append(remaining)

    def compare_with_asteroids(self, asteroid: Asteroid):
        """Compare the provided asteroid with the remaining asteroids"""
        # Base Case
        if not self.asteroids:
            return

        compare = self.asteroids.popleft()

        if self.will_collide(asteroid, compare):
            remaining = asteroid.collide(compare)
            # An asteroid remained from the impact. Try and compare it to the remaining
            if remaining:
                return self.compare_with_asteroids(remaining)
        else:
            # No collisions occur with asteroids so now we need to determine if we can place it on the end array
            self.compare_with_ending(asteroid)

    def compare_with_ending(self, asteroid: Asteroid):
        """Compare the provided asteroid with the 'ending' asteroids"""
        # Base Case
        if not self.ending:
            self.ending.append(asteroid)
            return

        # Compare latest ending with asteroid
        compare = self.ending.pop()
        # If they will collide, recursively iterate through the ending to destroy all in the asteroid's path
        if self.will_collide(compare, asteroid):
            remaining = compare.collide(asteroid)
            # asteroid survived
            if remaining == asteroid:
                return self.compare_with_ending(remaining)
        # No collisions occur so place the asteroid on the end
        else:
            self.ending.append(asteroid)

    @classmethod
    def will_collide(cls, a1: Asteroid, a2: Asteroid):
        """
        Determine if two asteroids will eventually collide

        >>> s = Space([])
        >>> s.will_collide(Asteroid(5), Asteroid(-5))
        True
        >>> s.will_collide(Asteroid(5), Asteroid(5))
        False
        """
        return a1.get_direction() != a2.get_direction()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    asteroid_collision(deque([1, 2, 3, -1]))
