__author__ = 'camzzz'

from StrategyUtils.random_utils import weighted_draw

from BaseStrategy import BaseStrategy


class MixedStrategy(BaseStrategy):
    def __init__(self, name, strategies, weightings, shuffle=False):
        super(MixedStrategy, self).__init__(name)
        assert len(strategies) == len(weightings)

        self.strategies = strategies
        self.weightings = weightings

    def initialise(self, num_fields, num_runs):
        super(MixedStrategy, self).initialise(num_fields, num_runs)
        for s in self.strategies:
            s.initialise(num_fields, num_runs)

    def soldiers_request(self, iteration):
        s = self.strategies[weighted_draw(self.weightings)]
        return s.soldiers_request(iteration)

    def post_results(self, score, soldiers_B, check_B):
        for s in self.strategies:
            s.post_results(score, soldiers_B, check_B)