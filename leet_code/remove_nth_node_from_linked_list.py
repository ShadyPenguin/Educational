"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given the head of a linked list, remove the nth node from the end of the list and return its head.



Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]


Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz


Follow up: Could you do this in one pass?

"""
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class ListNode:
    val: int = 0
    next: Optional["ListNode"] = None

    def append(self, node):
        if self.next is not None:
            self.insert(node)
            return
        self.next = node

    def insert(self, node):
        next_node = self.next
        self.next, node.next = node, next_node

    def remove(self):
        self.next = self.next.next

    @classmethod
    def from_list(cls, l: List[int]) -> "ListNode":
        head = tail = ListNode()
        for num in l:
            tail.next = ListNode(num)
            tail = tail.next
        return head

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        output = []
        while head is not None:
            output.append(head.val)
            head = head.next
        output.pop(-n)
        response = tail = ListNode()
        for el in output:
            tail.next = ListNode(el)
            tail = tail.next
        return response.next


def main():
    s = Solution()
    head = ListNode.from_list([1,2,3,4,5])
    expected = ListNode.from_list([1,2,3,5])
    assert s.removeNthFromEnd(head, 2) == expected


    head = ListNode.from_list([1])
    expected = ListNode.from_list([])
    assert s.removeNthFromEnd(head, 1) == expected

    head = ListNode.from_list([1,2])
    expected = ListNode.from_list([1])
    assert s.removeNthFromEnd(head, 1) == expected

if __name__ == "__main__":
    main()
