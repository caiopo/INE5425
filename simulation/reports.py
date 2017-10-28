from itertools import chain
from statistics import mean, StatisticsError


def failed_time(server):
    return sum((end - start) for start, end in server.fails)


def fail_rate(server):
    if server.state.current_time == 0:
        return 1

    return failed_time(server) / server.state.current_time


def occupied_time(server):
    return sum((e.end_time - e.start_time) for e in server.history)


def occupation_rate(server):
    if server.state.current_time == 0:
        return 1

    return occupied_time(server) / server.state.current_time


def mean_time_in_system(servers):
    entities = chain.from_iterable(s.history for s in servers)

    try:
        return mean((e.end_time - e.enqueue_time) for e in entities)
    except StatisticsError:
        return None


def mean_time_in_queue(servers):
    entities = chain.from_iterable(s.history for s in servers)

    try:
        return mean((e.start_time - e.enqueue_time) for e in entities)
    except StatisticsError:
        return None


def mean_entities_in_queue(server):
    ...
