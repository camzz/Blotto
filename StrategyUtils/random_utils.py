__author__ = 'camzzz'

import random


def random_allocation(weightings, number=100):
    result = [0.0 for _ in weightings]

    for _ in xrange(number):
        result[weighted_draw(weightings)] += 1

    return result


def weighted_draw(weightings):
    r = random.random()
    for i, w in enumerate(weightings):
        if r <= w:
            return i
        r -= w