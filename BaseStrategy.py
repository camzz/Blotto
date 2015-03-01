__author__ = 'camzzz'


class BaseStrategy(object):
    def __init__(self, name):
        self.name = name
        self.num_fields = None
        self.num_runs = None

    def initialise(self, num_fields, num_runs):
        self.num_fields = num_fields
        self.num_runs = num_runs

    def soldiers_request(self, iteration):
        pass

    def post_results(self, score, soldiers_B, check_A, check_B):
        pass
