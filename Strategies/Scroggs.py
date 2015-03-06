__author__ = "camzz"

from BaseStrategy import BaseStrategy
from random import randint

class Scroggs(BaseStrategy):
    """
    Copy this strategy and rename it to create your own!
    Check out CopierStrategy for an example
    """
    def __init__(self, name):
        """
        Create your strategy my writing MyStrategy(name, my_argument)
        
        Writing this method is entirely optional, if you dont want any extra arguments, leave it out
        If you leave it out, create your strategy my writing MyStrategy(name)
        
        Choose a cool name for extra points*!
        """
        super(Scroggs, self).__init__(name)
        
        #Store any variables you need later here


    def soldiers_request(self, iteration):
        """
        Here you are asked what your next move will be, return it 
        iteration is the number of which battle we are on 0->N (you probably wont need it)
        
        You can look at:
            self.opponent_allocations
            which is a list of the opponents strategies so far.Carefult not to change it!
            
            self.past_scores
            which is a list of the scores so far in this match.
            
            self.num_fields
            number of fields to place orders in, this should be the length of the list you return.
            Or just assume its 8 for the main contest
            
            self.my_argument
            You can use anything which you put in at setup (__init__ above).
            This might be used for more complicated strategies.
        """
        #Do some calucalations, use some random numbers, do whatever you want
        alloc = self.opponent_allocations
        average = [0]*8
        if len(alloc)>0:
            for go in alloc:
                for i,val in enumerate(go):
                    average[i]+=val
            for i,val in enumerate(average):
                average[i]/=len(alloc)

        sorted = average[:]
        sorted.sort()
        print sorted
        put = [0]*8
        used = []
        left = 100
        for min in sorted:
            for i,val in enumerate(average):
                if i not in used and min==val:
                    used.append(i)
                    if left>val:
                        put[i]=val+1
                        left-=val+1
                    else:
                        put[i]=left
                        left=0
        if left>0:
            for i in range(0,left):
                put[randint(0,7)]+=1
        return put
