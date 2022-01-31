# Definition for singly-linked list.
from dataclasses import dataclass
from typing import Optional, List, Tuple

@dataclass
class ListNode:
    val: int
    next: Optional["ListNode"] = None

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = tail = ListNode()

        while True:
            # break cases
            if list1 is None and list2 is None:
                return head.next
            elif list1 is None:
                tail.next = list2
                return head.next
            elif list2 is None:
                tail.next = list1
                return head.next

            # handle list1
            if list1.val <= list2.val:
                tail.next = ListNode(list1.val)
                # move each list forward one
                list1 = list1.next
                tail = tail.next
            else:
                # handle list 2
                tail.next = ListNode(list2.val)
                list2 = list2.next
                tail = tail.next


