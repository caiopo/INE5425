from functools import total_ordering


class Entity:
    number = 0

    def __init__(self, time, server):
        self.time = time
        self.server = server
        self.number = Entity.number
        Entity.number += 1

    def __lt__(self, other):
        return self.time < other.time

    def __eq__(self, other):
        return self.time == other.time
