import logging
from functools import total_ordering


@total_ordering
class Event:
    def __init__(self, time):
        self.time = time

    def run(self, state):
        raise NotImplementedError()

    def __lt__(self, other):
        return self.time < other.time

    def __eq__(self, other):
        return self.time == other.time


class StartSimulation(Event):
    def run(self, state):
        state.new_event(FinishSimulation(state.total_time))


class FinishSimulation(Event):
    def run(self, state):
        print('FinishSimulation#run')


class ServerEvent(Event):
    def __init__(self, time, server):
        super().__init__(time)

        self.server = server


class NewEntity(ServerEvent):
    def run(self, state):
        new_time = self.time + state.tec()

        entity = Entity(self.time, self.server)


class ServerFail(ServerEvent):
    def run(self, state):
        pass


class ServerFixed(ServerEvent):
    def run(self, state):
        pass


class StartComputing(ServerEvent):
    def run(self, state):
        pass


class FinishComputing(ServerEvent):
    def run(self, state):
        pass
