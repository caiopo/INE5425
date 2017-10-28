from heapq import heappop, heappush

from . import exceptions


class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.history = []

    def enqueue(self, item):
        heappush(self.heap, item)

    def dequeue(self):
        item = heappop(self.heap)
        self.history.append(item)
        return item

    @property
    def first(self):
        return self.heap[0]

    def __len__(self):
        return len(self.heap)

    def __iter__(self):
        return iter(sorted(self.heap))


class EntityQueue:
    def __init__(self, entity_limit=None):
        self.entity_limit = entity_limit
        self.queue = PriorityQueue()

    def enqueue(self, entity):
        if (self.entity_limit is not None and
                    len(self.queue) >= self.entity_limit):
            raise exceptions.EntityQueueFull()

        self.queue.enqueue(entity)

    def dequeue(self):
        return self.queue.dequeue()

    @property
    def __len__(self):
        return self.queue.__len__

    @property
    def __iter__(self):
        return self.queue.__iter__
