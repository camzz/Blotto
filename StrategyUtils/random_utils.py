
__author__ = 'camzzz'

import random
try:
    import numpy as np
except:
    pass


def random_draw_allocation(weightings, number=100):
    """ puts a soldier in a random field 100 times, according to the weightings """
    assert abs(sum(weightings) - 1.0) < 1e-6
    result = [0.0 for _ in weightings]
    for _ in xrange(number):
        result[weighted_draw(weightings)] += 1

    return result


def random_number_allocation(weightings, number=100):
    """
    Allocates soldiers to fields according to the relative size of several random numbers
    Mean in each field will be relative to the weightings passed
    """
    assert abs(sum(weightings) - 1.0) < 1e-6
    result = []
    for w in weightings:
        result.append(random.random() * w)
    result = [int(number * r / sum(result)) for r in result]

    while sum(result) != number:
        if sum(result) > number:
            result[weighted_draw(weightings)] -= 1
        else:
            result[weighted_draw(weightings)] += 1
    return result


def dirichlet_allocation(weightings, number=100):
    """
    Allocates soldiers to fields according to dirichlet distribution
    Weightings are mean proportion of soldiers in each field
    """
    assert abs(sum(weightings) - 1.0) < 1e-6
    result = [int(r) for r in np.random.dirichlet(weightings) * number]

    while sum(result) != number:
        if sum(result) > number:
            result[weighted_draw(weightings)] -= 1
        else:
            result[weighted_draw(weightings)] += 1
    return result


def get_allocation_uniform(num_fields, num_soldiers=100):
    """ gets an allocation uniformly from all possible allocations. According to some internet source..."""
    dividers = sorted(random.sample(xrange(1, num_soldiers + num_fields), num_fields - 1))
    return [a - b - 1 for a, b in zip(dividers + [num_soldiers + num_fields], [0] + dividers)]


def weighted_draw(weightings):
    """
    Draw a number from 0->(N-1)
    according to the weightings given (length N)
    """
    assert abs(1.0 - sum(weightings)) < 0.00001, "%s sum: %s" % (weightings, sum(weightings))
    r = random.random()
    for i, w in enumerate(weightings):
        if r <= w:
            return i
        r -= w
