__author__ = 'camzzz'

from Strategies import StaticStrategy
from StrategyUtils import StrategyRanker


def main():
    static_strat_list = []
    for i in xrange(0, 101, 1):
        for j in xrange(0, 101-i, 1):
            for k in xrange(j, 101-i-j):
                static_strat_list.append([i, j, k])

    strategies = []
    for s in static_strat_list:
        strategies.append(StaticStrategy('static_%s_1' % s, s, True))

    sr = StrategyRanker(strategies, num_fields=3, num_runs=1, total_score=True)
    sr.run()

    top_strats = sr.get_top_strategies(1)
    print top_strats


if __name__ == "__main__":
    main()