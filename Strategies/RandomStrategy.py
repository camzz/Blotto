__author__ = 'camzzz'

import random

from BaseStrategy import BaseStrategy
from general_utils import UsageError
from StrategyUtils.random_utils import random_draw_allocation, random_number_allocation, \
    dirichlet_allocation, get_allocation_uniform


class RandomStyle(object):
    NUMBER = 0
    DRAW = 1
    DIRICHLET = 2
    UNIFORM = 3

    @classmethod
    def get_name(cls, num):
        for k, v in cls.__dict__.iteritems():
            if v == num:
                return k
        else:
            raise Exception("RandomStyle not found: %s" % num)


class RandomStrategy(BaseStrategy):
    def __init__(self, name, weightings=None, shuffle=False, style=None):
        super(RandomStrategy, self).__init__(name)
        if style is None:
            self.style = RandomStyle.NUMBER
        else:
            self.style = style

        if self.style != RandomStyle.UNIFORM:
            assert weightings is not None
            assert abs(sum(weightings) - 1.0) < 1e-6, "weightings: %s" % weightings
            self.weightings = weightings

        self.shuffle = shuffle

    def soldiers_request(self, iteration):
        if self.style == RandomStyle.NUMBER:
            strategy = random_number_allocation(weightings=self.weightings)

        elif self.style == RandomStyle.DRAW:
            strategy = random_draw_allocation(weightings=self.weightings)

        elif self.style == RandomStyle.DIRICHLET:
            strategy = dirichlet_allocation(weightings=self.weightings)
            
        elif self.style == RandomStyle.UNIFORM:
            strategy = get_allocation_uniform(self.num_fields)

        else:
            raise UsageError("Style not recognised: %s" % RandomStyle.get_name(self.style))

        if self.shuffle:
            return sorted(strategy, key=lambda k: random.random())
        else:
            return strategy
