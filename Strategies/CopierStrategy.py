__author__ = "camzz/linus"

from random import randint

from BaseStrategy import BaseStrategy
from StrategyUtils.random_utils import 


class CopierStrategy(BaseStrategy):
    """
    This strategy copies a random move the opponent has made in the past.
    """
    def soldiers_request(self, iteration):
        
        if iteration == 0:
            #First move, nothing to copy :( pick a random one
            return get_allocation_uniform(self.num_fields)
        else:
            randomIndex = randint(0, len(self.opponent_allocations)-1)
            myMove = self.opponent_allocations[randomIndex]
            
            return myMove
