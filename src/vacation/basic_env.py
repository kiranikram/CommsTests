import random 
import scipy.stats as stats
import numpy as np
import sys
import gym
from gym import spaces 
sys.path.insert(0, "/Users/kiran_ikram/Documents/GitHub/CommsTests")


from utils import Actions, Seasons



#from agent import Agent

"Even if one agent packs the wrong item, they both get -20. If at least one packs the right utem, they get +5. If both agents pack the right item, they get +10."

#TODO for seasons can use Enum 

#TODO need to see how to trigger reset - and how 'dont impacts this - maybe for testing we set manual number of steps ? 


class SeasonForecast:
    def __init__(self,periods,n_steps,occlusion_pct):
        self.seasons = [1,2,3]
        self.generate_weather(periods)
        self.get_season()
        self.periods = periods
        self.nn_step = 0
        self.n_steps = n_steps
        self.occlusions_pct = occlusion_pct
        self.observation_space = spaces.Discrete(8)
        self.action_space = spaces.Discrete(4)
        
    def get_season(self):
        self.the_season =  stats.mode(self.forecast)[0][0]

    def generate_weather(self,periods):
        print('weather')
        self.forecast = np.array(random.choices(self.seasons,k=periods))

    #TODO make this dynamic (currently it is restricted to 2 agents)
    #TODO relay to MT , ask how to instantiate class give variable number of agents 
    def add_agents(self, agent_1, agent_2):

        self.agents = [agent_1, agent_2]

        agent_1.reset()
        agent_2.reset()

    def reset(self):
        self.generate_weather(self.periods)
        self.get_season()

        self.agents[0].reset()
        self.agents[1].reset()

        obs = {
            self.agents[0]: self.generate_agent_obs(self.agents[0]),
            self.agents[1]: self.generate_agent_obs(self.agents[1])
        }

        return obs

    def step(self):
        #self.step += 1

        #communicate 

        obs = {}
        rewards = {}
        dones = {}


        if not self.agents[0].done:
            obs[self.agents[0]] = self.generate_agent_obs()
        else:
            obs[self.agents[0]] = None

        if not self.agents[1].done:
            obs[self.agents[1]] = self.generate_agent_obs()
        else:
            obs[self.agents[1]] = None

        rewards[self.agents[0]] = self.get_agent_rew(self.agents[0])
        rewards[self.agents[1]] = self.get_agent_rew(self.agents[1])

        if self.step == self.n_steps:
            dones[self.agents[0]] = True
            dones[self.agents[1]] = True
        else: 
            dones[self.agents[0]] = False
            dones[self.agents[1]] = False

        return obs , rewards, dones

    def communicate(self):
        ag_1_msg = self.agents[0].get_rand_comms()
        ag_2_msg = self.agents[1].get_rand_comms()

    
        #how is the comms bit appended to locat agent obs ?! 



    def get_agent_rew(self,action):
        # remember doing action 'pack nothing' gets zero reward
        # TODO if agent has already packed item, should get no more reward for packing it twice : to do this can create cache of 'packed' items 
        #get the action from the action dict 

        agent_action = Actions[action]
        current_season = Seasons[self.the_season]
        
        if current_season == 'rainy':
            if agent_action == 'umbrella':
                rew = 5
            elif agent_action == 'beach_ball' or agent_action == 'skis':
                rew = -5

        elif current_season == 'snow':
            if agent_action == 'skis':
                rew = 5
            elif agent_action == 'beach_ball' or agent_action == 'umbrella': 
                rew = -5

        elif current_season == 'sunny':
            if agent_action == 'beach_ball':
                rew = 5
            elif agent_action == 'umbrella' or agent_action == 'skis':
                rew = -5 
 
        
        return rew


    def generate_agent_obs(self):

        full_obs = self.forecast

        no_of_occlusions = int(self.occlusions_pct*(len(full_obs)))

        occlusions = random.sample(range(0,len(full_obs)),no_of_occlusions)

        for index in occlusions:
            full_obs[index] = -1

        return full_obs

        #randomly select subset of two simulatneous values. mask all other values with -1. 
        #because its randomly selected - does not matter which agent it is for 



#episode_1=SeasonForecast(8)

#print(type(episode_1.forecast))

#print(episode_1.season())