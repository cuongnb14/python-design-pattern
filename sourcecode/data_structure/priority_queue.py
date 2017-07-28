class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # for python2 use __cmp__
    def __lt__(self, other):
        return self.score < other.score

    def __str__(self):
        return "{}: {}".format(self.name, self.score)


class PriorityQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        pop_index = 0
        for i in range(1, len(self.items)):
            if self.items[i] > self.items[pop_index]:
                pop_index = i

        item = self.items[pop_index]
        del self.items[pop_index]
        return item

    def print(self):
        for i in range(0, len(self.items)):
            print(self.items[i])


pq = PriorityQueue()
pq.push(12)
pq.push(11)
pq.push(12)
pq.push(120)

print(pq.pop())
print(pq.pop())

pq.print()

pq2 = PriorityQueue()
pq2.push(Student("Cuong", 10))
pq2.push(Student("Tuan", 8))
pq2.push(Student("Huy", 9))
pq2.push(Student("Manh", 9))

print(pq2.pop())
print(pq2.pop())
print(pq2.pop())
print(pq2.pop())
