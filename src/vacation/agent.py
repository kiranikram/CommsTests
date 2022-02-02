import random

"Here range of observation is what # of forecasts agent can see"
class Agent:

    def __init__(self, range_observation=2):

        self._done = False
        self.range_observation = range_observation


    #@staticmethod
    def get_random_actions(self):
        
        actions = [0,1,2,3]
        action = random.sample(actions,1)
        action = action[0]

        print(action)

        return action

    def gen_rand_comms(self,len_msgs):

        comms = [random.uniform(10.5, 75.5) for i in range(len_msgs)]

        return comms 


    #@property
    #def done(self):
        #return self._done



    #def apply_action(self, actions):
        #if self.done:
            #actions = {k: a * 0 for k, a in actions.items()}

        #self.current_actions = actions

    def reset(self):
        self.done = False


an_agent = Agent()
an_agent.get_random_actions()