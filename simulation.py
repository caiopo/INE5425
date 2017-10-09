from collections import deque
import exceptions
import events


class EventQueue:
    def __init__(self, entity_limit=None):
        self.entity_limit = entity_limit
        self.queue = deque()
        self._history = []

    def __len__(self):
        return len(self.queue)

    def enqueue(self, event):
        if (isinstance(event, events.NewEntity) and
                self._count_entities() == self.entity_limit):
            raise exceptions.EntityQueueFull()

        self.queue.append(event)

    def dequeue(self):
        event = self.queue.popleft()
        self._history.append(event)
        return event

    def _count_entities(self):
        return len([event for event in self.queue
                    if isinstance(event, events.NewEntity)])


class Statistics:
    def __init__(self):
        self.fails = 0
        self.fixes = 0
        self.entities = 0


class State:
    def __init__(self, time_limit):
        self.time_limit = time_limit

        self.queue = EventQueue()

        self.queue.enqueue(events.FinishSimulation(time_limit))

        self.tec1 = None
        self.tec2 = None
        self.ts1 = None
        self.ts2 = None
        self.tef = None
        self.tf = None


class Simulation:
    def __init__(self, state):
        self.state = state

    def run(self):
        while len(self.state.queue) > 0:
            event = self.state.queue.dequeue()

            event.run(self.state)


if __name__ == '__main__':
    Simulation(State(10)).run()
