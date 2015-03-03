__author__ = 'camzzz'


class BaseStrategy(object):
    """
    Base class for Blotto strategies
    
    Just make your strategy inherit from this, copy the example and forget allll about it...
    """
    def __init__(self, name):
        self.name = name
        self.num_fields = None
        self.num_runs = None

        self.opponent_allocations = []
        self.past_scores = []

    def __repr__(self):
        return "%s:%s" % (self.__class__.__name__, self.name)

    def initialise(self, num_fields, num_runs):
        """
        Called before the battle starts
        Wipes history we recorded from the last opponent
        """
        self.num_fields = num_fields
        self.num_runs = num_runs
        self.opponent_allocations = []
        self.past_scores = []

    def soldiers_request(self, iteration):
        """
        This method will be called each turn to ask for you allocation of soldiers
        return a list of positive integers with sum less than or equal to 100
        """
        pass

    def post_results(self, score, soldiers_B, check_B):
        """
        This method will be called after each individual game is resolved.
        It tells you the score (positive you won, negative you lost)
        It tells you what the opponents soldiers allocation was
        It tells you if the opponents allocation was deemed valid
        """
        self.past_scores.append(score)
        self.opponent_allocations.append(soldiers_B)
