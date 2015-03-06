__author__ = 'camzzz'

from GameManager import GameManager

from Strategies.CamzStrategy import CamzLearner
from Strategies.Scroggs import Scroggs
from Strategies.RandomStrategy import RandomStrategy, RandomStyle
from Strategies.MixedStrategy import MixedStrategy

c = CamzLearner('camz', '/home/cameron/Code/Blotto/data/beat_unif.json', keep_fct=1.0, add_fct=1.0)
s = Scroggs('scroggs')
r = RandomStrategy('r', style=RandomStyle.UNIFORM)
m = MixedStrategy('scroggs_and_unif', [s, r], [0.9, 0.1])


gm = GameManager(r, c, 8, 10000)

gm.run()gt
gm.plot_results()
gm.declare_winner()


#c.crop_db()
c.store_db()