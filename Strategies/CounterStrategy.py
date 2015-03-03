__author__ = 'camzzz'

from BaseStrategy import BaseStrategy
from StrategyUtils.assorted_utils import counter_allocation
from StrategyUtils.random_utils import random_draw_allocation


class CounterStrategy(BaseStrategy):
    """
    Counter the last move of the opponent, always beats a static strategy!
    will apply 'counter_allocation' function to oppoents last strategy N times, where N = counte_level, default 1
    """
    def __init__(self, name, counter_level=1):
        super(CounterStrategy, self).__init__(name)
        self.counter_level = counter_level

    def soldiers_request(self, iteration):
        if iteration == 0:
            #Nothing to copy yet
            return random_draw_allocation([1.0 / self.num_fields for _ in xrange(self.num_fields)])

        else:
            alloc = self.opponent_allocations[-1]
            for _ in xrange(self.counter_level):
                #Aha! We can beat the strategy which beats the strategy which will beat out opponent!
                #They wont catch me out, so clever!*
                alloc = counter_allocation(alloc)
            return alloc
        
# *not necessarily clever
