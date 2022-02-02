import random
import pytest 
import os
import sys
import numpy as np
sys.path.insert(0, "/Users/kiran_ikram/Documents/GitHub/CommsTests")
from src.vacation.agent import Agent
from src.vacation.basic_env import SeasonForecast
from src.vacation.utils import Actions, Seasons

def test_rl_loop():
    agent_1 = Agent()
    agent_2 = Agent()

    basic_env = SeasonForecast(periods=12,n_steps=24,occlusion_pct=0.4)
    basic_env.add_agents(agent_1, agent_2)

    basic_env.generate_weather(basic_env.periods)
    assert len(basic_env.forecast) == 12
    basic_env.get_season()

    actions = {agent_1: agent_1.get_random_actions(),
               agent_2: agent_2.get_random_actions()}

    assert type(actions) == dict

    obs , rewards ,done  = basic_env.step(actions)

    assert type(obs[agent_1]) == np.ndarray
    assert type(rewards[agent_1]) == int

   