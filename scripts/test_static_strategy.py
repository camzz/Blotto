__author__ = 'camzzz'

from GameManager import GameManager
from Strategies import StaticStrategy


def main():
    # GAME 1
    # Create strategies
    strategy_A = StaticStrategy('The Great Destroyer', [33, 33, 34], shuffle=True)
    strategy_B = StaticStrategy('The Even More Destroyer', [51, 47, 2])

    # Set up game
    gm = GameManager(strategy_A, strategy_B, num_fields=3, num_runs=100, total_score=True)
    gm.run()
    gm.plot_results()
    gm.declare_winner()

    # GAME 2
    # Create strategies
    strategy_A = StaticStrategy('The Great Destroyer 2', [33, 33, 34], shuffle=True)
    strategy_B = StaticStrategy('The Even More Destroyer 2', [51, 47, 2])

    # Set up game
    gm = GameManager(strategy_A, strategy_B, num_fields=3, num_runs=100, total_score=False)
    gm.run()
    gm.plot_results()
    gm.declare_winner()

if __name__ == "__main__":
    main()