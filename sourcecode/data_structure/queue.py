class Node:
    data = None
    next = None

    def __init__(self, data=None):
        self.data = data


class Queue:
    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None

    def is_empty(self):
        return self.length == 0

    def push(self, node):
        if not isinstance(node, Node):
            node = Node(node)
        if not self.head:
            self.head = node
        if self.last:
            self.last.next = node
        self.last = node
        self.length += 1

    def pop(self):
        if self.length > 0:
            result = self.head
            self.head = self.head.next
            if self.length == 1:
                self.last = None
            self.length -= 1
            return result
        else:
            return None

    def print(self):
        cursor = self.head
        while cursor:
            print(cursor.data)
            cursor = cursor.next


q = Queue()

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

q.push(n1)
q.push(n2)
q.push(n3)

q.push(4)
q.push(5)
q.push(6)

q.print()

print(q.pop().data)
print(q.pop().data)

q.print()
