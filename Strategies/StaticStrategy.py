__author__ = 'camzzz'

import random

from BaseStrategy import BaseStrategy


class StaticStrategy(BaseStrategy):
    """
    Strategy which always uses the same allocation of soldiers
    Create like: StaticStrategy('my_strategy', [10, 5, 20, 15, 20, 5 ,10, 15])
    Pas shuffle=True to randomise the order you return the values in.
    """
    def __init__(self, name, static_soldiers, shuffle=False):
        super(StaticStrategy, self).__init__(name)
        self.static_soldiers = static_soldiers
        self.shuffle = shuffle

    def soldiers_request(self, iteration):
        if self.shuffle:
            return sorted(self.static_soldiers, key=lambda k: random.random())
        else:
            return self.static_soldiers
