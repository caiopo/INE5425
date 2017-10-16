import random
from functools import partial


def normal(mean, sd):
    return partial(random.normalvariate, mean, sd)


def uniform(a, b):
    return partial(random.uniform, a, b)


def triangular(low, mode, high):
    return partial(random.triangular, low, high, mode)


def exponential(mean):
    return partial(random.expovariate, mean)


def constant(value):
    return lambda: value
