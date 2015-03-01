__author__ = 'camzzz'

from GameManager import GameManager
from Strategies import StaticStrategy, RandomStrategy, MixedStrategy


def main():
    # GAME 1
    # Create strategies
    a_1 = StaticStrategy('a_1', [50, 49, 1], shuffle=True)
    a_2 = StaticStrategy('a_2', [35, 60, 5], shuffle=True)

    strategy_A = MixedStrategy('MixedStart A', [a_1, a_2], [0.5, 0.5])
    strategy_B = RandomStrategy('Random Strat B', [0.50, 0.485, 0.015], shuffle=True)

    # Set up game
    gm = GameManager(strategy_A, strategy_B, num_fields=3, num_runs=10000, total_score=True)
    gm.run()
    gm.plot_results()
    gm.declare_winner()


if __name__ == "__main__":
    main()