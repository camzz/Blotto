__author__ = 'camzzz'

import random

from general_utils import USageError


def random_allocation(weightings, number=100, allocation_type=0):
    if allocation_type == 0:
        result = [0.0 for _ in weightings]

        for _ in xrange(number):
            result[weighted_draw(weightings)] += 1

        return result
    
    #Not checked 
    elif allocation_type == 1:
        result = []
        for w in weightings:
            result.append(random.random() * w)
        
        result = [int(100 * r / sum(result)) for r in result]
        while sum_result != 100:
            if sum_result > 100:
                result[weighted_draw(weightings)] -= 1
            else:
                result[weighted_draw(weightings)] += 1
        return result
    
    #Some more involved distributions to come
    
    else:
        raise UsageError("allocation_type not recognised: %s" % allocation_type)


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
