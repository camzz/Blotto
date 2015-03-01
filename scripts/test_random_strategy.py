__author__ = 'camzzz'

from GameManager import GameManager
from Strategies import RandomStrategy


def main():
    # GAME 1
    # Create strategies
    strategy_A = RandomStrategy('The Great Destroyer', [1/3.0, 1/3.0, 1/3.0], shuffle=True)
    strategy_B = RandomStrategy('The Even More Destroyer', [0.4, 0.4, 0.2])

    # Set up game
    gm = GameManager(strategy_A, strategy_B, num_fields=3, num_runs=1000, total_score=True)
    gm.run()
    gm.plot_results()
    gm.declare_winner()

    # GAME 2
    # Create strategies
    strategy_A = RandomStrategy('The Great Destroyer 2', [0.51, 0.48, 0.01], shuffle=True)
    strategy_B = RandomStrategy('The Even More Destroyer 2', [0.5, 0.5, 0.0], shuffle=True)

    # Set up game
    gm = GameManager(strategy_A, strategy_B, num_fields=3, num_runs=1000, total_score=False)
    gm.run()
    gm.plot_results()
    gm.declare_winner()


if __name__ == "__main__":
    main()