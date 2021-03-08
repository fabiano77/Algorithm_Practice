import sys
input = lambda: sys.stdin.readline().rstrip()

class min_heap:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)
        index = len(self.data)-1
        while index and self.data[index] < self.data[(index-1)//2]:
            self.data[index], self.data[(index-1)//2] = self.data[(index-1)//2], self.data[index]
            index = (index-1)//2

    def pop(self):
        if len(self) == 0:
            return 0

        item = self.data[0]
        if len(self.data) == 1:
            self.data.pop()
        else:
            self.data[0] = self.data.pop()
            self.siftdown(0)
        return item

    def __len__(self):
        return len(self.data)

    def siftdown(self, index):
        parent = index
        spotFound = False
        siftkey = self.data[parent]
        while 2*(parent+1) <= len(self.data) and not spotFound:
            if 2*(parent+1) < len(self.data) and self.data[2*parent+1] > self.data[2*parent+2]:
                smallchild = 2*parent + 2
            else:
                smallchild = 2*parent + 1

            if siftkey > self.data[smallchild]:
                self.data[parent] = self.data[smallchild]
                parent = smallchild
            else:
                spotFound = True
        self.data[parent] = siftkey

    def __str__(self):
        return str(self.data)

min_Q = min_heap()

for _ in range(int(input())):
    in_data = int(input())
    if in_data == 0:
        print(min_Q.pop())
    else:
        min_Q.push(in_data)