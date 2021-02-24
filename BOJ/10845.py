import sys
input = lambda: sys.stdin.readline().rstrip()
class Node:
    def __init__(self):
        self.data = None
        self.next = None

class Queue:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.cnt = 0

    def size(self):
        return self.cnt

    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0

    def push(self, item):
        new_node = Node()
        new_node.data = item
        self.tail.next = new_node
        self.tail = new_node

        if self.empty() == 1:
            self.head = new_node

        self.cnt += 1

    def pop(self):
        if self.empty():
            return -1
        self.cnt -= 1
        item = self.head.data
        self.head = self.head.next
        return item

    def front(self):
        if self.empty():
            return -1
        return self.head.data
    def back(self):
        if self.empty():
            return -1
        return self.tail.data

q = Queue()

for _ in range(int(input())):
    cmd = input()
    if cmd == 'pop':
        print(q.pop())
    elif cmd == 'size':
        print(q.size())
    elif cmd == 'empty':
        print(q.empty())
    elif cmd == 'front':
        print(q.front())
    elif cmd == 'back':
        print(q.back())
    elif cmd[:4] == 'push':
        q.push(int(cmd[4:]))
    