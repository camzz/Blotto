"""
                            /\
                           |   ^,
          ,_-/---;;___     |   ,\
 (^^-.. /^ /   /#/--/ ^^---/   \ \
  \ ) \^^-/_  /#/--/      |     ; \
   .\  )  \  \##|-;       /     |  ,
  /  ^\|   ) /#/--|      (      |  |
  {  / ^\  ||#|---|       \,    /  |
 /  /  | ^\_|#|---| _______.\.     /
 [  ^  /    _#-^^^^// ## # | ~    /
/  |  ;  _/       / | ##  # \     |
|  |  |/\(        | | ##### |     |
|  / / \_)\       | |  # #  /-.   |
|  /  ._ / ^\     | \. ### /--,  //
| /      \\-_\     \  \  ./--,  /|                    ---/^^^---\,
\/        |###)        ^^     /^ |                  /^     ____   ^\,
           \*#/           \__/ ,/|                /^    /^^----^^\   ^\
            \_/          /  _./ /\              /^    --___--_----^-,  ^\
            /^    |      |^^ _/^  |             |  -,-/^######^^\----\   \
            \    /      /--^^  _/^\            / -/^#############^\---\   |
              --__---^^/|   _-^/ ##\,         | /^.,;---;,.   #####^,--\  \|
                      / L/-^ /^ ##--|)-^^^^^\/ /_,--^-,    \,   #####;--;  |\
                     /    ,-/   ##-| |        \/       ^^\   \    ###\--\  | \
                    |   ,/     ##--| /  * ^  * |          \   \    ##|--|  | |
                   /    \    ###--/ /   _ | _   \          ^|  \   ##|--|   \ \
                   |     ^,####--/  |    \A/     |           \  |  ##\---\  | |
                   |       \##--/  ,^ *  /#\     |            | |   ##|--|  | |
                   |        \--/   /    / V \    /            \  \  ##|--|  |  \
                   \         ^\  ,/       |   * |              | ^  ##/-/   /  |
                    |\         ^V       *       /              |  \ #|--|  |   |
                     |^\  |          \         /               |  | #|--|  |   |
                     \  ^\/           ^;      |                |  | #|--|  |   |
                      \  /     /----^^^ \     /^^\             |  | #/-/  /    /
                       \ |    |      ^\  \        |             \ |#|--|  |   -
                        /     |\       \  ^\       \            | |#|--|  | ,/
                       /      | ;       \   ^       |           | |#|--/ | /
                       |      | \        ^   \       \          // #/-|   -
                      /       ^  ;        \   \       |        | |#|--| ,/
                     |       |   \         |   \      |        | ^#|--,/
                     |       |    ;        |   |       \      ,/|#|--/
                    /        |    |        |   |        |     | / ,/
                   /         |     \       |   |        |     / ,/
                  |         |      |       /   |        \    |,/
                 /          |      |      /    /         |   /
                /          /       /      (   /          |
               (          /-----^^^        ^^^|FLYingG0D./
                ^-------^^                    \-------^^

                         (from FLYingG0D: http://applejack.jwang.info/)
"""
from random import random, shuffle
from itertools import permutations
from simpleinterface import strategyOf

def PonyStrategy():
    return strategyOf(SupportVectorPony)


# assumes equal weights. inputs as (castles, soldiers).

def simplify(v,w):
    """Returns simpler but equivalent armies."""
    allNumsUsed = sorted(set(v)|set(w))
    mapping = {num:index for index,num in enumerate(allNumsUsed)}
    mapfn = lambda x: mapping[x]
    return tuple(sorted(map(mapfn,v))), tuple(sorted(map(mapfn,w)))


def memoize(f):
    cache = {}
    def memoizedf(*args):
        if args in cache: return cache[args]
        answer = f(*args)
        cache[args] = answer
        return answer
    return memoizedf
        
@memoize
def Escore(v,w):
    """Returns expected score of v vs. w.
    I suggest simplifying armies before passing them into this function."""
    v,w = simplify(v,w)
    distribution = scoreDistribution(v,w)
    total = 0
    for (score,times) in distribution.items():
        if score > 0: total += times
        if score < 0: total -= times
    return total

@memoize
def scoreDistribution(v,w):
    """Returns a distribution of the number of points v gets.
    output[k] = # of times v gets k points.
    Positive means v wins.
    I suggest simplifying armies before passing them into this function."""
    if len(v) == 0: return {0:1}
    # Try pairing v[0] with everything from w.
    total = {}
    for v0pair in xrange(len(w)):
        result0 = cmp(v[0], w[v0pair])
        remainingv = v[1:]
        remainingw = w[:v0pair]+w[v0pair+1:]
        remainingv,remainingw = simplify(remainingv,remainingw)
        resultRest = scoreDistribution(remainingv,remainingw)
        result = {score+result0:times for (score,times) in resultRest.items()}
        # add result to total
        for (score,times) in result.items():
            total[score] = total.get(score,0)+times

    return total

