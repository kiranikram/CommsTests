from _typeshed import SupportsKeysAndGetItem
import random 
import scipy.stats as stats
import numpy as np

from agent import Agent

"Even if one agent packs the wrong item, they both get -20. If at least one packs the right utem, they get +5. If both agents pack the right item, they get +10."

#TODO for seasons can use Enum 

#TODO need to see how to trigger reset - and how 'dont impacts this - maybe for testing we set manual number of steps ? 


class SeasonForecast:
    def __init__(self,periods,n_steps):
        self.seasons = [1,2,3]
        self.generate_weather(periods)
        self.get_season()
        self.periods = periods
        self.step = 0
        self.n_steps = n_steps
        
    def get_season(self):
        self.the_season =  stats.mode(self.forecast)[0][0]

    def generate_weather(self,periods):
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

    def step(self,actions):
        self.step += 1

        obs = {}
        rewards = {}
        dones = {}


        if not self.agents[0].done:
            obs[self.agents[0]] = self.generate_agent_obs(self.agents[0])
        else:
            obs[self.agents[0]] = None

        if not self.agents[1].done:
            obs[self.agents[1]] = self.generate_agent_obs(self.agents[1])
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

    def get_agent_rew(self,agent,actions):
        # remember doing action 'pack nothing' gets zero reward
        # TODO if agent has already packed item, should get no more reward for packing it twice : to do this can create cache of 'packed' items 
        #get the action from the action dict 

        if self.the_season = 'rainy':
            if action = umbrella:
                rew = 5
            elif action = beach_ball or action = skis:
                rew = -5

        if self.the_season = 'snow':
            if action = skis:
                rew = =5
            elif action = beach_ball or action = umbrella: 
                rew = -5

        if self.the_season = 'sunny':
            if action = beach_ball:
                rew = +5
            elif action = umbrella 

        return rew


    def generate_agent_obs(self, agent):
        #randomly select subset of two simulatneous values. mask all other values with -1. 
        #because its randomly selected - does not matter which agent it is for 


episode_1=SeasonForecast(8)

print(type(episode_1.forecast))

print(episode_1.season())