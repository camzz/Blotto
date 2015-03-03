__author__ = 'camzzz'

from StrategyUtils.random_utils import weighted_draw

from BaseStrategy import BaseStrategy


class MixedStrategy(BaseStrategy):
    """
    Allows you to mix up your completely different strategies
    Just pass in those strategies and the probability to use each one.
    
    s1 = MyStrategy('s1')
    s2 = MyStrategy('s2')
    
    mixed_strategy = MixedStrategy('TheMixerminator', [s1, s2], [0.6, 0.4])
    """
    def __init__(self, name, strategies, weightings):
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
