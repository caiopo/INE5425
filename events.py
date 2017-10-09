import logging


class Event:
    def __init__(self, time):
        self.time = time

    def run(self, state):
        raise NotImplementedError()


class NewEntity(Event):
    def run(self, state):
        pass


class ServerFail(Event):
    def run(self, state):
        pass


class ServerFixed(Event):
    def run(self, state):
        pass


class StartComputing(Event):
    def run(self, state):
        pass


class FinishComputing(Event):
    def run(self, state):
        pass


class FinishSimulation(Event):
    def run(self, state):
        print('FinishSimulation#run')
