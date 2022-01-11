import random

from utils import Actions

"Here range of observation is what # of forecasts agent can see"
class Agent:

    def __init__(self, range_observation=2):

        self._done = False
        self.range_observation = range_observation


    #@staticmethod
    def get_random_actions():

        actions = { Actions.Umbrella: random.choice((0, 1)),
                    Actions.BeachBall: random.choice((0, 1)),
                    Actions.Skis: random.choice((0,1)),
                    Actions.PackNothing: random.choice((0,1))
        }

        return actions

    #@property
    #def done(self):
        #return self._done



    #def apply_action(self, actions):
        #if self.done:
            #actions = {k: a * 0 for k, a in actions.items()}

        #self.current_actions = actions

    def reset(self):
        self.done = False
