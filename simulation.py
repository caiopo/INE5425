import exceptions
from collections import deque

import events
from queues import EntityQueue, PriorityQueue


class Server:
    def __init__(self, number, state):
        self.number = number
        self.working = True

    def process(self, entity, state):
        pass


class Statistics:
    def __init__(self):
        self.fails = 0
        self.fixes = 0
        self.total_entities = 0
        self.entities_blocked = 0


class State:
    # ugly
    def __init__(self, *, entity_limit=None, total_time,
                 tec1, tec2, ts1, ts2, tef, tf):
        self.total_time = total_time

        self.events = PriorityQueue()
        self.entities = EntityQueue(entity_limit)

        self.tec = (tec1, tec2)
        self.ts = (ts1, ts2)
        self.tef = tef
        self.tf = tf

        self.servers = (
            Server(0, self),
            Server(1, self),
        )

    @property
    def new_event(self):
        return self.queue.enqueue


class Simulation:
    def __init__(self, state):
        self.state = state
        self.started = False
        self.finished = False

    def step(self):
        if not self.started:
            self.started = True

        if not len(self.state.events):
            self.finished = True
            return self.state

        event = self.state.events.dequeue()

        event.run(self.state)

        return self.state

    def run_until_complete(self):
        while not self.finished:
            self.step()

        return self.state
