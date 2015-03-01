__author__ = 'camzzz'

import random

from BaseStrategy import BaseStrategy


class StaticStrategy(BaseStrategy):
    def __init__(self, name, static_soldiers, shuffle=False):
        super(StaticStrategy, self).__init__(name)
        if isinstance(static_soldiers, dict):
            self.static_soldiers_map = static_soldiers
        else:
            self.static_soldiers_map = {len(static_soldiers): static_soldiers}

        self.shuffle = shuffle

        self.static_strategy = None

    def __repr__(self):
        return "StaticStrategy: %s, shuffle:%s" % (self.static_soldiers_map, self.shuffle)

    def initialise(self, num_fields, num_runs):
        super(StaticStrategy, self).initialise(num_fields, num_runs)
        self.static_strategy = self.static_soldiers_map[num_fields]

    def soldiers_request(self, iteration):
        if self.shuffle:
            return sorted(self.static_strategy, key=lambda k: random.random())
        else:
            return self.static_strategy