__author__ = 'camzzz'

from GameManager import GameManager
from Strategies import StaticStrategy, CounterStrategy


def main():
    # GAME 1
    # Create strategies
    strategy_A = StaticStrategy('The Destroyer', [51, 47, 2], shuffle=False)
    strategy_B = StaticStrategy('The Shuffling Destroyer', [51, 47, 2], shuffle=True)
    strategy_C = CounterStrategy('The Counter')

    # Run games
    gm = GameManager(strategy_A, strategy_C, num_fields=3, num_runs=100, total_score=True)
    gm.run()
    gm.plot_results()
    gm.declare_winner()

    # Run games
    gm = GameManager(strategy_B, strategy_C, num_fields=3, num_runs=100, total_score=True)
    gm.run()
    gm.plot_results()
    gm.declare_winner()

if __name__ == "__main__":
    main()