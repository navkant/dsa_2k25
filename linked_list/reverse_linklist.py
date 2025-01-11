class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Solution:
    def __init__(self):
        self.head = None

    def print_linklist(self, node: Node):
        while node:
            print(node.data, end=' ')
            node = node.next

    def reverse_linklist(self, node: Node):
        if node.next is None:
            self.head = node
            return node

        prev_node = self.reverse_linklist(node.next)
        prev_node.next = node
        return node

    def solution(self, head: Node):
        tail = self.reverse_linklist(head)
        tail.next = None


if __name__ == "__main__":
    n4 = Node(data=4)
    n3 = Node(data=3, next=n4)
    n2 = Node(data=2, next=n3)
    n1 = Node(data=1, next=n2)
    obj = Solution()
    obj.solution(n1)
    obj.print_linklist(obj.head)

