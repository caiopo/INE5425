from heapq import heappop, heappush
import events
import exceptions


class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.history = []

    def enqueue(self, item):
        heappush(self.heap, item)

    def dequeue(self):
        event = heappop(self.heap)
        self.history.append(event)
        return event

    def __len__(self):
        return len(self.heap)

    def __iter__(self):
        return iter(self.heap)


class EntityQueue:
    def __init__(self, entity_limit=None):
        self.entity_limit = entity_limit
        self.queue = PriorityQueue()

    def enqueue(self, entity):
        if (self.entity_limit is not None and
                len(self.queue) >= self.entity_limit):
            raise exceptions.EntityQueueFull()

        self.queue.enqueue(entity)

    @property
    def dequeue(self):
        return self.queue.dequeue

    @property
    def __len__(self):
        return self.queue.__len__

    @property
    def __iter__(self):
        return self.queue.__iter__
