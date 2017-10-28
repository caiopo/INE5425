from functools import total_ordering

from .entity import Entity
from .exceptions import EntityQueueFull

INTERVAL = 0.1


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
        fail_events = [
            ServerFail(self.state, self.state.tef(), server)
            for server in self.state.servers
        ]

        entity_events = [
            NewEntity(self.state, server.tec(), server)
            for server in self.state.servers
        ]

        if self.state.total_time is not None:
            return entity_events + fail_events + [FinishSimulation(self.state, self.state.total_time)]

        return entity_events + fail_events


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
        if self.server.fail():
            self.next = ServerFixed(
                self.state, self.time + self.server.ts(), self.server)

        else:
            self.next = ServerFail(
                self.state, self.time + INTERVAL, self.server)

    def _next_event(self):
        return ServerFixed(
            self.state, self.time + self.state.tf(), self.server)


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
            self.next = StartComputing(
                self.state, self.time + INTERVAL, self.server)

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
