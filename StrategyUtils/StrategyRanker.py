__author__ = 'camzzz'

try:
    import progressbar
except:
    pass
from GameManager import GameManager


class StrategyRanker(object):
    def __init__(self, strategies, num_fields, num_runs, total_score=True):
        self.num_fields = num_fields
        self.num_runs = num_runs
        self.total_score = total_score

        self.strategies = strategies
        self.strategy_scores = [[s, 0.0] for s in strategies]

    def run(self):
        bar = progressbar.ProgressBar(maxval=len(self.strategies)*(len(self.strategies) + 1) / 2.0,
                                      widgets=[progressbar.Bar('=', '[', ']'), progressbar.Percentage()])
        k = 0
        for i in xrange(len(self.strategies)):
            for j in xrange(i+1, len(self.strategies)):
                gm = GameManager(self.strategies[i], self.strategies[j], self.num_fields, self.num_runs, self.total_score)
                gm.run()
                if gm.check_strategy_A_win():
                    self.strategy_scores[i][1] += 1
                else:
                    self.strategy_scores[j][1] += 1

                bar.update(k)
                k += 1

        self.sort_scores()
        bar.finish()

    def sort_scores(self):
        self.strategy_scores.sort(key=lambda i: i[1], reverse=True)

    def get_top_strategies(self, n=1):
        return [s for s, score in self.strategy_scores][0:n]
