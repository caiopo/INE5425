from collections import deque

from . import events, exceptions
from .entity import Entity
from .queues import EntityQueue, PriorityQueue


class Server:
    def __init__(self, n, state, tec, ts):
        self.n = n
        self.state = state
        self.tec = tec
        self.ts = ts

        self.busy = False
        self.entities = EntityQueue()
        self.current = None

    @property
    def other(self):
        return self.state.servers[not self.n]

    def enqueue(self, entity):
        self.entities.enqueue(entity)

    def dequeue(self):
        return self.entities.dequeue()

    def start_computing(self):
        self.busy = True
        self.current = self.dequeue()

    def finish_computing(self):
        self.busy = False
        self.current = None


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
        self.started = False
        self.finished = False

        self.enqueue(events.StartSimulation(self, 0))

        self.tef = tef
        self.tf = tf

        self.servers = (
            Server(0, self, tec1, ts1),
            Server(1, self, tec2, ts2),
        )

    def enqueue(self, event):
        self.events.enqueue(event)

    def dequeue(self):
        return self.events.dequeue()


class Simulation:
    def __init__(self, state):
        self.state = state

    def step(self):
        if not self.state.started:
            self.state.started = True

        if not len(self.state.events):
            self.state.finished = True

        if self.state.finished:
            return self.state

        event = self.state.events.dequeue()

        event.run()

        return self.state

    def run_until_complete(self):
        while not self.state.finished:
            self.step()

        return self.state
