class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None

    def add_head(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.length += 1

    def print(self):
        cursor = self.head
        while cursor:
            print(cursor.data, end=" ")
            cursor = cursor.next

    def _print_backward(self, head):
        if not head:
            return
        else:
            self._print_backward(head.next)
            print(head.data, end=", ")

    def print_backward(self):
        self._print_backward(self.head)

    def pretty_backward(self):
        print("[", end="")
        self._print_backward(self.head)
        print("]", end="")

    def __str__(self):
        return "LinkedList: {} node".format(self.length)


ll = LinkedList()
ll.add_head(1)
ll.add_head(2)
ll.add_head(3)

ll.print_backward()
ll.pretty_backward()
