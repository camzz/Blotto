__author__ = 'camzzz'

import random
import json

from BaseStrategy import BaseStrategy
from StrategyUtils.random_utils import get_allocation_uniform


class CamzBattle(BaseStrategy):
    def __init__(self, name, filename):
        super(CamzBattle, self).__init__(name)

        with open(filename) as f:
            self.strategy_db = json.load(f)
        self.total_db_score = sum(v for k, v in self.strategy_db.iteritems())

    def soldiers_request(self, iteration):
        # Pick allocation by score in db
        r = random.random()
        for k, v in self.strategy_db.iteritems():
            if r <= float(v) / self.total_db_score:
                return make_list(k)
            r -= float(v) / self.total_db_score

        else:
            raise


class CamzLearner(BaseStrategy):
    def __init__(self, name, filename, keep_fct, add_fct=0):
        super(CamzLearner, self).__init__(name)
        assert 0 <= keep_fct <= 1

        with open(filename) as f:
            self.strategy_db = json.load(f)

        with open(filename.replace('.json', '') + '_backup.json', 'w+') as f:
            json.dump(self.strategy_db, f, indent=4)

        self.filename = filename
        self.total_db_score = sum(v for k, v in self.strategy_db.iteritems())
        self.allocation = None
        self.keep_fct = keep_fct
        self.add_fact = add_fct

    def store_db(self):
        with open(self.filename, 'w+') as f:
            json.dump(self.strategy_db, f, indent=4)

    def crop_db(self):
        num_entries = len(self.strategy_db)
        threshold = sorted(self.strategy_db.values(), reverse=True)[int(num_entries * self.keep_fct) - 1]
        if threshold == 1:
            threshold = 2
        self.strategy_db = {k: v for k, v in self.strategy_db.iteritems() if v >= threshold}

    def soldiers_request(self, iteration):
        # Pick allocation by score in db
        if self.allocation is None:
            # Nothing in database yet, pick from uniform distribution and give it a point on us.
            self.allocation = get_allocation_uniform(self.num_fields)
            self.strategy_db[make_string(self.allocation)] = 1
            self.total_db_score = 1
            return self.allocation

        rn = random.random()
        for k, v in self.strategy_db.iteritems():
            #import pdb; pdb.set_trace()
            if rn <= (float(v) / self.total_db_score):
                self.allocation = make_list(k)
                break
            rn -= float(v) / self.total_db_score

        return sorted(self.allocation, key=lambda k: random.random())

    def post_results(self, score, soldiers_B, check_B):
        if check_B:
            if score > 0:
                self.strategy_db[make_string(self.allocation)] += 1
                self.total_db_score += 1
            elif score < 0:
                self.strategy_db[make_string(self.allocation)] -= 1
                if self.add_fact == 0:
                    self.strategy_db[make_string(soldiers_B)] = 1
                else:
                    n = self.strategy_db[make_string(self.allocation)] + 1
                    self.strategy_db[make_string(soldiers_B)] = n * self.add_fact
                if self.strategy_db[make_string(self.allocation)] == 0:
                    self.strategy_db.pop(make_string(self.allocation))


def make_string(t):
    return ' '.join(str(t) for t in t)


def make_list(s):
    return [int(i) for i in s.split(' ')]


def get_top_n_strats(filename, n=10):
    with open(filename) as f:
        strat_db = json.load(f)
        threshold = sorted(strat_db.values(), reverse=True)[min(n, len(strat_db) - 1)]
        return [make_list(k) for k, v in strat_db.iteritems() if v >= threshold]


def rebase_strats(filename, factor=10):
    with open(filename) as f:
        strat_db = json.load(f)
        strat_db_rebase = {k: int(v/factor) for k, v in strat_db.iteritems()}
    with open(filename, 'w+') as f, open(filename.replace('.json', '') + '_backup.json', 'w+') as f2:
        json.dump(strat_db, f2)
        json.dump(strat_db_rebase, f)