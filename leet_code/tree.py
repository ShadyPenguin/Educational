from dataclasses import dataclass


@dataclass
class Node:
    val: int = 0
    next: "Node" = None

    def __next__(self):
        return self.next

head = tail = Node()
for i in range(5):
    tail.next = Node(i)
    tail = tail.next


