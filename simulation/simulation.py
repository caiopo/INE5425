from . import events
from .entity import Entity
from .queues import EntityQueue, PriorityQueue


class Server:
    def __init__(self, n, state, tec, ts):
        self.n = n
        self.state = state
        self.tec = tec
        self.ts = ts

        self.entities = EntityQueue()
        self.current = None

        self.failed = None
        self.fails = []

    @property
    def other(self):
        return self.state.servers[not self.n]

    def enqueue(self, entity):
        if not isinstance(entity, Entity):
            raise TypeError()

        self.entities.enqueue(entity)

    def dequeue(self):
        return self.entities.dequeue()

    def start_computing(self):
        if self.failed is not None:
            return False

        self.current = self.dequeue()
        self.current.start_time = self.state.current_time

        return True

    def finish_computing(self):
        self.current.end_time = self.state.current_time
        self.current = None

    def fail(self):
        if self.current is not None:
            return False

        self.failed = self.state.current_time

        return True

    def fix(self):
        self.fails.append((self.failed, self.state.current_time))
        self.failed = None

    @property
    def history(self):
        h = self.entities.queue.history

        if len(h) > 1:
            return h[:-1]

        return h


class Statistics:
    def __init__(self):
        self.entities_entered = 0
        self.entities_left = 0
        self.entities_blocked = 0

    def __str__(self):
        values = ', '.join('{}={}'.format(*it) for it in self.__dict__.items())

        return 'Statistics({})'.format(values)


class State:
    # ugly
    def __init__(self, *,
                 entity_limit, total_time,
                 tec1, tec2, ts1, ts2, tef, tf):
        self.total_time = total_time

        self.events = PriorityQueue()
        self.entities = EntityQueue(entity_limit)
        self.started = False
        self.finished = False
        self.current_time = 0

        self.enqueue(events.StartSimulation(self, 0))

        self.tef = tef
        self.tf = tf

        self.servers = (
            Server(0, self, tec1, ts1),
            Server(1, self, tec2, ts2),
        )

        self.statistics = Statistics()

    def enqueue(self, event):
        if not isinstance(event, events.Event):
            raise TypeError()

        self.events.enqueue(event)

    def dequeue(self):
        event = self.events.dequeue()

        self.current_time = event.time

        return event


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

        event = self.state.dequeue()

        event.run()

        return self.state

    def run_until_complete(self):
        while not self.state.finished:
            self.step()

        return self.state
