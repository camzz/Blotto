__author__ = 'camzzz'


class BaseStrategy(object):
    def __init__(self, opponent_name, field_weightings, num_runs):
        self.opponent_name = opponent_name
        self.field_weightings = field_weightings
        self.num_runs = num_runs

    def soldiers_request(self, iteration):
        pass

    def post_results(self, score, soldiers_B, check_A, check_B):
        pass
