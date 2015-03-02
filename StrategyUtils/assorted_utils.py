__author__ = 'camzzz'


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


