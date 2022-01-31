"""
https://leetcode.com/problems/add-two-numbers/submissions/
"""
import logging
from dataclasses import dataclass
from typing import Optional

logging.basicConfig(level=logging.DEBUG)

@dataclass
class ListNode:
    val: int = 0
    next: Optional["ListNode"] = None

class Solution:
    head = tail = ListNode()

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Runtime O(n)
        212 ms	15.5 MB
        """
        remainder = 0
        while l1 is not None or l2 is not None:
            if l1 is None:
                remainder = self._add_to_tail(l2.val, remainder)
                l2 = l2.next
            elif l2 is None:
                remainder = self._add_to_tail(l1.val, remainder)
                l1 = l1.next
            else:
                logging.debug("else block")
                remainder = self._add_to_tail(l1.val, l2.val, remainder)
                l1, l2 = l1.next, l2.next

        if remainder:
            self.tail.next = ListNode(remainder)

        return self.head.next


    def _add_to_tail(self, *values):
        total = sum(values)
        logging.debug(f"Adding {total} to {self.tail=}")
        remainder, singles = divmod(total, 10)
        self.tail.next = ListNode(singles)
        self.tail = self.tail.next
        logging.debug(f"{remainder=}")
        return remainder

def main():
    s = Solution()
    l1 = l1t = ListNode()
    l2 = l2t = ListNode()

    l_input = [9,9,1]
    for i in l_input:
        l1t.next = ListNode(i)
        l1t = l1t.next

    r_input = [1]
    for i in r_input:
        l2t.next = ListNode(i)
        l2t = l2t.next

    answer = s.addTwoNumbers(l1.next, l2.next)
    while answer is not None:
        logging.info(answer.val)
        answer = answer.next

if __name__ == "__main__":
    main()
