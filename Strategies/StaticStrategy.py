__author__ = 'camzzz'

import random
import copy

from BaseStrategy import BaseStrategy


class StaticStrategy(BaseStrategy):
    def __init__(self, static_soldiers, shuffle=False):
        super(StaticStrategy, self).__init__()
        if isinstance(static_soldiers, dict):
            self.static_soldiers_map = static_soldiers
        else:
            self.static_soldiers_map = {len(static_soldiers): static_soldiers}

        self.shuffle = shuffle

        self.static_strategy = None

    def initialise(self, opponent_name, num_fields, num_runs):
        super(StaticStrategy, self).initialise(opponent_name, num_fields, num_runs)
        self.static_strategy = self.static_soldiers_map[num_fields]

    def soldiers_request(self, iteration):
        if self.shuffle:
            return random.shuffle(copy.copy(self.static_strategy))
        else:
            return self.static_strategy