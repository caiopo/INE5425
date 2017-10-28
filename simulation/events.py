from functools import total_ordering
from itertools import chain

from .entity import Entity
from .exceptions import EntityQueueFull

INTERVAL = 0.001


@total_ordering
class Event:
    def __init__(self, state, time):
        assert isinstance(time, (float, int))

        self.time = time
        self.state = state

    def run(self):
        print(type(self).__name__, self.time)

        self._run()

        next_event = self._next_event()

        if not isinstance(next_event, list):
            next_event = [next_event]

        for e in next_event:
            self.state.enqueue(e)

    def _run(self):
        raise NotImplementedError()

    def _next_event(self):
        return []

    def __lt__(self, other):
        return (self.time < other.time or
                self == other and EVENT_PRECEDENCE.index(type(self)) < EVENT_PRECEDENCE.index(type(other)))

    def __eq__(self, other):
        return self.time == other.time and EVENT_PRECEDENCE.index(type(self)) == EVENT_PRECEDENCE.index(type(other))


class StartSimulation(Event):
    def _run(self):
        pass

    def _next_event(self):
        server_events = list(chain.from_iterable([
            (ServerFail(self.state, self.state.tef(), server),
             NewEntity(self.state, server.tec(), server),
             StartComputing(self.state, 0, server))
            for server in self.state.servers
        ]))

        if self.state.total_time is not None:
            return server_events + [FinishSimulation(self.state, self.state.total_time)]

        return server_events


class FinishSimulation(Event):
    def _run(self):
        self.state.finished = True


class ServerEvent(Event):
    def __init__(self, state, time, server):
        super().__init__(state, time)

        self.server = server


class NewEntity(ServerEvent):
    def _run(self):
        try:
            self.server.enqueue(Entity(self.time, self.server))
        except EntityQueueFull:
            try:
                self.server.other.enqueue(Entity(self.time, self.server))
            except EntityQueueFull:
                self.state.statistics.entities_blocked += 1
            else:
                self.state.statistics.entities_entered += 1
        else:
            self.state.statistics.entities_entered += 1

    def _next_event(self):
        return NewEntity(self.state, self.time + self.server.tec(), self.server)


class ServerFail(ServerEvent):
    def _run(self):
        pass

    def _next_event(self):
        if self.server.fail():
            return ServerFixed(
                self.state, self.time + self.state.tf(), self.server)

        else:
            next_time = self.state.peek().time

            return ServerFail(
                self.state, next_time + INTERVAL, self.server)


class ServerFixed(ServerEvent):
    def _run(self):
        self.server.fix()

    def _next_event(self):
        return ServerFail(
            self.state, self.time + self.state.tef(), self.server)


class StartComputing(ServerEvent):
    def _run(self):
        if self.server.start_computing():
            self.next = FinishComputing(
                self.state, self.time + self.server.ts(), self.server)
        else:
            next_time = self.state.peek().time

            self.next = StartComputing(
                self.state, next_time + INTERVAL, self.server)

    def _next_event(self):
        return self.next


class FinishComputing(ServerEvent):
    def _run(self):
        self.state.statistics.entities_left += 1
        self.server.finish_computing()

    def _next_event(self):
        next_time = self.state.peek().time

        return StartComputing(self.state, next_time + INTERVAL, self.server)


EVENT_PRECEDENCE = [
    FinishSimulation,
    ServerFail,
    ServerFixed,
    FinishComputing,
    StartComputing,
    NewEntity,
    StartSimulation,
]
