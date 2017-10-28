import random


def normal(mean, sd):
    return lambda: abs(random.normalvariate(mean, sd))


def uniform(a, b):
    assert a < b

    return lambda: abs(random.uniform(a, b))


def triangular(low, mode, high):
    assert low <= mode <= high

    return lambda: abs(random.triangular(low, high, mode))


def exponential(mean):
    assert mean != 0

    return lambda: abs(random.expovariate(mean))


def constant(value):
    return lambda: abs(value)
