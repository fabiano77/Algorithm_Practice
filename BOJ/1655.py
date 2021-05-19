'''
1                   
1   (5) <-
1   2   (5)
1   2   (5)   (10) <-
-99 1   2   (5)   (10)
-99 1   2   (5)   (7)   (10) <-
-99 1   2   5   (5)   (7)   (10)
1
1
2
2
2
2
5
'''
'''
1
1 (5)
1 2 (5)
1 2 (5) (10)
1 2 10  (5) (10)
'''
import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
maxQ = []      #[0]에 가장 큰것
minQ = []      #[0]에 가장 작은 것
for i in range(n):
    heapq.heappush(maxQ, -int(input()))
    if i%2 == 1:
        heapq.heappush(minQ, -heapq.heappop(maxQ))
    elif maxQ and minQ and -maxQ[0] > minQ[0] :
        heapq.heappush(minQ, -heapq.heappop(maxQ))
        heapq.heappush(maxQ, -heapq.heappop(minQ))
        
    print(-maxQ[0])
    