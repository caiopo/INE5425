import logging
from functools import total_ordering


@total_ordering
class Event:
    def __init__(self, state, time):
        self.time = time
        self.state = state

    def run(self):
        print(type(self).__name__)

        self._run()

        next_event = self._next_event()

        if next_event is not None:
            self.state.enqueue(next_event)

    def _run(self):
        raise NotImplementedError()

    def _next_event(self):
        return None

    def __lt__(self, other):
        return self.time < other.time

    def __eq__(self, other):
        return self.time == other.time


class StartSimulation(Event):
    def _run(self):
        pass

    def _next_event(self):
        return FinishSimulation(self.state, self.state.total_time)


class FinishSimulation(Event):
    def _run(self):
        self.state.finished = True


class ServerEvent(Event):
    def __init__(self, state, time, server):
        super().__init__(state, time)

        self.server = server


class NewEntity(ServerEvent):
    def _run(self):
        self.server.enqueue(Entity(self.state, self.time, self.server))

        self.state.statistics.total_entities += 1

    def _next_event(self):
        return NewEntity(
            self.state, self.time + self.server.tec(), self.server)


class ServerFail(ServerEvent):
    def _run(self):
        pass

    def _next_event(self):
        return ServerFixed(
            self.state, self.time + self.state.tf(), self.server)


class ServerFixed(ServerEvent):
    def _run(self):
        pass

    def _next_event(self):
        return ServerFail(
            self.state, self.time + self.state.tef(), self.server)


class StartComputing(ServerEvent):
    def _run(self):
        entity = self.server.dequeue()

        self.server.compute()

    def _next_event(self):
        return FinishComputing(
            self.state, self.time + self.server.ts(), self.server)


class FinishComputing(ServerEvent):
    def _run(self):
        pass
