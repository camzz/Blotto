__author__ = "Linus"


from simple import Copier

def test():
    from GameManager import GameManager
    S = strategyOf(Copier, "Copier A")
    T = strategyOf(Copier, "Copier B")
    G = GameManager(S, T, [4,3,2,2,1,1,1], 100, 10)
    return G.run()


# This file helps interface simple.py with Matthew's code.
# strategyOf(Copier) returns a complicated object of type BaseStrategy,
# which plays like Copier and works with Matthew's codebase.
# To give it a name, use strategyOf(Copier, "super clever strategy").

def strategyOf(simpleStrat, name=None):
    if name == None:
        try:
            name = simpleStrat.__name__
        except:
            name = "<default name>"
    return Strategy(simpleStrat, name)


class Strategy(object):
    def __init__(self, simpleStrat, name="<default name>"):
        self.name = name
        self.simpleStrat = simpleStrat

    def __repr__(self):
        return self.name

    def initialise(self, weights, soldiers, num_runs=None):
        self.opponentsLastMove = None
        self.weights = weights
        self.soldiers = soldiers
        self.program = self.simpleStrat(weights, soldiers)

    def soldiers_request(self, iteration):
        if self.opponentsLastMove == None:
            return self.program.next()
        else:
            r = self.program.send(self.opponentsLastMove)
            print self.name, r
            return r

    def post_results(self, score, soldiers_B, check_B):
        self.opponentsLastMove = soldiers_B

    def wipe_history(self):
        self.initialise(self.weights, self.soldiers)
