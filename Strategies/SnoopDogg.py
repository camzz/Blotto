__author__ = 'camzzz'

import inspect
import random
import numpy as np

from BaseStrategy import BaseStrategy
from StrategyUtils.assorted_utils import counter_allocation


class SnoopDogg(BaseStrategy):
    def __init__(self, name):
        super(SnoopDogg, self).__init__(name)
        self.is_strategy_A = False
        self.opponent = None
        self.opponent_prediction = None
        self.random_state = None
        self.np_random_state = None

    def initialise(self, num_fields, num_runs):
        super(SnoopDogg, self).initialise(num_fields, num_runs)
        stack = inspect.stack()
        gm = stack[1][0].f_locals["self"]
        if gm.strategy_A == self:
            self.opponent = gm.strategy_B
            self.is_strategy_A = True
        else:
            self.opponent = gm.strategy_A
            self.is_strategy_A = False

        self.random_state = random.getstate()
        self.np_random_state = np.random.get_state()

    def soldiers_request(self, iteration):
        if self.is_strategy_A:
            self.random_state = random.getstate()
            self.np_random_state = np.random.get_state()
            opponent_prediction = self.opponent.soldiers_request(iteration)
            random.setstate(self.random_state)
            np.random.set_state(self.np_random_state)
        else:
            random.setstate(self.random_state)
            np.random.set_state(self.np_random_state)
            opponent_prediction = self.opponent.soldiers_request(iteration)
            self.random_state = random.getstate()
            self.np_random_state = np.random.get_state()

        self.opponent_prediction = opponent_prediction
        return counter_allocation(opponent_prediction)


def main():
    from Strategies.RandomStrategy import RandomStrategy, RandomStyle
    from GameManager import GameManager

    strategy_a = SnoopDog("Snoop!")
    strategy_b = RandomStrategy("Rando", [0.4, 0.4, 0.2], shuffle=True, style=RandomStyle.NUMBER)

    gm = GameManager(strategy_a, strategy_b, 3, 30, total_score=False)
    gm.run()
    gm.plot_results()
    gm.declare_winner()

if __name__ == "__main__":
    main()
