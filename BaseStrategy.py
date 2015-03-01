__author__ = 'camzzz'


class BaseStrategy(object):
    def __init__(self, name):
        self.name = name
        self.num_fields = None
        self.num_runs = None

        self.opponent_allocations = []
        self.past_scores = []

    def __repr__(self):
        return "%s:%s" % (self.__class__.__name__, self.name)

    def initialise(self, num_fields, num_runs):
        self.num_fields = num_fields
        self.num_runs = num_runs
        self.wipe_history()

    def soldiers_request(self, iteration):
        pass

    def post_results(self, score, soldiers_B, check_B):
        self.past_scores.append(score)
        self.opponent_allocations.append(soldiers_B)

    def wipe_history(self):
        self.opponent_allocations = []
        self.past_scores = []
