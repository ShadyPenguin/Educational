import heapq
from dataclasses import dataclass
from typing import List, Optional


@dataclass()
class ListNode:
    val: int
    next: "ListNode"

def insert(node: ListNode, val: int):
    new_node = ListNode(val, node.next)
    node.next = new_node

def search(node: ListNode, val: int):
    while node.next is not None:
        if node.next.val > val:
            break
        node = node.next
    return node


def merge_sort(lists: List[Optional[ListNode]]):
    output = ListNode()

    for node in lists:
        while node is not None:
            insert(search(output, node.val), node.val)
            node = node.next

    return output.next

def heap_sort(lists: List[Optional[ListNode]]):
    items = []
    for node in lists:
        while node is not None:
            items.append(node.val)
            node = node.next

    head = tail = ListNode()

    heap = heapq.heapify(items) # O(n)

    for _ in range(len(items)):
        tail.next = ListNode(heapq.heappop(heap))
        tail = tail.next

    return head.next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        This is using the search and insert methods

        Runtime
        3084 ms	18.4 MB
        """
        return heap_sort(lists)
