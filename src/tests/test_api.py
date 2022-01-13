import random
import pytest 
import os
import sys
os.getcwd()

sys.path.insert(0, "/Users/kiran_ikram/Documents/GitHub/CommsTests")

from src.env.agent import Agent
from src.env.basic_env import SeasonForecast




def test_rl_loop():
    """
    Tests the general RL api.
    """

    agent_1 = Agent()
    agent_2 = Agent()

    basic_env = SeasonForecast(periods=12,n_steps=24)

    basic_env.generate_weather
    print(basic_env.forecast)
    
    basic_env.add_agents(agent_1, agent_2)

    # make some assertions that 

  
    