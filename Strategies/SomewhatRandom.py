__author__ = "merovius"

from BaseStrategy import BaseStrategy
import random

class SomewhatRandom(BaseStrategy):
    def __init__(self, name):
        super(SomewhatRandom, self).__init__(name)

    def soldiers_request(self, iteration):
        fields = range(1,8)
        random.shuffle(fields)
        fields = fields[0:4]
        ret = [0] * 8
        for i in fields:
            ret[i] = 25
        return ret
