import random
import pytest 
import os
import sys
os.getcwd()

sys.path.insert(0, "/Users/kiran_ikram/Documents/GitHub/CommsTests")

from src.env.agent import Agent
from src.env.basic_env import SeasonForecast



#assert season is same for both agents at same time 
def test_rl_loop():
    """
    Tests the general RL api.
    """

    agent_1 = Agent()
    agent_2 = Agent()

    basic_env = SeasonForecast(periods=12,n_steps=24,occlusion_pct=0.4)

    basic_env.generate_weather

 
    action_ag_1 = agent_1.get_random_actions
    action_ag_2 = agent_2.get_random_actions

    

    agent_obs = basic_env.generate_agent_obs
    

    # make some assertions that 

  
    