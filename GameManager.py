__author__ = 'camzzz'

from general_utils import sign


class GameManager(object):
    def __init__(self, stategy_A, strategy_B, num_fields, num_runs, total_score=True):
        self.strategy_A = stategy_A
        self.strategy_B = strategy_B

        self.num_fields = num_fields
        self.num_runs = num_runs

        #Use the total score over many games, or number of individual games won, regardless of score
        self.total_score = total_score

        #results is a list of scores, positive is towards A, negative to B
        self.results = []

    def run(self):
        #initialise strategies
        self.strategy_A.initialise(opponent=self.strategy_B.name,
                                   num_fields=self.num_fields,
                                   num_runs=self.num_runs)
        self.strategy_B.initialise(opponent=self.strategy_A.name,
                                   num_fields=self.num_fields,
                                   num_runs=self.num_runs)

        for i in xrange(self.num_runs):
            self.iteration(i)

        return self.results

    def iteration(self, i):
        soldiers_A = self.strategy_A.soldiers_request(i)
        soldiers_B = self.strategy_B.soldiers_request(i)

        #Check what was placed
        check_A = self.check_solders(soldiers_A)
        check_B = self.check_solders(soldiers_B)

        #Resolve Battle
        score = self.resolve_battle(soldiers_A, soldiers_B, check_A, check_B)

        #Infom strategies
        self.strategy_A.post_results(score, soldiers_B, check_A, check_B)
        self.strategy_B.post_results(-score, soldiers_A, check_B, check_A)

        self.results.append(score)

    def check_solders(self, soldiers):
        check = 1
        try:
            check *= len(soldiers) == self.num_fields
            check *= all(int(s) == s for s in soldiers)
            check *= all(a >= 0 for a in soldiers)
            check *= sum(soldiers) <= 100.0
        except (TypeError, IndexError) as _:
            check = 0

        return check

    def resolve_battle(self, soldiers_A, soldiers_B, check_A, check_B):
        if check_A and not check_B:
            return self.num_fields
        if check_B and not check_A:
            return -self.num_fields
        if not check_B and not check_A:
            return 0

        score = 0
        for i in xrange(self.num_fields):
            score += sign(soldiers_A[i] - soldiers_B[i])

        if self.total_score:
            return score
        else:
            return sign(score)