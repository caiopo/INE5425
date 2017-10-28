from functools import total_ordering
from itertools import count

entity_count = count()


@total_ordering
class Entity:
    def __init__(self, time, server):
        self.enqueue_time = time
        self.server = server
        self.number = next(entity_count)
        self.start_time = None
        self.end_time = None

    def __lt__(self, other):
        return self.enqueue_time < other.enqueue_time

    def __eq__(self, other):
        return self.enqueue_time == other.enqueue_time
