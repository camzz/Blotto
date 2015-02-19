__author__ = 'camzzz'

import random

from BaseStrategy import BaseStrategy
from exceptions import UsageError
from StrategyUtils.random_utils import random_allocation


class RandomStrategy(BaseStrategy):
    def __init__(self, weightings, shuffle=False):
        super(RandomStrategy, self).__init__()
        if isinstance(weightings, dict):
            self.weightings_map = weightings
        else:
            self.weightings_map = {len(weightings): weightings}

        self.shuffle = shuffle

        self.weightings = None

    def initialise(self, opponent_name, num_fields, num_runs):
        super(RandomStrategy, self).initialise(opponent_name, num_fields, num_runs)
        self.weightings = self.weightings_map[num_fields]

        if sum(self.weightings) != 1.0:
            raise UsageError("Weightings must add to 1: %s" % self.weightings)

    def soldiers_request(self, iteration):
        strategy = random_allocation(weightings=self.weightings)

        if self.shuffle:
            return random.shuffle(strategy)
        else:
            return strategy