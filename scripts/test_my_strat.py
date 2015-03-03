__author__ = 'camzzz'

from GameManager import GameManager
from Strategies import *

#Import your strategy
#from Strategies.MyStrategy import MyStrategy


def main():
    # Add you own strategy here instead of StaticStrategy
    my_strat = StaticStrategy('MyStrat', [25, 25, 25, 25, 0, 0, 0, 0], shuffle=True)

    # Create opponent
    opponent = RandomStrategy('RandomStrategy', style=RandomStyle.UNIFORM)

    # Set up game
    gm = GameManager(my_strat, opponent, num_fields=8, num_runs=1)
    gm.run()
    # Uncomment this if you have matplotlib
    # gm.plot_results()
    gm.declare_winner()


if __name__ == "__main__":
    main()