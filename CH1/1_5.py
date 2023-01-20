# 实现一个队列，能够以给定的优先级来对元素排序

import heapq


class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        #推入heap的其实是一个元组
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


q = PriorityQueue()
q.push(1, 1)
q.push(-10, 5)
q.push(5, 10)
q.push(2, 10)
print(q.pop())
print(q.pop())