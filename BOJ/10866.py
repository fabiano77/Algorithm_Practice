class Node:
    def __init__(self):
        self.data = None
        self.prev = None
        self.next = None

class deque:
    def __init__(self):
        self.cnt = 0
        self.head = Node()
        self.tail = Node()

    def size(self):
        return self.cnt
    def empty(self):
        return 1 if self.cnt == 0 else 0
    def push_front(self, item):
        new_node = Node()
        new_node.data = item
        new_node.next = self.head
        self.head.prev = new_node

        self.head = new_node

        if self.empty():
            self.tail = new_node
        self.cnt += 1

    def push_back(self, item):
        new_node = Node()
        new_node.data = item
        new_node.prev = self.tail
        self.tail.next = new_node

        self.tail = new_node

        if self.empty():
            self.head = new_node
        self.cnt += 1

    def pop_front(self):
        if self.empty():
            return -1
        self.cnt -= 1
        del_node = self.head
        ret_item = del_node.data
        self.head = del_node.next
        del del_node
        if self.empty():
            self.head = Node()
            self.tail = Node()
        return ret_item

    def pop_back(self):
        if self.empty():
            return -1
        self.cnt -= 1
        del_node = self.tail
        ret_item = del_node.data
        self.tail = del_node.prev
        del del_node
        if self.empty():
            self.head = Node()
            self.tail = Node()
        return ret_item

    def front(self):
        if self.empty():
            return -1
        return self.head.data

    def back(self):
        if self.empty():
            return -1
        return self.tail.data

import sys
input = lambda: sys.stdin.readline().rstrip()

deq = deque()

for _ in range(int(input())):
    cmd = input()
    if cmd == 'size':
        print(deq.size())
    elif cmd == 'empty':
        print(deq.empty())
    elif cmd == 'front':
        print(deq.front())
    elif cmd == 'back':
        print(deq.back())
    elif cmd == 'pop_front':
        print(deq.pop_front())
    elif cmd == 'pop_back':
        print(deq.pop_back())
    elif cmd[:10] == 'push_front':
        deq.push_front(int(cmd[11:]))
    elif cmd[:9] == 'push_back':
        deq.push_back(int(cmd[10:]))
    