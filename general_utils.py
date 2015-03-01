__author__ = 'camzzz'


try:
    from numpy import sign
except ImportError:
    def sign(x):
        if x > 0:
            return 1
        elif x == 0:
            return 0
        else:
            return -1


class UsageError(Exception):
    pass


def cumulative_sum(itr):
    total = 0
    for v in itr:
        total += v
        yield total