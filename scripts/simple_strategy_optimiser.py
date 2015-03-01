__author__ = 'camzzz'

from GameManager import GameManager
from Strategies import StaticStrategy, RandomStrategy
import progressbar


class StrategyRanker(object):
    def __init__(self, strategies, num_fields, num_runs, total_score=True):
        self.num_fields = num_fields
        self.num_runs = num_runs
        self.total_score = total_score

        self.strategies = strategies
        self.strategy_scores = [[s, 0.0] for s in strategies]

    def run(self):
        bar = progressbar.ProgressBar(maxval=(len(self.strategies)**2),
                                      widgets=[progressbar.Bar('=', '[', ']'), progressbar.Percentage()])
        for i, s_a in enumerate(self.strategies):
            for j, s_b in enumerate(self.strategies):
                gm = GameManager(s_a, s_b, self.num_fields, self.num_runs, self.total_score)
                gm.run()
                if gm.check_strategy_A_win():
                    self.strategy_scores[i][1] += 1
                else:
                    self.strategy_scores[j][1] += 1

                bar.update(i * len(self.strategies) + j)

        self.sort_scores()
        bar.finish()

    def sort_scores(self):
        self.strategy_scores.sort(key=lambda i: i[1], reverse=True)

    def get_top_strategies(self, n=1):
        return [s for s, score in self.strategy_scores][0:n]


def main():
    static_strat_list = []
    for i in xrange(101):
        for j in xrange(0, 101-i):
            for k in xrange(j, 101-i-j):
                static_strat_list.append([i, j, k])

    strategies = []
    for s in static_strat_list:
        strategies.append(StaticStrategy('static_%s_1' % s, s, True))
        strategies.append(StaticStrategy('static_%s_0' % s, s, False))
    sr = StrategyRanker(strategies, num_fields=3, num_runs=1, total_score=True)
    sr.run()

    top_strats = sr.get_top_strategies(1)
    print top_strats


if __name__ == "__main__":
    main()