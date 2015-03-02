__author__ = 'camzzz'

import random


def random_allocation(weightings, number=100):
    result = [0.0 for _ in weightings]

    for _ in xrange(number):
        result[weighted_draw(weightings)] += 1

    return result


def weighted_draw(weightings):
    assert sum(weightings) == 1, "%s" % weightings
    r = random.random()
    for i, w in enumerate(weightings):
        if r <= w:
            return i
        r -= w


def counter_allocation(allocation):
    """
    :param allocation: list of integers, an allocation for a round of blotto
    :return: an allocation which would beat the input
    """
    result = [0.0 for _ in allocation]
    sorted_allocation = sorted(enumerate(allocation), key=lambda x: x[1], reverse=True)

    for i in xrange(1, len(sorted_allocation)):
        result[sorted_allocation[i][0]] = sorted_allocation[i][1] + 1

    result[sorted_allocation[0][0]] = 100 - int(sum(result))
    return result