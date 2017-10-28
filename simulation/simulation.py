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

    def start_computing(self):
        if self.failed is not None or len(self.entities) < 1:
            return False

        self.current = self.entities.dequeue()
        self.current.start_time = self.state.current_time

        return True

    def finish_computing(self):
        self.current.end_time = self.state.current_time
        self.current = None

    def fail(self):
        print('fail called')
        if self.current is not None:
            return False

        print('falhei')

        self.failed = self.state.current_time

        return True

    def fix(self):
        if self.failed is None:
            print('failed is none', self.n, self.current)
            return

        print('consertei')

        self.fails.append((self.failed, self.state.current_time))
        self.failed = None

    @property
    def history(self):
        yield from (e for e in self.entities.queue.history if e.end_time is not None)


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

    def peek(self):
        return self.events.first


class Simulation:
    def __init__(self, state):
        self.state = state

    def _step(self):
        if not self.state.started:
            self.state.started = True

        if not len(self.state.events):
            self.state.finished = True

        if self.state.finished:
            return self.state

        event = self.state.dequeue()

        event.run()

        return self.state

    def step(self):
        time_before = self.state.current_time

        while not self.state.finished:
            self._step()

            if (self.state.current_time - time_before) > 1:
                break

        return self.state

    def run_until_complete(self):
        while not self.state.finished:
            self.step()

        return self.state
