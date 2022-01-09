import random 
import scipy.stats as stats
import numpy as np

class SeasonForecast:
    def __init__(self,periods):
        self.seasons = [1,2,3]
        self.generate_weather(periods)
        self.get_season()
        self.periods = periods
        
    def get_season(self):
        self.the_season =  stats.mode(self.forecast)[0][0]

    def generate_weather(self,periods):
        self.forecast = np.array(random.choices(self.seasons,k=periods))

    def add_agents(self, agent_1, agent_2, random_position=True):

        self.agents = [agent_1, agent_2]

        self._place_agents(random_position)
        self._assign_colors()

        agent_1.reset()
        agent_2.reset()

    def reset(self):
        self.generate_weather(self.periods)
        self.get_season()

    def step(self):
        pass


episode_1=SeasonForecast(8)

print(type(episode_1.forecast))

print(episode_1.season())