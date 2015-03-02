__author__ = 'camzzz'

from BaseStrategy import BaseStrategy
from StrategyUtils.assorted_utils import counter_allocation, random_allocation


class CounterStrategy(BaseStrategy):
    def __init__(self, name, counter_level=1):
        super(CounterStrategy, self).__init__(name)
        self.counter_level = counter_level
        self.ready = False

    def __repr__(self):
        return "CounterStrategy counter_level %s" % self.counter_level

    def initialise(self, num_fields, num_runs):
        super(CounterStrategy, self).initialise(num_fields, num_runs)

    def soldiers_request(self, iteration):
        if not self.ready:
            return random_allocation([1.0 / self.num_fields for _ in xrange(self.num_fields)])

        else:
            alloc = self.opponent_allocations[-1]
            for _ in xrange(self.counter_level):
                alloc = counter_allocation(alloc)
            return alloc

    def post_results(self, score, soldiers_B, check_B):
        super(CounterStrategy, self).post_results(score, soldiers_B, check_B)
        self.ready = True

    def wipe_history(self):
        super(CounterStrategy, self).wipe_history()
        self.ready = False