import sys
n = int(input())

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None

class queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def empty(self):
        return not self.head

    def push(self, value):
        self.len += 1
        new_node = Node(value)
        if self.empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
        #tail 삽입
        self.tail = new_node

    def pop(self):
        if self.empty():
            return -1
        else:
            self.len -= 1
            value = self.head.data
            self.head = self.head.next
            return value

    def front(self):
        if len(self):
            return self.head.data
        else:
            return -1
    
    def back(self):
        if len(self):
            return self.tail.data
        else:
            return -1

    def __len__(self):
        return self.len
        


q = queue()

for _ in range(n):
    command = sys.stdin.readline().rstrip()
    if command == 'pop':
        print(q.pop())
    elif command[:4] == 'push':
        q.push(int(command[5:]))
    elif command == 'size':
        print(len(q))
    elif command == 'empty':
        if q.empty():
            print(1)
        else:
            print(0)
    elif command == 'front':
        print(q.front())
    elif command == 'back':
        print(q.back())