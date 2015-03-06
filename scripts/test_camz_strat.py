__author__ = 'camzzz'

from GameManager import GameManager
from Strategies import *

#Import your strategy
from Strategies.CamzStrategy import CamzBattle
from Strategies.SnoopDogg import SnoopDogg
from Strategies.Scroggs import Scroggs


def main():
    # Add you own strategy here instead of StaticStrategy
    camz = CamzBattle('Camz', "/home/cameron/Code/Blotto/data/camz_strategy.json")
    snoop = SnoopDogg('Snoop')

    # Create opponent
    scroggs = Scroggs('Scroggs')

    # Set up game
    gm = GameManager(snoop, scroggs, num_fields=8, num_runs=1000)
    gm.run()
    # Uncomment this if you have matplotlib
    gm.plot_results()
    gm.declare_winner()


if __name__ == "__main__":
    main()
