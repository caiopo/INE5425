from itertools import chain
from statistics import mean


def failed_time(server):
    return sum((end - start) for start, end in server.fails)


def fail_rate(server):
    return failed_time(server) / server.state.current_time


def occupied_time(server):
    return sum((e.end_time - e.start_time) for e in server.history) - failed_time(server)


def occupation_rate(server):
    return occupation_rate(server) / server.state.current_time


def mean_time_on_system(servers):
    entities = chain.from_iterable(s.history for s in servers)

    return mean((e.end_time - e.enqueue_time) for e in entities)


def mean_time_on_queue(servers):
    entities = chain.from_iterable(s.history for s in servers)

    return mean((e.start_time - e.enqueue_time) for e in entities)


def mean_entities_on_queue(server):
    ...
