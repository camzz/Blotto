__author__ = "Linus"


from simple import Copier


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

    def initialise(self, num_fields=None, num_runs=None):
        self.opponentsLastMove = None
        self.castles = num_fields
        self.soldiers = 100
        self.program = self.simpleStrat()

    def soldiers_request(self, iteration):
        if self.opponentsLastMove == None:
            return self.program.next()
        else:
            return self.program.send(self.opponentsLastMove)

    def post_results(self, score, soldiers_B, check_B):
        self.opponentsLastMove = soldiers_B

    def wipe_history(self):
        self.initialise(self.weights, self.soldiers)
