import heapq
class dual_priority_queue:
    ''' 
    최대값, 최솟값을 pop할 수 있는 이중 우선순위 큐
    '''
    def __init__(self):
        self.__min_Q = []
        self.__max_Q = []
        self.__del_min_Q = []
        self.__del_max_Q = []
    def push(self, item):
        heapq.heappush(self.__min_Q, item)
        heapq.heappush(self.__max_Q, (-item, item))
    def min_top(self):
        self.adjust()
        if len(self.__min_Q) == 0:
            return None
        return self.__min_Q[0]
    def min_pop(self):
        self.adjust()
        if len(self.__min_Q) == 0:
            return None
        item = heapq.heappop(self.__min_Q)
        heapq.heappush(self.__del_max_Q, (-item, item))
        return item
    def max_top(self):
        self.adjust()
        if len(self.__max_Q) == 0:
            return None
        return self.__max_Q[0][1]
    def max_pop(self):
        self.adjust()
        if len(self.__max_Q) == 0:
            return None
        item = heapq.heappop(self.__max_Q)[1]
        heapq.heappush(self.__del_min_Q, item)
        return item
    def adjust(self):
        while self.__del_min_Q and self.__del_min_Q[0] == self.__min_Q[0]:
            heapq.heappop(self.__min_Q)
            heapq.heappop(self.__del_min_Q)
        while self.__del_max_Q and self.__del_max_Q[0] == self.__max_Q[0]:
            heapq.heappop(self.__max_Q)
            heapq.heappop(self.__del_max_Q)
    def __len__(self):
        return len(self.__min_Q)-len(self.__del_min_Q)
    def __str__(self):
        '''
        주의 __str__을 사용하면 del_min_Q, del_max_Q를 삭제하여 보여주기 때문에 O(log N)을 보장하지 않음. \n
        디버그시에만 사용 권장.
        '''
        while self.__del_min_Q:
            del_item = self.__del_min_Q.pop()
            self.__min_Q.remove(del_item)
        while self.__del_max_Q:
            del_item = self.__del_max_Q.pop()
            self.__max_Q.remove(del_item)
        heapq.heapify(self.__min_Q)
        heapq.heapify(self.__max_Q)
        return 'min_Q: ' +str(self.__min_Q) + '\nmax_Q: '  + str(list(map(lambda value : value[1], self.__max_Q)))

import sys
read = sys.stdin.readline
for _ in range(int(read())):
    queue = dual_priority_queue()
    for _ in range(int(read())):
        command, num = read().split()
        num = int(num)
        if command == 'I':
            queue.push(num)
        elif command == 'D':
            if num == 1:
                queue.max_pop()
            elif num == -1:
                queue.min_pop()

    if len(queue):
        print(queue.max_top(), queue.min_top())
    else:
        print("EMPTY")