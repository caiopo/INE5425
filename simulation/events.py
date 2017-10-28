from functools import total_ordering

from .entity import Entity
from .exceptions import EntityQueueFull


@total_ordering
class Event:
    def __init__(self, state, time):
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
        fail_events = [
            ServerFail(self.state, self.state.tef(), server)
            for server in self.state.servers
        ]

        entity_events = [
            NewEntity(self.state, self.state.tec(), server)
            for server in self.state.servers
        ]

        events = [FinishSimulation(self.state, self.state.total_time)]

        return events + entity_events + fail_events


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
            self.state.statistics.entities_blocked += 1
        else:
            self.state.statistics.entities_entered += 1

    def _next_event(self):
        return NewEntity(
            self.state, self.time + self.server.tec(), self.server,
        )


class ServerFail(ServerEvent):
    def _run(self):
        self.state.statistics.fails += 1
        self.server.fail()

    def _next_event(self):
        return ServerFixed(
            self.state, self.time + self.state.tf(), self.server)


class ServerFixed(ServerEvent):
    def _run(self):
        self.state.statistics.fixes += 1
        self.server.fix()

    def _next_event(self):
        return ServerFail(
            self.state, self.time + self.state.tef(), self.server)


class StartComputing(ServerEvent):
    def _run(self):
        if not self.server.start_computing():
            self.next = StartComputing(
                self.state, self.time + 1, self.server)
        else:
            self.next = FinishComputing(
                self.state, self.time + self.server.ts(), self.server)

    def _next_event(self):
        return self.next


class FinishComputing(ServerEvent):
    def _run(self):
        self.state.statistics.entities_entered += 1

    def _next_event(self):
        return StartComputing(self.state, self.time, self.server)


EVENT_PRECEDENCE = [
    FinishSimulation,
    ServerFail,
    ServerFixed,
    FinishComputing,
    StartComputing,
    NewEntity,
    StartSimulation,
]
