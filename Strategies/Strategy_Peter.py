import random
import BaseStrategy

class Strategy(BaseStrategy.BaseStrategy):
    """
    Strategy which just tries to win the majority of each game, 5/8 of the battles.
    Call using opponent = Strategy_Peter.Strategy('Strategy_Peter')
    """
    def __init__(self, name):
        super(Strategy, self).__init__(name)
        self.static_soldiers = [20, 20, 20, 20, 20, 0, 0, 0]
        self.shuffle = True

    def soldiers_request(self, iteration):
        if self.shuffle:
            return sorted(self.static_soldiers, key=lambda k: random.random())
        else:
            return self.static_soldiers