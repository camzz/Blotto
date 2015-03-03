__author__ = 'camzzz'

try:
    import matplotlib.pyplot as plt
    PLOTTING = True
except:
    PLOTTING = False
from general_utils import sign, cumulative_sum


class GameManager(object):
    """
    This class battles two strategies, you dont need to know how it works but to set it up for testing for the main competition:
    gm = GameManager(strategy_A, strategy_B, 8, 10000)
    gm.run()
    
    use gm.plot_results() to see a nice plot *requires matplotlib
    use gm.declare_winner() to see how you did!
    """
    def __init__(self, stategy_A, strategy_B, weights, soldiers, num_runs, total_score=False):
        self.strategy_A = stategy_A
        self.strategy_B = strategy_B

        self.weights = weights
        self.soldiers = soldiers
        self.num_runs = num_runs

        #Use the total score over many games, or number of individual games won, regardless of score
        self.total_score = total_score

        #results is a list of scores, positive is towards A, negative to B
        self.results = []

    def run(self):
        #initialise strategies
        self.strategy_A.initialise(weights=self.weights, soldiers=self.soldiers,
                                   num_runs=self.num_runs)
        self.strategy_B.initialise(weights=self.weights, soldiers=self.soldiers,
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
        self.strategy_A.post_results(score, soldiers_B, check_B)
        self.strategy_B.post_results(-score, soldiers_A, check_A)

        self.results.append(score)

    def check_solders(self, soldiers):
        check = 1
        try:
            check *= len(soldiers) == len(self.weights)
            check *= all(int(s) == s for s in soldiers)
            check *= all(a >= 0 for a in soldiers)
            check *= sum(soldiers) <= self.soldiers
        except (TypeError, IndexError) as _:
            check = 0

        return check

    def resolve_battle(self, soldiers_A, soldiers_B, check_A, check_B):
        if check_A and not check_B:
            return sum(self.weights) if self.total_score else 1
        if check_B and not check_A:
            return -sum(self.weights) if self.total_score else 0
        if not check_B and not check_A:
            return 0

        score = 0
        for i in xrange(len(self.weights)):
            score += sign(soldiers_A[i] - soldiers_B[i])*self.weights[i]

        if self.total_score:
            return score
        else:
            return sign(score)

    def plot_results(self):
        if not PLOTTING: return
        data = list(cumulative_sum(self.results))
        plt.plot(data)
        plt.ylabel('A - B points')
        plt.show(block=False)

    def get_max_score(self):
        if self.total_score:
            return self.num_runs * sum(self.weights)
        else:
            return self.num_runs

    def declare_winner(self):
        s = sum(self.results)
        if s > 0:
            print "%s is the winner by %s points!" % (self.strategy_A.name, s)
            print "Max possible points: %s" % self.get_max_score()
            print "Percentage of highest score: %.2f%%" % (100 * s / self.get_max_score())

        elif s < 0:
            print "%s is the winner by %s points!" % (self.strategy_B.name, -s)
            print "Max possible points: %s" % self.get_max_score()
            print "Percentage of highest score: %.2f%%" % (100 * -s / self.get_max_score())

        else:
            print "The game was a tie!"
        plt.show()

    def check_strategy_A_win(self):
        if sum(self.results) > 0:
            return True
        else:
            return False

    def check_strategy_B_win(self):
        if sum(self.results) < 0:
            return True
        else:
            return False
