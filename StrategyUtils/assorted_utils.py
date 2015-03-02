__author__ = 'camzzz'

import random
import numpy as np


def random_draw_allocation(weightings, number=100):
    result = [0.0 for _ in weightings]
    for _ in xrange(number):
        result[weighted_draw(weightings)] += 1

    return result


def random_number_allocation(weightings, number=100):
    result = []
    for w in weightings:
        result.append(random.random() * w)

    result = [int(number * r / sum(result)) for r in result]

    weightings_p = [float(w)/sum(weightings) for w in weightings]
    while sum(result) != number:
        if sum(result) > number:
            result[weighted_draw(weightings_p)] -= 1
        else:
            result[weighted_draw(weightings_p)] += 1
    return result


def dirichlet_allocation():
    pass


def get_allocation_uniform(num_fields, num_soldeirs=100):
    pass


def weighted_draw(weightings):
    assert abs(1.0 - sum(weightings)) < 0.00001, "%s sum: %s" % (weightings, sum(weightings))
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


