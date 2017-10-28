from functools import total_ordering


@total_ordering
class Entity:
    def __init__(self, time, server):
        self.enqueue_time = time
        self.server = server
        self.number = Entity.number
        self.start_time = None
        self.end_time = None

    def __lt__(self, other):
        return self.time < other.time

    def __eq__(self, other):
        return self.time == other.time