def wchoice(ary):
    ''' ary is like [ (apple,1), (banana,3), (orange,2.5) ] '''
    total = sum(map(lambda x:x[1],ary))
    windex = random()*total
    for a in ary:
        if windex < a[1]:
            return a[0]
        windex -= a[1]
    return ary[0]

def randPermute(army):
    army = list(army)
    shuffle(army)
    return tuple(army)


def exploit(army):
    """outputs something that beats army."""
    indices = sorted(range(8), key=lambda x: army[x], reverse=True)
    free = army[indices[0]]+army[indices[1]]
    army = list(army)
    army[indices[0]] = 0
    army[indices[1]] = 0
    remain = [(free+i)/8 for i in xrange(8)]
    for i in xrange(8):
        army[i] += remain[i]
    shuffle(army)
    return tuple(army)


def TitForTat():
    myMove = (12,13,12,13,12,13,12,13)
    while True:
        myMove = yield randPermute(myMove)


def Rando():
    while True:
        opMove = yield randomArmy(8,100)


def Spike():
    myMove = (12,13,12,13,12,13,12,13)
    while True:
        opMove = yield myMove
        myMove = exploit(opMove)


def TwilightSparkle():
    probabilities = [((19, 11, 6, 1, 20, 24, 16, 3), 0.06712891007048691),
                     ((13, 21, 2, 11, 13, 23, 0, 17), 0.17855225365300534),
                     ((18, 1, 3, 15, 15, 10, 24, 14), 0.03942729245189962),
                     ((0, 16, 11, 14, 18, 24, 9, 8), 0.09753941406388889),
                     ((9, 7, 13, 25, 17, 0, 9, 20), 0.033650064428034455),
                     ((13, 11, 1, 16, 16, 8, 14, 21), 0.0018917024053525257),
                     ((22, 10, 10, 4, 14, 17, 15, 8), 0.0315844696525452),
                     ((1, 13, 21, 23, 0, 20, 20, 2), 0.04139443418397904),
                     ((25, 8, 14, 10, 7, 6, 6, 24), 0.031048559934158834),
                     ((14, 12, 26, 3, 6, 2, 25, 12), 0.005058708289555274),
                     ((5, 10, 22, 11, 16, 4, 7, 25), 0.07450160124446505),
                     ((8, 22, 2, 12, 22, 25, 0, 9), 0.048234180578795326),
                     ((12, 15, 8, 19, 15, 4, 23, 4), 0.06186939549536513),
                     ((18, 5, 20, 3, 6, 25, 17, 6), 0.1017761268766971),
                     ((5, 12, 9, 7, 7, 16, 19, 25), 0.038598706996638844),
                     ((26, 2, 18, 13, 8, 4, 5, 24), 0.01753381474324712),
                     ((21, 12, 15, 4, 8, 8, 12, 20), 0.004724210019466477),
                     ((4, 10, 1, 1, 24, 24, 21, 15), 0.06016293787779099),
                     ((19, 3, 8, 22, 2, 20, 8, 18), 0.06532321703463988)]
    while True:
        op = yield randPermute(wchoice(probabilities))


def SupportVectorPony():
    # Pre-computation here.
    ponies = [TwilightSparkle(), Spike(), TitForTat()]
    scores = {p:0 for p in ponies}
    alpha = 0.995
    herds = {p:tuple(p.next()) for p in ponies}
    myMove = herds[ponies[0]]
    shuffles = {ponies[0]:True, ponies[1]:False, ponies[2]:True}
    usage = {p:0 for p in ponies}
    iterations = 0
    while True:

        # play my herd:
        opponentsLastMove = yield myMove
        
        # update scores.
        for p in ponies:
            if shuffles[p]:
                score = Escore(herds[p], tuple(opponentsLastMove))
            else:
                result = [cmp(herds[p][i],opponentsLastMove[i])
                          for i in xrange(8)]
                result = cmp(sum(result),0)
                score = 40320*result
            scores[p] += score
            scores[p] *= alpha
        #print scores

        # each pony must compute a move
        herds = {p:tuple(p.send(opponentsLastMove)) for p in ponies}
        # compute myMove here.
        bestPony = max(ponies, key=lambda p: scores[p])
        usage[bestPony] += 1
        iterations += 1
        if iterations == 900:
            print usage
            print scores
        myMove = herds[bestPony]
