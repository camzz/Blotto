__author__ = 'camzzz'

from GameManager import GameManager

from Strategies.CamzStrategy import CamzLearner
from Strategies.Scroggs import Scroggs
from Strategies.RandomStrategy import RandomStrategy, RandomStyle
from Strategies.MixedStrategy import MixedStrategy

c = CamzLearner('camz', '/home/cameron/Code/Blotto/data/beat_scroggs.json', keep_fct=1.0, add_fct=1.0)
s = Scroggs('s')
r = RandomStrategy('r', style=RandomStyle.UNIFORM)
m = MixedStrategy('scroggs_and_unif', [s, r], [0.9, 0.1])


gm = GameManager(m, c, 8, 3000)

gm.run()
gm.plot_results()
gm.declare_winner()


#c.crop_db()
c.store_db()